#!/usr/bin/env python
#-*-coding: utf-8-*-

# Version: 0.1
# Author: Anson Tang <anson.tkg@gmail.com>
# License: Copyright(c) 2015 Anson.Tang
# Summary: 

import os
import sys
import logging

from logging.handlers import RotatingFileHandler

LEVEL = {'ERROR': logging.ERROR,
       'WARNING': logging.WARNING,
          'INFO': logging.INFO,
         'DEBUG': logging.DEBUG,
         }

#Init logging
def init_logging(filename, level, count=100, max_size=10485760):
    logger = logging.getLogger()
    logger.setLevel(LEVEL[level])
    handler = RotatingFileHandler(filename,
            maxBytes=max_size,
            backupCount=count,
            )
    formatter = logging.Formatter('[%(asctime)s] %(message)s')
    handler.setFormatter(formatter)  
    logger.addHandler(handler)



class Log(object):
    @staticmethod
    def error(*args):
        logging.error("{} {}: {} {}".format("\033[31m[ E ]", (os.path.basename(sys._getframe().f_back.f_code.co_filename), sys._getframe().f_back.f_code.co_name, sys._getframe().f_back.f_lineno), ' '.join((str(a) for a in args)),  "\033[0m"))

    @staticmethod
    def warn(*args):
        logging.warn("{} {}: {} {}".format("\033[33m[ W ]", (os.path.basename(sys._getframe().f_back.f_code.co_filename), sys._getframe().f_back.f_code.co_name, sys._getframe().f_back.f_lineno), ' '.join((str(a) for a in args)), "\033[0m"))

    @staticmethod
    def info(*args):
        logging.info("{} {}: {} {}".format("\033[32m[ I ]", (os.path.basename(sys._getframe().f_back.f_code.co_filename), sys._getframe().f_back.f_code.co_name, sys._getframe().f_back.f_lineno), ' '.join((str(a) for a in args)), "\033[0m"))

    @staticmethod
    def debug(*args):
        logging.debug("{} {}: {} {}".format("\033[37m[ D ]", (os.path.basename(sys._getframe().f_back.f_code.co_filename), sys._getframe().f_back.f_code.co_name, sys._getframe().f_back.f_lineno), ' '.join((str(a) for a in args)), "\033[0m"))

