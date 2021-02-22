#!/usr/bin/env python3

#import gi
#gi.require_version("Gdk", "3.0")
#from gi.repository import Gdk

#allmonitors = []

#gdkdsp = Gdk.Display.get_default()
#for i in range(gdkdsp.get_n_monitors()):
#    monitor = gdkdsp.get_monitor(i)
#    scale = monitor.get_scale_factor()
#    geo = monitor.get_geometry()
#    allmonitors.append([
#        monitor.get_model()] + [n * scale for n in [
#            geo.x, geo.y, geo.width, geo.height
#        ]
#    ])

#print(allmonitors)


import os
list_display = os.popen("xrandr --listmonitors | grep '*' | awk {'print $4'}").read().splitlines()
# or based on the comment of this answer 