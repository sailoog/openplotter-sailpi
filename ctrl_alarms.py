#!/usr/bin/env python

# This file is part of Openplotter.
# Copyright (C) 2015 by sailoog <https://github.com/sailoog/openplotter>
#
# Openplotter is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# any later version.
# Openplotter is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Openplotter. If not, see <http://www.gnu.org/licenses/>.

import sys, subprocess
from classes.conf import Conf
from classes.paths import Paths

action=sys.argv[1]

paths=Paths()
currentpath=paths.currentpath

conf=Conf()

data=conf.get('ALARMS', 'triggers')
triggers=data.split('||')
triggers.pop()

for index,item in enumerate(triggers):
	ii=item.split(',')
	triggers[index]=ii

tmp=''

#stop all
if action=='0':
	for index,item in enumerate(triggers):
		tmp +='0,'
		tmp +=triggers[index][1]+','+triggers[index][2]+','+triggers[index][3]+'||'
	conf.set('ALARMS', 'triggers', tmp)
	subprocess.Popen(['pkill', '-f', 'message.py'])
	subprocess.Popen(['pkill', '-9', 'mpg123'])
	
#start all
if action=='1':
	for index,item in enumerate(triggers):
		tmp +='1,'
		tmp +=triggers[index][1]+','+triggers[index][2]+','+triggers[index][3]+'||'
	conf.set('ALARMS', 'triggers', tmp)

subprocess.call(['pkill', '-f', 'monitoring.py'])
subprocess.Popen(['python',currentpath+'/monitoring.py', '0'])

sys.exit()