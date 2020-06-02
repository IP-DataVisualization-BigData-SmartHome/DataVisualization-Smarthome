# -*- coding: utf-8 -*-
"""
@author: Lukas Schnittcher


                                                                                                                                                
                                                                                                                                                          
"""

import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import dash
import datetime as dt
from postgre import postgre_connector, pd

room_dict = {
             'Küche' : ('t1','rh_1'),
             'Wohnzimmer' : ('t2','rh_2'),
             'Waschküche' : ('t3','rh_3'),
             'Arbeitszimmer' : ('t4','rh_4'),
             'Badezimmer' : ('t5','rh_5'),
             'Bügelzimmer' : ('t7','rh_7'),
             'Kinderzimmer' : ('t8','rh_8'),
             'Schlafzimmer' : ('t9','rh_9')
             }
                                                                                                                                                  
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
                                                                                                                                                           html.Label(className='room-selection', children='Arbeitszimmer', htmlFor='Az', id='Arbeitszimmer')
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
                                                                                                                                     html.Div(className='graph', children= [], id = 'analytics_graph')
                                                                                                                                              
                                                                                                                                              
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
                                                                                                                                                                                 {'label': ' Temperatur draußen', 'value': 'tempd'},
                                                                                                                                                                                 {'label': ' Luftfeuchtigkeit draußen', 'value': 'humd'}
                                                                                                                                                                         ],
                                                                                                                                                                value='temp',
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
                                                                                                                                                                 end_date= pd.to_datetime(DB_conn.get_last_date()['datum'][0]).date(),
                                                                                                                                                                 start_date= pd.to_datetime(DB_conn.get_first_date()['datum'][0]).date(),
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
                                                                                                                                                                value='a',
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

DB_conn = postgre_connector()

site = analytics()

app.layout = site.get_site()


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
 
@app.callback(
    Output('analytics_graph', 'children'),  
    [Input('Arbeitszimmer', 'n_clicks'),
     Input('Badezimmer', 'n_clicks'),
     Input('Bügelzimmer', 'n_clicks'),
     Input('Kinderzimmer', 'n_clicks'),
     Input('Küche', 'n_clicks'),
     Input('Schlafzimmer', 'n_clicks'),
     Input('Waschküche', 'n_clicks'),
     Input('Wohnzimmer', 'n_clicks'),
     Input('daterange', 'start_date'),
     Input('daterange', 'end_date'),
     Input('mode_data', 'value'),
     Input('mode_time', 'value')])
def graph_cb(value1, value2, value3, value4, value5, value6, value7, value8, start_date, end_date, mode_data, mode_time):
    

    retDiv = html.Div(children = [])
    #graph = dcc.Graph(config = {'responsible' : True})
    start_date = dt.datetime.strptime(start_date, '%Y-%m-%d')
    end_date = dt.datetime.strptime(end_date, '%Y-%m-%d')

    room_list = []
    gath = []
    
    checkstring = ''
    
    if mode_data == 'temp':
        room_list += [room_dict[x][0] for x in site.rooms]
        result = DB_conn.get_data(start_date, end_date, mode_time, room_list)  
    
    elif mode_data == 'tempd':
        room_list += [room_dict[x][0] for x in site.rooms] 
        room_list += ['t_out']
        site.rooms += ['Temperatur Draußen']
        result = DB_conn.get_data(start_date, end_date, mode_time, room_list)
        
    elif mode_data == 'hum':
        room_list += [room_dict[x][1] for x in site.rooms]
        result = DB_conn.get_data(start_date, end_date, mode_time, room_list)
    
    elif mode_data == 'humd':
        room_list += [room_dict[x][1] for x in site.rooms]
        room_list += ['rh_out']
        site.rooms += ['Luftfeuchtigkeit Draußen']
        result = DB_conn.get_data(start_date, end_date, mode_time, room_list)
        
    data_col = list(result.columns).copy()
    data_col.remove('datum')
        
    for col,name in zip(data_col, site.rooms):
        if col != 'datum':
            fig_data = {'x' : result['datum'], 'y' : result[col], 'type' : 'bar', 'name' : name}
            gath.append(fig_data)
    
    #checkstring += str(data_col) + '  ' + str(site.rooms) + '  ' + str(room_list) 
    #checkstring += str(room_list)
    #checkstring += '  ' + str(site.rooms)
    
    if mode_data == 'tempd':
        site.rooms.remove('Temperatur Draußen')
    elif mode_data == 'humd':
        site.rooms.remove('Luftfeuchtigkeit Draußen')
    
    fig = { 'data' : gath, 'layout': {'title': 'Analytics Graph'}}
    graph = dcc.Graph(figure=fig)

    #checkstring += str(fig)
    
    retDiv.children = graph
    
    return retDiv



if __name__ == '__main__':
    app.run_server(debug=True)




