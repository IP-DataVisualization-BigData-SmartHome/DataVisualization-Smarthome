# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:18:10 2020

@author: Mues
"""

import dash_html_components as html
import dash_core_components as dcc
from datetime import datetime as dt
import psycopg2
from postgre import postgre_connector
from datetime import timedelta

class Dashboard:

    def __init__(self):
        DB_connector = postgre_connector()
        erster_eintrag = DB_connector.get_first_date()
        letzter_eintrag = DB_connector.get_last_date()
        self.__erster_eintrag_timestamp = erster_eintrag['date'][0]
        self.__letzter_eintrag_timestamp = letzter_eintrag['date'][0]
        # print(self.__letzter_eintrag_timestamp)
        #print(type(erster_eintrag))
        #print(type(letzter_eintrag))
        #print(erster_eintrag['date'])
        #print(letzter_eintrag['date'].head())
 
    def dashboard_seite(self, uhrzeiten):
        return html.Div([
                            html.Div(hidden='true', id='variablen_abspeichern'),
                            html.Nav(className='fixed-top',
                                     children=
                                                 html.Div(className='container-fluid head-design',
                                                          children=[
                                                                      html.Div(className='row',
                                                                               children=[
                                                                                           #html.Div(id='temp_draussen'),
                                                                                            html.Div(className='col-2 text-right text-head',
                                                                                                     children=
                                                                                                                 html.Div(id='temp_draussen'#children='10°C'
                                                                                                                          #<!-- Datensatz: Temperatur draußen -->
                                                                                                                          )
                                                                                                     ),
                                                                                           html.Div(className='col-2',                                                                                                                                                                                                                             
                                                                                                    ),
                                                                                           html.Div(#className='col-4 text-center text-head',
                                                                                                    style={'margin-top': '32px', 'position':'relative', 'z-index':'3'},
                                                                                                    className='col-1,5 text-center text-head2',
                                                                                                    children=
                                                                                                                dcc.Dropdown(id='dropdown-uhrzeit',
                                                                                                                             #style={ 'position':'absolute', 'z-index':'3'},
                                                                                                                             placeholder='Uhrzeit',
                                                                                                                             options=[{'label': i.strftime("%H:%M") + ' Uhr', 'value': i} for i in uhrzeiten],
                                                                                                                             )
                                                                                                    
                                                                                                                #html.A(className='nav-head',
                                                                                                                 #      href='#',
                                                                                                                  #     children='18:20'
                                                                                                                       #<!-- Bei Click Uhrzeitauswahl -->
                                                                                                                   #    )
                                                                                                    ),
                                                                                            html.Div(style={'margin-top': '25px', 'position':'relative', 'z-index':'3'},
                                                                                                    className='col-4',                                
                                                                                                    id='Datum',
                                                                                                    children=   
                                                                                                                dcc.DatePickerSingle(                                                                                                                                        
                                                                                                                                        #style={'background-color': '#000000'},
                                                                                                                                        id='my-date-picker-single',
                                                                                                                                        display_format='DD.MM.YYYY',
                                                                                                                                        min_date_allowed=self.__erster_eintrag_timestamp,
                                                                                                                                        max_date_allowed=self.__letzter_eintrag_timestamp - timedelta(days=1),
                                                                                                                                        #min_date_allowed=dt(2016, 1, 11),
                                                                                                                                        #max_date_allowed=dt(2016, 5, 27),
                                                                                                                                        initial_visible_month=self.__erster_eintrag_timestamp,
                                                                                                                                        #initial_visible_month=dt(2016, 1, 11),
                                                                                                                                        #date=str(dt(2016, 1, 11))
                                                                                                                                        date=str(self.__letzter_eintrag_timestamp)
                                                                                                                                    )
                                                                                                                #html.A(className='nav-head',
                                                                                                                 #      href='#',
                                                                                                                  #     children=' Montag, 17. Nov.'
                                                                                                                       #<!-- Bei Click Datumauswahl -->
                                                                                                                   #    )
                                                                                                    ),
                                                                                           #html.Div(id='output-test-callback'),
                                                                                           html.Div(id='luftfeuchte_wind_draussen'),
                                                                                           # html.Div(className='col-2 text-center luft-wind',
                                                                                           #          children=[
                                                                                           #                      html.Div(children='Luftfeuchte: 43%'
                                                                                           #                               #<!-- Datensatz: Luftfeuchte draußen -->
                                                                                           #                               ),
                                                                                           #                      html.Div(children='Wind: 10 km/h'
                                                                                           #                               #<!-- Datensatz: Wind draußen -->
                                                                                           #                               )
                                                                                           #                      ]
                                                                                           #          )
                                                                                       ]
                                                                               ),
                                                                      html.Div(className='row',
                                                                               children=[
                                                                                   html.Div(className='col-4 text-right text-head',
                                                                                                    #children=
                                                                                                     #           html.Div(children='10°C'
                                                                                                      #                   #<!-- Datensatz: Temperatur draußen -->
                                                                                                       #                  )
                                                                                                    ),
                                                                                          # html.Div(className='text-center',                                
                                                                                           #         id='Datum',
                                                                                            #        children=   
                                                                                             #                   dcc.DatePickerSingle(
                                                                                              #                                          #style={'background-color': '#000000'},
                                                                                               #                                         id='my-date-picker-single',
                                                                                                #                                        display_format='DD.MM.YYYY',
                                                                                                 #                                       min_date_allowed=dt(2016, 1, 11),
                                                                                                  #                                      max_date_allowed=dt(2016, 5, 27),
                                                                                                   #                                     initial_visible_month=dt(2016, 1, 11),
                                                                                                    #                                    date=str(dt(2016, 1, 11, 23, 59, 59))
                                                                                                     #                               )
                                                                                                                #html.A(className='nav-head',
                                                                                                                 #      href='#',
                                                                                                                  #     children=' Montag, 17. Nov.'
                                                                                                                       #<!-- Bei Click Datumauswahl -->
                                                                                                                   #    )
                                                                                                    #),
                                                                                           #html.Div(id='output-test-callback')
                                                                                           ]
                                                                               )
                                                              ])
                                                 ),       
                                html.Div(className='container main',
                                         children=[                                                                
                                                    html.Div(className='row',
                                                             children=[
                                                                         html.Div(className='col-2 main-div relative d-flex justify-content-center',
                                                                                  children=
                                                                                              html.Div(id='stromverbrauch_lichtverbrauch')
                                                                                              # html.Div(className='sidecard',
                                                                                              #          children=[
                                                                                              #                      html.Div(className='strom',
                                                                                              #                               #<!-- Strom-Fläche -->
                                                                                              #                               children=[
                                                                                              #                                           html.Div(className='verbrauch-text',
                                                                                              #                                                    children='Stromverbrauch'
                                                                                              #                                                    ),
                                                                                              #                                           html.Div(children=
                                                                                              #                                                            html.I(className='mdi mdi-flash icons-verbrauch')
                                                                                              #                                                    ),
                                                                                              #                                           html.Div(className='stromverbrauch verbrauch-zahl',
                                                                                              #                                                    children='200 W'
                                                                                              #                                                    #<!-- Stromverbrauch eintragen -->
                                                                                              #                                                    )
                                                                                              #                                          ] 
                                                                                                                                        
                                                                                              #                               ),
                                                                                              #                      html.Div(className='licht',
                                                                                              #                               #<!-- Licht-Fläche -->
                                                                                              #                               children=[
                                                                                              #                                           html.Div(className='verbrauch-text',
                                                                                              #                                                    children='Lichtverbrauch'
                                                                                              #                                                    ),
                                                                                              #                                           html.Div(children=
                                                                                              #                                                                html.I(className='mdi mdi-lightbulb-on icons-verbrauch')
                                                                                              #                                                    ),
                                                                                              #                                           html.Div(className='stromverbrauch verbrauch-zahl',
                                                                                              #                                                    children='22 W'
                                                                                              #                                                    #<!-- Lichtverbrauch eintragen -->
                                                                                              #                                                    )
                                                                                              #                                           ]
                                                                                              #                               )
                                                                                              #              ])
                                                                                      ),
                                                                         html.Div(className='col-8',
                                                                                  children=
                                                                                              html.Div(className='row',
                                                                                                       children=[
                                                                                                                   html.A(className='kreise-link',
                                                                                                                          href='bad.html',
                                                                                                                          children=
                                                                                                                                   html.Div(className='colorwrapper bad',
                                                                                                                                            children=
                                                                                                                                                        html.Div(id='zimmer5')
                                                                                                                                                        #html.Div(className='colorcircle',
                                                                                                                                                         #        children=[
                                                                                                                                                          #                   html.Div(className='filled',
                                                                                                                                                           #                           id='bad-fill'),
                                                                                                                                                            #                 html.P(children='19°'),
                                                                                                                                                             #                html.P(children='50%')
                                                                                                                                                               #          ]
                                                                                                                                                                # )
                                                                                                                                            )
                                                                                                                           ),
                                                                                                                   html.A(className='kreise-link',
                                                                                                                          href='arbeit.html',
                                                                                                                          children=                                                                                                                   
                                                                                                                                   html.Div(className='colorwrapper arbeits',
                                                                                                                                            children=
                                                                                                                                                        html.Div(id='zimmer4')
                                                                                                                                                        # html.Div(className='colorcircle',
                                                                                                                                                        #          children=[
                                                                                                                                                        #                      html.Div(className='filled',
                                                                                                                                                        #                               id='arbeits-fill'),
                                                                                                                                                        #                      html.P(children='19°'),
                                                                                                                                                        #                      html.P(children='50%')
                                                                                                                                                        #                  ]
                                                                                                                                                        #          )
                                                                                                                                            ),
                                                                                                                           ),
                                                                                                                   html.A(className='kreise-link',
                                                                                                                          href='schlaf.html',
                                                                                                                          children=                                                                                                                   
                                                                                                                                   html.Div(className='colorwrapper schlaf',
                                                                                                                                            children=
                                                                                                                                                        html.Div(id='zimmer9')
                                                                                                                                                        # html.Div(className='colorcircle',
                                                                                                                                                        #          children=[
                                                                                                                                                        #                      html.Div(className='filled',
                                                                                                                                                        #                               id='schlaf-fill'),
                                                                                                                                                        #                      html.P(children='19°'),
                                                                                                                                                        #                      html.P(children='50%')
                                                                                                                                                        #                  ]
                                                                                                                                                        #          )
                                                                                                                                            ),
                                                                                                                           ),
                                                                                                                   html.A(className='kreise-link',
                                                                                                                          href='wasch.html',
                                                                                                                          children=
                                                                                                                                   html.Div(className='colorwrapper wasch',
                                                                                                                                            children=
                                                                                                                                                        html.Div(id='zimmer3')
                                                                                                                                                        # html.Div(className='colorcircle',
                                                                                                                                                        #          children=[
                                                                                                                                                        #                      html.Div(className='filled',
                                                                                                                                                        #                               id='wasch-fill'),
                                                                                                                                                        #                      html.P(children='19°'),
                                                                                                                                                        #                      html.P(children='50%')
                                                                                                                                                        #                  ]
                                                                                                                                                        #          )
                                                                                                                                            ),
                                                                                                                           ),
                                                                                                                   html.A(className='kreise-link',
                                                                                                                          href='kinder.html',
                                                                                                                          children=
                                                                                                                                   html.Div(className='colorwrapper kinder',
                                                                                                                                            children=
                                                                                                                                                        html.Div(id='zimmer8')
                                                                                                                                                        # html.Div(className='colorcircle',
                                                                                                                                                        #          children=[
                                                                                                                                                        #                      html.Div(className='filled',
                                                                                                                                                        #                               id='kinder-fill'),
                                                                                                                                                        #                      html.P(children='19°'),
                                                                                                                                                        #                      html.P(children='50%')
                                                                                                                                                        #                  ]
                                                                                                                                                        #          )
                                                                                                                                            ),
                                                                                                                           ),
                                                                                                                   html.A(className='kreise-link',
                                                                                                                          href='buegel.html',
                                                                                                                          children=
                                                                                                                                   html.Div(className='colorwrapper buegel',
                                                                                                                                            children=
                                                                                                                                                        html.Div(id='zimmer7')
                                                                                                                                                        # html.Div(className='colorcircle',
                                                                                                                                                        #          children=[
                                                                                                                                                        #                      html.Div(className='filled',
                                                                                                                                                        #                               id='buegel-fill'),
                                                                                                                                                        #                      html.P(children='19°'),
                                                                                                                                                        #                      html.P(children='50%')
                                                                                                                                                        #                  ]
                                                                                                                                                        #          )
                                                                                                                                            ),
                                                                                                                           ),
                                                                                                                   html.A(className='kreise-link',
                                                                                                                          href='kueche.html',
                                                                                                                          children=
                                                                                                                                   html.Div(className='colorwrapper kueche',
                                                                                                                                            children=
                                                                                                                                                        html.Div(id='zimmer1')
                                                                                                                                                        # html.Div(className='colorcircle',
                                                                                                                                                        #          children=[
                                                                                                                                                        #                      html.Div(className='filled',
                                                                                                                                                        #                               id='kueche-fill'),
                                                                                                                                                        #                      html.P(children='19°'),
                                                                                                                                                        #                      html.P(children='50%')
                                                                                                                                                        #                  ]
                                                                                                                                                        #          )
                                                                                                                                            ),
                                                                                                                           ),
                                                                                                                   html.A(className='kreise-link',
                                                                                                                          href='wohn.html',
                                                                                                                          children=
                                                                                                                                   html.Div(className='colorwrapper wohn',
                                                                                                                                            children=
                                                                                                                                                        html.Div(id='zimmer2')
                                                                                                                                                        # html.Div(className='colorcircle',
                                                                                                                                                        #          children=[
                                                                                                                                                        #                     html.Div(className='filled',
                                                                                                                                                        #                              id='wohn-fill'),
                                                                                                                                                        #                     html.P(children='19°'),
                                                                                                                                                        #                     html.P(children='50%')
                                                                                                                                                        #                     ]
                                                                                                                                                        #         )
                                                                                                                                            ),
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
    
    
    





