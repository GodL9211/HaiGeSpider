#! -*-conding=: UTF-8 -*-
# 2024/5/7 15:08
import subprocess
from loguru import logger

if __name__ == '__main__':
    # 使用 subprocess 模块执行 Node.js 命令
    result = subprocess.run(["node", "add.js", "init",  "3", "5"], capture_output=True, text=True)

    # 输出执行结果
    logger.info(f"Node.js 执行结果: {result.stdout.strip()}")
