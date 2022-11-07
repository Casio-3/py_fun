import requests
from pwn import *

url = 'https://challenge.address/'
charset = string.ascii_letters + string.digits
user = 'N0obcAs10'
entry_url = 'https://example.com/'

s = requests.Session()
s.verify = False
requests.urllib3.disable_warnings(requests.urllib3.exceptions.InsecureRequestWarning)


def solve_pow():
    html = s.get(url=url).text
    task = re.search(r"== \w{6}", html)[0][-6:]
    log.info(f"Q: md5(xxxx)[-6:] == {task}")
    answer = iters.mbruteforce(lambda x: md5sumhex(x.encode())[-6:] == task, alphabet=charset, length=4, method='fixed')
    if answer:
        log.success(f"A: md5({answer}) == {md5sumhex(answer.encode())}")
        return answer
    else:
        log.failure("solution not found, check it.")
        return None


def push_entry(username, entry):
    proof = solve_pow()
    res = s.post(url=url + 'guest/crawl',
                 data={"username": username, "entry": entry, "proof": proof})
    if "Success" in res.text:
        log.success(f"{username} push entry: {entry}")
    else:
        log.failure("push failed.")


push_entry(user, entry_url)
