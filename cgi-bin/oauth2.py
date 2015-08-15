#!/usr/bin/python

import os

from httplib2 import Http
import oauth2client
import gflags
from oauth2client import tools
from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.tools import run_flow
from oauth2client.tools import run
from oauth2client.file import Storage

SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'

home_dir 		= os.path.expanduser('~')
credential_dir	= os.path.join(home_dir, '.credentials')

if not os.path.exists(credential_dir):
	os.makedirs(credential_dir)

credential_path	= os.path.join(credential_dir, 'calendar.json')

store 			= oauth2client.file.Storage(credential_path)
credentials		= store.get()

if not credentials or credentials.invalid:
	flow			= flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
	flow.user_agent	= "test_application"
	credentials 	= run(flow, store)

	print 'Storing credentials to ' + credential_path

service		= build('calendar', 'v3', http=credentials.authorize(Http()))
calendars	= service.calendarList().list().execute()
print "Content-type: text/html\n"

for calendar in calendars['items']:
	print calendar['id'].encode('utf-8')
	print calendar['summary'].encode('utf-8')

## vim: set ts=4 : ##
