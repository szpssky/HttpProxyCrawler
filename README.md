# HttpProxyCrawler

获取Http代理服务器地址的爬虫程序，主要从2个免费代理网站爬取,地址列表保存在proxyAddress.txt中，爬取的服务器地址每隔1小时自动更新并进行可用性检测

linux系统可使用以下命令后台运行
```shell
nohup python3 main.py &
```



