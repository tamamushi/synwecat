#!/usr/bin/env python
# coding: utf-8

import os

from httplib2 import Http
import oauth2client
from apiclient.discovery import build
from oauth2client.file import Storage

	
class GoogleCalendar:
	def __init__(self, userid):
		home_dir		= os.path.expanduser('~')
		credential_dir	= os.path.join(home_dir, '.credentials')
		credential_path	= os.path.join(credential_dir, 'calendar.json')

	    #if not os.path.exists(credential_dir):
		
		store 			= oauth2client.file.Storage(credential_path)
		credentials		= store.get()
		self.service	= build('calendar', 'v3', http=credentials.authorize(Http()))

	def getCalendarId(self, calendarStr):

		calendars	= self.service.calendarList().list().execute()
		for calendar in calendars['items']:
			if calendar['summary'] == calendarStr:
				return calendar['id'].encode("utf-8")

	def getScheduleList(self, calId):

		events	= self.service.events().list(	calendarId = calId,
												timeMin = '2015-05-01T00:00:00Z',
												timeMax = '2015-05-30T23:59:59Z',
												singleEvents = True
												).execute()
		for event in events['items']:
			print "%s, %s [%s] - [%s]" % (	event['summary'],
											event["start"]["date"],
											event["start.dateTime"],
											event["end.dateTime"])
											
		

if __name__ == '__main__':
	str	= u"ビジネス（予定）"

	gc	= GoogleCalendar("t.koube")
	id	= gc.getCalendarId(str);
	print id
	gc.getScheduleList(id)
	
## vim: set ts=4 : ##
