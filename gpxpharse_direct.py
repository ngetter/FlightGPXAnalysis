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
tmp = 0

# sampling frequency (compare to last sample_span )
sample_span = 10

# window of sample_spaning after extracting the data
WND = 30

for track in gpx.tracks:
    for segment in track.segments:
        for point in range(sample_span, len(segment.points)):
            tmp = segment.points[point]
            points.append(tmp)
            record =  dict(
                speed = tmp.speed_between(segment.points[point -sample_span]),
                angle = tmp.elevation_angle(segment.points[point -sample_span]),
            )
            vals.append(record)

dfx = pd.DataFrame(vals)
mdfx = dfx.rolling(WND).mean()

dfx.plot()
mdfx.plot()
