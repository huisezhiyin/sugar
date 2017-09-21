import os
import binascii

binascii.b2a_base64(os.urandom(24))[:-1]
