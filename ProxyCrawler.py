#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Michael Shen'

import requests
from bs4 import BeautifulSoup
import re

class ProxyCrawler:
    def __init__(self):
        self.ProxyWebUrl_kuaidaili = 'http://www.kuaidaili.com/free/inha/'
        self.header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'www.kuaidaili.com',
            'Referer': 'http://www.kuaidaili.com/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
        }
        self.list_proxyAddr = []
        self.avilableProxy = set()
        self.ProxyWebUrl_xicidaili = "http://www.xicidaili.com/nn/"
        self.header_xici = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'www.xicidaili.com',
            'Referer': 'http://www.kuaidaili.com/',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
        }

    def crawler_kuaidaili(self, pageNum):
        currentPageUrl = self.ProxyWebUrl_kuaidaili + str(pageNum)
        response = requests.get(currentPageUrl, headers=self.header)
        soup = BeautifulSoup(response.text, 'html.parser')
        tag = soup.find_all(id='list')[0]
        td_list = tag.find_all('td')
        for i in range(len(td_list)):
            if i % 7 == 0:
                self.list_proxyAddr.append(str(td_list[i].string) + ':' + str(td_list[i + 1].string))
                # with open('proxyAddress.txt','w') as f:
                #     for addr in self.list_proxyAddr:
                #         f.write(addr+'\n')

    def crawler_xicidaili(self,pageNum):
        currenturl = self.ProxyWebUrl_xicidaili + str(pageNum)
        response = requests.get(currenturl,headers = self.header_xici)

        patternIp = re.compile('\d+\.\d+\.\d+\.\d+')
        patternPort = re.compile('<td>\d\d+</td>')
        ip = patternIp.findall(response.text)
        port = patternPort.findall(response.text)
        for i in range(len(ip)):
            self.list_proxyAddr.append(ip[i]+":"+port[i][4:-5])


    def isAvailable(self, ipaddress):
        proxy_para = dict()
        proxy_para['http'] = ipaddress
        try:
            response = requests.get('http://www.baidu.com', headers={
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate, sdch',
                'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Host': 'www.baidu.com',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
            }, proxies=proxy_para, timeout=3)
            return True
        except Exception as err:
            return False

    def startCrawler(self,pageNum):
        self.crawler_kuaidaili(pageNum)
        self.crawler_xicidaili(pageNum)

        # with open('proxyAddress.txt', 'w') as f:
        #     for addr in self.list_proxyAddr:
        #         f.write(addr + '\n')

        # for i in range(1, 1000):
        #     item = random.choice(self.list_proxyAddr)
        #     if self.isAvailable(item):
        #         self.avilableProxy.add(item)
        #
        # with open('proxyAddress.txt', 'w') as f:
        #     for addr in self.avilableProxy:
        #         f.write(addr + '\n')



# c = ProxyCrawler()
# # c.startCrawler()
# # print(c.isAvailable('211.167.248.228:8080'))
# for i in range(1,20):
#     c.startCrawler(i)
#     print(i)
#     with open('proxyAddress.txt', 'w') as f:
#         for addr in c.list_proxyAddr:
#             f.write(addr + '\n')
# c.crawler_xicidaili(1)