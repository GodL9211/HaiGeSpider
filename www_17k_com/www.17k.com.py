#! -*-conding=: UTF-8 -*-
# 2023/9/6 13:53

# cookie使用

import requests


def main():
    session = requests.session()
    data = {
        "loginName": 13678792076,
        "password": "."
    }
    url = "https://passport.17k.com/ck/user/login"
    session.post(url, data=data)

    # 我的书架
    rsp = session.get(url="https://user.17k.com/ck/author2/shelf?page=1&appKey=2406394919").json()
    print(rsp)


if __name__ == '__main__':
    main()
