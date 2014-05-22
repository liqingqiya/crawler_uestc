#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'liqing'

import os.path

#template 
TEMPLATE_PATH = "template/"

#static
STATIC_PATH = "static/"

JS_URL = u"/static/bootstrap/js"
CSS_URL = u"/static/bootstrap/css"
IMG_URL = u"/static/bootstrap/img"

#site path
SITE_PATH = os.path.dirname(os.path.abspath(__file__))

#log 目录
LOG_PATH = os.path.join(SITE_PATH, "log")
#log file
LOG_FILE = os.path.join(LOG_PATH, "web.log")


