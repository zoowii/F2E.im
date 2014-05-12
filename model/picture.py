#!/usr/bin/env python
# coding=utf-8
#
# Copyright 2012 F2E.im
# Do have a faith in what you're doing.
# Make your life a story worth telling.
from __future__ import print_function

from lib.query import Query
from lib import utils


class PictureModel(Query):
    def __init__(self, db):
        self.db = db
        self.table_name = "picture"
        super(PictureModel, self).__init__()

    def gen_picture_url(self, info):
        return utils.get_public_url_by_key(info['store_key'])