#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'liqing'

import unittest
import sys
import json

sys.path.append("../")
sys.path.append("../../")

from util.log import logging
from database import DB
from mongo import find_news_by_datetime
from setting import mongodb

class TestDatabase(unittest.TestCase):

  def test_find_document(self):
    ret = mongodb.find_document(collect_name="news", condition={"datetime":"2014-04-25"})
    for i in ret:
      print i
    #print list(ret)
    #print ret[0]
  def test_find_one_document(self):
  def test_insert_document(self):
  def test_update_document(self):
  def test_delete_document(self):

if __name__ == "__main__":
  unittest.main()
