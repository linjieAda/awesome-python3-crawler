# -*- coding: utf-8 -*-

import requests
from pyquery import PyQuery as pq
import re

headers ={
    #这边cookie替换成你的cookie
    'Cookie':'_s_tentry=-; Apache=2043009155772.877.1493366305502; SINAGLOBAL=2043009155772.877.1493366305502; ULV=1493366305511:1:1:1:2043009155772.877.1493366305502:; SSOLoginState=1493366438; CONTENT-HONGBAO-G0=7d445b5a50e3de93469daee37a45469d; SCF=AkMy7_Xi59AJxSCTwwO3adXohgohWBNBfX9aBCZfhgoD9TFk0qRENQxYDglr0TzR9SxElHL3e0WE1PtxUcrywIQ.; SUB=_2A250BoehDeThGeVP7FIX8SfIzz-IHXVXdf5prDV8PUJbmtBeLRPlkW-XLIuCXAIvnP2vDcZhDfT7CBhzGw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWovnjVGuZEu81ysCgRl4wJ5JpX5o2p5NHD95Q0eKM7So24ShB0Ws4Dqcj.i--Xi-zRiKn7i--fi-isi-zfi--RiKyWi-zpi--ci-88iKyF; SUHB=0auQ6x26IsPlbV; ALF=1524902765; UOR=,,login.sina.com.cn,',
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
}

def getuid():
    url = 'http://chunjie.hongbao.weibo.com/hongbao2017/h5index'
    z = requests.get(url, headers=headers)
    if z.status_code == 200:
        d = pq(z.content)
        alluidHtml = d('.m-auto-box')
        alluid = []
        for i in alluidHtml:
            alluid.append(d(i).attr('action-data'))
        alluid = [alluid[0]]
        return alluid

def getst(url):
    # 带上request headers
    z = requests.get(url, headers)
    jscode = z.content.decode('utf-8')
    print(type(jscode))
    print(jscode)
    matchObj = re.match(r"(weibo)", jscode)
    # matchObj = re.match(r"st:'(.*?)'", jscode)
    print(matchObj)
    print(matchObj.group())
    print(matchObj.group(1))

# def testExample():
#     str = "st:'57e91c', '"
#     print(type(str))
#     matchObj = re.match(r"st:'(.*?)'", str)
#     print(matchObj, matchObj.group(), matchObj.group(1))

if __name__ == '__main__':
    # testExample()
    uids = getuid()
    for uid in uids:
        # 生成红包页面的url
        url = 'http://hongbao.weibo.com/h5/aboutyou?groupid=1000110&ouid=%s' % uid
        getst(url)