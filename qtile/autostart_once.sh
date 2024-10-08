#!/bin/bash

# Apply wallpaper using wal
./~/Downloads/wal/wal -b 282738 -i ~/Wallpaper/wall.jpg &&

# Start picom
picom --config ~/.config/picom/picom.conf &


xmodmap ~/.Xmodmap
