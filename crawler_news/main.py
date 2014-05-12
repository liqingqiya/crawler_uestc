#!/usr/bin/env python
#-*- coding:utf-8 -*-

import time
import os

from bs4 import BeautifulSoup
from util.log import logging
from util import tool
from config import URL

if __name__=="__main__":
  logging.info("crawling...")

  #将数据爬下来,并写到本地的json文件中
  tool.write_to_json_file()

  #将爬下来的数据写入到mongo数据库,以便将来分析
  tool.write_to_mongo_db()

  logging.error("success!")


