#! -*-conding=: UTF-8 -*-
# 2024/5/7 18:18
from playwright.sync_api import sync_playwright

if __name__ == '__main__':

    # 启动 Playwright
    with sync_playwright() as p:
        # 启动 Chromium 浏览器
        browser = p.chromium.launch()

        # 创建新页面
        page = browser.new_page()

        # 打开网页
        page.goto("about:blank")

        # 定义 JavaScript 代码
        js_code = """
        function add(a, b) {
            return a + b;
        }
        """

        # 在当前页面上执行 JavaScript 代码
        result = page.evaluate(js_code, [3, 5])

        # 输出执行结果
        print("JavaScript 执行结果:", result)

        # 关闭浏览器
        browser.close()


