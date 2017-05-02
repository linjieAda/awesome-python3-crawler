import requests
import time
import hashlib

def hax_md5(str):
    md5 = hashlib.md5()
    md5.update(str.encode('utf-8'))
    return md5.hexdigest()

_h5_tk_ = 'IzkOzY2K+CX0A0Bg51LvUQKXRgOZzLAGUSN7yLmh0Wp05u8UdcFTTg=='
cookie_sign = 'Po+D4nUgg5bFq6BIAGJ7gvPYpDRsNfwaswCybBccJkX6w8/qCDmjnonsyt3QGODN+Ua2uzBu2etFjvmY0Prs9XAEX6vUV7OM'

def getToken():
    tk = _h5_tk_
    return tk

def getApiSign(jsondata):
    dataArray = sorted(jsondata)
    strData = ''
    for oneData in dataArray:
        strData = strData + oneData + str(jsondata[oneData])
    strData = strData + getToken()
    print(strData)
    return hax_md5(strData)

def getPayload():
    basedata = {
        'appKey': 999,
        'timestamp': int(round(time.time() * 1000)),
        'v': 1.0,
        'method': 'shopAround.getAttract',
        'shopCode': '51c21cae12094cf988759ccb2dc4ff1c',
      }
    sign = getApiSign(basedata)
    return sign

payload = {
    'appKey': 999,
    'timestamp': int(round(time.time() * 1000)),
    'v': 1.0,
    'method': 'shopAround.getAttract',
    'shopCode': '51c21cae12094cf988759ccb2dc4ff1c',
    'sign': getPayload()
}

url = 'http://api.h.t0.isspu.com/router'

cookies = {
    'sign': cookie_sign,
    '_h5_tk_': _h5_tk_
}

r = requests.post(url, data=payload, cookies=cookies)
print(r.text)