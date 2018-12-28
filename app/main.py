#!/usr/bin/env python
# -*- coding: utf-8 -*-

from webapp2 import WSGIApplication, Route

from handlers.main import AdminPage, MainPage, StoriesJson, StoryJson


ADMIN_HANDLERS = [
    Route(AdminPage.URL, AdminPage),
]
APP_HANDLERS = [
    Route(StoryJson.URL, StoryJson),
    Route(StoriesJson.URL, StoriesJson),

    Route(MainPage.URL, MainPage)
]

admin = WSGIApplication(ADMIN_HANDLERS, debug=True)
app = WSGIApplication(APP_HANDLERS, debug=True)
