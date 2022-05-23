#!/usr/bin/python
#A simple and lightweight script to set wallpapers every x seconds.
import time, os, random, setproctitle

#Set here your path folder and time.
path='/path/to/your/wallpaper/folder'
timer=120#seconds

#Set process name as 'PyBackground'
try:
    setproctitle.setproctitle('PyBackground')
except (ImportError, AttributeError):
    pass 

#Check which DE or WM is running.
desktop=(os.getenv('XDG_CURRENT_DESKTOP'))
#KDE Plasma
if desktop=='KDE':
    try:
        while True:
            w=os.path.abspath(path+'/'+random.choice(os.listdir(path)))
            os.system('plasma-apply-wallpaperimage "'+w+'"')
            time.sleep(timer)
    except KeyboardInterrupt:
	    print("Exiting...")
#If anything else it will try to do it through feh
else:
    try:
	    while True:
		    os.system('feh --randomize --bg-scale '+path)
		    time.sleep(timer)
    except KeyboardInterrupt:
	    print("Exiting...")
