from pwn import *
import requests

log.level = 'DEBUG'


class Solver:
    def __init__(self, username, password, nonce) -> None:
        self.username = username
        self.password = password
        self.nonce = nonce

    def brute(self, el_random, i) -> bool:
        payload = self.username + self.password + el_random + str(i)
        s256 = sha256sumhex(payload.encode())
        s256hex = int(f'0x{s256}', 16)
        return s256hex < pow(2, 256 - self.nonce)

    def run(self):
        s = requests.Session()

        try:
            resp = s.get("https://security.bilibili.com/crack1/index").text
            el_random = re.search('id="random" type="hidden" value="(.*?)"', resp).group(1)
        except Exception as e:
            log.failure(f'{e}')
            return None

        log.info(f'{self.__dict__}\nrandom value: {el_random}')
        i = iters.mbruteforce(lambda x: self.brute(el_random, x), string.digits, length=7, method='upto')
        if i:
            payload = self.username + self.password + el_random + str(i)
            s256 = sha256sumhex(payload.encode())
            s256hex = int(f'0x{s256}', 16)
            log.debug(f'{s256hex} == s256hex')
            log.debug(f'{pow(2, 256 - self.nonce)} == pow(2, 256 - nonce)')
            r = s.post("https://security.bilibili.com/crack1/login", json={
                "username": self.username,
                "password": self.password,
                "nonce": self.nonce,
                "random": el_random,
                "proof": str(i)
            })
            r.encoding = 'utf-8'
            if r.status_code == 502:
                print('502😅')
                sleep(1.14514)
            else:
                print(r.status_code)
                print(r.text)
        else:
            log.failure(f'Not found.')


username0 = "admin"
password0 = "bili1024"
nonce0 = 20  # fuck your random

while True:
    solver = Solver(username0, password0, nonce0)
    solver.run()
