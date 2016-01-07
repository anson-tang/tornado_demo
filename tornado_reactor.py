#!/usr/bin/env python
#-*-coding: utf-8-*-

# Version: 0.1
# Author: Anson Tang <anson.tkg@gmail.com>
# License: Copyright(c) 2015 Anson.Tang
# Summary: 
from __future__ import print_function

from tornado.ioloop import IOLoop, PeriodicCallback
from datetime import datetime
from time import time

def my_partial(data):
    print("\n %s: in my_partial .............:%s ." % (datetime.now(), data))


def main():
    print(time())
    periodic = PeriodicCallback(lambda:my_partial(time()), 2000)
    periodic.start()

    IOLoop.instance().start()


main()
