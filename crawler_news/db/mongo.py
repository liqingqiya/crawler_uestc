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

def update_news_by_id(news_id, news_dict):
  """
  根据news的唯一id,更新文档
  """
  return update_document({"_id":news_id}, new_dict)

def delete_news_by_id(news_id):
  """
  根据id号删除文档
  """
  mongodb.delete_document({"_id":news_id})

def delete_news_by_datetime(datetime):
  """
  根据时间,来删除新闻
  """
  mongodb.delete_document({"datetime":datetime})

def find_news_by_datetime(datetime):
  """
  找到一定时间的新闻
  """
  return mongodb.find_document({"datetime":datetime})

def find_news_by_id(news_id):
  """
  根据id查询news
  """
  return mongodb.find_document({"_id":news_id})
