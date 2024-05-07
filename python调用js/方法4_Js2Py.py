#! -*-conding=: UTF-8 -*-
# 2024/5/7 16:14
from js2py import eval_js


if __name__ == '__main__':
    # JavaScript 示例代码
    js_code = """
    function add(a, b) {
        return a + b;
    }
    """

    # 执行 JavaScript 代码
    result = eval_js(js_code + "add(3, 5)")

    # 输出执行结果
    print("JavaScript 执行结果:", result)

