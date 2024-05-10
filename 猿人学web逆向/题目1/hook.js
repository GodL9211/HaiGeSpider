(function () {
    'use strict';

    var cookieTemp = "";

    // 定义属性描述符对象
    var cookieDescriptor = {
        set: function (val) {
            debugger;
            console.log('Hook捕获到cookie设置->', val);
            cookieTemp = val;
            return val;
        },
        get: function () {
            return cookieTemp;
        }
    };

    // 使用 Object.defineProperty() 定义属性 'f'
    Object.defineProperty(window, 'f', cookieDescriptor);
})();
