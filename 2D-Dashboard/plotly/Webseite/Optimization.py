# -*- coding: utf-8 -*-
"""

@author: Lukas Schnittcher

Die Klasse repräsentiert die Plotly Version der Analytics-HTML Seite

"""
import dash_html_components as html
import dash_core_components as dcc
import datetime as dt
from postgre import postgre_connector
from optimazation_help import optimazation_dict, Taupunkt, energyfromwind
import copy
import pandas as pd


class Optimization:

    #Initalisierung, falls ein Datum beim Aufrufen der Seite bereits in Dashboard.py ausgewählt wurde
    def __init__(self, date = None):
        self.date = date
    
    #Set-Date Methode, falls auf optimazaion.py ein anderes Datum ausgewählt wird
    def set_date(self, date):
        self.date = date
    
    #In den Vorlagen aus optimazation_help.py werden die Div-Elemente gesucht, in denen das Plotly Diagramm eingebunden wird                    
    def ref_finder(self, ref):
        while True:
            if type(ref) != list and ref.children == 'Plotly Diagramm':
                break
            elif type(ref) == list:
                ref = ref[1]
            else:
                ref = ref.children
                
        return ref
    
    #Hilfe-Funktion, erstellt aus einer Liste aus Listen eine Flache-Liste
    def flat_list(self, lol):
        flatlist = []
        for sublist in lol:
            for item in sublist:
                flatlist.append(item)
        return flatlist
                
        
    #Berechnung der Temperatur-Grenze, ab dem Schimmel-Gefährund auftritt (Wird immer getriggert)
    def schimmel_case(self):
       result = self.result[['datum','t1', 'rh_1', 't2', 'rh_2', 't3', 'rh_3', 't4', 'rh_4', 't5', 'rh_5',
                        't6', 'rh_6', 't7', 'rh_7', 't8', 'rh_8', 't9', 'rh_9', 't_out']]
   
       tdewlist = []
       
       test = []
       for temp, hum in zip(list(result['t1']),list(result['rh_1'])):
           test.append([Taupunkt(temp, hum)])
       tdewlist.append(('Küche', test))
       
       test = []
       for temp, hum in zip(list(result['t2']),list(result['rh_2'])):
           test.append([Taupunkt(temp, hum)])
       tdewlist.append(('Wohnzimmer', test))
    
       test = []
       for temp, hum in zip(list(result['t3']),list(result['rh_3'])):
           test.append([Taupunkt(temp, hum)])
       tdewlist.append(('Waschküche', test))
       
       test = []
       for temp, hum in zip(list(result['t4']),list(result['rh_4'])):
           test.append([Taupunkt(temp, hum)])
       tdewlist.append(('Büro', test))
       
       test = []    
       for temp, hum in zip(list(result['t5']),list(result['rh_5'])):
           test.append([Taupunkt(temp, hum)])
       tdewlist.append(('Badezimmer', test))          
       test = []
       
       for temp, hum in zip(list(result['t7']),list(result['rh_7'])):
           test.append([Taupunkt(temp, hum)])
       tdewlist.append(('Bügelzimmer', test))
       
       test = []
       for temp, hum in zip(list(result['t8']),list(result['rh_8'])):
           test.append([Taupunkt(temp, hum)])
       tdewlist.append(('Kinderzimmer', test))
       
       test = []
       for temp, hum in zip(list(result['t9']),list(result['rh_9'])):
           test.append([Taupunkt(temp, hum)])
       tdewlist.append(('Elternzimmer', test))
       
       room = ('', [])
       max_val = 0
       
       for i,v in tdewlist:
           if max(max(v)) > max_val:
               max_val = max(max(v))
               room = (i,self.flat_list(v))
                    
       data = []
       div = copy.deepcopy(optimazation_dict['schimmel'])
       tag = div.children
       graphtag = self.ref_finder(tag)                   
       data.append({'x' : list(result['datum']), 'y' : list(result['t1']), 'type' : 'line', 'name' : 'Temperatur [°C]', 'marker' : { 'color' : '#33C1B1'}, 'textposition' : 'bottom center'})
       data.append({'x' : list(result['datum']), 'y' : list(result['rh_1']), 'type' : 'line', 'name' : 'Luftfeuchte [%]', 'marker' : { 'color' : '#000000'},'textposition' : 'bottom center'})
       data.append({'x' : list(result['datum']), 'y' : room[1], 'type' : 'line', 'name' : 'Taupunkt [°C]: ' + room[0], 'marker' : { 'color' : '#093D40'},'textposition' : 'bottom center'})
       #data.append({'x' : list(result['datum']), 'y' : list(result['t_out']), 'type' : 'line', 'name' : 'Temperatur Draußen [°C]', 'marker' : { 'color' : '#9B9C9F'},'textposition' : 'bottom center'})
       #data.append({'x' : list(result['datum']), 'y' : list(test), 'type' : 'line', 'name' : 'gemittelter Oberflächentemepraturwert [°C]', 'marker' : { 'color' : '#33C1B1'},'textposition' : 'bottom center'})
       
       fig = { 'data' : data, 'layout' : {'title' : 'Schimmel-Case', 'yaxis' : {'title' : 'Temperatur [°C]'}}}
       graph = dcc.Graph(figure = fig, config = {'responsible' : True})
       graphtag.children = graph
       graphtag.className = 'card-graph-optimization'

       return div
    
    #Sichtbarkeits-Case: Wie weit kann man aktuell gucken, bei Grenzwertüberschreitung wird dieses Event getriggert
    def visibility_case(self):
        result = self.result[['datum','visibility']]
        threshold = self.threshold['visibility'][0]
        
        filt_result = result[result['visibility'] > threshold]
        
        if len(filt_result) > 45:
            
            data = []
            
            div = copy.deepcopy(optimazation_dict['visibility'])
            tag = div.children
            graphtag = self.ref_finder(tag) 
            
            data.append({'x' : list(self.result['datum']), 'y' : list(self.result['visibility']), 'type' : 'line', 'name' : 'Sichtbarkeit [km]', 'marker' : { 'color' : '#33C1B1'},'textposition' : 'bottom center'})
            data.append({'x' : list(filt_result['datum']), 'y' : list(filt_result['visibility']), 'type' : 'bar', 'name' : 'Gute Sichtbarkeit [km]', 'marker' : { 'color' : '#000000' }, 'textposition' : 'bottom center'})

            fig = { 'data' : data, 'layout' : {'title' : 'Schöner Tag heute!', 'yaxis' : {'title' : 'Weite [km]'}}}
            
            graph = dcc.Graph(figure = fig, config = {'responsible' : True})
            graphtag.children = graph
            graphtag.className = 'card-graph-optimization'
            
            return div
        else:
            return False
    
    #Windspeed-Case: Wie stark ist der Wind
    def windspeed_case(self):
        result = self.result[['datum','windspeed']]
        threshold = self.threshold['windspeed'][0]
        
        date = pd.Timestamp.to_pydatetime(result['datum'][0])
        
        cond1 = pd.Timestamp(year = date.year, month = date.month, day = date.day, hour = 7, minute = 0 )
        cond2 = pd.Timestamp(year = date.year, month = date.month, day = date.day, hour = 22, minute = 0 )
        
        filt_result = result[result['windspeed'] > threshold]
                
        time_filt = filt_result[(filt_result.datum >= cond1) & (filt_result.datum <= cond2)]
        
        energy_sum = 0
        for ws in result['windspeed']:
            energy_sum += energyfromwind(ws)
        
        
        energy_sum *= 0.001 * 1/144
        
        if len(time_filt) > 35:
            
            data = []
            
            div = copy.deepcopy(optimazation_dict['windspeed'])
            tag = div.children
            graphtag = self.ref_finder(tag) 
            
            data.append({'x' : list(self.result['datum']), 'y' : list(self.result['windspeed']), 'type' : 'line', 'name' : 'Windgeschwindigkeit [m/s]', 'textposition' : 'bottom center' ,'marker' : { 'color' : '#33C1B1'}})
            data.append({'x' : list(time_filt['datum']), 'y' : list(time_filt['windspeed']), 'type' : 'bar', 'name' : 'Starke Windgeschwindigkeiten [m/s]', 'textposition' : 'bottom center' ,'marker' : { 'color' : '#000000' }})

            fig = { 'data' : data, 'x' : 'Test', 'layout' : {'title' : 'Wäsche aufhängen oder Windrad lohnt sich! ' + str("{:.3f}".format(energy_sum)) + ' kW würden heute erzeugt ' , 'yaxis' : {'title' : 'Geschwindigkeit [m/s]'}}}
            
            graph = dcc.Graph(figure = fig, config = {'responsible' : True})
            graphtag.children = graph
            graphtag.className = 'card-graph-optimization'
            
            return div
        else:
            return False
    
    #Appliances-Case: Wurde am Tag unnötig Strom verbraucht?
    def appliances_case(self):
        result = self.result[['datum','appliances']]
        threshold = self.threshold['appliances'][0]
        
        date = pd.Timestamp.to_pydatetime(result['datum'][0])
        
        cond1 = pd.Timestamp(year = date.year, month = date.month, day = date.day, hour = 0, minute = 0 )
        cond2 = pd.Timestamp(year = date.year, month = date.month, day = date.day, hour = 7, minute = 0 )
        cond3 = pd.Timestamp(year = date.year, month = date.month, day = date.day, hour = 21, minute = 30 )
        cond4 = pd.Timestamp(year = date.year, month = date.month, day = date.day, hour = 23, minute = 50 )
        
        filt_result = result[result['appliances'] > threshold]
                
        time_filt = filt_result[(filt_result.datum >= cond1) & (filt_result.datum <= cond2) | (filt_result.datum >= cond3) & (filt_result.datum <= cond4) ] 
        
        if len(time_filt) >= 6:
            
            data = []
            
            div = copy.deepcopy(optimazation_dict['appliances'])
            tag = div.children
            graphtag = self.ref_finder(tag) 
            
            data.append({'x' : list(self.result['datum']), 'y' : list(self.result['appliances']), 'type' : 'line', 'name' : 'Stromverbrauch durch Geräte [W/h]', 'marker' : { 'color' : '#33C1B1'}, 'textposition' : 'bottom center'})
            data.append({'x' : list(time_filt['datum']), 'y' : list(time_filt['appliances']), 'type' : 'bar', 'name' : 'Unnötiger Stromverbrauch [W/h]', 'marker' : { 'color' : '#000000' }, 'textposition' : 'bottom center'})

            fig = { 'data' : data, 'layout' : {'title' : 'Lief der Fernseher in der Nacht?', 'yaxis' : {'title' : 'Leistung [W/h]'}}}
            
            graph = dcc.Graph(figure = fig, config = {'responsible' : True})
            graphtag.children = graph
            graphtag.className = 'card-graph-optimization'
            
            return div
        else:
            return False
        
    #Light-Case: War am dem Tag eventuell das Licht unnötig an?
    def lights_case(self):
        result = self.result[['datum','lights']]
        threshold = self.threshold['lights'][0]
        
        date = pd.Timestamp.to_pydatetime(result['datum'][0])
        
        cond1 = pd.Timestamp(year = date.year, month = date.month, day = date.day, hour = 0, minute = 0 )
        cond2 = pd.Timestamp(year = date.year, month = date.month, day = date.day, hour = 7, minute = 0 )
        cond3 = pd.Timestamp(year = date.year, month = date.month, day = date.day, hour = 10, minute = 0 )
        cond4 = pd.Timestamp(year = date.year, month = date.month, day = date.day, hour = 17, minute = 00 )
        
        filt_result = result[result['lights'] > threshold]
                
        time_filt = filt_result[(filt_result.datum >= cond1) & (filt_result.datum <= cond2) | (filt_result.datum >= cond3) & (filt_result.datum <= cond4) ]
        
        if len(time_filt) >= 6:
            
            data = []
            
            div = copy.deepcopy(optimazation_dict['lights'])
            tag = div.children
            graphtag = self.ref_finder(tag) 
            
            data.append({'x' : list(self.result['datum']), 'y' : list(self.result['lights']), 'type' : 'line', 'name' : 'Stromverbrauch durch Licht [W/h]', 'marker' : { 'color' : '#33C1B1'}, 'textposition' : 'bottom center'})
            data.append({'x' : list(time_filt['datum']), 'y' : list(time_filt['lights']), 'type' : 'bar', 'name' : 'Unnötiger Stromverbrauch [W/h]', 'marker' : { 'color' : '#000000' }, 'textposition' : 'bottom center'})

            fig = { 'data' : data, 'layout' : {'title' : 'Licht vielleicht angelassen?','yaxis' : {'title' : 'Leistung [W/h]'}}}
            
            graph = dcc.Graph(figure = fig, config = {'responsible' : True})
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
                                                                                           html.Div(className='col-4 head-date',
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
                                                                                                    children = html.A(children = html.Img(src='assets/logo.png', height=70, width='auto'), href='start'))
                                                                                       ]
                                                                               )
                                                          )
                                     ),
                            html.Main(children=
                                                  html.Div(className='container-fluid main', id = 'main',
                                                           children=
                                                                       html.Div(className='row',
                                                                                children=[
                                                                                            html.Div(className='col-1'
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