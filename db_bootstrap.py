#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys

from datetime import datetime

__author__ = 'Daniel'


def start_stamp(func):
  """decorator
  """
  def ret(*args):
    print ("%s: exec %s" % (str(datetime.now()), func.__name__))
    return func(*args)

  return ret


class Connection(object):
  def __init__(self, db_name, default_file):
    print "running at db: %s" % (db_name)
    self.con = mdb.connect(read_default_file=default_file, db=db_name)
    # cur = self.con.cursor()
    # self.con.commit()
