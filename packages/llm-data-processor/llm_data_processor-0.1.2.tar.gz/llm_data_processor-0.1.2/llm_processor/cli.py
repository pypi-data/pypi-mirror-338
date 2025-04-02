import argparse
import asyncio
import os
import sys

from .processor import run_processor


def main():
    """Command line entry point"""
    parser = argparse.ArgumentParser(description='LLM Data Processing Tool')
    parser.add_argument('config', help='Configuration file path (.json or .yaml)')
    args = parser.parse_args()

    # Check if file exists
    if not os.path.exists(args.config):
        print(f"Error: Configuration file does not exist: {args.config}")
        sys.exit(1)

    # Run processor
    asyncio.run(run_processor(args.config))


if __name__ == '__main__':
    main()
