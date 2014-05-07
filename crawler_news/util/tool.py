#!/usr/bin/env python
#-*- coding:utf-8 -*-

import json
import tempfile
import re
import requests

from bs4 import BeautifulSoup

from config import URL

def get_last_web_page_number():
  """
  解析web page，获得最大页数
  """
  r = get_web_page_by_url(url = URL.format(page_number=1))
  soup = BeautifulSoup(r)
  max_number = int(soup.find("div", attrs={"id":"pageTurnning"}).find("span", attrs={"class":"pageinfo"}).strong.get_text())
  return max_number

def get_web_page_by_url(url):
  """
  获得html文件，并且要检验该文件是否符合规范
  如果不符合，修复成规范html文件，然后返回
  由于我们学校的奇葩,get请求返回了多个html标签
  特此修复,不然beautifulsoup会自动裁剪,漏掉我们需要的信息.
  """
  #create a temp file
  temp = tempfile.TemporaryFile()
  temp_1 = tempfile.TemporaryFile("a+")
  remove_1 = re.compile("""<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">""")
  remove_2 = re.compile("""<.*html.*>""")
  raw_data = requests.get(url=url).content
  # print type(raw_data)
  # temp.write(raw_data.encode("utf-8"))
  temp.write(raw_data)

  #seek(0)是必须的,写完文件的时候已经写到了文件末尾.
  temp.seek(0)
  for i in temp:
    if remove_1.match(i) is None and remove_2.match(i) is None:
      temp_1.write(i)
  temp_1.seek(0)
  soup = BeautifulSoup(temp_1.read())

  #这里需要进行utf-8编码
  return soup.prettify().encode("utf-8")


def load_and_parse(page):
  """
  传入，加载html文件对象 | 或者字符串
  并解析
  最后返回一系列json数据包
  """
  soup = BeautifulSoup(page)
  news_list = soup.find("div", id="AbroadStudy_menu")
  result = news_list.find_all("a", attrs={"target":"_blank","href":True})
  for item in result:
    json_data = json.dumps(dict(title=item["title"], link=item["href"]))
    yield json_data

if __name__ == "__main__":
  pass
