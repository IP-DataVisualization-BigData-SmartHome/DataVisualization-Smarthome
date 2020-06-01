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

room_dict = {
             'Küche' : ('t1','rh_1'),
             'Wohnzimmer' : ('t2','rh_2'),
             'Waschraum' : ('t3','rh_3'),
             'Arbeitszimmer' : ('t4','rh_4'),
             'Badezimmer' : ('t5','rh_5'),
             'Bügelzimmer' : ('t7','rh_7'),
             'Kinderzimmer' : ('t8','rh_8'),
             'Elternzimmer' : ('t9','rh_9')
             }


def graph_cb(value):
    
    retDiv = html.Div(children = [])
    
    gathering = []
    
    if value == None: return 
    day1 = dt.datetime(2016, 1, 17)
    day2 = dt.datetime(2016, 2, 23)
    result = dbcon.get_data(day1, day2, 'h', [])
    data = []
    rooms =['Arbeitszimmer', 'Kinderzimmer']
    # Pro Raum nur temp und Luftfeuchte (Pro Graph)
    
    for room in rooms:
        roomtupel = room_dict[room]
        graphObj = dcc.Graph()
        tmp = {'y' : list(result[roomtupel[0]]), 'x' : list(result['datum']), 'type' : 'bar', 'name' : roomtupel[0]}
        data.append(tmp)
        tmp = {'y' : list(result[roomtupel[1]]), 'x' : list(result['datum']), 'type' : 'bar', 'name' : roomtupel[1]}
        data.append(tmp)
        tmp = {'title' : str(room)}
        ret = {}
        ret['data'] = data
        ret['layout'] = tmp
        graphObj.figure = ret
        gathering.append(graphObj)
    retDiv.children = gathering     
    
    return retDiv
 
print(graph_cb(0))   
    
    
day1 = dt.datetime(2016, 1, 17)
    day2 = dt.datetime(2016, 4, 23)
    result = dbcon.get_data(day1, day2, 'd', [])
    data = []
    rooms =['Arbeitszimmer', 'Kinderzimmer']
    # Pro Raum nur temp und Luftfeuchte (Pro Graph)
    
    for room in rooms:
        roomtupel = room_dict[room]
        graphObj = dcc.Graph()
        tmp = {'y' : list(result[roomtupel[0]]), 'x' : list(result['datum']), 'type' : 'bar', 'name' : roomtupel[0]}
        data.append(tmp)
        tmp = {'y' : list(result[roomtupel[1]]), 'x' : list(result['datum']), 'type' : 'bar', 'name' : roomtupel[1]}
        data.append(tmp)
        tmp = {'title' : str(room)}
        ret = {}
        ret['data'] = data
        ret['layout'] = tmp
        graphObj.figure = ret
        gathering.append(graphObj)
    retDiv.children = gathering     
    
    return retDiv    