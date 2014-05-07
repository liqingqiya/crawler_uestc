#!/usr/bin/env python
#-*- coding:utf-8 -*-

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

from util import logging

mongo_client = None
try:
  mongo_client = MongoClient(host = "127.0.0.1", port = 27017)
  logging.info("MongoDB connected successfully")
except ConnectionFailure, e:
  logging.error("Could not connect to MongoDB:%s"%str(e))
