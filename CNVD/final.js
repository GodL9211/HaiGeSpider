window = {}
window.navigator={
'userAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}
document = global
location = {}

function hash(_0x5d0145) {
  function _0x2798ba(_0x117b3c, _0xfbf47) {
    return (_0x117b3c & 2147483647) + (_0xfbf47 & 2147483647) ^ _0x117b3c & 2147483648 ^ _0xfbf47 & 2147483648;
  }

  function _0x292489(_0xd627c8) {
    var _0x33fd1a = "0123456789abcdef";
    var _0x3ed587 = "";

    for (var _0x565448 = 7; _0x565448 >= 0; _0x565448--) {
      _0x3ed587 += _0x33fd1a["charAt"](_0xd627c8 >> _0x565448 * 4 & 15);
    }

    return _0x3ed587;
  }

  function _0x32cec6(_0x2f9a51) {
    var _0x18c6d4 = (_0x2f9a51["length"] + 8 >> 6) + 1,
        _0x161aad = new Array(_0x18c6d4 * 16);

    for (var _0x14646b = 0; _0x14646b < _0x18c6d4 * 16; _0x14646b++) {
      _0x161aad[_0x14646b] = 0;
    }

    for (_0x14646b = 0; _0x14646b < _0x2f9a51["length"]; _0x14646b++) {
      _0x161aad[_0x14646b >> 2] |= _0x2f9a51["charCodeAt"](_0x14646b) << 24 - (_0x14646b & 3) * 8;
    }

    _0x161aad[_0x14646b >> 2] |= 128 << 24 - (_0x14646b & 3) * 8;
    _0x161aad[_0x18c6d4 * 16 - 1] = _0x2f9a51["length"] * 8;
    return _0x161aad;
  }

  function _0x299c93(_0x254d5e, _0xbd18a5) {
    return _0x254d5e << _0xbd18a5 | _0x254d5e >>> 32 - _0xbd18a5;
  }

  function _0x591ec7(_0x3ec413, _0xdb33c4, _0x4fa93b, _0x5aca86) {
    if (_0x3ec413 < 20) {
      return _0xdb33c4 & _0x4fa93b | ~_0xdb33c4 & _0x5aca86;
    }

    if (_0x3ec413 < 40) {
      return _0xdb33c4 ^ _0x4fa93b ^ _0x5aca86;
    }

    if (_0x3ec413 < 60) {
      return _0xdb33c4 & _0x4fa93b | _0xdb33c4 & _0x5aca86 | _0x4fa93b & _0x5aca86;
    }

    return _0xdb33c4 ^ _0x4fa93b ^ _0x5aca86;
  }

  function _0x138af1(_0x1012d4) {
    return _0x1012d4 < 20 ? 1518500249 : _0x1012d4 < 40 ? 1859775393 : _0x1012d4 < 60 ? -1894007588 : -899497514;
  }

  var _0x3c6420 = _0x32cec6(_0x5d0145);

  var _0x4a942a = new Array(80);

  var _0x138ab1 = 1732584193;

  var _0x46af20 = -271733879;

  var _0x4813bb = -1732584194;

  var _0x127743 = 271733878;

  var _0x428fb8 = -1009589776;

  for (var _0x37a925 = 0; _0x37a925 < _0x3c6420["length"]; _0x37a925 += 16) {
    var _0xc1ab55 = _0x138ab1;
    var _0x10726a = _0x46af20;
    var _0x3fe880 = _0x4813bb;
    var _0x5c10b5 = _0x127743;
    var _0x22dbd9 = _0x428fb8;

    for (var _0x43981c = 0; _0x43981c < 80; _0x43981c++) {
      if (_0x43981c < 16) {
        _0x4a942a[_0x43981c] = _0x3c6420[_0x37a925 + _0x43981c];
      } else {
        _0x4a942a[_0x43981c] = _0x299c93(_0x4a942a[_0x43981c - 3] ^ _0x4a942a[_0x43981c - 8] ^ _0x4a942a[_0x43981c - 14] ^ _0x4a942a[_0x43981c - 16], 1);
      }

      t = _0x2798ba(_0x2798ba(_0x299c93(_0x138ab1, 5), _0x591ec7(_0x43981c, _0x46af20, _0x4813bb, _0x127743)), _0x2798ba(_0x2798ba(_0x428fb8, _0x4a942a[_0x43981c]), _0x138af1(_0x43981c)));
      _0x428fb8 = _0x127743;
      _0x127743 = _0x4813bb;
      _0x4813bb = _0x299c93(_0x46af20, 30);
      _0x46af20 = _0x138ab1;
      _0x138ab1 = t;
    }

    _0x138ab1 = _0x2798ba(_0x138ab1, _0xc1ab55);
    _0x46af20 = _0x2798ba(_0x46af20, _0x10726a);
    _0x4813bb = _0x2798ba(_0x4813bb, _0x3fe880);
    _0x127743 = _0x2798ba(_0x127743, _0x5c10b5);
    _0x428fb8 = _0x2798ba(_0x428fb8, _0x22dbd9);
  }

  return _0x292489(_0x138ab1) + _0x292489(_0x46af20) + _0x292489(_0x4813bb) + _0x292489(_0x127743) + _0x292489(_0x428fb8);
}

function go(_0x32a5b3) {
  function _0x21fb99() {
    var _0x545b1f = window["navigator"]["userAgent"],
        _0x532256 = ["Phantom"];

    for (var _0x417d05 = 0; _0x417d05 < _0x532256["length"]; _0x417d05++) {
      if (_0x545b1f["indexOf"](_0x532256[_0x417d05]) != -1) {
        return true;
      }
    }

    if (window["callPhantom"] || window["_phantom"] || window["Headless"] || window["navigator"]["webdriver"] || window["navigator"]["__driver_evaluate"] || window["navigator"]["__webdriver_evaluate"]) {
      return true;
    }
  }

  if (_0x21fb99()) {
    return;
  }

  var _0x10ddd6 = new Date();

  function _0x359a3d(_0x3c7d66, _0x1ad087) {
    var _0x67eeaa = _0x32a5b3["chars"]["length"];

    for (var _0x221b64 = 0; _0x221b64 < _0x67eeaa; _0x221b64++) {
      for (var _0x2f0539 = 0; _0x2f0539 < _0x67eeaa; _0x2f0539++) {
        var _0x584827 = _0x1ad087[0] + _0x32a5b3["chars"]["substr"](_0x221b64, 1) + _0x32a5b3["chars"]["substr"](_0x2f0539, 1) + _0x1ad087[1];

        if (hash(_0x584827) == _0x3c7d66) {
          console.log(_0x584827)
          return [_0x584827, new Date() - _0x10ddd6];
        }
      }
    }
  }

  var _0x486dae = _0x359a3d(_0x32a5b3["ct"], _0x32a5b3["bts"]);

  if (_0x486dae) {
    var _0xa4da8b;

    if (_0x32a5b3["wt"]) {
      _0xa4da8b = parseInt(_0x32a5b3["wt"]) > _0x486dae[1] ? parseInt(_0x32a5b3["wt"]) - _0x486dae[1] : 500;
    } else {
      _0xa4da8b = 1500;
    }

    // setTimeout(function () {
    //   var _0x1359ce = _0x32a5b3["tn"] + "=" + _0x486dae[0] + ";Max-age=" + _0x32a5b3["vt"] + "; path = /";
    //
    //   if (_0x32a5b3["is"]) {
    //     _0x1359ce = _0x1359ce + "; SameSite=None; Secure";
    //   }
    //
    //   document["cookie"] = _0x1359ce;
    //   console.log(_0x1359ce)
    //   location["href"] = location["pathname"] + location["search"];
    // }, _0xa4da8b);

    var _0x1359ce = _0x32a5b3["tn"] + "=" + _0x486dae[0] + ";Max-age=" + _0x32a5b3["vt"] + "; path = /";

    if (_0x32a5b3["is"]) {
      _0x1359ce = _0x1359ce + "; SameSite=None; Secure";
    }

    document["cookie"] = _0x1359ce;
    console.log(_0x1359ce)
    location["href"] = location["pathname"] + location["search"];
    return _0x486dae[0]
  } else {
    console.log("请求验证失败");
  }
}

go({
  "bts": ["1719382124.722|0|amj", "dHkz%2F5UXlIQhXQElHzQj84%3D"],
  "chars": "cCWCwOqOAhFTbQgJiiEclm",
  "ct": "cfa6c1b49264198b8313c8dd1c5aaa08134b4297",
  "ha": "sha1",
  "is": true,
  "tn": "__jsl_clearance_s",
  "vt": "3600",
  "wt": "1500"
});