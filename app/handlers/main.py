#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from handlers import BaseHandler


class MainPage(BaseHandler):
    URL = r'/<:.*>'

    def get(self, value=None):
        self._render_html('index.html')


class AdminPage(BaseHandler):
    URL = r'/admin/<:.*>'

    def get(self, value=None):
        self._render_html('admin.html')


class StoriesJson(BaseHandler):
    URL = r'/stories'

    def get(self):
        self.response.set_status(200)
        self.response.headers['Content-Type'] = 'application/json'
        obj = {
            'id': 1,
            'text': True,
            'img': 'https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwiR3eiPusLfAhUC0BoKHfY4DcQQjRx6BAgBEAU&url=https%3A%2F%2Fpixabay.com%2Ffr%2Fimg-src-x-ciaoo-pic-2310895%2F&psig=AOvVaw25zaXR8f1GYDIuilJaDrz3&ust=1546084067272379',
        }
        self.response.out.write(json.dumps([obj for i in range(0, 10)]))


class StoryJson(BaseHandler):
    URL = r'/story/<id:.*>/<page:.*>'

    def get(self, id=None, page=None):
        self.response.set_status(200)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json.dumps({
            'id': id,
            'page': page,
        }))
