CryptoJS = require('crypto-js')

get_sign = function (text, aesKey, aesIv) {
    let iv = CryptoJS.enc.Utf8.parse(aesIv); // 偏移量
    let key = CryptoJS.enc.Utf8.parse(aesKey); // key
    let data = CryptoJS.enc.Utf8.parse(JSON.stringify(text));  // data
    console.log(data)
    let aes = CryptoJS.AES.encrypt(data, key, {
        iv: iv,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Iso10126
    });
    return aes.toString()
};

const iv_key = function (random) {
    return random.split("").reverse().join("").split("@")
}


function run(x, y, random) {

    let data = {
        "cx": x,
        "cy": y,
        "scale": 0.5,
        "slidingEvents": [
            {
                "mx": 41,
                "my": 205,
                "ts": Date.now()
            },
            {
                "mx": 1,
                "my": 0,
                "ts": 55
            },
            {
                "mx": 1,
                "my": 0,
                "ts": 7
            },
            {
                "mx": 2,
                "my": 0,
                "ts": 9
            },
            {
                "mx": 2,
                "my": 0,
                "ts": 7
            },
            {
                "mx": 2,
                "my": 0,
                "ts": 9
            },
            {
                "mx": 3,
                "my": 0,
                "ts": 7
            },
            {
                "mx": 2,
                "my": 0,
                "ts": 9
            },
            {
                "mx": 2,
                "my": 0,
                "ts": 15
            },
            {
                "mx": 1,
                "my": 0,
                "ts": 9
            },
            {
                "mx": 1,
                "my": 0,
                "ts": 88
            }
        ]
    }
    let a = iv_key(random),
        iv = a[1],
        key = a[0];
    return get_sign(data, key, iv)
}



// bbb = "uKNIYCpnGUcLMmMv@yKhyq3NsffHkYKka"
// run(aaa, bbb)