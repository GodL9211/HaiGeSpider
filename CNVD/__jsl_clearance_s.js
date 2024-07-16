const CryptoJs = require("crypto-js");

function hash(type, value) {
    if (type === "md5") {
        return CryptoJs.MD5(value).toString();
    }
    if (type === "sha1") {
        return CryptoJs.SHA1(value).toString();
    }
    if (type === "sha256") {
        return CryptoJs.SHA256(value).toString();
    }
}

function get__jsl_clearance_s(data) {
    // Import the required library for hashing
    const crypto = require('crypto');

    // Get the length of chars array
    const charsLen = data.chars.length;

    // Loop through each combination of chars
    for (let i = 0; i < charsLen; i++) {
        for (let j = 0; j < charsLen; j++) {
            // Construct the clearance string
            const clearance = data.bts[0] + data.chars[i] + data.chars[j] + data.bts[1];

            // Create a hash object based on the specified algorithm
            let hash;
            if (data.ha === 'md5') {
                hash = crypto.createHash('md5');
            } else if (data.ha === 'sha1') {
                hash = crypto.createHash('sha1');
            } else if (data.ha === 'sha256') {
                hash = crypto.createHash('sha256');
            }

            // Update the hash object with the clearance string
            hash.update(clearance);

            // Get the hexadecimal digest of the hash
            const result = hash.digest('hex');

            // Compare the result with the given ct value
            if (result === data.ct) {
                // If the result matches, return the clearance value
                return clearance;
            }
        }
    }

    // If no matching clearance value is found, return null or handle accordingly
    return null;
}

const _clearance = get__jsl_clearance_s(data = {
  "bts": ["1719382124.722|0|amj", "dHkz%2F5UXlIQhXQElHzQj84%3D"],
  "chars": "cCWCwOqOAhFTbQgJiiEclm",
  "ct": "cfa6c1b49264198b8313c8dd1c5aaa08134b4297",
  "ha": "sha1",
  "is": true,
  "tn": "__jsl_clearance_s",
  "vt": "3600",
  "wt": "1500"
})

console.log(_clearance)