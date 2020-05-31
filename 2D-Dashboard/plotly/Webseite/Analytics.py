# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:18:10 2020

@author: Mues

 html.Nav(className='navbar fixed-bottom',
                                         children= 
                                                     html.Div(className='container-fluid navdiv',
                                                              children= [
                                                                              html.Div(className='col navdiv', 
                                                                                       children = 
                                                                                                       html.A(className='nav-link nav-link-active', href='#',
                                                                                                              children = [
                                                                                                                          html.I(className='mdi mdi-google-analytics navicon'),
                                                                                                                          html.P(className='nav-text', children='Analytics')
                                                                                                                         ]
                                                                                                             )
                                                                                       ),
                                                                              html.Div(className='col navdiv', 
                                                                                       children = 
                                                                                                       html.A(className='nav-link', href='dashboard.html',
                                                                                                              children = [
                                                                                                                          html.I(className='mdi mdi-home navicon'),
                                                                                                                          html.P(className='nav-text', children='Dashboard')
                                                                                                                         ]
                                                                                                             )
                                                                                       ),
                                                                              html.Div(className='col navdiv', 
                                                                                       children = 
                                                                                                       html.A(className='nav-link', href='optimization.html',
                                                                                                              children = [
                                                                                                                          html.I(className='mdi mdi-sync navicon'),
                                                                                                                          html.P(className='nav-text', children='Optimization')
                                                                                                                         ]
                                                                                                             )
                                                                                       )                         
                                                                          ]                   
                                                                )
                                        )

