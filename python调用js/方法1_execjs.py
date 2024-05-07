#! -*-conding=: UTF-8 -*-
# 2024/5/7 15:04
from loguru import logger
import execjs

# 定义 JavaScript 代码
# js_code = """
# function add(a, b) {
#     return a + b;
# }
# """

if __name__ == '__main__':
    # Python 示例代码

    js_code = open("add.js", "r", encoding="utf-8").read()

    # 使用 PyExecJS 执行 JavaScript 代码
    ctx = execjs.compile(js_code)

    # 调用 JavaScript 函数，并计算结果
    result = ctx.call("add", 3, 5)
    logger.info(f"调用 JavaScript 函数的结果为: {result}")

