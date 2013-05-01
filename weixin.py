import requests

login       = "http://mp.weixin.qq.com/cgi-bin/login?lang=zh_CN"
getMessage  = "http://mp.weixin.qq.com/cgi-bin/getmessage?t=wxm-message&token=689881865&lang=zh_CN&count=50"
user = "username=libsysu%40163.com&pwd=152ed960b613b67008ca54c756b4ced0&imgcode=&f=json"

r = requests.post(login, data=user)
cookie = []
for c in r.cookies:
    cookie.append(c.value)
cookies = {}
cookies['cert']         = cookie[0]
cookies['slave_sid']    = cookie[1]
cookies['slave_user']   = cookie[2]

#print requests.get("http://httpbin.org/cookies", cookies=cookies).text

#print requests.get("http://httpbin.org/get", cookies=cookies).content
Message = requests.get(getMessage, cookies=cookies)
print Message.content

