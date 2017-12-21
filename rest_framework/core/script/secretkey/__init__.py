# -*- coding: utf-8 -*-
"""
密钥生成命令，比如AES的密钥
"""
import base64
import string

from rest_framework.core.exceptions import CommandError
from rest_framework.core.script.base import Manager
from rest_framework.utils.functional import get_random_string
from rest_framework.utils.transcoder import force_bytes

__author__ = 'caowenbin'

SecretKeyCommand = Manager(usage='密钥生成命令')


@SecretKeyCommand.option('-l', '--length', dest='length', type=int, default=16, help="密钥长度，值只能为16、24、32")
@SecretKeyCommand.option('-c', '--allowed_chars', dest='allowed_chars', default=None, help="生成密钥的字符集")
def aes(app, length=16, allowed_chars=None):
    """
    AES密钥
    """
    if length not in (16, 24, 32):
        raise CommandError("密钥长度只能为16、24或32")

    if allowed_chars is None:
        allowed_chars = string.digits + string.ascii_letters + string.punctuation

    key = get_random_string(length=length, allowed_chars=allowed_chars)
    key_bytes = force_bytes(key)
    aes_key = base64.b64encode(key_bytes).rstrip(b"=")
    print("AES KEY:", aes_key)