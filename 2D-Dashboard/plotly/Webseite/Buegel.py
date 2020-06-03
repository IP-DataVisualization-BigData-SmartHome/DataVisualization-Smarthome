# -*- coding: utf-8 -*-
"""
Created on Fri May 22 17:13:22 2020

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
import numpy  as np

class Buegel:

    def buegel_seite(self, uhrzeiten, dashboard_datum_liste, dashboard_uhrzeit):
            DB_connector = postgre_connector()
            result = None
            initial_datum = None
            erster_eintrag = DB_connector.get_first_date()
            letzter_eintrag = DB_connector.get_last_date()
            self.__erster_eintrag_timestamp = erster_eintrag['datum'][0]
            self.__letzter_eintrag_timestamp = letzter_eintrag['datum'][0]            
            if(dashboard_datum_liste != None and dashboard_uhrzeit != None):                               
                day1 = [int(dashboard_datum_liste[0]),int(dashboard_datum_liste[1]),int(dashboard_datum_liste[2]),00,00]
                day2 = [int(dashboard_datum_liste[0]),int(dashboard_datum_liste[1]),int(dashboard_datum_liste[2]),23,50]
                result = DB_connector.get_data(day1, day2, 'a', ['t7', 'rh_7'])                    
                initial_datum = dt(int(dashboard_datum_liste[0]), int(dashboard_datum_liste[1]), int(dashboard_datum_liste[2]))              
                result_durchschnitt = DB_connector.get_data(day1, day2, 'a', ['t7', 'rh_7'])
                
                durchschnitt_temp = np.array(result_durchschnitt['t7']).mean().round(0)
                durchschnitt_luftfeucht = np.array(result_durchschnitt['rh_7']).mean().round(0)
                                                                                             
                
            else:                
                initial_datum = dt(self.__erster_eintrag_timestamp.year,self.__erster_eintrag_timestamp.month,self.__erster_eintrag_timestamp.day)
                day1 = [self.__erster_eintrag_timestamp.year,self.__erster_eintrag_timestamp.month,self.__erster_eintrag_timestamp.day,00,00]
                day2 = [self.__erster_eintrag_timestamp.year,self.__erster_eintrag_timestamp.month,self.__erster_eintrag_timestamp.day,23,50]
                result = DB_connector.get_data(day1, day2, 'a', ['t7', 'rh_7'])
                result_durchschnitt = DB_connector.get_data(day1, day2, 'a', ['t7', 'rh_7'])
                
                durchschnitt_temp = np.array(result_durchschnitt['t7']).mean().round(0)
                durchschnitt_luftfeucht = np.array(result_durchschnitt['rh_7']).mean().round(0)
            return html.Div([
                                html.Nav(className='fixed-top',
                                     children=
                                                 html.Div(className='container-fluid head-design',
                                                          children=[
                                                                      html.Div(className='row',
                                                                               children=[
                                                                                           html.Div(id='temp_draussen'),                                                                                         
                                                                                           html.Div(className='col-5',                                                                                                                                                                                                                             
                                                                                                    ),
                                                                                           
                                                                                            html.Div(style={'margin-top': '25px', 'position':'relative', 'z-index':'3'},
                                                                                                    className='col-3',                                
                                                                                                    id='Datum',
                                                                                                    children=   
                                                                                                                dcc.DatePickerSingle(                                                                                                                                        
                                                                                                                                        #style={'background-color': '#000000'},
                                                                                                                                        id='DatePickerBuegel',
                                                                                                                                        display_format='DD.MM.YYYY',
                                                                                                                                        min_date_allowed=self.__erster_eintrag_timestamp,
                                                                                                                                        max_date_allowed=self.__letzter_eintrag_timestamp - timedelta(days=1),
                                                                                                                                        #min_date_allowed=dt(2016, 1, 11),
                                                                                                                                        #max_date_allowed=dt(2016, 5, 27),
                                                                                                                                        initial_visible_month=initial_datum,
                                                                                                                                        #initial_visible_month=dt(2016, 1, 11),
                                                                                                                                        #date=str(dt(2016, 1, 11))
                                                                                                                                        date=str(initial_datum)
                                                                                                                                    )                                                                                                                
                                                                                                    ),                                                                                           
                                                                                           html.Div(id='luftfeuchte_wind_draussen'),                                                                                           
                                                                                       ]
                                                                               ),
                                                                      html.Div(className='row',
                                                                               children=
                                                                                   html.Div(className='col-4 text-right text-head'),
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
                                                                                                     children='Bügelzimmer'
                                                                                                     ),#Raumname
                                                                                             html.Div(className='container-fluid data-container',
                                                                                                      id='Durchschnitt_Temp_Luftfeuchte_Buegel',
                                                                                                      children=
                                                                                                                  html.Div(className='row',
                                                                                                                           children=[
                                                                                                                                       html.Div(className='col',
                                                                                                                                                children=
                                                                                                                                                           html.P(className='data temp',
                                                                                                                                                                  children=[
                                                                                                                                                                              durchschnitt_temp,#'20',#Raum Temperatur
                                                                                                                                                                              html.I(className='mdi mdi-temperature-celsius kreis-icon')
                                                                                                                                                                          ]
                                                                                                                                                                  )
                                                                                                                                               ),
                                                                                                                                       html.Div(className='col',
                                                                                                                                                children=
                                                                                                                                                           html.P(className='data temp',
                                                                                                                                                                  children=[
                                                                                                                                                                              durchschnitt_luftfeucht,#'60',#Raum Temperatur
                                                                                                                                                                              html.I(className='mdi mdi-water-percent kreis-icon')
                                                                                                                                                                          ]
                                                                                                                                                                  )
                                                                                                                                               )
                                                                                                                                       ]
                                                                                                                           )
                                                                                                      ),
                                                                                              html.Div(children=dcc.Graph(
                                                                                                                             id='Graph_Temperatur_Buegel',
                                                                                                                             figure = {
                                                                                                                                 'data': [
                                                                                                                                             {'x': result['datum'], 'y': result['t7'], 'type': 'scatter', 'name': 'SF'},
                                                                                                                                         ],
                                                                                                                                  'layout': {
                                                                                                                                              'title': 'Temperatur'
                                                                                                                                            }
                                                                                                                                     }
                                                                                                                             ),
                                                                                                                     ),
                                                                                                   
                                                                                             
                                                                                               html.Div(style={'margin-top': '50px'},
                                                                                                        children=dcc.Graph(
                                                                                                                              id='Graph_Luftfeucht_Buegel',
                                                                                                                              figure = {
                                                                                                                                  'data': [
                                                                                                                                              {'x': result['datum'], 'y': result['rh_7'], 'type': 'scatter', 'name': 'SF'},
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
                                                                                                                         src='/assets/Grundriss2D-buegel.svg'
                                                                                                                         )
                                                                                                    )
                                                                                 )
                                                                        ]
                                                              )
                                         )
                                ])
