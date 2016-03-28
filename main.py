#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Michael Shen'

import ProxyCrawler
import CheckAvailableDaemon
import time
import threading

print("代理服务器地址抓取开始..................")
crawler = ProxyCrawler.ProxyCrawler()
for i in range(1,10):
    crawler.startCrawler(i)
    with open('proxyAddress.txt', 'w') as f:
        for addr in crawler.list_proxyAddr:
            f.write(addr + '\n')
print('初始化抓取完成,已生成文本文件............')
del crawler
while(True):
    # t = threading.Thread(target=CheckAvailableDaemon.check, name='LoopThread')
    # t.setDaemon(True)
    # t.start()
    #
    print("开始进行服务器可用性检测.............")
    CheckAvailableDaemon.check()
    CheckAvailableDaemon.check()
    print('1小时候后更新ip地址集')
    time.sleep(3600)
    crawler = ProxyCrawler.ProxyCrawler()
    crawler.startCrawler(1)
    with open('proxyAddress.txt', 'a') as f:
        for addr in crawler.list_proxyAddr:
            f.write(addr + '\n')
    del crawler


