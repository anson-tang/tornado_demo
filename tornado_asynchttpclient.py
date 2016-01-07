#!/usr/bin/env python
#-*-coding: utf-8-*-

# Version: 0.1
# Author: Anson Tang <anson.tkg@gmail.com>
# License: Copyright(c) 2015 Anson.Tang
# Summary: 
import urllib

from tornado.ioloop import IOLoop
from tornado.httpclient import AsyncHTTPClient


def handler_request(response):
    if response.error:
        print("Error: ", response.code, response.error)
    else:
        print("TYPE:%s, BODY:%s." % (type(response.body), response.body))
    IOLoop.instance().stop()

if __name__ == "__main__":
    url = 'http://localhost/travian/sysconfig?unzip=1'
    method = 'GET'
    client = AsyncHTTPClient()
    if method == 'GET':
        client.fetch(url, callback=handler_request, method=method)
        IOLoop.instance().start()
    elif method == "POST":
        body = {'name':'war', 'author':'Tom', 'content':'kow...'}
        data = urllib.urlencode(body)
        client.fetch(url, callback=handler_request, method=method, body=data)
        IOLoop.instance().start()
    else:
        print("ERROR！！！")
