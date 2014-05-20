#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'liqing'

import logging

FORMAT = "%(name)s:%(levelname)s:%(module)s:%(lineno)d:%(message)s"

logging.basicConfig(format=FORMAT, level = logging.DEBUG)


if __name__ == "__main__":
  logging.info("just a test message")
