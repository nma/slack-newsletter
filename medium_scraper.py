#!/usr/bin/python3
# -*- coding: utf8 -*-
import requests
import attr
import json
import re
from attr.validators import instance_of

ROOT_URL = "https://medium.com/"
ESCAPE_CHARACTERS = "])}while(1);</x>"
ACCEPT_HEADER = {"Accept": "application/json"}


@attr.s
class MediumReader(object):
    user = attr.ib(validator=instance_of(str))
    escaper = re.compile(r'{}'.format(re.escape(ESCAPE_CHARACTERS)))

    def __sliding_window_paginator(self):
        pass

    def get_posts(self) -> dict:
        response = requests.get('{}/{}/latest?format=json'.format(ROOT_URL, self.user))
        return json.loads(self.escaper.sub('', response.text))
