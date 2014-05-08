#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'liqing'

import json
import os

from bs4 import BeautifulSoup
from util.log import logging
from util import tool
from config import URL
from db.mongo import *
import requests

#从已经下载下来的html文件解析,并写入json文件
def write():
  #打开文件
  fi = open("jiaowuchu.html","r")
  with open("news.json", "w+") as news:
    for item_json_data in tool.load_and_parse(page = fi):
      #写入文件
      news.write(item_json_data+"\n")
  logging.info("success!")

#将上一步写的文件按行打印出来
def read():
  with open("news.json","r") as news:
    for line in news:
      json_data = json.loads(line)
      print "title", json_data["title"]
      print "link", json_data["link"]
      print

#请求一个网页
def get_page():
  r = requests.get(url=URL)
  with open("uestc_test.html","w") as fi:
    fi.write(r.content)

  soup = BeautifulSoup(r.body)
  with open("uestc_test_soup.html","w") as fi:
      fi.write(soup.prettify().encode("utf-8"))

#使用tool.py的函数,获得page
def get_fixed_page():
  page = tool.get_web_page_by_url(url=URL)
  with open("uestc_test_fixed.html","w") as fi:
    #fi.write(page.encode("utf-8"))
    fi.write(page)

def read_all_news():
  current_folder = os.path.dirname(__file__)
  os.chdir(os.path.join(current_folder,"2014/05/07"))
  with open("news.txt","a+") as fi:
    for i in xrange(1,12):
      with open("news_%s.json"%i,"r") as news:
        for line in news:
          json_data = json.loads(line)
          print >>fi, "title", json_data["title"].encode("utf-8")
          print >>fi, "link", json_data["link"].encode("utf-8")
          print >>fi

def start_mongo():
  """
  启动mongo数据库
  """
  insert_news({"d":1})

if __name__=="__main__":
  # write()
  # read()
  # get_page()
  # get_fixed_page()
  #read_all_news()
  start_mongo()
