#!/usr/bin/env python
#-*- coding:utf-8 -*-

import glob
import os
import sys
import fnmatch

root_path = os.path.dirname(os.path.abspath(__file__))

def recurive_remove(path):
  print "enter recurive_remove..."
  print "path:%s"%path
  os.chdir(root_path)
  for item in glob.glob("*.pyc"):
    os.remove(item)

  for item in os.listdir(root_path):
    print "item:%s"%item
    if os.path.isdir(item):
      recurive_remove(item)
  
if __name__ == "__main__":
  recurive_remove(root_path)

  print root_path
  print os.getcwd()
