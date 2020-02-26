#!/usr/bin/env python
# -*- coding: utf-8 -*-


from extension.baseSpider import BaseSpider
import json
import logging

class Plugin(BaseSpider):
    '''data from https://github.com/jiangxianli/ProxyIpLib'''

    def __init__(self):
        BaseSpider.__init__(self)
        self.urls = ['http://ip.jiangxianli.com/api/proxy_ips']
        self.idle = 60 * 30 # idle 30 miniutes.

    def _parse(self, results, text):
        try:
            data = json.loads(text)

            if data.get('code') != 0:
                return
            data = data.get('data')

            for r in data.get('data'):
                results.append({
                    'host': r.get('ip'),
                    'port': int(r.get('port')),
                    'protocol': r.get('protocol'),
                    'supportProtocol': r.get('protocol'),
                    'location': 'cn'
                })
                
            self.next = data.get('next_page_url')
        except Exception as e:
            logging.error("FreeHTTPSpider error:%s" % e)
