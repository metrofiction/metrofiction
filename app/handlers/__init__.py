#!/usr/bin/env python
# -*- coding: utf-8 -*-

from webapp2 import RequestHandler

from appengine_config import JINJA_ENVIRONMENT


class BaseHandler(RequestHandler):

    @staticmethod
    def _get_template(html):
        return JINJA_ENVIRONMENT.get_template(html)

    def _render_html(self, template, params={}, code=200):
        page = self._get_template(template)
        self.response.set_status(code)
        self.response.write(page.render(**params))
