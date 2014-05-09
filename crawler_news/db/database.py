#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'liqing'

from pymongo import Connection
from bson.objectid import ObjectId
from bson.errors import *
from pymongo import ASCENDING, DESCENDING
from pymongo.errors import *

from util.log import logging

class DB(object):

  _conn = None
  _database = None

  def __init__(self, Parameter):
    """
    mongodb连接
    初始化
    """
    try:
      self.__class__._conn = Connection(Parameter['host'], Parameter['port'])
      self.__class__._database = self.__class__._conn[Parameter.get("file_db", "crawler_db")]
    except Exception, e:
      logging.critical('Failed to connect mongodb: %s' % (e) )
      return None

  @property
  def _db(self):
    return self.__class__._database

  def insert_document(self, collect_name, data):
    """
    data必须是一个json数据 | 字典
    """
    logging.info("enter insert_document...")
    logging.info("data:%s"%data)
    _id = self._db[collect_name].insert(data)
    logging.info("leaveing insert_document...")
    return _id

  def update_document(self, collect_name, condition, data):
    _id = self._db[collect_name].find_and_modify(query=condition, update=data, new=True)
    return _id

  def delete_document(self, collect_name, condition={}):
    self._db[collect_name].remove(condition)


  def find_document(self, collect_name, codition):
    info = self._db[collect_name].find(condition)
    return info
