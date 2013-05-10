#!/usr/bin/env python
import dbus
import sys
import subprocess

#connect to SessionBus
bus = dbus.SessionBus()

#load the correct Interface
banshee = bus.get_object('org.bansheeproject.Banshee', '/org/bansheeproject/Banshee/PlayerEngine')
banshee = dbus.Interface(banshee, 'org.bansheeproject.Banshee.PlayerEngine')
#extract userrating
userRating = int(banshee.GetRating())

#modify the rating
if sys.argv[1] == 'inc':
	if userRating < 5:
		userRating += 1
		subprocess.call( ['banshee', '--set-rating='+str(userRating)])
elif sys.argv[1] == 'dec':
	if userRating > 0:
		userRating -= 1
		subprocess.call( ['banshee', '--set-rating='+str(userRating)])
elif sys.argv[1] == 'res':
	subprocess.call( ['banshee', '--set-rating=3'])
elif sys.argv[1] == 'min':
	subprocess.call( ['banshee', '--set-rating=0'])
elif sys.argv[1] == 'max':
	subprocess.call( ['banshee', '--set-rating=5'])
