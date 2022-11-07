import requests

proxy = {
    'http': 'http://127.0.0.1:8080'
}
# header = {
#     "Content-type": "application/x-www-form-urlencoded"
# }


def main():
    url = 'http://httpbin.org/post'
    data = {
        'key': 'value'
    }
    r = requests.post(url, data=data, proxies=proxy)
    print(r.text)


if __name__ == '__main__':
    main()
