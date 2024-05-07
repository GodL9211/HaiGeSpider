#! -*-conding=: UTF-8 -*-
# 2024/5/7 18:18
from playwright.sync_api import sync_playwright

if __name__ == '__main__':
    # 启动 Playwright
    with sync_playwright() as p:
        # 启动 Chromium 浏览器
        browser = p.chromium.launch(headless=False)

        # 创建新页面
        page = browser.new_page()

        # 打开网页
        page.goto("https://baidu.com")

        # 定义 JavaScript 代码
        js_code = """
        function add(a, b) {
            return a + b;
        }
        """
        page.add_script_tag(content=js_code)  # 使用 page.add_script_tag() 方法将其注入到页面中，然后在页面上执行它
        # 在当前页面上执行 JavaScript 代码
        result = page.evaluate("add(5, 7)")

        # 输出执行结果
        print("JavaScript 执行结果:", result)  # JavaScript 执行结果: 12

        # 关闭浏览器
        browser.close()
