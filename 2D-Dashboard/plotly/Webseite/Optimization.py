# -*- coding: utf-8 -*-
"""
Created on Sun May 10 16:27:30 2020

@author: Mues
"""

import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash
from postgre import postgre_connector
import datetime as dt
import numpy as np


class Optimization:

    def __init__(self, date = None):
        self.date = date
        
   
                    
 
    def optimization_seite(self):
        return html.Div([
                            html.Nav(className = 'nav-abstand',
                                     children=
                                                 html.Div(className='container-fluid head-design',
                                                          children=
                                                                      html.Div(className='row',
                                                                               children=[
                                                                                           html.Div(className='col-4'),
                                                                                           html.Div(className='col-4 text-center head-optimization',
                                                                                                    children=
                                                                                                                html.A(children='Optimization')
                                                                                                    ),
                                                                                           html.Div(className='col-4')
                                                                                       ]
                                                                               )
                                                          )
                                     ),
                            html.Main(children=
                                                  html.Div(className='container-fluid main', id = 'main',
                                                           children=
                                                                       html.Div(className='row',
                                                                                children=[
                                                                                            html.Div(className='col-1',
                                                                                                     children=[
                                                                                                                 html.I(className='mdi mdi-weather-sunny'),
                                                                                                                 html.I(className='mdi mdi-wind-turbine'),
                                                                                                                 html.I(className='mdi mdi-solar-power'),
                                                                                                                 html.I(className='mdi mdi-water-percent'),
                                                                                                                 html.I(className='mdi mdi-home-thermometer'),
                                                                                                                 html.I(className='mdi mdi-home-thermometer-outline'),
                                                                                                                 html.I(className='mdi mdi-weather-pouring')
                                                                                                             ]
                                                                                                     ),
                                                                                            html.Div(className='col-5',
                                                                                                    #erste Spalte
                                                                                                     children=[
                                                                                                                 html.Div(className='card',
                                                                                                                          children=
                                                                                                                                      html.Div(className='card-body',
                                                                                                                                               children=[
                                                                                                                                                           html.Div(className='row',
                                                                                                                                                                    children=[
                                                                                                                                                                                html.Div(className='col-8',
                                                                                                                                                                                         children=
                                                                                                                                                                                                     html.H5(className='card-title',
                                                                                                                                                                                                             children='Dämmung ist schlecht'
                                                                                                                                                                                                             )
                                                                                                                                                                                         ),
                                                                                                                                                                                html.Div(className='col-4 text-right',
                                                                                                                                                                                         children=
                                                                                                                                                                                                     html.I(className='mdi mdi-home-thermometer card-icon')
                                                                                                                                                                                         )
                                                                                                                                                                                ]
                                                                                                                                                                    ),
                                                                                                                                                           html.Div(className='row',
                                                                                                                                                                    children=
                                                                                                                                                                                html.Div(className='col-12',
                                                                                                                                                                                         children=
                                                                                                                                                                                                     html.Div(className='card-graph',
                                                                                                                                                                                                              children='Plotly Diagramm'
                                                                                                                                                                                                              )
                                                                                                                                                                                         )
                                                                                                                                                                    ),
                                                                                                                                                           html.P(className='card-text',
                                                                                                                                                                  children='Mögliche Ursachen: Dämmung / Heizung'
                                                                                                                                                                  ),
                                                                                                                                                           html.A(className='card-btn btn btn-sm',
                                                                                                                                                                  href='#',
                                                                                                                                                                  children='Mehr dazu'
                                                                                                                                                                  #Link zu Analytics
                                                                                                                                                                  )
                                                                                                                                                           ]
                                                                                                                                               )
                                                                                                                          ),
                                                                                                                 html.Div(className='card',
                                                                                                                          children=
                                                                                                                                      html.Div(className='card-body',
                                                                                                                                               children=[
                                                                                                                                                           html.Div(className='row',
                                                                                                                                                                    children=[
                                                                                                                                                                                html.Div(className='col-8',
                                                                                                                                                                                         children=
                                                                                                                                                                                                     html.H5(className='card-title',
                                                                                                                                                                                                             children='Viele Sonnenstunden'
                                                                                                                                                                                                             )
                                                                                                                                                                                         ),
                                                                                                                                                                                html.Div(className='col-4 text-right',
                                                                                                                                                                                         children=
                                                                                                                                                                                                     html.I(className='mdi mdi-solar-power card-icon')
                                                                                                                                                                                         )
                                                                                                                                                                                ]
                                                                                                                                                                    ),
                                                                                                                                                           html.Div(className='row',
                                                                                                                                                                    children=
                                                                                                                                                                                html.Div(className='col-12',
                                                                                                                                                                                         children=
                                                                                                                                                                                                     html.Div(className='card-graph',
                                                                                                                                                                                                              children='Plotly Diagramm'
                                                                                                                                                                                                              )
                                                                                                                                                                                         )
                                                                                                                                                                    ),
                                                                                                                                                           html.P(className='card-text',
                                                                                                                                                                  children='Der Bau einer Solaranlage würde sich lohnen'
                                                                                                                                                                  ),
                                                                                                                                                           html.A(className='card-btn btn btn-sm',
                                                                                                                                                                  href='#',
                                                                                                                                                                  children='Mehr dazu'
                                                                                                                                                                  #Link zu Analytics
                                                                                                                                                                  )
                                                                                                                                                           ]
                                                                                                                                               )
                                                                                                                          )
                                                                                                         ]
                                                                                                     ),
                                                                                            html.Div(className='col-5',
                                                                                                     #zweite Spalte
                                                                                                     children= [
                                                                                                                html.Div(className='card',
                                                                                                                          children=
                                                                                                                                      html.Div(className='card-body',
                                                                                                                                               children=[
                                                                                                                                                           html.Div(className='row',
                                                                                                                                                                    children=[
                                                                                                                                                                                html.Div(className='col-8',
                                                                                                                                                                                         children=
                                                                                                                                                                                                     html.H5(className='card-title',
                                                                                                                                                                                                             children='Viel Wind'
                                                                                                                                                                                                             )
                                                                                                                                                                                         ),
                                                                                                                                                                                html.Div(className='col-4 text-right',
                                                                                                                                                                                         children=
                                                                                                                                                                                                     html.I(className='mdi mdi-wind-turbine card-icon')
                                                                                                                                                                                         )
                                                                                                                                                                                ]
                                                                                                                                                                    ),
                                                                                                                                                           html.Div(className='row',
                                                                                                                                                                    children=
                                                                                                                                                                                html.Div(className='col-12',
                                                                                                                                                                                         children=
                                                                                                                                                                                                     html.Div(className='card-graph',
                                                                                                                                                                                                              children='Plotly Diagramm'
                                                                                                                                                                                                              )
                                                                                                                                                                                         )
                                                                                                                                                                    ),
                                                                                                                                                           html.P(className='card-text',
                                                                                                                                                                  children='Der Bau einer Windkraftanlage würde sich lohnen'
                                                                                                                                                                  ),
                                                                                                                                                           html.A(className='card-btn btn btn-sm',
                                                                                                                                                                  href='#',
                                                                                                                                                                  children='Mehr dazu'
                                                                                                                                                                  #Link zu Analytics
                                                                                                                                                                  )
                                                                                                                                                           ]
                                                                                                                                               )
                                                                                                                          ),
                                                                                            html.Div(className='card',
                                                                                                                          children=
                                                                                                                                      html.Div(className='card-body',
                                                                                                                                               children=[
                                                                                                                                                           html.Div(className='row',
                                                                                                                                                                    children=[
                                                                                                                                                                                html.Div(className='col-8',
                                                                                                                                                                                         children=
                                                                                                                                                                                                     html.H5(className='card-title',
                                                                                                                                                                                                             children='Wenig Wolken'
                                                                                                                                                                                                             )
                                                                                                                                                                                         ),
                                                                                                                                                                                html.Div(className='col-4 text-right',
                                                                                                                                                                                         children=
                                                                                                                                                                                                     html.I(className='mdi mdi-white-balance-sunny card-icon')
                                                                                                                                                                                         )
                                                                                                                                                                                ]
                                                                                                                                                                    ),
                                                                                                                                                           html.Div(className='row',
                                                                                                                                                                    children=
                                                                                                                                                                                html.Div(className='col-12',
                                                                                                                                                                                         children=
                                                                                                                                                                                                     html.Div(className='card-graph',
                                                                                                                                                                                                              children='Plotly Diagramm'
                                                                                                                                                                                                              )
                                                                                                                                                                                         )
                                                                                                                                                                    ),
                                                                                                                                                           html.P(className='card-text',
                                                                                                                                                                  children='Schönes Wetter, gehen Sie spazieren!'
                                                                                                                                                                  ),
                                                                                                                                                           html.A(className='card-btn btn btn-sm',
                                                                                                                                                                  href='#',
                                                                                                                                                                  children='Mehr dazu'
                                                                                                                                                                  #Link zu Analytics
                                                                                                                                                                  )
                                                                                                                                                           ]
                                                                                                                                               )
                                                                                                                          )
                                                                                            ]
                                                                                                                #Ende zweite Spalte
                                                                                                        ),
                                                                                            html.Div(className='col-1'),
                                                                                        ]
                                                                                )
                                                               )
                                          ),
                            html.Nav(className='navbar fixed-bottom',
                                                             children=
                                                                         html.Div(className='container-fluid navdiv',
                                                                                  children=[
                                                                                              html.Div(className='col navdiv',
                                                                                                       children=
                                                                                                                   html.A(className='nav-link',
                                                                                                                          href='analytics.html',
                                                                                                                          children=[
                                                                                                                                      html.I(className='mdi mdi-google-analytics navicon'),
                                                                                                                                      html.P(className='nav-text',
                                                                                                                                             children='Analytics'
                                                                                                                                             )
                                                                                                                                  ]
                                                                                                                          )
                                                                                                       ),
                                                                                              html.Div(className='col navdiv',
                                                                                                       children=
                                                                                                                   html.A(className='nav-link nav-link-active',
                                                                                                                          href='#',
                                                                                                                          children=[
                                                                                                                                      html.I(className='mdi mdi-home navicon'),
                                                                                                                                      html.P(className='nav-text',
                                                                                                                                             children='Dashboard'
                                                                                                                                             )
                                                                                                                                  ]
                                                                                                                          )
                                                                                                       ),
                                                                                              html.Div(className='col navdiv',
                                                                                                       children=
                                                                                                                   html.A(className='nav-link ',
                                                                                                                          href='optimization.html',
                                                                                                                          children=[
                                                                                                                                      html.I(className='mdi mdi-sync navicon'),
                                                                                                                                      html.P(className='nav-text',
                                                                                                                                             children='Optimization'
                                                                                                                                             )
                                                                                                                                  ]
                                                                                                                          )
                                                                                                       )
                                                                                              ]
                                                                                  )
                                         )
                        ])

@app
 def case_check():
        if site.date != None:    
            date = dt.datetime(site.date.year, site.date.month, site.date.day, 0, 0)
            date2 = date + dt.timedelta(hours= 23, minutes = 50)
            db_con = postgre_connector()
            threshold = db_con.get_data(site.date, site.date, 'm', [])
            result = db_con.get_data(date, date2, 'a', [])
            
            for col_t, col_r in zip(threshold, result):
                if col_t != 'datum':
                    
            # Weiter am besten die Werte eines tages mit dem Monatlcihen Durchschnitsswerten vergleichen,
            # bei größer wird dann das Optimierungs-event getriggert


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
    '/home/lukas/Desktop/IP_Repo/DataVisualization-Smarthome/2D-Dashboard/css/optimization.css',
    '/home/lukas/Desktop/IP_Repo/DataVisualization-Smarthome/2D-Dashboard/css/main.css',
]

app = dash.Dash(external_stylesheets=external_stylesheets, external_scripts=external_scripts)
app.title = 'Optimazation'

site = Optimization()

app.layout = site.optimization_seite()


if __name__ == '__main__':
    app.run_server(debug=True)