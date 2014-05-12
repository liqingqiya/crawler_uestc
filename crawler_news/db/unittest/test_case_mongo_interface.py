#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'liqing'

import unittest
import sys
from bson import ObjectId

sys.path.append("../")
sys.path.append("../../")

from util.log import logging
from mongo import *

class TestMongo(unittest.TestCase):

  def test_find_news_by_datetime(self):
    ret = find_news_by_datetime(datetime="2014-04-25")
    print ret

  def test_find_news_by_id(self):
    ret = find_news_by_id(news_id=ObjectId("536ccf856e955202a464671a"))
    print "ret:", ret


if __name__ == "__main__":
  unittest.main()
