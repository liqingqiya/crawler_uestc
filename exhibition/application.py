#!/usr/bin/env python
#-*- coding:utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options
import tornado.log

from tornado.options import define, options
from tornado.log import logging

import modules
import config

from routing import routing

define("port", default = 8000, help = "")

class Application(tornado.web.Application):

  def __init__(self):
    settings = dict(
        ui_module = modules,
        template_path = config.TEMPLATE_PATH, 
        static_path = config.STATIC_PATH,
        site_path = config.SITE_PATH,
        autoescape = None,
        debug = True
        )
    super(Application, self).__init__(routing, **settings)

def start():
  #options.log_file_prefix = config.LOG_FILE  #set log file
  tornado.options.options.logging = "debug"
  tornado.options.parse_command_line()
  try:
    application = Application()

    logging.info("start server...")

    httpserver = tornado.httpserver.HTTPServer(application)
    httpserver.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
  except Exception,e:
    logging.critical("start failed!")
    logging.error("%s"%str(e))

if __name__ == "__main__":
  start()
