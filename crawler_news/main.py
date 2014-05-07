#!/usr/bin/env python
#-*- coding:utf-8 -*-

import time
import os

from bs4 import BeautifulSoup
from util.log import logging
from util import tool
from config import URL

if __name__=="__main__":
  try:
    #获得最大页数，确定爬虫范围
    last_page_number = tool.get_last_web_page_number()
    #打开文件
    current_dir = os.path.dirname(__file__)
    yyyy = time.strftime("%Y")
    mm = time.strftime("%m")
    dd = time.strftime("%d")
    folder = os.path.join(current_dir, yyyy, mm, dd)
    if not os.path.exists(folder):
      os.makedirs(folder)
    os.chdir(folder)
    logging.debug(last_page_number)
    for i in range(1,last_page_number+1):
      with open("news_%s.json"%i, "w+") as news:
        #获取页面
        page = tool.get_web_page_by_url(URL.format(page_number=i))
        #解析
        for item_json_data in tool.load_and_parse(page):
          #写入文件
          news.write(item_json_data+"\n")

    logging.info("success!")
  except:
    logging.error("fail!")


