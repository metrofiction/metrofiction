#!/usr/bin/env python
# -*- coding: utf-8 -*-

from handlers import BaseHandler


class MainPage(BaseHandler):
    URL = r'/<:.*>'

    def get(self, value=None):
        self._render_html('index.html')


class HelloPage(BaseHandler):
    URL = r'/hello'

    def get(self, value=None):
        self._render_html('hello.html')


class AdminPage(BaseHandler):
    URL = r'/admin/<:.*>'

    def get(self, value=None):
        self._render_html('admin.html')
