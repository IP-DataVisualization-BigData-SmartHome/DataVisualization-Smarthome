#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Formel-Taupunkt :https://www.wetterochs.de/wetter/feuchte.html
Formel-Windenergie: https://www.engineeringtoolbox.com/wind-power-d_1214.html

@author: Lukas Schnittcher

Helper-File für Optimazation.py
Die einzelnen Vorlagen für die Optimazations-Cases werden hier verwaltet, ebenso die Formel zur Berechnung des "Schimmel-Risikos"
Sobald irgendeine Temperatur unter der Grenze der Berechneten Temperatur fällt, ist diese Stelle Schimmelgefährdet
"""

import dash_html_components as html
import dash_core_components as dcc
import math
import pandas as pd
from math import pi

#Formel zur Berechnung des Taupunktes Formel-Quelle: https://www.wetterochs.de/wetter/feuchte.html
def Taupunkt(temp, hum):
    if temp >= 0:
        a = 7.5
        b = 237.3
    else:
        a = 7.6
        b = 240.7
    
    rk_gas = 8314.3
    mw = 18.016
    
    sdd = 6.1078 * 10**((a*temp)/(b+temp))
    dd = hum/100 * sdd
    v = math.log(dd/6.1078, 10)
    
    return b*v/(a-v)

#Formel zur Berechnung der Energie aus Windgeschwindigkeit
def energyfromwind(windspeed):
    p = 1.208
    d = 3
    v = windspeed
    
    return (0.2*p*pi*d*d*v**3)/8

#Dictionary welches die HTML-Vorlage für die Optimazation-Cases bereit hält        
optimazation_dict = {'lights' : html.Div(className='card',
                                                                                                                         children=
                                                                                                                                      html.Div(className='card-body',
                                                                                                                                               children=[
                                                                                                                                                           html.Div(className='row',
                                                                                                                                                                    children=[
                                                                                                                                                                                html.Div(className='col-8',
                                                                                                                                                                                         children=
                                                                                                                                                                                                     html.H5(className='card-title-optimization',
                                                                                                                                                                                                             children='Hoher Energieverbrauch durch Licht in der letzten Nacht'
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
                                                                                                                                                           html.P(className='card-text-optimization', id = 'lightstext',
                                                                                                                                                                  children='Mögliche Ursachen: Dämmung / Heizung'
                                                                                                                                                                  ),
                                                                                                                                                           html.Button('Mehr Dazu', id='lightsbt', className = 'opti-button')
                                                                                                                                                           ]
                                                                                                                                               )
                                                                                                                          ),
                     'appliances' : html.Div(className='card',
                                                                                                                          children=
                                                                                                                                      html.Div(className='card-body',
                                                                                                                                               children=[
                                                                                                                                                           html.Div(className='row',
                                                                                                                                                                    children=[
                                                                                                                                                                                html.Div(className='col-8',
                                                                                                                                                                                         children=
                                                                                                                                                                                                     html.H5(className='card-title-optimization',
                                                                                                                                                                                                             children='Hoher Energieverbrauch in der letzten Nacht'
                                                                                                                                                                                                             )
                                                                                                                                                                                         ),
                                                                                                                                                                                html.Div(className='col-4 text-right',
                                                                                                                                                                                         children=
                                                                                                                                                                                                     html.I(className='mdi mdi-power-plug card-icon')
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
                                                                                                                                                           html.P(className='card-text-optimization', id = 'appliancestext',
                                                                                                                                                                  children='Der Bau einer Solaranlage würde sich lohnen'
                                                                                                                                                                  ),
                                                                                                                                                           html.Button('Mehr Dazu', id='appliancesbt',className = 'opti-button')
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
                                                                                                                                                           html.P(className='card-text-optimization', id = 'windspeedtext',
                                                                                                                                                                  children='Der Bau einer Windkraftanlage würde sich lohnen'
                                                                                                                                                                  ),
                                                                                                                                                           html.Button('Mehr Dazu', id='windspeedbt', className = 'opti-button')
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
                                                                                                                                                           html.P(className='card-text-optimization', id = 'visibilitytext',
                                                                                                                                                                  children='Schönes Wetter, gehen Sie spazieren!'
                                                                                                                                                                  ),
                                                                                                                                                           html.Button('Mehr Dazu', id='visibilitybt', className = 'opti-button')
                                                                                                                                                           ]
                                                                                                                                               )
                                                                                                                          ),
                      'schimmel' :  html.Div(className='card',
                                                                                                                          children=
                                                                                                                                      html.Div(className='card-body',
                                                                                                                                               children=[
                                                                                                                                                           html.Div(className='row',
                                                                                                                                                                    children=[
                                                                                                                                                                                html.Div(className='col-8',
                                                                                                                                                                                         children=
                                                                                                                                                                                                     html.H5(className='card-title-optimization',
                                                                                                                                                                                                             children='Schimmel hoch'
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
                                                                                                                                                                                                     html.Div(
                                                                                                                                                                                                              children='Plotly Diagramm'
                                                                                                                                                                                                              )
                                                                                                                                                                                         )
                                                                                                                                                                    ),
                                                                                                                                                           
                                                                                                                                                                    
                                                                                                                                                           html.P(className='card-text-optimization', id = 'schimmeltext',
                                                                                                                                                                  children='Schönes Wetter, gehen Sie spazieren!'
                                                                                                                                                                  ),
                                                                                                                                                           html.Button('Mehr Dazu', id='schimmelbt', className = 'opti-button')
                                                                                                                                                           
                                                                                                                                                           
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