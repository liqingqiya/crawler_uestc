#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'liqing'

from mongo_backend import DB

#数据库配置
DATABASE_SETTINGS = {
  "host": "localhost",
  "port": 27017,
  "data_file":"rainbow",
  "max_pool_size":10,
}

mongo_backend = DB(DATABASE_SETTINGS)
