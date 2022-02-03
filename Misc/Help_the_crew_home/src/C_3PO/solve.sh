#!/bin/bash
filenames="*.jpg"
freq="9898"
for filename in $filenames; do
    string=$(exiftool $filename | grep Spatial | cut -d':' -f 2 | xargs)
    if [ $freq = $string ]; then
        exiftool $filename;
        break;
    fi;
    echo -ne "                              \rfile: $filename freq: $string\r"
done