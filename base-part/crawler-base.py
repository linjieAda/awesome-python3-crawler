# _*_ coding: utf-8 _*_

"""
python_spider.py by xianhu
"""

import urllib.error
from urllib.parse import urlencode
from urllib.request import  HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, HTTPCookieProcessor, urlopen, Request, ProxyHandler, build_opener, install_opener
import http.cookiejar

# 定义变量
url = 'https://www.zhihu.com/login/phone_num'
headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}

# 最简单的抓取方式
response = urlopen(url, timeout=10)
html = response.read().decode('utf-8')

# 使用Request实例代替url
request = Request(url, data=None, headers={})
response = urlopen(request, timeout=10)

# 发送数据，在Request中添加data参数
data = urlencode({ 'captcha': 'htpd', '_xsrf': '383a2997c38f11c513d4cbe7a4b2b00b'})
request = Request(url, data=data) #POST方法
request = Request(url + '?%s' % data) #GET方法
response = urlopen(request, timeout=10)
print(response.read())

# 发送Header, 即在Request()中添加header的参数
request = Request(url, data=data, headers=headers)
request.add_header('Referer', 'http://www.baidu.com') #另一种添加header方式
response = urlopen(request, timeout=10)

# 网页抓取引发异常;
try:
    urlopen(request, timeout=10)
except urllib.error.HTTPError as e:
    print(e.code, e.reason)
except urllib.error.URLError as e:
    print(e.errno, e.reason)


#使用代理，防IP被封或IP次数受限
proxy_handler = ProxyHandler(proxies={'http': '111.123.76.12:8080'})
opener = build_opener((proxy_handler))  #直接用代理方式打开
response = opener.open(url)

install_opener(opener)  # 安装全局opener，
response = urlopen(url)

# 使用cookie和cookiejar, 应对服务器检查
cookie_jar = http.cookiejar.CookieJar
cookie_jar_handler = HTTPCookieProcessor(cookiejar=cookie_jar)
opener = build_opener(cookie_jar_handler)
response = opener.open(url)

# 发送在浏览器中获取的cookie，两种方式：
#（1）直接放到headers里
headers = {
    "User-Agent": "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)",
    "Cookie": "PHPSESSID=btqkg9amjrtoeev8coq0m78396; USERINFO=n6nxTHTY%2BJA39z6CpNB4eKN8f0KsYLjAQTwPe%2BhLHLruEbjaeh4ulhWAS5RysUM%2B; "
}
request = Request(url, headers=headers)

# (2) 构建cookie， 添加到cookiejar中
cookie = http.cookiejar.Cookie(name='name', value='xx', domain='xx')
cookie_jar.set_cookie(cookie)
response = opener.open(url)

# 抓取网页中的图片，同样适用于文件
response = urlopen('http://ww3.sinaimg.cn/large/7d742c99tw1ee7dac2766j204q04qmxq.jpg')
with open('test.jpg', 'wb') as file_img:
    file_img.write(response.read())

# HTTP认证: HTTP身份验证
password_mgr = HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(realm=None, uri=url, user='user', passwd='password')
handler = HTTPBasicAuthHandler(password_mgr)
opener = build_opener(handler)
response = opener.open(url, timeout=10)
