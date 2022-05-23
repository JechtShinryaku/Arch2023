#!/bin/bash
#Automate video encoding, mainly used to re-encoding my gameplays.
if [ "$1" == "" ]; then
    echo "ERROR No file"
    exit 1
fi
clear
dirvideo=`dirname "$(realpath "$1")"`
newfile=$dirvideo/RE-$1
time ffmpeg -i "$(realpath "$1")" -b:v 8M -preset placebo -profile:v main -level:v 4.2 -vcodec libx264 -acodec copy "$newfile"
