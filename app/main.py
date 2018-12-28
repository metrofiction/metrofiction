#!/usr/bin/env python
# -*- coding: utf-8 -*-

from webapp2 import WSGIApplication, Route

from handlers.main import HelloPage, AdminPage, MainPage


ADMIN_HANDLERS = [
    Route(AdminPage.URL, AdminPage),
]
APP_HANDLERS = [
    Route(HelloPage.URL, HelloPage),
    Route(MainPage.URL, MainPage)
]

admin = WSGIApplication(ADMIN_HANDLERS, debug=True)
app = WSGIApplication(APP_HANDLERS, debug=True)
