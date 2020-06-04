# -*- coding: utf-8 -*-
"""
Created on Sun May 10 16:27:30 2020

@author: Mues
"""

import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash
from postgre import postgre_connector
from optimazation_help import optimazation_dict
import datetime as dt
import numpy as np
import copy

def ref_finder(ref):
    while True:
        if type(ref) != list and ref.children == 'Plotly Diagramm':
            break
        elif type(ref) == list:
            ref = ref[1]
        else:
            ref = ref.children
            
    return ref

class Optimization:

    def __init__(self, date = None):
        self.date = date
        
    def case_check(self):
        if self.date != None:
            
            retDiv = html.Div()
            child_list = []
            filt_list = []


            
            case_dict = { 'visibility' : False, 'windspeed' : False}
            
            date = dt.datetime(site.date.year, self.date.month, self.date.day, 0, 0)
            date2 = date + dt.timedelta(hours= 23, minutes = 50)
            db_con = postgre_connector()
            threshold = db_con.get_data(site.date, site.date, 'm', [])
            result = db_con.get_data(date, date2, 'a', [])
            
            for col in result.columns:
                if col != 'datum':
                    filt_result = result[['datum', col]]
                    filt_result = filt_result[result[col] > threshold[col][0]]
                    if filt_result.empty != True and len(filt_result) >= 72:
                        if col in case_dict.keys():
                            case_dict[col] = True
                        filt_list.append(filt_result)
         
            for case in case_dict.keys():
                if case_dict[case] == True:
                    frame = None
                    for df in filt_list:
                        if case in df.columns:
                            frame = df
                    data = []
                    div = copy.deepcopy(optimazation_dict[case])
                    tag = div.children
                    graphtag = ref_finder(tag)                   
                    data.append({'x' : list(result['datum']), 'y' : list(result[case]), 'type' : 'bar', 'name' : case})
                    data.append({'x' : list(frame['datum']), 'y' : list(frame[case]), 'type' : 'bar', 'name' : case + ' mit überschreitung'})
                    fig = { 'data' : data, 'layout' : {'title' : case}}
                    graph = dcc.Graph(figure = fig)
                    graphtag.children = graph
                    graphtag.className = 'card-graph'
                    child_list.append(div)
            
          
            retDiv.children = child_list
            
            return retDiv
                    
 
    def optimization_seite(self):
        return html.Div([
                            html.Nav(className = 'nav-abstand',
                                     children=
                                                 html.Div(className='container-fluid head-design',
                                                          children=
                                                                      html.Div(className='row',
                                                                               children=[
                                                                                           html.Div(className='col-4'),
                                                                                           html.Div(className='col-4 text-center head-optimization',
                                                                                                    children=
                                                                                                                html.A(children='Optimization')
                                                                                                    ),
                                                                                           html.Div(className='col-4')
                                                                                       ]
                                                                               )
                                                          )
                                     ),
                            html.Main(children=
                                                  html.Div(className='container-fluid main', id = 'main',
                                                           children=
                                                                       html.Div(className='row',
                                                                                children=[
                                                                                            html.Div(className='col-1',
                                                                                                     children=[
                                                                                                                 html.I(className='mdi mdi-weather-sunny'),
                                                                                                                 html.I(className='mdi mdi-wind-turbine'),
                                                                                                                 html.I(className='mdi mdi-solar-power'),
                                                                                                                 html.I(className='mdi mdi-water-percent'),
                                                                                                                 html.I(className='mdi mdi-home-thermometer'),
                                                                                                                 html.I(className='mdi mdi-home-thermometer-outline'),
                                                                                                                 html.I(className='mdi mdi-weather-pouring')
                                                                                                             ]
                                                                                                     ),
                                                                                            html.Div(className='col-10', children = self.case_check()),
                                                                                            
                                                                                            html.Div(className='col-1'),
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
                        ])



                    
            


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
    '/home/lukas/Desktop/IP_Repo/DataVisualization-Smarthome/2D-Dashboard/css/optimization.css',
    '/home/lukas/Desktop/IP_Repo/DataVisualization-Smarthome/2D-Dashboard/css/main.css',
]

app = dash.Dash(external_stylesheets=external_stylesheets, external_scripts=external_scripts)
app.title = 'Optimazation'

site = Optimization(dt.datetime(2016, 4 , 15))
test = site.case_check()
#print(test)
app.layout = site.optimization_seite()


if __name__ == '__main__':
    app.run_server(debug=True)