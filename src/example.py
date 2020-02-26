#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pony.orm import *
from core.data import ProxyItem
from datetime import datetime, timedelta
import logging

class Plugin():
    def start(self, hosting):
        logging.debug('local plugin running...')
        with db_session:
            if not exists(x for x in ProxyItem if x.protocol=='http' and x.host=='0.0.0.0' and x.port==8000):
                expired = int((datetime.now() + timedelta(days=360*10)).timestamp())
                ProxyItem(protocol='http', supportProtocol='http/https', host='127.0.0.1', port=8000, expired=expired,isok=True,validCount=0,failedCount=0)
