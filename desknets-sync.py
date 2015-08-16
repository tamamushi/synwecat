#!/usr/bin/env python
# coding: utf-8

from desknets import Desknets
<<<<<<< HEAD

rb	= Desknets("93","ZD0a2YhY")
=======
import ConfigParser

config	= ConfigParser.ConfigParser()
config.read('synwecat.conf')

hostname	= config.get('Desknets', 'hostname')
user		= config.get('Desknets', 'user')
password	= config.get('Desknets', 'password')


## get schedule by csv
rb	= Desknets(hostname).authorize(user, password)
print rb.getScheduleByCSV(user,"2014-12-28", 30)
>>>>>>> 4179d0fe1bc3174121614caf7d7f56371eba7568

## vim:set ts=4 : ##
