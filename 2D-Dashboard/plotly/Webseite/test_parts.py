#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 12:32:14 2020

@author: lukas




 {
        ' src': 'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css',
        'integrity': 'sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN',
        'crossorigin': 'anonymous'
    },
     'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css',

"""

import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash

Header = html.Div(children=
                        dcc.RadioItems(
                                       options=[
                                           {'label': ' Temperatur ', 'value': 'temp'},
                                           {'label': ' Luftfeuchtigkeit', 'value': 'hum'},
                                           {'label': ' Temperatur draußen', 'value': 'tempd'}
                                               ],
                                       value='MTL',
                                       labelStyle={'display': 'inline-block'},
                                       labelClassName = 'labeltest'
                                       )
                  )
                                            
external_scripts = [
    {
        'src': 'https://code.jquery.com/jquery-3.2.1.slim.min.js',
        'integrity': 'sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm',
        'crossorigin': 'anonymous'
    },
    {
        'src': 'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js',
        'integrity': 'sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q',
        'crossorigin': 'anonymous'
    },
    {
        'src': 'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js',
        'integrity': 'sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl',
        'crossorigin': 'anonymous'
    },
]


external_stylesheets = [
       
    'https://cdn.materialdesignicons.com/5.1.45/css/materialdesignicons.min.css',
    dbc.themes.BOOTSTRAP,
    '/home/lukas/Desktop/IP_Repo/DataVisualization-Smarthome/2D-Dashboard/css/analytics.css',
    '/home/lukas/Desktop/IP_Repo/DataVisualization-Smarthome/2D-Dashboard/css/main.css',
]

app = dash.Dash(external_stylesheets=external_stylesheets, external_scripts=external_scripts)
app.title = 'Analytics'

app.layout = html.Div(Header)

if __name__ == "__main__":
    app.run_server()