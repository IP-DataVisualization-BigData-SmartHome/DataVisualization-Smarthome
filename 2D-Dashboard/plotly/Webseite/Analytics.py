# -*- coding: utf-8 -*-
"""
@author: Lukas Schnittcher


                                                                                                                                                          html.Div(className='form-check-inline', 
                                                                                                                                                                   children= [
                                                                                                                                                                               html.Button(className='checkbox', type='radio', name='TimeFrame', id='Tag', value='D'),
                                                                                                                                                                               html.Label(className='time', htmlFor='Tag', children='TAG', id='d')
                                                                                                                                                                             ]
                                                                                                                                                                   ),
                                                                                                                                                          html.Div(className='form-check-inline', 
                                                                                                                                                                   children= [
                                                                                                                                                                               html.Button(className='checkbox', type='radio', name='TimeFrame', id='Woche', value='W'),
                                                                                                                                                                               html.Label(className='time', htmlFor='Woche', children='WOCHE', id = 'w')
                                                                                                                                                                             ]
                                                                                                                                                                   ),
                                                                                                                                                          html.Div(className='form-check-inline', 
                                                                                                                                                                   children= [
                                                                                                                                                                               html.Button(className='checkbox', type='radio', name='TimeFrame', id='Monat', value='M'),
                                                                                                                                                                               html.Label(className='time', htmlFor='Monat', children='MONAT', id = 'm')
                                                                                                                                                                             ]
                                                                                                                                                                   )
                     
                                                                                                                                                           html.Div(className='frame', 
                                                                                                                                               children= [
                                                                                                                                                           html.Button(className='checkbox', name='room', type='checkbox', value='1', id = 'All'),
                                                                                                                                                           html.Label(className='room-selection', htmlFor = 'All', children='Alle', id='Alle')
                                                                                                                                                         ]
                                                                                                                                               ),
                                                                                                                                                          
"""

import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import dash
#import postgre

