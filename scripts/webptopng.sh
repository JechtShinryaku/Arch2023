#!/bin/bash
#Convert one webp file or all in folder to png, use argument 'a' to convert all.
if [ "$1" == "" ]; then
    echo "ERROR No file"
    exit 1
fi
clear
#Use argument 'a' to convert all in folder
if [ "$1" == "a" ];
	then
		for i in `find . -type f -name "*.webp"`; do
			dir=`dirname "$(realpath "$i")"`
			newfile=$dir/"$(basename "$i" .webp)".png
			dwebp "$(realpath "$i")" -o "$newfile"
		done
	else	
		dir=`dirname "$(realpath "$1")"`
		newfile=$dir/"$(basename "$1" .webp)".png
		dwebp "$(realpath "$1")" -o "$newfile"
fi
