// JavaScript 示例代码
function add(a, b) {
    return a + b;
}

// 新增一个导出函数（node方式）
module.exports.init = function (arg1, arg2) {
    // 调用函数，并返回
    console.log(add(arg1, arg2));
};

// 调用 init 方法并传递参数
module.exports.init(parseInt(process.argv[3]), parseInt(process.argv[4]));