# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import gpxpy
import gpxpy.gpx
import pandas as pd

gpx_file = open('Move_2016_09_02_15_29_40_Paragliding.gpx', 'r') 
gpx = gpxpy.parse(gpx_file)
vals = []
points = []


WND = 50
WIN_TYPE = 'hamming'

for track in gpx.tracks:
    for segment in track.segments:        
        for point in segment.points:  
            points.append(point)
            record =  dict(
                altitude = float(point.extensions['altitude']),
                verticalSpeed = float(point.extensions['verticalSpeed']),
            )
            vals.append(record)
        
dfx = pd.DataFrame(vals)
mdfx = dfx.rolling(WND, win_type = WIN_TYPE).mean()

#dfx['verticalSpeed'].plot()
#mdfx['verticalSpeed'].plot()

mdfx['verticalSpeed'].hist()
            


