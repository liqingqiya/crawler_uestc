#!/usr/bin/env python
#-*- coding:utf-8 -*-

import glob
import os
import sys

root_path = os.path.dirname(os.path.abspath(__file__))

def recurive_remove(path):
  os.chdir(root_path)
  for item in os.listdir(root_path):
    if os.path.isdir(item):
      recurive_remove(item)
    else:
      if fnmatch.fnmatch(item, "*.pyc"):
        os.remove(item)
        print "remove:%s"%item

  
if __name__ == "__main__":
  recurive_remove(root_path)

  print root_path
  print os.getcwd()
