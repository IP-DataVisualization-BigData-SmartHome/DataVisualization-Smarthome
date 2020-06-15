# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 10:31:36 2020

@author: Mues
"""
import dash_html_components as html
import dash_core_components as dcc
import datetime as dt
from postgre import postgre_connector
from optimazation_help import optimazation_dict, Taupunkt
import copy


case_dict = { 'visibility' : False, 'windspeed' : False, 'appliances' : False, 'lights' : False, 'schimmel' : False}

class Optimization:

    def __init__(self, date = None):
        self.date = date
                        
    def ref_finder(self, ref):
        while True:
            if type(ref) != list and ref.children == 'Plotly Diagramm':
                break
            elif type(ref) == list:
                ref = ref[1]
            else:
                ref = ref.children
                
        return ref
        
    def schimmel_case(self, result):
       result = result[['datum','t1', 'rh_1', 't2', 'rh_2', 't3', 'rh_3', 't4', 'rh_4', 't5', 'rh_5',
                        't6', 'rh_6', 't7', 'rh_7', 't8', 'rh_8', 't9', 'rh_9', 't_out']]
       
       tdewlist = []
       
       for temp, hum in zip(list(result['t1']),list(result['rh_1'])):
           tdewlist.append(Taupunkt(temp, hum))
    
       test = 0.5*(result['t1']-result['t_out']) + result['t_out']
          
       data = []
       div = copy.deepcopy(optimazation_dict['schimmel'])
       tag = div.children
       graphtag = self.ref_finder(tag)                   
       data.append({'x' : list(result['datum']), 'y' : list(result['t1']), 'type' : 'line', 'name' : 'Temperatur'})
       data.append({'x' : list(result['datum']), 'y' : list(result['rh_1']), 'type' : 'line', 'name' : 'Luftfeuchte'})
       data.append({'x' : list(result['datum']), 'y' : tdewlist, 'type' : 'line', 'name' : 'Taupunkt'})
       data.append({'x' : list(result['datum']), 'y' : list(result['t_out']), 'type' : 'line', 'name' : 'Temperatur Draußen'})
       data.append({'x' : list(result['datum']), 'y' : list(test), 'type' : 'line', 'name' : 'gemittelter Oberflächentemepraturwert'})
       
       fig = { 'data' : data, 'layout' : {'title' : 'Schimmel_Test'}}
       graph = dcc.Graph(figure = fig)
       graphtag.children = graph
       graphtag.className = 'card-graph-optimization'

       return div
    
    def case_check(self):
        if self.date != None:
            
            retDiv = html.Div()
            child_list = []
            filt_list = []

            date = dt.datetime(self.date.year, self.date.month, self.date.day, 0, 0)
            date2 = date + dt.timedelta(hours= 23, minutes = 50)
            db_con = postgre_connector()
            threshold = db_con.get_data(self.date, self.date, 'm', [])
            result = db_con.get_data(date, date2, 'a', [])
            
            for col in result.columns:
                if col != 'datum':
                    filt_result = result[['datum', col]]
                    filt_result = filt_result[result[col] > threshold[col][0]]
                    if filt_result.empty != True and len(filt_result) >= 5:
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
                    graphtag = self.ref_finder(tag)                   
                    data.append({'x' : list(result['datum']), 'y' : list(result[case]), 'type' : 'bar', 'name' : case})
                    data.append({'x' : list(frame['datum']), 'y' : list(frame[case]), 'type' : 'bar', 'name' : case + ' mit überschreitung'})
                    fig = { 'data' : data, 'layout' : {'title' : case}}
                    graph = dcc.Graph(figure = fig)
                    graphtag.children = graph
                    graphtag.className = 'card-graph-optimization'
                    child_list.append(div)
            
          
            child_list.append(self.schimmel_case(result))
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
                                                                                                                   html.A(className='nav-link nav-link-active',
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
                        ])