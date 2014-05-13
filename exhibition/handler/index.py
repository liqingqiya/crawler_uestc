#!/usr/bin/env python
#-*- coding:utf-8 -*-

__author__ = 'liqing'

import tornado.web

from tornado.log import logging 

class IndexHandler(tornado.web.RequestHandler):
  """
  TODO
  """

  def get(self):
    """
    TODO
    """
    logging.info("entering IndexHandler...get")
    self.render_string("index.html") 
    logging.info("leaving IndexHandler...get")

  def post(self):
    """
    TODO
    """
    pass
