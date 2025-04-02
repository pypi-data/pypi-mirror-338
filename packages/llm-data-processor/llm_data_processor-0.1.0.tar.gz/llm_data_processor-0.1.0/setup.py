from setuptools import setup, find_packages

setup(
    name="llm-data-processor",
    version="0.1.0",  # 根据你的版本调整
    description="A processor for LLM tasks",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="DG chen",
    author_email="94503663@qq.com",
    url="https://github.com/yourusername/llm-processor",
    packages=find_packages(exclude=["tasks", "tasks.*"]),
    include_package_data=True,
    install_requires=[
        "pyyaml",
        "requests",
        "asyncio",
        "aiohttp",
    ],
    entry_points={
        "console_scripts": [
            "llm-processor=llm_processor.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
)
