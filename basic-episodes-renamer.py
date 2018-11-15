# This script allow you to quickly rename episodes of tv series, useful for kodi
# Made by Scott RIDEL
# v1.0

import os, re
L = []
regex = ".*(s[0-9]{2}e[0-9]{2}).*(.mp4|.avi|.mkv)$"
for i in os.listdir('.'):
    if re.match(regex, i, re.I):
        L = re.findall(regex, i, re.I)
        n = L[0][0].upper()+L[0][1].lower()
        os.rename(i, n)