class analytics:
    
    def __init__(self):
        self.rooms = []
        self.mode = 'd'
        self.data = 'temp'
    
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
                                    html.Div(
                                              children=
                                                 html.Div(className='container-fluid main', 
                                                          children= [
                                                                                            html.Div(className='row', 
                                                                                                     children= [ 
                                                                                                                 html.Div(className='col-3',
                                                                                                                          children= [
                                                                                                                                     
                                                                                                                                      html.Div(className='frame', 
                                                                                                                                               children= [
                                                                                                                                                           html.Button(className='checkbox', name='room', type='checkbox', value='2', id = 'Az'),
                                                                                                                                                           html.Label(className='room-selection', htmlFor = 'Az', children='Arbeitszimmer', id='Arbeitszimmer')
                                                                                                                                                         ]
                                                                                                                                               ),
                                                                                                                                      html.Div(className='frame', 
                                                                                                                                               children= [
                                                                                                                                                           html.Button(className='checkbox', name='room', type='checkbox', value='3', id = 'Baz'),
                                                                                                                                                           html.Label(className='room-selection', htmlFor = 'Baz', children='Badezimmer', id = 'Badezimmer')
                                                                                                                                                         ]
                                                                                                                                               ),
                                                                                                                                      html.Div(className='frame', 
                                                                                                                                               children= [
                                                                                                                                                           html.Button(className='checkbox', name='room', type='checkbox', value='4', id = 'Büz'),
                                                                                                                                                           html.Label(className='room-selection', htmlFor = 'Büz', children='Bügelzimmer', id = 'Bügelzimmer')
                                                                                                                                                         ]
                                                                                                                                               ),
                                                                                                                                      html.Div(className='frame', 
                                                                                                                                               children= [
                                                                                                                                                           html.Button(className='checkbox', name='room', type='checkbox', value='5', id = 'Kz'),
                                                                                                                                                           html.Label(className='room-selection', htmlFor = 'Kz', children='Kinderzimmer', id = 'Kinderzimmer')
                                                                                                                                                         ]
                                                                                                                                               ),                                                                   
                                                                                                                                      html.Div(className='frame', 
                                                                                                                                               children= [
                                                                                                                                                           html.Button(className='checkbox', name='room', type='checkbox', value='6', id = 'Kü'),
                                                                                                                                                           html.Label(className='room-selection', htmlFor = 'Kü', children='Küchenzimmer', id = 'Küche')
                                                                                                                                                         ]
                                                                                                                                               ),                  
                                                                                                                                      html.Div(className='frame', 
                                                                                                                                               children= [
                                                                                                                                                           html.Button(className='checkbox', name='room', type='checkbox', value='7', id = 'Sz'),
                                                                                                                                                           html.Label(className='room-selection', htmlFor = 'Sz', children='Schlafzimmer', id = 'Schlafzimmer')
                                                                                                                                                         ]
                                                                                                                                               ),
                                                                                                                                      html.Div(className='frame', 
                                                                                                                                               children= [
                                                                                                                                                           html.Button(className='checkbox', name='room', type='checkbox', value='8', id = 'Wk'),
                                                                                                                                                           html.Label(className='room-selection', htmlFor = 'Wk', children='Waschküche', id = 'Waschküche')
                                                                                                                                                         ]
                                                                                                                                               ),         
                                                                                                                                      html.Div(className='frame', 
                                                                                                                                               children= [
                                                                                                                                                           html.Button(className='checkbox', name='room', type='checkbox', value='9', id = 'Wz'),
                                                                                                                                                           html.Label(className='room-selection', htmlFor = 'Wz', children='Wohnzimmer', id = 'Wohnzimmer')
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
                                                                                                                        
                                                                                                                        ),
                                                                                                               html.Div(className='col-9',
                                                                                                                        children = [
                                                                                                                                    html.Div(className='select form-check-inline',
                                                                                                                                             children= [
                                                                                                                                                         dcc.RadioItems(
                                                                                                                                                                 options=[
                                                                                                                                                                                 {'label': ' Temperatur ', 'value': 'temp'},
                                                                                                                                                                                 {'label': ' Luftfeuchtigkeit', 'value': 'hum'},
                                                                                                                                                                                 {'label': ' Temperatur draußen', 'value': 'tempd'}
                                                                                                                                                                         ],
                                                                                                                                                                value='MTL',
                                                                                                                                                                labelStyle={'display': 'inline-block'},
                                                                                                                                                                labelClassName = 'time'
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
                                                                                                                                                 
                                                                                                                                                         dcc.RadioItems(
                                                                                                                                                                 options=[
                                                                                                                                                                                 {'label': ' Tage', 'value': 'd'},
                                                                                                                                                                                 {'label': ' Wochen', 'value': 'w'},
                                                                                                                                                                                 {'label': ' Monate', 'value': 'm'}
                                                                                                                                                                         ],
                                                                                                                                                                value='MTL',
                                                                                                                                                                labelStyle={'display': 'inline-block'},
                                                                                                                                                                labelClassName = 'time'
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

site = analytics()

app.layout = site.get_site()

'''
@app.callback(
    Output('Arbeitszimmer', 'style'),
    [Input('Arbeitszimmer', 'n_clicks')])
def click_az(value):
    if value % 2 == 1:
        site.rooms.append('Arbeitszimmer')
        return { 'color' : '#00B1AC'}
    else:
        if 'Arbeitszimmer' in site.rooms:
            site.rooms.remove('Arbeitszimmer')
        return { 'color' : '#BFC0BF'}
    
@app.callback(
    Output('Badezimmer', 'style'),
    [Input('Badezimmer', 'n_clicks')])
def click_baz(value):
    if value % 2 == 1:
        site.rooms.append('Badezimmer')
        return { 'color' : '#00B1AC'}
    else:
        if 'Badezimmer' in site.rooms:
            site.rooms.remove('Badezimmer')
        return { 'color' : '#BFC0BF'}

@app.callback(
    Output('Bügelzimmer', 'style'),
    [Input('Bügelzimmer', 'n_clicks')])
def click_büz(value):
    if value % 2 == 1:
        site.rooms.append('Bügelzimmer')
        return { 'color' : '#00B1AC'}
    else:
        if 'Bügelzimmer' in site.rooms:
            site.rooms.remove('Bügelzimmer')
        return { 'color' : '#BFC0BF'}

@app.callback(
    Output('Kinderzimmer', 'style'),
    [Input('Kinderzimmer', 'n_clicks')])
def click_kz(value):
    if value % 2 == 1:
        site.rooms.append('Kinderzimmer')
        return { 'color' : '#00B1AC'}
    else:
        if 'Kinderzimmer' in site.rooms:
            site.rooms.remove('Kinderzimmer')
        return { 'color' : '#BFC0BF'}  

@app.callback(
    Output('Küche', 'style'),
    [Input('Küche', 'n_clicks')])
def click_kü(value):
    if value % 2 == 1:
        site.rooms.append('Küche')
        return { 'color' : '#00B1AC'}
    else:
        if 'Küche' in site.rooms:
            site.rooms.remove('Küche')
        return { 'color' : '#BFC0BF'}   

@app.callback(
    Output('Schlafzimmer', 'style'),
    [Input('Schlafzimmer', 'n_clicks')])
def click_sz(value):
    if value % 2 == 1:
        site.rooms.append('Schlafzimmer')
        return { 'color' : '#00B1AC'}
    else:
        if 'Schlafzimmer' in site.rooms:
            site.rooms.remove('Schlafzimmer')
        return { 'color' : '#BFC0BF'} 
    
@app.callback(
    Output('Waschküche', 'style'),
    [Input('Waschküche', 'n_clicks')])
def click_wk(value):
    if value % 2 == 1:
        site.rooms.append('Waschküche')
        return { 'color' : '#00B1AC'}
    else:
        if 'Waschküche' in site.rooms:
            site.rooms.remove('Waschküche')
        return { 'color' : '#BFC0BF'} 

@app.callback(
    Output('Wohnzimmer', 'style'),
    [Input('Wohnzimmer', 'n_clicks')])
def click_wz(value):
    if value % 2 == 1:
        site.rooms.append('Wohnzimmer')
        return { 'color' : '#00B1AC'}
    else:
        if 'Wohnzimmer' in site.rooms:
            site.rooms.remove('Wohnzimmer')
        return { 'color' : '#BFC0BF'} 
'''    
"""
@app.callback(
    [Output('d', 'style'), Output('w', 'style'), Output('m', 'style')],
    [Input('d', 'id')])
def click_day(value):
    return { 'color' : '#00B1AC'}, { 'color' : '#BFC0BF'}, { 'color' : '#BFC0BF'}

@app.callback(
    [Output('d', 'style'), Output('w', 'style'), Output('m', 'style')],
    [Input('w', 'id')])
def click_week(value):
    return { 'color' : '#BFC0BF'}, { 'color' : '#00B1AC'}, { 'color' : '#BFC0BF'}


@app.callback(
    [Output('d', 'style'), Output('w', 'style'), Output('m', 'style')],
    [Input('w', 'n_clicks')])
def click_week(value):
    return { 'color' : '#BFC0BF'}, { 'color' : '#00B1AC'}, { 'color' : '#BFC0BF'}

@app.callback(
    [Output('d', 'style'), Output('w', 'style'), Output('m', 'style')],
    [Input('m', 'n_clicks')])
def click_month(value):
    return { 'color' : '#BFC0BF'}, { 'color' : '#BFC0BF'}, { 'color' : '#00B1AC'}

"""

if __name__ == '__main__':
    app.run_server(debug=True)




