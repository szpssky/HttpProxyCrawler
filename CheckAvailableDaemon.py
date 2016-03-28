#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Michael Shen'

import requests
import random
import time


def check():
    # while (True):
    count = 0
    i = 0
    proxy_para = dict()
    with open('proxyAddress.txt', 'r') as f:
        list_addr = f.readlines()
        len_addr = len(list_addr)
    if len_addr == 0:
        print("无可用代理服务器地址,本轮不检测")
        # break
    while (True):

        try:
            i = random.randint(0, len(list_addr) - 1)
            ipaddress = list_addr.pop().strip('\n')
            proxy_para['http'] = ipaddress
        except Exception as err:
            print('随机失败' + str(err))
            if i == 0:
                break
            continue

        count += 1
        try:
            response = requests.get('http://www.baidu.com/', headers={
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate, sdch',
                'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Host': 'www.baidu.com',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
            }, proxies=proxy_para, timeout=2)
            with open('test.html') as f:
                f.write(response.txt)
            list_addr.append(proxy_para['http'])
        except Exception as err:
            print("检测到:" + proxy_para['http'] + '连接失败,移除该地址')
        print(count)
        if count == len_addr:
            with open('proxyAddress.txt', 'w') as f:
                for addr in list_addr:
                    f.write(addr.strip('\n') + '\n')
            break
    print('检测完成停止30分钟')
    list_addr.clear()
    # break
