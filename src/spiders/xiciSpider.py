#!/usr/bin/env python
# -*- coding: utf-8 -*-


from lxml import etree
from extension.baseSpider import BaseSpider
import logging

class Plugin(BaseSpider):
    def __init__(self):
        BaseSpider.__init__(self)
        self.urls = [
            'http://www.xicidaili.com/',
            'http://www.xicidaili.com/nn/',
            'http://www.xicidaili.com/nt/',
            'http://www.xicidaili.com/wn/',
            'http://www.xicidaili.com/wt/'
        ]

    def _parse(self, results, text):
        html = etree.HTML(text)
        rows = html.xpath('//table[@id="ip_list"]/tr[@class!="subtitle"]')

        for r in rows:
            try:
                ptype = str.lower(r[5].text)
                results.append({
                    'host': r[1].text,
                    'port': int(r[2].text),
                    'protocol': ptype if ptype != 'socks4/5' else 'socks5',
                    'supportProtocol': ptype,
                    'location': 'cn'
                })
            except:
                logging.error("XiciSpider error:%s" % e)
