def u_encode(text: str):
    return ''.join(r'\u{:04x}'.format(ord(char)) for char in text)


def u_decode(unicode: bytes):
    return unicode.decode('unicode_escape')


if __name__ == '__main__':
    print(u_encode('Ca5io3'))

    print(u_decode(b'\u0063\u0073\u0061'))
