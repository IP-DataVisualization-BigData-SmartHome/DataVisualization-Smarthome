# -*- coding: utf-8 -*-
"""
Created on Sun May 10 16:27:30 2020

@author: Mues
"""

import dash_html_components as html



class Optimization:

 
    def optimization_seite(self):
        return html.Div([
                            html.Nav(className='fixed-top',
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
                                                  html.Div(className='container-fluid main',
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
                                                                                                                                                                                                             children='Dämmung im Wohnzimmer schlecht'
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
                                                                                                     children=
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
                                                                                                                          )
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