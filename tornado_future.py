#!/usr/bin/env python
#-*-coding: utf-8-*-

# Version: 0.1
# Author: Anson Tang <anson.tkg@gmail.com>
# License: Copyright(c) 2015 Anson.Tang
# Summary: 

from tornado.concurrent import Future

from tornado import gen
from tornado.httpclient import AsyncHTTPClient
from tornado.web import RequestHandler
from tornado.ioloop import IOLoop

def Index(RequestHandler):
    @gen.coroutine
    def get(self):
        url = 'www.facebook.com'

        response = yield AsyncHTTPClient().fetch(url)
        print(response.body)


class Test(object):
    def __init(self):
        self.attrib = None
        self.loading = False
        self.future = yield Future()
        self._all_future = list()

    @gen.coroutine
    def load(self):
        print("attrib:%s, loading:%s." % (self.attrib, self.loading))
        if self.attrib is None:
            if self.loading:
                future = yield Future()
                self._all_future.append(future)
            else:
                self.attrib = yield
                self.attrib = 'attrib'

if __name__ == "__main__":
    tt = Test()
    tt.load()
