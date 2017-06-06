# -*- coding: utf-8 -*-

import jinja2
from jinja2 import nodes
from jinja2.ext import Extension

from  passlib.hash import sha512_crypt


def _passlib_hash(passwd):
#         return sha512_crypt.encrypt(passwd)
        return sha512_crypt.using(rounds=5000).encrypt(passwd)

class Passlib_ext(Extension):
    tags = set(['passlib_hash'])

    def __init__(self, environment):
        super(Passlib_ext, self).__init__(environment)

        # add the defaults to the environment
        environment.filters['passlib_hash'] = _passlib_hash
