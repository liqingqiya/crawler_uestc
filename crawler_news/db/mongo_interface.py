#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'liqing'

from util.log import logging
from setting import mongo_backend

"""
mongo_backend逻辑操作
"""
def insert_news(news_dict):
  logging.info("enter insert_news...")
  logging.info("leaving insert_news...")
  return mongo_backend.insert_document("news", news_dict)

def update_news_by_id(news_id, news_dict):
  """
  根据news的唯一id,更新文档
  """
  logging.info("enter update_news_by_id...")
  logging.info("leave update_news_by_id...")
  return mongo_backend.update_document({"_id":news_id}, new_dict)

def delete_news_by_id(news_id):
  """
  根据id号删除文档
  """
  logging.info("enter delete_news_by_id...")
  mongo_backend.delete_document({"_id":news_id})
  logging.info("leave delete_news_by_id...")

def delete_news_by_datetime(datetime):
  """
  根据时间,来删除新闻
  """
  logging.info("enter delete_news_by_datetime...")
  mongo_backend.delete_document({"datetime":datetime})
  logging.info("leave delete_news_by_datetime...")

def find_news_by_datetime(datetime):
  """
  找到一定时间的新闻
  """
  logging.info("enter find_news_by_datetime...")
  logging.info("leave find_news_by_datetime...")
  return mongo_backend.find_document(collect_name="news", condition={"datetime":datetime})

def find_news_by_id(news_id):
  """
  根据id查询news
  """
  logging.info("enter find_news_by_id...")
  logging.info("enter find_news_by_id...")
  return mongo_backend.find_one_document("news", condition={"_id":news_id})

if __name__ == "__main__":
  pass
