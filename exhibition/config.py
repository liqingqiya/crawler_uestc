#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'liqing'

import os.path

#template 
TEMPLATE_PATH = "template/"

#static
STATIC_PATH = "static/"

#site path
SITE_PATH = os.path.dirname(os.path.abspath(__file__))

#log file
LOG_FILE = os.path.join(SITE_PATH, "log")
