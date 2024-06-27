window = {}
window.navigator={
'userAgent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}
document = global
location = {}


function hash(_0x9060ec) {
  function _0x4f2105(_0x548e11, _0xd6f7ee) {
    return (_0x548e11 & 2147483647) + (_0xd6f7ee & 2147483647) ^ _0x548e11 & 2147483648 ^ _0xd6f7ee & 2147483648;
  }

  function _0x47bf39(_0x1f2dca) {
    var _0x3be7c6 = "0123456789abcdef";
    var _0x403cd2 = "";

    for (var _0x49d9bb = 7; _0x49d9bb >= 0; _0x49d9bb--) {
      _0x403cd2 += _0x3be7c6["charAt"](_0x1f2dca >> _0x49d9bb * 4 & 15);
    }

    return _0x403cd2;
  }

  function _0x374691(_0x3431f4) {
    var _0x2277fb = (_0x3431f4["length"] + 8 >> 6) + 1,
        _0x4c0e2f = new Array(_0x2277fb * 16);

    for (var _0x30af97 = 0; _0x30af97 < _0x2277fb * 16; _0x30af97++) {
      _0x4c0e2f[_0x30af97] = 0;
    }

    for (_0x30af97 = 0; _0x30af97 < _0x3431f4["length"]; _0x30af97++) {
      _0x4c0e2f[_0x30af97 >> 2] |= _0x3431f4["charCodeAt"](_0x30af97) << 24 - (_0x30af97 & 3) * 8;
    }

    _0x4c0e2f[_0x30af97 >> 2] |= 128 << 24 - (_0x30af97 & 3) * 8;
    _0x4c0e2f[_0x2277fb * 16 - 1] = _0x3431f4["length"] * 8;
    return _0x4c0e2f;
  }

  function _0x4b3f91(_0x5b9026, _0x3ad37a) {
    return _0x5b9026 << _0x3ad37a | _0x5b9026 >>> 32 - _0x3ad37a;
  }

  function _0x1a51fe(_0x146005, _0x208eab, _0x37ebce, _0x2300eb) {
    if (_0x146005 < 20) {
      return _0x208eab & _0x37ebce | ~_0x208eab & _0x2300eb;
    }

    if (_0x146005 < 40) {
      return _0x208eab ^ _0x37ebce ^ _0x2300eb;
    }

    if (_0x146005 < 60) {
      return _0x208eab & _0x37ebce | _0x208eab & _0x2300eb | _0x37ebce & _0x2300eb;
    }

    return _0x208eab ^ _0x37ebce ^ _0x2300eb;
  }

  function _0x5657a6(_0x2b076a) {
    return _0x2b076a < 20 ? 1518500249 : _0x2b076a < 40 ? 1859775393 : _0x2b076a < 60 ? -1894007588 : -899497514;
  }

  var _0x433d77 = _0x374691(_0x9060ec);

  var _0x1520f3 = new Array(80);

  var _0x236556 = 1732584193;

  var _0x126bca = -271733879;

  var _0x3ca08c = -1732584194;

  var _0x1ad745 = 271733878;

  var _0x3d4ab1 = -1009589776;

  for (var _0x52e4f0 = 0; _0x52e4f0 < _0x433d77["length"]; _0x52e4f0 += 16) {
    var _0x5d6482 = _0x236556;
    var _0x1bdba3 = _0x126bca;
    var _0x256655 = _0x3ca08c;
    var _0xaf9465 = _0x1ad745;
    var _0x35abf5 = _0x3d4ab1;

    for (var _0x57665f = 0; _0x57665f < 80; _0x57665f++) {
      if (_0x57665f < 16) {
        _0x1520f3[_0x57665f] = _0x433d77[_0x52e4f0 + _0x57665f];
      } else {
        _0x1520f3[_0x57665f] = _0x4b3f91(_0x1520f3[_0x57665f - 3] ^ _0x1520f3[_0x57665f - 8] ^ _0x1520f3[_0x57665f - 14] ^ _0x1520f3[_0x57665f - 16], 1);
      }

      t = _0x4f2105(_0x4f2105(_0x4b3f91(_0x236556, 5), _0x1a51fe(_0x57665f, _0x126bca, _0x3ca08c, _0x1ad745)), _0x4f2105(_0x4f2105(_0x3d4ab1, _0x1520f3[_0x57665f]), _0x5657a6(_0x57665f)));
      _0x3d4ab1 = _0x1ad745;
      _0x1ad745 = _0x3ca08c;
      _0x3ca08c = _0x4b3f91(_0x126bca, 30);
      _0x126bca = _0x236556;
      _0x236556 = t;
    }

    _0x236556 = _0x4f2105(_0x236556, _0x5d6482);
    _0x126bca = _0x4f2105(_0x126bca, _0x1bdba3);
    _0x3ca08c = _0x4f2105(_0x3ca08c, _0x256655);
    _0x1ad745 = _0x4f2105(_0x1ad745, _0xaf9465);
    _0x3d4ab1 = _0x4f2105(_0x3d4ab1, _0x35abf5);
  }

  return _0x47bf39(_0x236556) + _0x47bf39(_0x126bca) + _0x47bf39(_0x3ca08c) + _0x47bf39(_0x1ad745) + _0x47bf39(_0x3d4ab1);
}

function go(_0x184054) {
  function _0x1ec4b0() {
    var _0x3646eb = window["navigator"]["userAgent"],
        _0x5e1c0f = ["Phantom"];

    for (var _0x29f991 = 0; _0x29f991 < _0x5e1c0f["length"]; _0x29f991++) {
      if (_0x3646eb["indexOf"](_0x5e1c0f[_0x29f991]) != -1) {
        return true;
      }
    }

    if (window["callPhantom"] || window["_phantom"] || window["Headless"] || window["navigator"]["webdriver"] || window["navigator"]["__driver_evaluate"] || window["navigator"]["__webdriver_evaluate"]) {
      return true;
    }
  }

  if (_0x1ec4b0()) {
    return;
  }

  var _0x4e5f24 = new Date();

  function _0x5e134f(_0x36f76f, _0x37172a) {
    var _0x2265b3 = _0x184054["chars"]["length"];

    for (var _0x391a5a = 0; _0x391a5a < _0x2265b3; _0x391a5a++) {
      for (var _0x38f12b = 0; _0x38f12b < _0x2265b3; _0x38f12b++) {
        var _0x1f3544 = _0x37172a[0] + _0x184054["chars"]["substr"](_0x391a5a, 1) + _0x184054["chars"]["substr"](_0x38f12b, 1) + _0x37172a[1];

        if (hash(_0x1f3544) == _0x36f76f) {
          console.log(_0x1f3544)
          return [_0x1f3544, new Date() - _0x4e5f24];
        }
      }
    }
  }

  var _0x2c759c = _0x5e134f(_0x184054["ct"], _0x184054["bts"]);

  if (_0x2c759c) {
    var _0x10de0d;

    if (_0x184054["wt"]) {
      _0x10de0d = parseInt(_0x184054["wt"]) > _0x2c759c[1] ? parseInt(_0x184054["wt"]) - _0x2c759c[1] : 500;
    } else {
      _0x10de0d = 1500;
    }

    // setTimeout(function () {
    //   var _0x158088 = _0x184054["tn"] + "=" + _0x2c759c[0] + ";Max-age=" + _0x184054["vt"] + "; path = /";
    //
    //   if (_0x184054["is"]) {
    //     _0x158088 = _0x158088 + "; SameSite=None; Secure";
    //   }
    //
    //   document["cookie"] = _0x158088;
    //   location["href"] = location["pathname"] + location["search"];
    // }, _0x10de0d);

    var _0x158088 = _0x184054["tn"] + "=" + _0x2c759c[0] + ";Max-age=" + _0x184054["vt"] + "; path = /";

    if (_0x184054["is"]) {
      _0x158088 = _0x158088 + "; SameSite=None; Secure";
    }

    document["cookie"] = _0x158088;
    location["href"] = location["pathname"] + location["search"];
    console.log(_0x158088)
    return _0x158088
  } else {
    alert("请求验证失败");
  }
}

go({
  "bts": ["1719472445.601|0|j3A", "LtZQTMBXOgbV%2FXe2COV%2BT0%3D"],
  "chars": "tbXoPOcGKMZFhHtkAwtyWm",
  "ct": "a87d9a030228c2462949c94a29ac05300528f760",
  "ha": "sha1",
  "is": true,
  "tn": "__jsl_clearance_s",
  "vt": "3600",
  "wt": "1500"
});