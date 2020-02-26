#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree
from extension.baseSpider import BaseSpider
import logging


class Plugin(BaseSpider):
    
    def __init__(self):
        BaseSpider.__init__(self)
        self.urls = [
            'https://www.kuaidaili.com/free/inha/%s/' % (i) for i in range(1, 50)]
        self.idle = 10 * 60 #idle 10 minutes.

    def _parse(self, results, text):
        try:
            html = etree.HTML(text)
            rows = html.xpath('//div[@id="list"]/table/tbody/tr')

            for r in rows:
                ptype = str.lower(r[3].text)
                results.append({
                    'host': r[0].text,
                    'port': int(r[1].text),
                    'protocol': ptype if ptype != 'socks4/5' else 'socks5',
                    'supportProtocol': ptype,
                    'location': 'cn'
                })
        except Exception as e:
            logging.error("KuaidailiSpider error:%s" % e)
