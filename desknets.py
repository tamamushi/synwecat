#!/usr/bin/env python
# coding: utf-8

import mechanize

class Desknets:
	def __init__(self,name,password):
		self.br = mechanize.Browser()
		self.br.open("http://124.146.219.249/cgi-def/dnet/dnet.cgi")
		self.br.select_form(nr=0)

		self.br["uid"]		= [name]
		self.br["_word"]	= password
		self.br.submit()

	def getScheduleByCSV(self)
		res		= self.br.open("http://124.146.219.249/cgi-def/dnet/dnet.cgi?page=schpsetexport");
		forms	= mechanize.ParseResponse(_res)
		form	= forms[0]

		form["uid"]		= ["93"]
		form.click(name = "s_add", 
		form["syear"]	= ["2015"]
		form["smonth"]	= ["04"]
		form["sday"]	= ["28"]

		form["eyear"]	= ["2015"]
		form["emonth"]	= ["05"]
		form["eday"]	= ["28"]

## vim:set ts=4 : ##
