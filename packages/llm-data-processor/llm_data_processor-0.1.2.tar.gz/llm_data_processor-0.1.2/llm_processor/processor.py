import os
import asyncio
import json
import logging
import re
import time
import yaml
from datetime import datetime
from collections import deque
import random
import asyncpg
from openai import AsyncOpenAI

# 设置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger('llm_processor')


class LLMProcessor:
    """LLM数据处理器"""

    def __init__(self, config_path):
        """初始化处理器"""
        self.config = self._load_config(config_path)
        self.db_pool = None
        self.model_selector = None
        self.system_prompt = None
        self.total_processed = 0
        self.total_records = 0
        self.start_time = time.time()

    def _load_config(self, config_path):
        """加载配置文件"""
        try:
            if config_path.endswith('.json'):
                with open(config_path, 'r', encoding='utf-8') as f:
                    config = json.load(f)
            elif config_path.endswith(('.yaml', '.yml')):
                with open(config_path, 'r', encoding='utf-8') as f:
                    config = yaml.safe_load(f)
            else:
                raise ValueError(f"不支持的配置文件格式: {config_path}")

            # 添加环境变量替换
            config = self._replace_env_vars(config)

            # 验证必要的配置项
            required_fields = ['db', 'table', 'query_fields', 'result_fields', 'id_field', 'input_field']
            missing = [field for field in required_fields if field not in config]
            if missing:
                raise ValueError(f"配置缺少必要字段: {', '.join(missing)}")

            return config
        except Exception as e:
            logger.error(f"加载配置文件失败: {str(e)}")
            raise

    def _replace_env_vars(self, config):
        """递归替换配置中的环境变量引用"""
        if isinstance(config, dict):
            return {k: self._replace_env_vars(v) for k, v in config.items()}
        elif isinstance(config, list):
            return [self._replace_env_vars(i) for i in config]
        elif isinstance(config, str) and '${' in config and '}' in config:
            # 替换形如 ${VAR_NAME} 的环境变量引用
            pattern = r'\${([^}]+)}'
            matches = re.findall(pattern, config)
            result = config
            for var_name in matches:
                env_value = os.environ.get(var_name, '')
                if not env_value:
                    logger.warning(f"环境变量 {var_name} 未设置或为空")
                result = result.replace(f'${{{var_name}}}', env_value)
            return result
        else:
            return config

    async def initialize(self):
        """初始化连接和资源"""
        # 加载提示词
        self.system_prompt = await self._load_prompt()

        # 创建模型选择器
        self.model_selector = ModelSelector(self.config.get('model_configs', []))

        # 创建数据库连接池
        try:
            self.db_pool = await asyncpg.create_pool(
                **self.config['db'],
                min_size=self.config.get('db_pool_min_size', 5),
                max_size=self.config.get('db_pool_max_size', 20)
            )
            logger.info("数据库连接池创建成功")
        except Exception as e:
            logger.error(f"数据库连接失败: {str(e)}")
            raise

        # 获取字段索引
        query_fields = self.config['query_fields']
        self.id_field_index = query_fields.index(self.config['id_field'])
        self.input_field_index = query_fields.index(self.config['input_field'])

        # 准备SQL语句
        self._prepare_sql()

    async def _load_prompt(self):
        """加载提示词"""
        # 首先检查配置中是否直接定义了system_prompt
        if 'system_prompt' in self.config:
            logger.info("使用配置文件中定义的提示词")
            return self.config['system_prompt']

        # 如果没有直接定义，尝试从文件加载
        prompt_file = self.config.get('prompt_file')
        prompt_var = self.config.get('prompt_var')

        if not prompt_file:
            logger.warning("未找到提示词定义，使用空提示词")
            return ""

        try:
            if prompt_file.endswith('.py'):
                # 动态加载Python模块
                namespace = {}
                with open(prompt_file, 'r', encoding='utf-8') as f:
                    exec(f.read(), namespace)
                return namespace.get(prompt_var, '')
            else:
                # 直接读取文本文件
                with open(prompt_file, 'r', encoding='utf-8') as f:
                    return f.read().strip()
        except Exception as e:
            logger.error(f"加载提示词失败: {str(e)}")
            raise

    def _prepare_sql(self):
        """准备SQL语句"""
        table = self.config['table']
        query_fields = self.config['query_fields']
        result_fields = self.config['result_fields']
        id_field = self.config['id_field']
        filter_condition = self.config.get('filter_condition', '1=1')

        self.sql = {
            "get_unprocessed": f"""
                SELECT {', '.join(query_fields)} FROM {table}
                WHERE {filter_condition}
                ORDER BY {id_field}
                LIMIT $1
            """,
            "get_total": f"""
                SELECT COUNT(*) FROM {table}
                WHERE {filter_condition}
            """,
            "create_temp_table": f"""
                CREATE TEMP TABLE {{temp_table}} (
                    {', '.join([f"{field} TEXT" for field in result_fields])},
                    model_flag TEXT, 
                    {id_field} TEXT
                )
            """,
            "update_from_temp": f"""
                UPDATE {table} t
                SET {', '.join([f"{field} = tmp.{field}" for field in result_fields])},
                    model_flag = tmp.model_flag
                FROM {{temp_table}} tmp
                WHERE t.{id_field} = tmp.{id_field}
            """
        }

    async def run(self):
        """运行处理任务"""
        logger.info(f"开始处理任务: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        logger.info(f"处理表: {self.config['table']}")

        # 获取总记录数
        self.total_records = await self._get_total_records()
        logger.info(f"需要处理 {self.total_records} 条记录")

        # 创建信号量和队列
        self.semaphore = asyncio.Semaphore(self.config.get('concurrency', 10))
        self.write_queue = asyncio.Queue(maxsize=self.config.get('queue_max_size', 20))

        # 启动写入任务
        self.writer_task = asyncio.create_task(self._batch_writer())

        # 防卡住机制
        processed_ids = set()

        # 主处理循环
        while True:
            batch = await self._get_unprocessed()
            if not batch:
                break

            # 检查是否有新记录
            new_records = []
            for record in batch:
                id_value = record[self.id_field_index]
                if id_value not in processed_ids:
                    new_records.append(record)
                    processed_ids.add(id_value)

            if not new_records:
                logger.warning("检测到循环处理相同记录，退出循环")
                break

            await self._process_batch(new_records)

        # 完成写入
        await self.write_queue.put(None)
        await self.writer_task

        # 打印统计信息
        total_time = time.time() - self.start_time
        logger.info(f"任务完成: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        logger.info(f"总耗时: {self._format_time(total_time)}")
        if self.total_processed > 0:
            logger.info(f"平均每条耗时: {total_time / self.total_processed:.1f}秒")

        # 关闭连接池
        if self.db_pool:
            await self.db_pool.close()

    async def _batch_writer(self):
        """批量写入处理器"""
        while True:
            batch_data = await self.write_queue.get()
            if batch_data is None:  # 结束信号
                break

            await self._update_batch(batch_data)
            self.write_queue.task_done()

    async def _update_batch(self, batch_data):
        """更新一批数据"""
        for retry in range(3):
            try:
                start_time = time.time()
                temp_table_name = f"temp_update_{int(time.time())}"

                async with self.db_pool.acquire() as conn:
                    # 创建临时表
                    create_temp_sql = self.sql["create_temp_table"].format(temp_table=temp_table_name)
                    await conn.execute(create_temp_sql)

                    # 批量插入数据
                    await conn.copy_records_to_table(temp_table_name, records=batch_data)

                    # 从临时表更新主表
                    update_sql = self.sql["update_from_temp"].format(temp_table=temp_table_name)
                    await conn.execute(update_sql)

                    # 删除临时表
                    await conn.execute(f"DROP TABLE {temp_table_name}")

                logger.info(f"批次更新完成: {len(batch_data)}条记录, 耗时: {time.time() - start_time:.2f}秒")
                break  # 成功则跳出循环

            except Exception as e:
                if retry < 2:
                    wait_time = 2 * (retry + 1)
                    logger.warning(f"批量更新失败 (尝试 {retry + 1}/3): {str(e)}")
                    await asyncio.sleep(wait_time)
                else:
                    logger.error(f"批量更新最终失败: {str(e)}")

    async def _get_total_records(self):
        """获取总记录数"""
        try:
            async with self.db_pool.acquire() as conn:
                return await conn.fetchval(self.sql["get_total"])
        except Exception as e:
            logger.error(f"获取总记录数失败: {str(e)}")
            return 0

    async def _get_unprocessed(self):
        """获取未处理的记录"""
        batch_size = self.config.get('batch_size', 1000)
        try:
            async with self.db_pool.acquire() as conn:
                return await conn.fetch(self.sql["get_unprocessed"], batch_size)
        except Exception as e:
            logger.error(f"获取未处理数据失败: {str(e)}")
            return []

    async def _process_batch(self, batch):
        """处理一批记录"""
        tasks = []
        for record in batch:
            id_value = record[self.id_field_index]
            input_value = record[self.input_field_index]
            tasks.append(self._process_one(id_value, input_value))

        results = await asyncio.gather(*tasks, return_exceptions=True)
        valid_results = [r for r in results if r and not isinstance(r, Exception)]

        if valid_results:
            await self.write_queue.put(valid_results)

    async def _process_one(self, id_value, input_value):
        """处理单条记录"""
        async with self.semaphore:
            try:
                result = await self._call_llm(input_value)
                self.total_processed += 1
                self._print_progress(input_value)

                if not result or not isinstance(result, dict):
                    logger.warning(f"跳过记录: {input_value[:30]}... - 无效的结果格式")
                    return None

                # 动态获取结果字段
                values = [result.get(field) for field in self.config['result_fields']]
                # 添加model_flag和id_field
                values.append(self.config.get('model_flag', 'processed'))
                values.append(id_value)

                return tuple(values)
            except Exception as e:
                logger.error(f"处理异常 {input_value[:30]}...: {str(e)}")
                return None

    async def _call_llm(self, input_text):
        """调用LLM处理输入文本"""
        max_retries = self.config.get('max_retries', 3)

        for attempt in range(max_retries):
            # 每次尝试重新选择模型
            model_config = self.model_selector.select_model()

            try:
                start_time = time.time()
                client = await model_config.get_client()

                # 添加超时保护
                response = await asyncio.wait_for(
                    client.chat.completions.create(
                        model=model_config.model_name,
                        messages=[
                            {"role": "system", "content": self.system_prompt},
                            {"role": "user", "content": input_text}
                        ],
                        temperature=0.7
                    ),
                    timeout=30
                )

                model_config.add_latency(time.time() - start_time)

                # 解析响应
                return self._parse_json_response(response.choices[0].message.content)

            except asyncio.TimeoutError:
                if attempt < max_retries - 1:
                    logger.warning(f"请求超时: {input_text[:30]}... (尝试 {attempt + 1}/{max_retries})")
                    await asyncio.sleep((attempt + 1) * 2)
                else:
                    logger.error(f"最终处理超时: {input_text[:30]}...")
                    return None
            except Exception as e:
                if attempt < max_retries - 1:
                    logger.warning(f"处理失败: {input_text[:30]}... (尝试 {attempt + 1}/{max_retries}): {str(e)}")
                    await asyncio.sleep((attempt + 1) * 2)
                else:
                    logger.error(f"最终处理失败: {input_text[:30]}...: {str(e)}")
                    return None

    def _parse_json_response(self, text):
        """解析LLM响应中的JSON"""
        # 清理控制字符
        clean_text = re.sub(r'(?<!\\\\)[\x00-\x1F\x7F-\x9F]', '', text)

        try:
            # 尝试直接解析
            return json.loads(clean_text)
        except json.JSONDecodeError:
            # 提取JSON部分
            try:
                json_str = re.sub(r'^.*?({.*}).*?$', r'\1', clean_text, flags=re.DOTALL)
                json_str = json_str.replace('```json', '').replace('```', '').strip()
                return json.loads(json_str)
            except:
                logger.error(f"JSON解析失败: {clean_text[:100]}...")
                return None

    def _print_progress(self, current_item):
        """打印进度信息"""
        elapsed = time.time() - self.start_time
        avg_time = elapsed / max(self.total_processed, 1)
        eta = (self.total_records - self.total_processed) * avg_time if self.total_records > 0 else 0

        # 基本进度信息
        progress_pct = self.total_processed / max(self.total_records, 1) * 100
        logger.info(f"进度: {self.total_processed}/{self.total_records} ({progress_pct:.1f}%) - {current_item[:30]}...")
        logger.info(
            f"已用时: {self._format_time(elapsed)} | 平均: {avg_time:.1f}秒/条 | 剩余: {self._format_time(eta)}")

    @staticmethod
    def _format_time(seconds):
        """格式化时间"""
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{int(hours)}小时{int(minutes)}分{int(seconds)}秒"


class ModelConfig:
    """模型配置类"""

    def __init__(self, api_key, base_url, model_name, night_only=False, initial_weight=1.0):
        self.api_key = api_key
        self.base_url = base_url
        self.model_name = model_name
        self.night_only = night_only
        self.initial_weight = initial_weight
        self._client = None
        self.latencies = deque(maxlen=50)
        self.weight = initial_weight
        logging.getLogger("openai").setLevel(logging.WARNING)
        logging.getLogger("httpx").setLevel(logging.WARNING)

    async def get_client(self):
        """获取或初始化API客户端"""
        if not self._client:
            self._client = AsyncOpenAI(api_key=self.api_key, base_url=self.base_url)
        return self._client

    def add_latency(self, latency):
        """记录请求延迟"""
        self.latencies.append(latency)

    def get_avg_latency(self):
        """获取平均延迟"""
        return sum(self.latencies) / len(self.latencies) if self.latencies else 1.0

    def is_available(self):
        """检查模型是否可用"""
        if not self.night_only:
            return True
        current_hour = datetime.now().hour
        return current_hour >= 19 or current_hour < 8


class ModelSelector:
    """模型选择器"""

    def __init__(self, model_configs):
        self.models = []
        for config in model_configs:
            model = ModelConfig(
                api_key=config.get('api_key', 'xinference'),
                base_url=config.get('base_url', ''),
                model_name=config.get('model_name', ''),
                night_only=config.get('night_only', False),
                initial_weight=config.get('initial_weight', 1.0)
            )
            self.models.append(model)

        # 如果没有配置模型，添加一个默认模型
        if not self.models:
            self.models.append(ModelConfig(
                api_key="xinference",
                base_url="http://localhost:9997/v1",
                model_name="default_model"
            ))

        self.update_weights()

    def update_weights(self):
        """基于延迟更新权重"""
        # 筛选可用模型
        available_models = [model for model in self.models if model.is_available()] or self.models

        # 获取延迟和初始权重
        latencies = [model.get_avg_latency() for model in available_models]
        initial_weights = [model.initial_weight for model in available_models]

        # 计算新权重
        if not any(latencies):
            # 无延迟数据时使用初始权重
            total_iw = sum(initial_weights) or 1.0
            for model, iw in zip(available_models, initial_weights):
                model.weight = iw / total_iw
            return

        # 延迟越低权重越高，并考虑初始权重
        inverse_latencies = [1.0 / lat * iw for lat, iw in zip(latencies, initial_weights)]
        total = sum(inverse_latencies) or 1.0

        # 更新权重
        for model, inv_lat in zip(available_models, inverse_latencies):
            model.weight = inv_lat / total

    def select_model(self):
        """根据权重选择模型"""
        available_models = [model for model in self.models if model.is_available()] or self.models
        self.update_weights()
        weights = [model.weight for model in available_models]
        return random.choices(available_models, weights=weights, k=1)[0]


async def run_processor(config_path):
    """运行处理器的入口函数"""
    processor = LLMProcessor(config_path)
    await processor.initialize()
    await processor.run()
