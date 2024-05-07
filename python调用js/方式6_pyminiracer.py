#! -*-conding=: UTF-8 -*-
# 2024/5/7 17:48
from py_mini_racer import MiniRacer

if __name__ == '__main__':
    # 创建 PyMiniRacer 实例
    ctx = MiniRacer()

    js_code = """
    function add(a, b) {
        return a + b;
    }
    """
    # 在 JavaScript 环境中执行代码并传递参数
    ctx.eval(js_code)
    result = ctx.call("add", 3, 5)

    # 输出执行结果
    print("JavaScript 执行结果:", result)