"""

import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import dash
#import postgre


class analytics:
    
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
                                                                                            html.Div(className='col-4')
                                                                                          ]
                                                                                )
                                                         )
                                     ),
                            html.Main(                                                    
                                    html.Form(method='post', action = '',
                                              children=
                                                 html.Div(className='container-fluid main', 
                                                          children= [
                                                                                            html.Div(className='row', 
                                                                                                     children= [ 
                                                                                                                 html.Div(className='col-3',
                                                                                                                          children= [
                                                                                                                                      html.Div(className='frame', 
                                                                                                                                               children= [
                                                                                                                                                           html.Button(className='checkbox', name='room', type='checkbox', value='1', id = 'Alle'),
                                                                                                                                                           html.Label(className='room-selection', htmlFor = 'Alle', children='Alle')
                                                                                                                                                         ]
                                                                                                                                               ),
                                                                                                                                      html.Div(className='frame', 
                                                                                                                                               children= [
                                                                                                                                                           html.Button(className='checkbox', name='room', type='checkbox', value='2', id = 'Arbeitszimmer'),
                                                                                                                                                           html.Label(className='room-selection', htmlFor = 'Arbeitszimmer', children='Arbeitszimmer')
                                                                                                                                                         ]
                                                                                                                                               ),
                                                                                                                                      html.Div(className='frame', 
                                                                                                                                               children= [
                                                                                                                                                           html.Button(className='checkbox', name='room', type='checkbox', value='3', id = 'Badezimmer'),
                                                                                                                                                           html.Label(className='room-selection', htmlFor = 'Badezimmer', children='Badezimmer')
                                                                                                                                                         ]
                                                                                                                                               ),
                                                                                                                                      html.Div(className='frame', 
                                                                                                                                               children= [
                                                                                                                                                           html.Button(className='checkbox', name='room', type='checkbox', value='4', id = 'Bügelzimmer'),
                                                                                                                                                           html.Label(className='room-selection', htmlFor = 'Bügelzimmer', children='Bügelzimmer')
                                                                                                                                                         ]
                                                                                                                                               ),
                                                                                                                                      html.Div(className='frame', 
                                                                                                                                               children= [
                                                                                                                                                           html.Button(className='checkbox', name='room', type='checkbox', value='5', id = 'Kinderzimmer'),
                                                                                                                                                           html.Label(className='room-selection', htmlFor = 'Kinderzimmer', children='Kinderzimmer')
                                                                                                                                                         ]
                                                                                                                                               ),                                                                   
                                                                                                                                      html.Div(className='frame', 
                                                                                                                                               children= [
                                                                                                                                                           html.Button(className='checkbox', name='room', type='checkbox', value='6', id = 'Küche'),
                                                                                                                                                           html.Label(className='room-selection', htmlFor = 'Küche', children='Küche')
                                                                                                                                                         ]
                                                                                                                                               ),                  
                                                                                                                                      html.Div(className='frame', 
                                                                                                                                               children= [
                                                                                                                                                           html.Button(className='checkbox', name='room', type='checkbox', value='7', id = 'Schlafzimmer'),
                                                                                                                                                           html.Label(className='room-selection', htmlFor = 'Schlafzimmer', children='Schlafzimmer')
                                                                                                                                                         ]
                                                                                                                                               ),
                                                                                                                                      html.Div(className='frame', 
                                                                                                                                               children= [
                                                                                                                                                           html.Button(className='checkbox', name='room', type='checkbox', value='8', id = 'Waschküche'),
                                                                                                                                                           html.Label(className='room-selection', htmlFor = 'Waschküche', children='Waschküche')
                                                                                                                                                         ]
                                                                                                                                               ),         
                                                                                                                                      html.Div(className='frame', 
                                                                                                                                               children= [
                                                                                                                                                           html.Button(className='checkbox', name='room', type='checkbox', value='9', id = 'Wohnzimmer'),
                                                                                                                                                           html.Label(className='room-selection', htmlFor = 'Wohnzimmer', children='Wohnzimmer')
                                                                                                                                                         ]
                                                                                                                                               )
                                                                                                                                    ]
                                                                                                                        ),
                                                                                                                html.Div(className='col-9',
                                                                                                                          children= 
                                                                                                                                     html.Div(className='graph', children='Plotly Diagramm')
                                                                                                                        )
                                                                                                                ]
                                                                                                    ),
                                                                                            html.Div(className='row',
                                                                                                     children= [
                                                                                                               html.Div(className='col-3',
                                                                                                                        children=
                                                                                                                                    html.Button('Absenden',type='submit')
                                                                                                                        ),
                                                                                                               html.Div(className='col-9',
                                                                                                                        children = [
                                                                                                                                    html.Div(className='select form-check-inline',
                                                                                                                                             children= [
                                                                                                                                                          html.Div(className='form-check-inline', 
                                                                                                                                                                   children= [
                                                                                                                                                                               html.Button(className='checkbox', type='checkbox', name='Attselect', id='Temp', value='Temp'),
                                                                                                                                                                               html.Label(className='time', htmlFor='Temp', children='Temperatur')
                                                                                                                                                                             ]
                                                                                                                                                                   ),
                                                                                                                                                          html.Div(className='form-check-inline', 
                                                                                                                                                                   children= [
                                                                                                                                                                               html.Button(className='checkbox', type='checkbox', name='Attselect', id='Luft', value='Hum1'),
                                                                                                                                                                               html.Label(className='time', htmlFor='Luft', children='Luftfeuchte')
                                                                                                                                                                             ]
                                                                                                                                                                   ),
                                                                                                                                                          html.Div(className='form-check-inline', 
                                                                                                                                                                   children= [
                                                                                                                                                                               html.Button(className='checkbox', type='checkbox', name='Attselect', id='TempD', value='TempD'),
                                                                                                                                                                               html.Label(className='time', htmlFor='TempD', children='Temp. draußen')
                                                                                                                                                                             ]
                                                                                                                                                                   )
                                                                                                                                                          ]
                                                                                                                                            ),
                                                                                                                                   html.Div(className='select form-check-inline',
                                                                                                                                            children = 
                                                                                                                                                          html.Div(className='form-check-inline datepicker',
                                                                                                                                                                   children= [
                                                                                                                                                                                html.Button(className='checkbox'),
                                                                                                                                                                                html.Label(className='time', children='Letzter tag: Placeholder Datepicker')
                                                                                                                                                                             ]
                                                                                                                                                                  )
                                                                                                                                           ),
                                                                                                                                   html.Div(className='select form-check-inline',
                                                                                                                                             children= [
                                                                                                                                                          html.Div(className='form-check-inline', 
                                                                                                                                                                   children= [
                                                                                                                                                                               html.Button(className='checkbox', type='radio', name='TimeFrame', id='Tag', value='D'),
                                                                                                                                                                               html.Label(className='time', htmlFor='Tag', children='TAG')
                                                                                                                                                                             ]
                                                                                                                                                                   ),
                                                                                                                                                          html.Div(className='form-check-inline', 
                                                                                                                                                                   children= [
                                                                                                                                                                               html.Button(className='checkbox', type='radio', name='TimeFrame', id='Woche', value='W'),
                                                                                                                                                                               html.Label(className='time', htmlFor='Woche', children='WOCHE')
                                                                                                                                                                             ]
                                                                                                                                                                   ),
                                                                                                                                                          html.Div(className='form-check-inline', 
                                                                                                                                                                   children= [
                                                                                                                                                                               html.Button(className='checkbox', type='radio', name='TimeFrame', id='Monat', value='M'),
                                                                                                                                                                               html.Label(className='time', htmlFor='Monat', children='MONAT')
                                                                                                                                                                             ]
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
                                                                                                                   html.A(className='nav-link',
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
                                                                                                                                     
                        ]
                    )

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
    '/home/lukas/Desktop/IP_Repo/DataVisualization-Smarthome/2D-Dashboard/css/analytics.css',
    '/home/lukas/Desktop/IP_Repo/DataVisualization-Smarthome/2D-Dashboard/css/main.css',
]

app = dash.Dash(external_stylesheets=external_stylesheets, external_scripts=external_scripts)
app.title = 'Analytics'

@app.callback(
    [Output(component_id='Alle', component_property='style'),
     Output(component_id='Alle', component_property='value')],
    [Input(component_id='Alle', component_property='value')]
)
def update_output_div(input_value):
    if(input_value == 0):
        return { 'color' : '#00B1AC' }, 1
    else:
        return { 'color' : '#BFC0BF' }, 0



site = analytics()

app.layout = site.get_site()
app.run_server(debug = True)




