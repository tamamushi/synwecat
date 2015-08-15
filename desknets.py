#!/usr/bin/env python
# coding: utf-8

import mechanize
import datetime
from datetime import timedelta

class Desknets:

	HOSTNAME	= ""

	## constructor for Desknets. This method must needed hostname.
	## and optional arguments userid and password.
	def __init__(self,host,userid="",password=""):
		self.br 		= mechanize.Browser()
		self.HOSTNAME	= host

		if userid and password:
			self.authorize(userid,password)

	## call to authorize screen, and authorize user.
	## userid is number
	def authorize(self,userid, password):
		self.br.open("http://" + self.HOSTNAME + "/cgi-def/dnet/dnet.cgi")
		self.br.select_form(nr=0)
		self.br["uid"]		= [userid]
		self.br["_word"]	= password
		self.br.submit()
		return self

	def getScheduleByCSV(self,userid, startday, period):
		_res		= self.br.open("http://" + self.HOSTNAME + "/cgi-def/dnet/dnet.cgi?page=schpsetexport");
		_forms		= mechanize.ParseResponse(_res)
		_form		= _forms[0]

		_form["uid"]	= [userid]
		forms			= mechanize.ParseResponse(self.br.open(_form.click(name='s_add', nr=0)))
		form			= forms[0]

		## 開始日付をセット
		sdate			= datetime.datetime.strptime(startday, '%Y-%m-%d')
		form["syear"]	= [sdate.strftime("%Y")]
		form["smonth"]	= [sdate.strftime("%m")]
		form["sday"]	= [sdate.strftime("%d")]

		## 終了日付をセット
		edate			= sdate + timedelta(days = period)
		form["eyear"]	= [edate.strftime("%Y")]
		form["emonth"]	= [edate.strftime("%m")]
		form["eday"]	= [edate.strftime("%d")]
		response		= self.br.open(form.click(name="s_ok", nr=0))

		return response.read()

if __name__ == '__main__':
	import doctest
	doctest.testmod()

## vim:set ts=4 : ##
