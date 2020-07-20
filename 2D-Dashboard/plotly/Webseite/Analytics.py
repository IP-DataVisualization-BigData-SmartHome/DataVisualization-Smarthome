# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 15:41:43 2020

@author: Mues
"""

import dash_html_components as html
import dash_core_components as dcc
import datetime as dt
from postgre import postgre_connector, pd

class analytics:
    
    def __init__(self):
        self.active_rooms = {'Arbeitszimmer' : False, 'Badezimmer' : True, 'Bügelzimmer' : False,
                             'Kinderzimmer' : False, 'Küche' : False, 'Schlafzimmer' : False,
                             'Waschküche' : False, 'Wohnzimmer' : False }
        self.start_date = dt.date(2016, 2 , 16)
        self.end_date = dt.date(2016, 2 , 24)
        self.mode = 'a'
        self.data = 'tempd'
        self.graph = html.Div(className='graph-analytics')
    
    
    def set_active_room(self, room):
        if self.active_rooms[room] == False:
            return { 'color' : '#BFC0BF'}
        else: 
            return { 'color' : '#00B1AC'} 
    
    def get_site(self):
        return html.Div([   
                            html.Nav(className='fixed-top', 
                                     children= 
                                                 html.Div(className='container-fluid head-design',
                                                          children= 
                                                                       html.Div(className='row',
                                                                                children= [
                                                                                            html.Div(className='col-4'),
                                                                                            html.Div(className='col-4 text-center head-analytics', 
                                                                                                     children= html.A('Analytics')
                                                                                                     ),
                                                                                            html.Div(className='col-4 text-right logo', id = 'mydiv',
                                                                                                    children = html.A(children = html.Img(src='assets/logo.png', height=70, width='auto'), href='start'))
                                                                                          ]
                                                                                )
                                                         )
                                     ),
                            html.Main(className='analyticsbody', children =                                                    
                                    html.Div(
                                              children=
                                                 html.Div(className='container-fluid main', 
                                                          children= [
                                                                                            html.Div(className='row', style = {'padding-top' : '30px'}, 
                                                                                                     children= [ 
                                                                                                                 html.Div(className='col-3',
                                                                                                                          children= [
                                                                                                                                     
                                                                                                                                      html.Div(className='frame', 
                                                                                                                                               children= [
                                                                                                                                                           html.Button(className='checkbox',  name='room', type='checkbox', value='2', id = 'Az'),
                                                                                                                                                           html.Label(className='room-selection', children='Arbeitszimmer', htmlFor='Az', id='Arbeitszimmer',
                                                                                                                                                                      style = self.set_active_room('Arbeitszimmer'))
                                                                                                                                                         ]
                                                                                                                                               ),
                                                                                                                                      html.Div(className='frame', 
                                                                                                                                               children= [
                                                                                                                                                           html.Button(className='checkbox', name='room', type='checkbox', value='3', id = 'Baz'),
                                                                                                                                                           html.Label(className='room-selection', htmlFor = 'Baz', children='Badezimmer', id = 'Badezimmer',
                                                                                                                                                                      style = self.set_active_room('Badezimmer'))
                                                                                                                                                         ]
                                                                                                                                               ),
                                                                                                                                      html.Div(className='frame', 
                                                                                                                                               children= [
                                                                                                                                                           html.Button(className='checkbox', name='room', type='checkbox', value='4', id = 'Büz'),
                                                                                                                                                           html.Label(className='room-selection', htmlFor = 'Büz', children='Bügelzimmer', id = 'Bügelzimmer',
                                                                                                                                                                      style = self.set_active_room('Bügelzimmer'))
                                                                                                                                                         ]
                                                                                                                                               ),
                                                                                                                                      html.Div(className='frame', 
                                                                                                                                               children= [
                                                                                                                                                           html.Button(className='checkbox', name='room', type='checkbox', value='5', id = 'Kz'),
                                                                                                                                                           html.Label(className='room-selection', htmlFor = 'Kz', children='Kinderzimmer', id = 'Kinderzimmer',
                                                                                                                                                                      style = self.set_active_room('Kinderzimmer'))
                                                                                                                                                         ]
                                                                                                                                               ),                                                                   
                                                                                                                                      html.Div(className='frame', 
                                                                                                                                               children= [
                                                                                                                                                           html.Button(className='checkbox', name='room', type='checkbox', value='6', id = 'Kü'),
                                                                                                                                                           html.Label(className='room-selection', htmlFor = 'Kü', children='Küche', id = 'Küche',
                                                                                                                                                                      style = self.set_active_room('Küche'))
                                                                                                                                                         ]
                                                                                                                                               ),                  
                                                                                                                                      html.Div(className='frame', 
                                                                                                                                               children= [
                                                                                                                                                           html.Button(className='checkbox', name='room', type='checkbox', value='7', id = 'Sz'),
                                                                                                                                                           html.Label(className='room-selection', htmlFor = 'Sz', children='Schlafzimmer', id = 'Schlafzimmer',
                                                                                                                                                                      style = self.set_active_room('Schlafzimmer'))
                                                                                                                                                         ]
                                                                                                                                               ),
                                                                                                                                      html.Div(className='frame', 
                                                                                                                                               children= [
                                                                                                                                                           html.Button(className='checkbox', name='room', type='checkbox', value='8', id = 'Wk'),
                                                                                                                                                           html.Label(className='room-selection', htmlFor = 'Wk', children='Waschküche', id = 'Waschküche',
                                                                                                                                                                      style = self.set_active_room('Waschküche'))
                                                                                                                                                         ]
                                                                                                                                               ),         
                                                                                                                                      html.Div(className='frame', 
                                                                                                                                               children= [
                                                                                                                                                           html.Button(className='checkbox', name='room', type='checkbox', value='9', id = 'Wz'),
                                                                                                                                                           html.Label(className='room-selection', htmlFor = 'Wz', children='Wohnzimmer', id = 'Wohnzimmer',
                                                                                                                                                                      style = self.set_active_room('Wohnzimmer'))
                                                                                                                                                         ]
                                                                                                                                               )
                                                                                                                                    ]
                                                                                                                        ),
                                                                                                                html.Div(className='col-9',
                                                                                                                          children= 
                                                                                                                                     html.Div(className='graph', children= [self.graph], id = 'analytics_graph')
                                                                                                                                              
                                                                                                                                              
                                                                                                                        )
                                                                                                                ]
                                                                                                                
                                                                                                    ),
                                                                                            html.Div(className='row',
                                                                                                     children= [
                                                                                                               html.Div(className='col-3',
                                                                                                                        
                                                                                                                        ),
                                                                                                               html.Div(className='col-9 dataselect',
                                                                                                                        children = [
                                                                                                                                    html.Div(className='select form-check-inline',
                                                                                                                                             children= [
                                                                                                                                                         dcc.RadioItems(
                                                                                                                                                                 options=[
                                                                                                                                                                                 {'label': ' Temperatur ', 'value': 'temp'},
                                                                                                                                                                                 {'label': ' Luftfeuchtigkeit', 'value': 'hum'},
                                                                                                                                                                                 {'label': ' Temperatur draußen', 'value': 'tempd'},
                                                                                                                                                                                 {'label': ' Luftfeuchtigkeit draußen', 'value': 'humd'}
                                                                                                                                                                         ],
                                                                                                                                                                value= self.data,
                                                                                                                                                                labelStyle={'display': 'inline-block'},
                                                                                                                                                                labelClassName = 'time',
                                                                                                                                                                id = 'mode_data'
                                                                                                                                                                        )
                                                                                                                                                       ]
                                                                                                                                            ),
                                                                                                                                   html.Div(className='select form-check-inline',
                                                                                                                                            children = 
                                                                                                                                                          
                                                                                                                                                         dcc.DatePickerRange(
                                                                                                                                                                 id='daterange',
                                                                                                                                                                 min_date_allowed=dt.datetime(2016, 1, 12),
                                                                                                                                                                 max_date_allowed=dt.datetime(2016, 5, 26),
                                                                                                                                                                 initial_visible_month=dt.datetime(2016, 1, 13),
                                                                                                                                                                 #end_date= pd.to_datetime(DB_conn.get_last_date()['datum'][0]).date(),
                                                                                                                                                                 #start_date= pd.to_datetime(DB_conn.get_first_date()['datum'][0]).date(),
                                                                                                                                                                 start_date = self.start_date,
                                                                                                                                                                 end_date = self.end_date,
                                                                                                                                                                 className='daterange',
                                                                                                                                                                 with_portal = True
                                                                                                                                                                             )                
                                                                                                                                                                   
                                                                                                                                           ),
                                                                                                                                   html.Div(className='select form-check-inline',
                                                                                                                                             children= [
                                                                                                                                                 
                                                                                                                                                         dcc.RadioItems(
                                                                                                                                                                 options=[
                                                                                                                                                                                 {'label' : ' Minuten', 'value': 'a'},
                                                                                                                                                                                 {'label': ' Stunden', 'value': 'h'},
                                                                                                                                                                                 {'label': ' Tage', 'value': 'd'},
                                                                                                                                                                                 {'label': ' Monate', 'value': 'm'}
                                                                                                                                                                         ],
                                                                                                                                                                value= self.mode,
                                                                                                                                                                labelStyle={'display': 'inline-block'},
                                                                                                                                                                labelClassName = 'time',
                                                                                                                                                                id = 'mode_time'
                                                                                                                                                                        )                                                
                                                                                                                                                          ]
                                                                                                                                            )
                                                                                                                                    ]
                                                                                                                        )
                                                                                                            ]
                                                                                                    )
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
                                                                                                                   html.A(className='nav-link nav-link-active',
                                                                                                                          href='analytics',
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
                                                                                                                   html.A(className='nav-link',
                                                                                                                          href='dashboard',
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
                                                                                                                          href='optimization',
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
                                                                                                                                     
                        ]
                    )
       