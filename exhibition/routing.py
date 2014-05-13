#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'liqing'

import handler.index

routing = [
   (r'/',handler.index.IndexHandler),
  ]
