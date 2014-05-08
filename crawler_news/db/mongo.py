#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'liqing'

from util.log import logging
from setting import mongodb

"""
mongodb逻辑操作
"""
def insert_news(news_dict):
  logging.info("enter insert_news...")
  logging.info("leaving insert_news...")
  return mongodb.insert_document("news", news_dict)

def update_news(condition, news_dict):
  pass

def delete_news():
  pass

def find_news():
  pass


