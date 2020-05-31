# -*- coding: utf-8 -*-
"""
Created on Fri May 22 17:17:56 2020

@author: Mues
"""

# -*- coding: utf-8 -*-
"""
Created on Fri May 22 16:44:22 2020

@author: Mues
"""

import dash_core_components as dcc
import dash_html_components as html
import psycopg2
from postgre import postgre_connector
from datetime import datetime as dt
from datetime import timedelta

class Wohn:

    def wohn_seite(self, uhrzeiten, dashboard_datum_liste, dashboard_uhrzeit):
            DB_connector = postgre_connector()
            
            day1 = [int(dashboard_datum_liste[0]),int(dashboard_datum_liste[1]),int(dashboard_datum_liste[2]),00,00]
            day2 = [int(dashboard_datum_liste[0]),int(dashboard_datum_liste[1]),int(dashboard_datum_liste[2]),23,50]
            result = DB_connector.get_data(day1, day2, 'a', ['t2', 'rh_2'])
            #print(result)
            
            erster_eintrag = DB_connector.get_first_date()
            letzter_eintrag = DB_connector.get_last_date()
            self.__erster_eintrag_timestamp = erster_eintrag['date'][0]
            self.__letzter_eintrag_timestamp = letzter_eintrag['date'][0]
            return html.Div([
                                 html.Nav(className='fixed-top',
                                     children=
                                                 html.Div(className='container-fluid head-design',
                                                          children=[
                                                                      html.Div(className='row',
                                                                               children=[
                                                                                           html.Div(id='temp_draussen'),
                                                                                           # html.Div(className='col-4 text-right text-head',
                                                                                           #          children=
                                                                                           #                      html.Div(children='10°C'
                                                                                           #                               #<!-- Datensatz: Temperatur draußen -->
                                                                                           #                               )
                                                                                           #          ),
                                                                                           html.Div(className='col-1',                                                                                                                                                                                                                             
                                                                                                    ),
                                                                                           
                                                                                            html.Div(style={'margin-top': '25px', 'position':'relative', 'z-index':'3'},
                                                                                                    className='col-3',                                
                                                                                                    id='Datum',
                                                                                                    children=   
                                                                                                                dcc.DatePickerSingle(                                                                                                                                        
                                                                                                                                        #style={'background-color': '#000000'},
                                                                                                                                        id='DatePickerWohn',
                                                                                                                                        display_format='DD.MM.YYYY',
                                                                                                                                        min_date_allowed=self.__erster_eintrag_timestamp,
                                                                                                                                        max_date_allowed=self.__letzter_eintrag_timestamp - timedelta(days=1),
                                                                                                                                        #min_date_allowed=dt(2016, 1, 11),
                                                                                                                                        #max_date_allowed=dt(2016, 5, 27),
                                                                                                                                        initial_visible_month=dt(int(dashboard_datum_liste[0]), int(dashboard_datum_liste[1]), int(dashboard_datum_liste[2])),
                                                                                                                                        #initial_visible_month=dt(2016, 1, 11),
                                                                                                                                        #date=str(dt(2016, 1, 11))
                                                                                                                                        date=str(dt(int(dashboard_datum_liste[0]), int(dashboard_datum_liste[1]), int(dashboard_datum_liste[2])))
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
                                html.Div(className='container-fluid main',
                                         children=
                                                     html.Div(className='row reihe',
                                                              children=[
                                                                        html.Div(className='col-lg-7 left',
                                                                                 children=[
                                                                                             html.H1(className='ueber',
                                                                                                     children='Wohnzimmer'
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
                                                                                                       children=dcc.Graph(
                                                                                                                             id='Graph_Temperatur_Wohn',
                                                                                                                             figure = {
                                                                                                                                 'data': [
                                                                                                                                             {'x': result['date'], 'y': result['t2'], 'type': 'scatter', 'name': 'SF'},
                                                                                                                                         ],
                                                                                                                                  'layout': {
                                                                                                                                              'title': 'Temperatur'
                                                                                                                                            }
                                                                                                                                     }
                                                                                                                             ),
                                                                                                                     ),
                                                                                                   
                                                                                             
                                                                                               html.Div(className='card-graph',
                                                                                                        style={'margin-top': '300px'},
                                                                                                        children=dcc.Graph(
                                                                                                                              id='Graph_Luftfeucht_Wohn',
                                                                                                                              figure = {
                                                                                                                                  'data': [
                                                                                                                                              {'x': result['date'], 'y': result['rh_2'], 'type': 'scatter', 'name': 'SF'},
                                                                                                                                          ],
                                                                                                                                   'layout': {
                                                                                                                                               'title': 'Luftfeuchtigkeit'
                                                                                                                                             }
                                                                                                                                      }
                                                                                                                              ),
                                                                                                                      ),
                                                                                          ]
                                                                                 ),
                                                                        html.Div(className='col-lg-5 right',
                                                                                 children=
                                                                                             html.A(href='dashboard.html',
                                                                                                    children=
                                                                                                                html.Img(className='haus',
                                                                                                                         src='/assets/Grundriss2D-wohn.svg'
                                                                                                                         )
                                                                                                    )
                                                                                 )
                                                                        ]
                                                              )
                                         )
                                ])
