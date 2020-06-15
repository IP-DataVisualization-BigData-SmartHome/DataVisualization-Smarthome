#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 15:47:16 2020

@author: lukas
"""

import dash_html_components as html
import dash_core_components as dcc

optimazation_dict = {'fall1' : html.Div(className='card',
                                                                                                                          children=
                                                                                                                                      html.Div(className='card-body',
                                                                                                                                               children=[
                                                                                                                                                           html.Div(className='row',
                                                                                                                                                                    children=[
                                                                                                                                                                                html.Div(className='col-8',
                                                                                                                                                                                         children=
                                                                                                                                                                                                     html.H5(className='card-title-optimization',
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
                                                                                                                                                                                                     html.Div(className='card-graph-optimization',
                                                                                                                                                                                                              children='Plotly Diagramm'
                                                                                                                                                                                                              )
                                                                                                                                                                                         )
                                                                                                                                                                    ),
                                                                                                                                                           html.P(className='card-text-optimization',
                                                                                                                                                                  children='Mögliche Ursachen: Dämmung / Heizung'
                                                                                                                                                                  ),
                                                                                                                                                           html.A(className='card-btn-optimization btn btn-sm',
                                                                                                                                                                  href='#',
                                                                                                                                                                  children='Mehr dazu'
                                                                                                                                                                  #Link zu Analytics
                                                                                                                                                                  )
                                                                                                                                                           ]
                                                                                                                                               )
                                                                                                                          ),
                     'fall2' : html.Div(className='card',
                                                                                                                          children=
                                                                                                                                      html.Div(className='card-body',
                                                                                                                                               children=[
                                                                                                                                                           html.Div(className='row',
                                                                                                                                                                    children=[
                                                                                                                                                                                html.Div(className='col-8',
                                                                                                                                                                                         children=
                                                                                                                                                                                                     html.H5(className='card-title-optimization',
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
                                                                                                                                                                                                     html.Div(className='card-graph-optimization',
                                                                                                                                                                                                              children='Plotly Diagramm'
                                                                                                                                                                                                              )
                                                                                                                                                                                         )
                                                                                                                                                                    ),
                                                                                                                                                           html.P(className='card-text-optimization',
                                                                                                                                                                  children='Der Bau einer Solaranlage würde sich lohnen'
                                                                                                                                                                  ),
                                                                                                                                                           html.A(className='card-btn-optimization btn btn-sm',
                                                                                                                                                                  href='#',
                                                                                                                                                                  children='Mehr dazu'
                                                                                                                                                                  #Link zu Analytics
                                                                                                                                                                  )
                                                                                                                                                           ]
                                                                                                                                               )
                                                                                                                          ),
                                                                                                         
                                                                                                     
                     'windspeed' : html.Div(className='card',
                                                                                                                          children=
                                                                                                                                      html.Div(className='card-body',
                                                                                                                                               children=[
                                                                                                                                                           html.Div(className='row',
                                                                                                                                                                    children=[
                                                                                                                                                                                html.Div(className='col-8',
                                                                                                                                                                                         children=
                                                                                                                                                                                                     html.H5(className='card-title-optimization',
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
                                                                                                                                                                                                     html.Div(className='card-graph-optimization',
                                                                                                                                                                                                              children='Plotly Diagramm'
                                                                                                                                                                                                              )
                                                                                                                                                                                         )
                                                                                                                                                                    ),
                                                                                                                                                           html.P(className='card-text-optimization',
                                                                                                                                                                  children='Der Bau einer Windkraftanlage würde sich lohnen'
                                                                                                                                                                  ),
                                                                                                                                                           html.A(className='card-btn-optimization btn btn-sm',
                                                                                                                                                                  href='#',
                                                                                                                                                                  children='Mehr dazu'
                                                                                                                                                                  #Link zu Analytics
                                                                                                                                                                  )
                                                                                                                                                           ]
                                                                                                                                               )
                                                                                                                          ),
                     'visibility' :  html.Div(className='card',
                                                                                                                          children=
                                                                                                                                      html.Div(className='card-body',
                                                                                                                                               children=[
                                                                                                                                                           html.Div(className='row',
                                                                                                                                                                    children=[
                                                                                                                                                                                html.Div(className='col-8',
                                                                                                                                                                                         children=
                                                                                                                                                                                                     html.H5(className='card-title-optimization',
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
                                                                                                                                                                                                     html.Div(className='card-graph-optimization',
                                                                                                                                                                                                              children='Plotly Diagramm'
                                                                                                                                                                                                              )
                                                                                                                                                                                         )
                                                                                                                                                                    ),
                                                                                                                                                           html.P(className='card-text-optimization',
                                                                                                                                                                  children='Schönes Wetter, gehen Sie spazieren!'
                                                                                                                                                                  ),
                                                                                                                                                           html.A(className='card-btn-optimization btn btn-sm',
                                                                                                                                                                  href='#',
                                                                                                                                                                  children='Mehr dazu'
                                                                                                                                                                  #Link zu Analytics
                                                                                                                                                                  )
                                                                                                                                                           ]
                                                                                                                                               )
                                                                                                                          )
                     }
"""

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
                                                                                                                                                                                                     html.H5(className='card-title-optimization',
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
                                                                                                                                                                                                     html.Div(className='card-graph-optimization',
                                                                                                                                                                                                              children='Plotly Diagramm'
                                                                                                                                                                                                              )
                                                                                                                                                                                         )
                                                                                                                                                                    ),
                                                                                                                                                           html.P(className='card-text-optimization',
                                                                                                                                                                  children='Mögliche Ursachen: Dämmung / Heizung'
                                                                                                                                                                  ),
                                                                                                                                                           html.A(className='card-btn-optimization btn btn-sm',
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
                                                                                                                                                                                                     html.H5(className='card-title-optimization',
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
                                                                                                                                                                                                     html.Div(className='card-graph-optimization',
                                                                                                                                                                                                              children='Plotly Diagramm'
                                                                                                                                                                                                              )
                                                                                                                                                                                         )
                                                                                                                                                                    ),
                                                                                                                                                           html.P(className='card-text-optimization',
                                                                                                                                                                  children='Der Bau einer Solaranlage würde sich lohnen'
                                                                                                                                                                  ),
                                                                                                                                                           html.A(className='card-btn-optimization btn btn-sm',
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
                                                                                                                                                                                                     html.H5(className='card-title-optimization',
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
                                                                                                                                                                                                     html.Div(className='card-graph-optimization',
                                                                                                                                                                                                              children='Plotly Diagramm'
                                                                                                                                                                                                              )
                                                                                                                                                                                         )
                                                                                                                                                                    ),
                                                                                                                                                           html.P(className='card-text-optimization',
                                                                                                                                                                  children='Der Bau einer Windkraftanlage würde sich lohnen'
                                                                                                                                                                  ),
                                                                                                                                                           html.A(className='card-btn-optimization btn btn-sm',
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
                                                                                                                                                                                                     html.H5(className='card-title-optimization',
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
                                                                                                                                                                                                     html.Div(className='card-graph-optimization',
                                                                                                                                                                                                              children='Plotly Diagramm'
                                                                                                                                                                                                              )
                                                                                                                                                                                         )
                                                                                                                                                                    ),
                                                                                                                                                           html.P(className='card-text-optimization',
                                                                                                                                                                  children='Schönes Wetter, gehen Sie spazieren!'
                                                                                                                                                                  ),
                                                                                                                                                           html.A(className='card-btn-optimization btn btn-sm',
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

"""