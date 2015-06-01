#!/usr/bin/env python

import os

from httplib2 import Http
import oauth2client
import gflags
from oauth2client import tools
from apiclient.discovery import build
from oauth2client.client import flow_from_clientsecrets
from oauth2client.tools import run_flow
from oauth2client.file import Storage

SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'

def get_credentials():

	try:
	    import argparse
	    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
	except ImportError:
		flags = None

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
		credentials 	= run_flow(flow, store, flags)

		print 'Storing credentials to ' + credential_path
	return credentials

def main():
	credentials = get_credentials()
	service		= build('calendar', 'v3', http=credentials.authorize(Http()))

	calendars	= service.calendarList().list().execute()
	for calendar in calendars['items']:
		print "%s, %s" % (calendar['id'], calendar['summary'])

if __name__ == '__main__':
	main()

## vim: set ts=4 : ##
