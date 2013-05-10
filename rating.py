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

#some converting
if userRating == 0.2:
  rating = 1
elif userRating == 0.4:
	rating = 2
elif userRating == 0.6:
	rating = 3
elif userRating == 0.8:
	rating = 4
elif userRating == 1:
	rating = 5
else:
	rating = 0

#modify the rating
if sys.argv[1] == 'inc':
	if rating < 5:
		rating += 1
		subprocess.call( ['banshee', '--set-rating='+str(rating)])
elif sys.argv[1] == 'dec':
	if rating > 0:
		rating -= 1
		subprocess.call( ['banshee', '--set-rating='+str(rating)])
elif sys.argv[1] == 'res':
	subprocess.call( ['banshee', '--set-rating=3'])
elif sys.argv[1] == 'min':
	subprocess.call( ['banshee', '--set-rating=0'])
elif sys.argv[1] == 'max':
	subprocess.call( ['banshee', '--set-rating=5'])
