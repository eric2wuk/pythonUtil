from urllib import request

req = request.Request('http://winonama.cn/')
req.add_header('User-Agent', 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
for i in range(10):
    with request.urlopen(req) as f:
        print('Status:' , f.status, f.reason)
        for k , v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', f.read().decode('utf-8'))
