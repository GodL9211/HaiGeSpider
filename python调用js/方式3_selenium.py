#! -*-conding=: UTF-8 -*-

from selenium import webdriver

# 启动 Chrome 浏览器
driver = webdriver.Chrome()

# 打开网页
driver.get("about:blank")

# 定义 JavaScript 代码
js_code = """
    function add(a, b) {
        return a + b;
    }
    """

# 在当前页面上执行 JavaScript 代码，并传递参数
result = driver.execute_script(js_code + " return add(3, 5)")

# 输出执行结果
print("JavaScript 执行结果:", result)

# 关闭浏览器
driver.quit()

