def get_cookie():
    import urllib.request
    import http.cookiejar
    cookie = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open('https://baidu.com/')
    for item in cookie:
        print('%s = %s' % (item.name, item.value))


get_cookie()