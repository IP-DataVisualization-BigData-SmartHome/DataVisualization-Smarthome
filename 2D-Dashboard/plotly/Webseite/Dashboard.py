# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:18:10 2020

@author: Mues
"""

import dash_html_components as html



class Dashboard:

 
    def dashboard_seite(self):
        return html.Div([
                            html.Nav(className='fixed-top',
                                     children=
                                                 html.Div(className='container-fluid head-design',
                                                          children=[
                                                                      html.Div(className='row',
                                                                               children=[
                                                                                           html.Div(className='col-3 text-right text-head',
                                                                                                    children=
                                                                                                                html.I(className='mdi mdi-weather-sunny headicon'
                                                                                                                       #Datensatz: Termperatur draussen
                                                                                                                       )
                                                                                                    ),
                                                                                           html.Div(className='col-1 text-left text-head',
                                                                                                    children=
                                                                                                                html.Div(children='10°C'
                                                                                                                         #<!-- Datensatz: Temperatur draußen -->
                                                                                                                         )
                                                                                                    ),
                                                                                           html.Div(className='col-4 text-center text-head',
                                                                                                    children=
                                                                                                                html.A(className='nav-head',
                                                                                                                       href='#',
                                                                                                                       children='18:20'
                                                                                                                       #<!-- Bei Click Uhrzeitauswahl -->
                                                                                                                       )
                                                                                                    ),
                                                                                           html.Div(className='col-4 text-left luft-wind',
                                                                                                    children=[
                                                                                                                html.Div(children='Luftfeuchte: 43%'
                                                                                                                         #<!-- Datensatz: Luftfeuchte draußen -->
                                                                                                                         ),
                                                                                                                html.Div(children='Wind: 10 km/h'
                                                                                                                         #<!-- Datensatz: Wind draußen -->
                                                                                                                         )
                                                                                                                ]
                                                                                                    )
                                                                                       ]
                                                                               ),
                                                                      html.Div(className='row',
                                                                               children=[
                                                                                           html.Div(className='col-4'),
                                                                                           html.Div(className='col-4 text-center',
                                                                                                    id='Datum',
                                                                                                    children=
                                                                                                                html.A(className='nav-head',
                                                                                                                       href='#',
                                                                                                                       children=' Montag, 17. Nov.'
                                                                                                                       #<!-- Bei Click Datumauswahl -->
                                                                                                                       )
                                                                                                    ),
                                                                                           html.Div(className='col-4')
                                                                                           ]
                                                                               )
                                                              ])
                                                 ),
                                html.Div(className='helpdiv',
                                         children=
                                                     html.A(href='#',
                                                            children=
                                                                        html.I(className='mdi mdi-help-circle-outline helpicon')
                                                            )
                                         ),
                                html.Div(className='container-fluid',
                                         children=[
                                                    html.Div(className='row',
                                                             children=[
                                                                         html.Div(className='col-2 main-div relative d-flex justify-content-center',
                                                                                  children=
                                                                                              html.Div(className='sidecard',
                                                                                                       children=[
                                                                                                                   html.Div(className='strom',
                                                                                                                            #<!-- Strom-Fläche -->
                                                                                                                            children=[
                                                                                                                                        html.Div(className='verbrauch-text',
                                                                                                                                                 children='Stromverbrauch'
                                                                                                                                                 ),
                                                                                                                                        html.Div(children=
                                                                                                                                                         html.I(className='mdi mdi-flash icons-verbrauch')
                                                                                                                                                 ),
                                                                                                                                        html.Div(className='stromverbrauch verbrauch-zahl',
                                                                                                                                                 children='200 W'
                                                                                                                                                 #<!-- Stromverbrauch eintragen -->
                                                                                                                                                 )
                                                                                                                                       ] 
                                                                                                                                        
                                                                                                                            ),
                                                                                                                   html.Div(className='licht',
                                                                                                                            #<!-- Licht-Fläche -->
                                                                                                                            children=[
                                                                                                                                        html.Div(className='verbrauch-text',
                                                                                                                                                 children='Lichtverbrauch'
                                                                                                                                                 ),
                                                                                                                                        html.Div(children=
                                                                                                                                                             html.I(className='mdi mdi-lightbulb-on icons-verbrauch')
                                                                                                                                                 ),
                                                                                                                                        html.Div(className='stromverbrauch verbrauch-zahl',
                                                                                                                                                 children='22 W'
                                                                                                                                                 #<!-- Lichtverbrauch eintragen -->
                                                                                                                                                 )
                                                                                                                                        ]
                                                                                                                            )
                                                                                                           ])
                                                                                      ),
                                                                         html.Div(className='col-8',
                                                                                  children=
                                                                                              html.Div(className='row',
                                                                                                       children=[
                                                                                                                   html.Div(className='colorwrapper bad',
                                                                                                                            children=
                                                                                                                                        html.Div(className='colorcircle',
                                                                                                                                                 children=[
                                                                                                                                                             html.Div(className='filled',
                                                                                                                                                                      id='bad-fill'),
                                                                                                                                                             html.P(children='19°'),
                                                                                                                                                             html.P(children='50%')
                                                                                                                                                         ]
                                                                                                                                                 )
                                                                                                                            ),
                                                                                                                   html.Div(className='colorwrapper arbeits',
                                                                                                                            children=
                                                                                                                                        html.Div(className='colorcircle',
                                                                                                                                                 children=[
                                                                                                                                                             html.Div(className='filled',
                                                                                                                                                                      id='arbeits-fill'),
                                                                                                                                                             html.P(children='19°'),
                                                                                                                                                             html.P(children='50%')
                                                                                                                                                         ]
                                                                                                                                                 )
                                                                                                                            ),
                                                                                                                   html.Div(className='colorwrapper schlaf',
                                                                                                                            children=
                                                                                                                                        html.Div(className='colorcircle',
                                                                                                                                                 children=[
                                                                                                                                                             html.Div(className='filled',
                                                                                                                                                                      id='schlaf-fill'),
                                                                                                                                                             html.P(children='19°'),
                                                                                                                                                             html.P(children='50%')
                                                                                                                                                         ]
                                                                                                                                                 )
                                                                                                                            ),
                                                                                                                   html.Div(className='colorwrapper wasch',
                                                                                                                            children=
                                                                                                                                        html.Div(className='colorcircle',
                                                                                                                                                 children=[
                                                                                                                                                             html.Div(className='filled',
                                                                                                                                                                      id='wasch-fill'),
                                                                                                                                                             html.P(children='19°'),
                                                                                                                                                             html.P(children='50%')
                                                                                                                                                         ]
                                                                                                                                                 )
                                                                                                                            ),
                                                                                                                   html.Div(className='colorwrapper kinder',
                                                                                                                            children=
                                                                                                                                        html.Div(className='colorcircle',
                                                                                                                                                 children=[
                                                                                                                                                             html.Div(className='filled',
                                                                                                                                                                      id='kinder-fill'),
                                                                                                                                                             html.P(children='19°'),
                                                                                                                                                             html.P(children='50%')
                                                                                                                                                         ]
                                                                                                                                                 )
                                                                                                                            ),
                                                                                                                   html.Div(className='colorwrapper buegel',
                                                                                                                            children=
                                                                                                                                        html.Div(className='colorcircle',
                                                                                                                                                 children=[
                                                                                                                                                             html.Div(className='filled',
                                                                                                                                                                      id='buegel-fill'),
                                                                                                                                                             html.P(children='19°'),
                                                                                                                                                             html.P(children='50%')
                                                                                                                                                         ]
                                                                                                                                                 )
                                                                                                                            ),
                                                                                                                   html.Div(className='colorwrapper kueche',
                                                                                                                            children=
                                                                                                                                        html.Div(className='colorcircle',
                                                                                                                                                 children=[
                                                                                                                                                             html.Div(className='filled',
                                                                                                                                                                      id='kueche-fill'),
                                                                                                                                                             html.P(children='19°'),
                                                                                                                                                             html.P(children='50%')
                                                                                                                                                         ]
                                                                                                                                                 )
                                                                                                                            ),
                                                                                                                   html.Div(className='colorwrapper wohn',
                                                                                                                            children=
                                                                                                                                        html.Div(className='colorcircle',
                                                                                                                                                 children=[
                                                                                                                                                            html.Div(className='filled',
                                                                                                                                                                     id='wohn-fill'),
                                                                                                                                                            html.P(children='19°'),
                                                                                                                                                            html.P(children='50%')
                                                                                                                                                            ]
                                                                                                                                                )
                                                                                                                            ),
                                                                                                                   html.Div(className='align-self-center',
                                                                                                                            children=
                                                                                                                                        html.Img(src='/assets/Grundriss2D-01_imagemap_2-01.svg', className='haus')
                                                                                                                            )
                                                                                                                   ]
                                                                                                       )
                                                                                      ),
                                                                         html.Div(className='col-2 main-div')
                                                                         ]
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
                                                    
                                             ]),
                               
                            ])
    
    
    





