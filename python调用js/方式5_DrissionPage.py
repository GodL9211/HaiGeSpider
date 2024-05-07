#! -*-conding=: UTF-8 -*-
# 2024/5/7 17:28
from DrissionPage import ChromiumPage


if __name__ == '__main__':
    page = ChromiumPage()

    # 打开网页
    page.get("about:blank")

    # 定义 JavaScript 代码
    js_code = """
    function add(a, b) {
        return a + b;
    }
    """

    # 在当前页面上执行 JavaScript 代码，并传递参数
    result = page.run_js(js_code + " return add(8, 5)")  # JavaScript 执行结果: 13

    # 输出执行结果
    print("JavaScript 执行结果:", result)

    page.quit()

