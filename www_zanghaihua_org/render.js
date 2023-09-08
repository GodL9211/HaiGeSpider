const puppeteer = require('puppeteer');
console.log('脚本开始执行1');

const url = process.argv[2];
console.log(url);

async function renderPage(url) {
    console.log('renderPage函数开始执行');
    const browser = await puppeteer.launch({executablePath: "C:\\Users\\lianhaifeng\\AppData\\Local\\ms-playwright\\chromium-1076\\chrome-win\\chrome.exe"});
    const page = await browser.newPage();

    console.log(`正在加载页面: ${url}`);

    try {
        await page.goto(url, {waitUntil: 'networkidle2'}); // 等待页面加载完成
        console.log('页面加载完成');

        const content = await page.content(); // 获取渲染后的HTML内容
        console.log('已获取页面内容');

        await browser.close();
        console.log('浏览器已关闭');
        return content;
    } catch (error) {
        console.error('发生错误:', error);
        await browser.close(); // 在错误情况下也关闭浏览器
        throw error; // 将错误传播到调用者
    }
}

async function main() {
    try {
        const renderedHTML = await renderPage(url);
        // 在这里处理渲染后的HTML内容
        console.log('渲染后的HTML内容:');
        console.log(renderedHTML);
    } catch (error) {
        console.error('发生错误:', error);
    }
}

main(); // 调用主函数以开始执行代码


