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
    logging.info("leave insert_document...")
    return _id

  def update_document(self, collect_name, condition, data):
    logging.info("enter update_document...")
    _id = self._db[collect_name].find_and_modify(query=condition, update=data, new=True)
    logging.info("leave update_document...")
    return _id

  def delete_document(self, collect_name, condition={}):
    logging.info("enter delete_document...")
    self._db[collect_name].remove(condition)
    logging.info("leave delete_document...")


  def find_document(self, collect_name, condition={}):
    """
    提供mongo数据库底层的数据查询
    """
    logging.info("enter find_document...")
    logging.info("collect_name=%s condition=%s"%(collect_name, condition))
    info = self._db[collect_name].find(condition)
    logging.info("leaving find_document...")
    #查询返回的是一个游标实例,具有迭代环境
    return list(info)

  def find_one_document(self, collect_name, condition={}):
    """
    find only one document
    """
    logging.info("enter find_one_document...")
    logging.info("collect_name=%s condition=%s"%(collect_name, condition))
    logging.info("leave find_one_document...")
    #返回一个字典
    return self._db[collect_name].find_one(condition)

