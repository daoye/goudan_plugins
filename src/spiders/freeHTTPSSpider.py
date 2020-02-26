#!/usr/bin/env python
# -*- coding: utf-8 -*-


from lxml import etree
from extension.baseSpider import BaseSpider
import logging

class Plugin(BaseSpider):

    def __init__(self):
        BaseSpider.__init__(self)
        self.urls = ['https://31f.cn/https-proxy/']
        self.idle = 10 * 60 #idle 10 miniutes

    def _parse(self, results, text):
        try:
            html = etree.HTML(text)
            rows = html.xpath('//table[@class="table table-striped"]//tr')

            for r in rows[1:]:
                results.append({
                    'host': r[1].text,
                    'port': int(r[2].text),
                    'protocol': 'https',
                    'supportProtocol': 'https',
                    'location': 'cn'
                })
        except Exception as e:
            logging.error("FreeHTTPSSpider error:%s" % e)
