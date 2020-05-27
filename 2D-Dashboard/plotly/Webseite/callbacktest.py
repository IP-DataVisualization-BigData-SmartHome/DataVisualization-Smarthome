#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 13:54:02 2020

@author: lukas
"""

import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc
from postgre import postgre_connector
import datetime as dt
app = dash.Dash()

dbcon = postgre_connector()

app.layout = html.Div(children = [ dcc.Graph(
        id='test2',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'
            }
        }
    ),
    html.Button(id='test1')
    ]
    )

@app.callback(
    Output('test2', 'figure'),
    [Input('test1', 'n_clicks')])
def graph_cb(value):
    day1 = dt.datetime(2016, 1, 17)
    day2 = dt.datetime(2016, 2, 23)
    result = dbcon.get_data(day1, day2, 'a', ['t1', 't2', 'rh_1'])
    data = []
    
    for col in result.keys():
        if col != 'date':
            tmp = {'y' : list(result[col]), 'x' : list(result['date']), 'type' : 'bar', 'name' : col}
            data.append(tmp)
    
    tmp = {'title' : 'Test_Graph'}
    ret = {}
    ret['data'] = data
    ret['layout'] = tmp
    return ret
 
def testing(value):
    day1 = dt.datetime(2016, 1, 17)
    day2 = dt.datetime(2016, 2, 23)
    result = dbcon.get_data(day1, day2, 'a', ['t1', 't2', 'rh_1'])
    data = []
    
    retDiv = html.Div(children= [])
    
    for room in site.rooms:
        graphObj = dcc.Graph()
        for col in result.keys():
            if col != 'date':
                tmp = {'x' : list(data[col]), 'y' : list(data['date']), 'type' : 'bar', 'name' : col}
                data.append(tmp)
    
    tmp = {'title' : 'Test_Graph'}
    ret = {}
    ret['data'] = data
    ret['layout'] = tmp
    ret.append(tmp)
    return ret   

if __name__ == '__main__':
    app.run_server(debug=True)
    
    
    
    