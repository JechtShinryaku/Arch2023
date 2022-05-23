#!/usr/bin/python
#Set an animated wallpaper for sway desktop, can be one file or a folder with multiple files.
#Requirements: mpvpaper

import time, os, random, setproctitle, sys

videoPath='/mnt/Alfheim/Videos/Anime/LiveWallapers/Monogatari'#Default path to one video or folder will be used if there is not path as argument.
imgPath='~/.Wallpapers/last'#Path to static img
output='LVDS-1'#To get your ouputs-> swaymsg -t get_outputs

#Set 'WaylandVideoBackground' as process name.
try:
    setproctitle.setproctitle('WaylandVideoBackground')
except (ImportError, AttributeError):
    pass 


#Check 'wayland'
desktop=(os.getenv('XDG_SESSION_TYPE'))
if desktop=='wayland':
    print('Wayland detected OK')
    if len(sys.argv)>1:
        videoPath=sys.argv[1]
    try:
        os.system('killall swaybg')#Remove background image from sway.
        #UNCOMMNET THE LINE WITH THE CONFIGURATION YOU WANT, JUST ONE
        #os.system('mpvpaper '+output+' -o "--loop-file=inf" \''+videoPath+'\'')#Plays one file loop infinite
        #os.system('mpvpaper '+output+' -o "no-audio --loop-file=inf" \''+videoPath+'\'')#Plays one file loop infinite without sound
        os.system('mpvpaper '+output+' -o "--loop-playlist shuffle" \''+videoPath+'\'')#Plays random
        #os.system('mpvpaper '+output+' -o "no-audio --loop-playlist shuffle" \''+videoPath+'\'')#Plays random without sound
        
        
        os.system('swaymsg output '+output+' bg '+imgPath+' fill')#Restore last image
    except KeyboardInterrupt:
	    print("Exiting...")

else:
    try:
        print('No Wayland detected')
        os.system('swaymsg output '+output+' bg '+imgPath+' fill')
        quit()
    except KeyboardInterrupt:
	    print("Exiting...")
