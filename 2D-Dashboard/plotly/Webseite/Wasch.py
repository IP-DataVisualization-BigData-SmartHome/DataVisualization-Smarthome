# -*- coding: utf-8 -*-
"""
Created on Fri May 22 17:17:12 2020

@author: Mues
"""

# -*- coding: utf-8 -*-
"""
Created on Fri May 22 16:44:22 2020

@author: Mues
"""

import dash_html_components as html

class Wasch:

    def wasch_seite(self):
            return html.Div([
                                html.Nav(className='fixed-top',
                                     children=
                                                 html.Div(className='container-fluid head-design',
                                                          children=[
                                                                      html.Div(className='row',
                                                                               children=[
                                                                                           html.Div(className='col-4 text-right text-head',
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
                                                                                           html.Div(className='col text-center',
                                                                                                    id='Datum',
                                                                                                    children=
                                                                                                                html.A(className='nav-head',
                                                                                                                       href='#',
                                                                                                                       children=' Montag, 17. Nov.'
                                                                                                                       #<!-- Bei Click Datumauswahl -->
                                                                                                                       )
                                                                                                    )                                                                        
                                                                                           ]
                                                                               )
                                                              ])
                                 ),
                                html.Div(className='container-fluid main',
                                         children=
                                                     html.Div(className='row reihe',
                                                              children=[
                                                                        html.Div(className='col-lg-7 left',
                                                                                 children=[
                                                                                             html.H1(className='ueber',
                                                                                                     children='Waschküche'
                                                                                                     ),#Raumname
                                                                                             html.Div(className='container-fluid data-container',
                                                                                                      children=
                                                                                                                  html.Div(className='row',
                                                                                                                           children=[
                                                                                                                                       html.Div(className='col',
                                                                                                                                                children=
                                                                                                                                                           html.P(className='data temp',
                                                                                                                                                                  children=[
                                                                                                                                                                              '20',#Raum Temperatur
                                                                                                                                                                              html.I(className='mdi mdi-temperature-celsius kreis-icon')
                                                                                                                                                                          ]
                                                                                                                                                                  )
                                                                                                                                               ),
                                                                                                                                       html.Div(className='col',
                                                                                                                                                children=
                                                                                                                                                           html.P(className='data temp',
                                                                                                                                                                  children=[
                                                                                                                                                                              '60',#Raum Temperatur
                                                                                                                                                                              html.I(className='mdi mdi-water-percent kreis-icon')
                                                                                                                                                                          ]
                                                                                                                                                                  )
                                                                                                                                               )
                                                                                                                                       ]
                                                                                                                           )
                                                                                                      ),
                                                                                             html.Div(className='card-graph',
                                                                                                      children='Plotly Diagramm1'
                                                                                                      ),
                                                                                             html.Div(className='card-graph',
                                                                                                      children='Plotly Diagramm2'
                                                                                                      )
                                                                                          ]
                                                                                 ),
                                                                        html.Div(className='col-lg-5 right',
                                                                                 children=
                                                                                             html.A(href='dashboard.html',
                                                                                                    children=
                                                                                                                html.Img(className='haus',
                                                                                                                         src='/assets/Grundriss2D-wasch.svg'
                                                                                                                         )
                                                                                                    )
                                                                                 )
                                                                        ]
                                                              )
                                         )
                                ])
