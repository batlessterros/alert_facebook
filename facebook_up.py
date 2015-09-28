#!/usr/bin/python
#-*- coding: utf-8 -*-
import requests
import signal
import time
import sys

while True:
    sys.stdout.write("Still down at: "+time.strftime("%Hh%M"))
    sys.stdout.flush()
    fb_down = 0
    try:
        r = requests.get("https://www.facebook.com", timeout=5)
    except KeyboardInterrupt:
        sys.exit(0)
    except:
        fb_down = 1
        sys.stdout.write("\r")
        continue

    sys.stdout.write("\r")
    if(r.status_code == 200):
        sys.stdout.write("\r")
        print("World has been saved!")
        if(raw_input("Print what has been get? (y/N)\n") == "y"):
            print("World has been saved!")
            sys.stdout.write(r.text)
        break
