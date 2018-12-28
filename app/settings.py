#!/usr/bin/env python
# -*- coding: utf-8 -*-
ENV = 'LOCAL'

GCP_SCOPES = [
    'https://www.googleapis.com/auth/cloud-platform',
    'https://www.googleapis.com/auth/bigquery'
]

SPREADSHEET_SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets.readonly'
]
CALENDARS_SCOPES = [
    'https://www.googleapis.com/auth/calendar.readonly'
]

SCOPES = GCP_SCOPES+SPREADSHEET_SCOPES+CALENDARS_SCOPES

IMPORT_BUCKET_NAME = 'clake-dev-import'

GOOGLE_USER_ADMIN = 'apps@cirruseo.com'
OWNER_DOCS = 'owner.docs@cirruseo.com'
ADMIN_GROUP = 'si@cirruseo.com'

# CLIENTS ID / SECRET
JS_CLIENT_ID = '493163773964-lekvhh8avfku4b3aihlh8k4e554odorf.apps.googleusercontent.com'
JS_CLIENT_SECRET = 'smdlbYymrs-DauCXwKZCeOus'
API_KEY = 'AIzaSyC9W_lK2LgC6NuZJ6cE2T6i47UGnxgdOxI'
AUTH_SCOPES = [
    'https://www.googleapis.com/auth/userinfo.email'
]
