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
import pandas as pd


case_dict = { 'visibility' : False, 'windspeed' : False, 'appliances' : False, 'lights' : False, 'schimmel' : False}

class Optimization:

    def __init__(self, date = None):
        self.date = date
        
    def set_date(self, date):
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
        
    def schimmel_case(self):
       result = self.result[['datum','t1', 'rh_1', 't2', 'rh_2', 't3', 'rh_3', 't4', 'rh_4', 't5', 'rh_5',
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
    
    def visibility_case(self):
        result = self.result[['datum','visibility']]
        threshold = self.threshold['visibility'][0]
        
        filt_result = result[result['visibility'] > threshold]
        
        if len(filt_result) > 1:
            
            data = []
            
            div = copy.deepcopy(optimazation_dict['visibility'])
            tag = div.children
            graphtag = self.ref_finder(tag) 
            
            data.append({'x' : list(self.result['datum']), 'y' : list(self.result['visibility']), 'type' : 'line', 'name' : 'Sichtbarkeit', 'marker' : { 'color' : '#33C1B1'}})
            data.append({'x' : list(filt_result['datum']), 'y' : list(filt_result['visibility']), 'type' : 'bar', 'name' : 'Gute Sichtbarkeit', 'marker' : { 'color' : '#EE0000' }})

            fig = { 'data' : data, 'layout' : {'title' : 'Schöner Tag heute!'}}
            
            graph = dcc.Graph(figure = fig)
            graphtag.children = graph
            graphtag.className = 'card-graph-optimization'
            
            return div
        else:
            return False
    
    def windspeed_case(self):
        result = self.result[['datum','windspeed']]
        threshold = self.threshold['windspeed'][0]
        
        date = pd.Timestamp.to_pydatetime(result['datum'][0])
        
        cond1 = pd.Timestamp(year = date.year, month = date.month, day = date.day, hour = 7, minute = 0 )
        cond2 = pd.Timestamp(year = date.year, month = date.month, day = date.day, hour = 22, minute = 0 )
        
        filt_result = result[result['windspeed'] > threshold]
                
        time_filt = filt_result[(filt_result.datum >= cond1) & (filt_result.datum <= cond2)]
        
        if len(time_filt) > 1:
            
            data = []
            
            div = copy.deepcopy(optimazation_dict['windspeed'])
            tag = div.children
            graphtag = self.ref_finder(tag) 
            
            data.append({'x' : list(self.result['datum']), 'y' : list(self.result['windspeed']), 'type' : 'line', 'name' : 'Windgeschwindigkeit', 'marker' : { 'color' : '#33C1B1'}})
            data.append({'x' : list(time_filt['datum']), 'y' : list(time_filt['windspeed']), 'type' : 'bar', 'name' : 'Starke Windgeschwindigkeiten', 'marker' : { 'color' : '#EE0000' }})

            fig = { 'data' : data, 'layout' : {'title' : 'Wäsche aufhängen oder Windrad lohnt sich!'}}
            
            graph = dcc.Graph(figure = fig)
            graphtag.children = graph
            graphtag.className = 'card-graph-optimization'
            
            return div
        else:
            return False
    
    def appliances_case(self):
        result = self.result[['datum','appliances']]
        threshold = self.threshold['appliances'][0]
        
        date = pd.Timestamp.to_pydatetime(result['datum'][0])
        
        cond1 = pd.Timestamp(year = date.year, month = date.month, day = date.day, hour = 0, minute = 0 )
        cond2 = pd.Timestamp(year = date.year, month = date.month, day = date.day, hour = 7, minute = 0 )
        cond3 = pd.Timestamp(year = date.year, month = date.month, day = date.day, hour = 22, minute = 0 )
        cond4 = pd.Timestamp(year = date.year, month = date.month, day = date.day, hour = 23, minute = 50 )
        
        filt_result = result[result['appliances'] > threshold]
                
        time_filt = filt_result[(filt_result.datum >= cond1) & (filt_result.datum <= cond2) & (filt_result.datum <= cond3) & (filt_result.datum <= cond4) ] 
        
        if len(time_filt) > 1:
            
            data = []
            
            div = copy.deepcopy(optimazation_dict['appliances'])
            tag = div.children
            graphtag = self.ref_finder(tag) 
            
            data.append({'x' : list(self.result['datum']), 'y' : list(self.result['appliances']), 'type' : 'line', 'name' : 'Stromverbrauch durch Geräte', 'marker' : { 'color' : '#33C1B1'}})
            data.append({'x' : list(time_filt['datum']), 'y' : list(time_filt['appliances']), 'type' : 'bar', 'name' : 'Unnötiger Stromverbrauch', 'marker' : { 'color' : '#EE0000' }})

            fig = { 'data' : data, 'layout' : {'title' : 'Lief der Fernseher in der Nacht?'}}
            
            graph = dcc.Graph(figure = fig)
            graphtag.children = graph
            graphtag.className = 'card-graph-optimization'
            
            return div
        else:
            return False
    
    def lights_case(self):
        result = self.result[['datum','lights']]
        threshold = self.threshold['lights'][0]
        
        date = pd.Timestamp.to_pydatetime(result['datum'][0])
        
        cond1 = pd.Timestamp(year = date.year, month = date.month, day = date.day, hour = 0, minute = 0 )
        cond2 = pd.Timestamp(year = date.year, month = date.month, day = date.day, hour = 7, minute = 0 )
        cond3 = pd.Timestamp(year = date.year, month = date.month, day = date.day, hour = 10, minute = 0 )
        cond4 = pd.Timestamp(year = date.year, month = date.month, day = date.day, hour = 17, minute = 00 )
        
        filt_result = result[result['lights'] > threshold]
                
        time_filt = filt_result[(filt_result.datum >= cond1) & (filt_result.datum <= cond2) & (filt_result.datum <= cond3) & (filt_result.datum <= cond4) ]
        
        if len(time_filt) > 1:
            
            data = []
            
            div = copy.deepcopy(optimazation_dict['lights'])
            tag = div.children
            graphtag = self.ref_finder(tag) 
            
            data.append({'x' : list(self.result['datum']), 'y' : list(self.result['lights']), 'type' : 'line', 'name' : 'Stromverbrauch durch Licht', 'marker' : { 'color' : '#33C1B1'}})
            data.append({'x' : list(time_filt['datum']), 'y' : list(time_filt['lights']), 'type' : 'bar', 'name' : 'Unnötiger Stromverbrauch', 'marker' : { 'color' : '#EE0000' }})

            fig = { 'data' : data, 'layout' : {'title' : 'Licht vielleicht angelassen?'}}
            
            graph = dcc.Graph(figure = fig)
            graphtag.children = graph
            graphtag.className = 'card-graph-optimization'
            
            return div
        else:
            return False
    
    def case_check(self):
        if self.date != None:
            
            retDiv = html.Div()

            date = dt.datetime(self.date.year, self.date.month, self.date.day, 0, 0)
            date2 = date + dt.timedelta(hours= 23, minutes = 50)
            db_con = postgre_connector()
            self.threshold = db_con.get_data(self.date, self.date, 'm', [])
            self.result = db_con.get_data(date, date2, 'a', [])
            
            case_list = []
            
            visibility = self.visibility_case()
            windspeed = self.windspeed_case()
            appliances = self.appliances_case()
            lights = self.appliances_case()
            schimmel = self.schimmel_case()
            
            if appliances != False:
                case_list.append(appliances)
            
            if lights != False:
                case_list.append(lights)
                
            case_list.append(schimmel)
                
            if windspeed != False:
                case_list.append(windspeed)
                
            if visibility != False:
                case_list.append(visibility)

            retDiv.children = case_list
            
            return retDiv
                    
 
    def optimization_seite(self):
        return html.Div([
                            html.Nav(className = 'nav-abstand',
                                     children=
                                                 html.Div(className='container-fluid head-design',
                                                          children=
                                                                      html.Div(className='row',
                                                                               children=[
                                                                                           html.Div(className='col-4',
                                                                                                    children=   
                                                                                                                dcc.DatePickerSingle(                                                                                                                                                                                                                                                                                
                                                                                                                                        id='datepicker-optimization',
                                                                                                                                        className = 'datepicker-opti',
                                                                                                                                        display_format='DD.MM.YYYY',
                                                                                                                                        min_date_allowed=dt.datetime(2016, 1, 12),
                                                                                                                                        max_date_allowed=dt.datetime(2016, 5, 26),
                                                                                                                                        initial_visible_month=self.date.month,
                                                                                                                                        #initial_visible_month=dt(2016, 1, 11),
                                                                                                                                        #date=str(dt(2016, 1, 11))
                                                                                                                                        date=self.date
                                                                                                                                    )
                                                                                                    ),
                                                                                           html.Div(className='col-4 text-center head-optimization',
                                                                                                    children=
                                                                                                                html.A(children='Optimization')
                                                                                                    ),
                                                                                           html.Div(className='col-4 text-right logo', id = 'mydiv',
                                                                                                    children = html.Img(src='assets/logo.png', height=80, width=20))
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