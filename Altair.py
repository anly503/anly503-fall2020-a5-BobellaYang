#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 03:02:02 2021

@author: yangbo
"""

import pandas as pd
import altair as alt

df = pd.read_csv("finalhouseholdplug.csv")
df["household"] = df["household"].astype('category')

#selector = alt.selection(type="single", empty='none', on='mouseover')
click = alt.selection_multi(encodings=['color'])

gp_chart = alt.Chart(df).mark_bar().encode(
  alt.Column('plug', title= 'Plug type'), alt.X('household', title = 'Household'),
  alt.Y('measurement', axis=alt.Axis(grid=False), title = 'Overall Usage (Hz)'), 
  color= alt.condition(
        click, # replace the previous condition with the selector
        'plug',
        alt.value("lightgrey")),
  tooltip = ['household', 'plug', 'measurement']
).add_selection(
    click  # Add the selector here so that the chart knows to use it
    ).interactive()
  

alt.renderers.enable('altair_viewer')
gp_chart.save('altair.html')