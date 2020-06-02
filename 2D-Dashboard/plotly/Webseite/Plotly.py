# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:41:53 2020

@author: Mues
"""


import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from Dashboard import Dashboard
from Optimization import Optimization
from Bad import Bad
from Buegel import Buegel
from Kinder import Kinder
from Kueche import Kueche
from Schlaf import Schlaf
from Wasch import Wasch
from Arbeit import Arbeit
from Wohn import Wohn
import psycopg2
from postgre import postgre_connector
from datetime import datetime as dt
from Uhrzeit_datum import Uhrzeit_datum





external_scripts = [
    'https://code.jquery.com/jquery-3.2.1.slim.min.js',
    'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js',
    'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js'
]

external_stylesheets = [
        dbc.themes.BOOTSTRAP,
        'https://cdn.materialdesignicons.com/5.1.45/css/materialdesignicons.min.css'
]

def erzeuge_uhrzeiten():
    DB_connector = postgre_connector()
    uhrzeiten_liste = []
    time_intervall = int(DB_connector.get_time_intervall())
    
    for i in range(0,24):
        minutenzaehler = time_intervall * -1
        for j in range(0, int(60/time_intervall)):
            minutenzaehler += time_intervall
            uhrzeiten_liste.append(dt(year = 9999, month = 1, day = 1, hour=i, minute=minutenzaehler))
    
    return uhrzeiten_liste      



uhrzeiten = erzeuge_uhrzeiten()

uhrzeit_datum = Uhrzeit_datum()


app = dash.Dash(external_stylesheets=external_stylesheets, external_scripts=external_scripts)
app.title = 'Dashboard'

app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        <!--<div>My Custom header</div>-->
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
       <!-- <div>My Custom footer</div>-->
    </body>
</html>
'''

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

dashboard = Dashboard()
optimization = Optimization()
bad = Bad()
buegel = Buegel()
kinder = Kinder()
kueche = Kueche()
schlaf = Schlaf()
wasch = Wasch()
arbeit = Arbeit()
wohn = Wohn()


#erzeugt die Unterseiten
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname'),
                # dash.dependencies.Input('my-date-picker-single', 'date'),
                # dash.dependencies.Input('dropdown-uhrzeit', 'value')
               ])


def display_page(pathname):
    
    # if(date == None or value == None):
    #     datum_liste = dashboard_datum_gesplittet(date)
    #     uhrzeit = dashboard_uhrzeit_gesplittet(value)
    
    if pathname == '/dashboard.html':
        return dashboard.dashboard_seite(uhrzeiten)
    elif pathname== '/optimization.html':
        return optimization.optimization_seite()
    elif pathname== '/bad.html':
        return bad.bad_seite(uhrzeiten, uhrzeit_datum.datum, uhrzeit_datum.uhrzeit)
    elif pathname== '/buegel.html':
        return buegel.buegel_seite(uhrzeiten, uhrzeit_datum.datum, uhrzeit_datum.uhrzeit)
    elif pathname== '/kinder.html':
        return kinder.kinder_seite(uhrzeiten, uhrzeit_datum.datum, uhrzeit_datum.uhrzeit)
    elif pathname== '/kueche.html':
        return kueche.kueche_seite(uhrzeiten, uhrzeit_datum.datum, uhrzeit_datum.uhrzeit)
    elif pathname== '/schlaf.html':
        return schlaf.schlaf_seite(uhrzeiten, uhrzeit_datum.datum, uhrzeit_datum.uhrzeit)
    elif pathname== '/wasch.html':
        return wasch.wasch_seite(uhrzeiten, uhrzeit_datum.datum, uhrzeit_datum.uhrzeit)
    elif pathname== '/arbeit.html':
        return arbeit.arbeit_seite(uhrzeiten,  uhrzeit_datum.datum, uhrzeit_datum.uhrzeit)
    elif pathname== '/wohn.html':
        return wohn.wohn_seite(uhrzeiten, uhrzeit_datum.datum, uhrzeit_datum.uhrzeit)
    else:
        return Dashboard().dashboard_seite(uhrzeiten)
    
@app.callback(
    dash.dependencies.Output('variablen_abspeichern','children'),
   [dash.dependencies.Input('my-date-picker-single', 'date'),
    dash.dependencies.Input('dropdown-uhrzeit', 'value')])

def dashboard_uhrzeit_tage_abspeichern(date, value):
            if(date != None and value != None):
                uhrzeit_datum.uhrzeit = dashboard_uhrzeit_gesplittet(value)
                uhrzeit_datum.datum = dashboard_datum_gesplittet(date)
                #dashboard_datum_liste = dashboard_datum_gesplittet(date)
                #dashboard_uhrzeit = dashboard_uhrzeit_gesplittet(value)
                #print(dashboard_datum_liste)
                #print(dashboard_uhrzeit)
            
    
@app.callback(
    dash.dependencies.Output('zimmer1', 'children'),
   [dash.dependencies.Input('my-date-picker-single', 'date'),
    dash.dependencies.Input('dropdown-uhrzeit', 'value')])

def kugel_zimmer1(date, value):
            if date == None or value == None:
                return None
            else:
                 #DB_connector = postgre_connector()
                 #day1 = [2016,4,12]
                 #day2 = [2016,4,13]
                 #result = DB_connector.get_data(day1, day2, 'a', ['t1, t2, rh_1'])
                 #print(result)
                
                #print(date)
                #print(value)
                # date_gesplittet = date.split('-',3)
                # jahr = date_gesplittet[0]
                # monat = date_gesplittet[1]                
                # date_gesplittet_gesplittet = date_gesplittet[2].split(' ', 2)
                # tag = date_gesplittet_gesplittet[0]
                # jahr_zahl = int(jahr)
                # monat_zahl = int(monat)
                # tag_zahl = int(tag)
                
                # value_gesplittet = value.split('T', 2)
                # print(value_gesplittet[1])
               # print(type(date))
                datum_liste = dashboard_datum_gesplittet(date)
                uhrzeit = dashboard_uhrzeit_gesplittet(value)
                
                return dashboard_erstellung_zimmer_kugeln(datum_liste, uhrzeit, 't1', 'rh_1')
                
            #     print(datum_liste)
            #     print(uhrzeit)
                
            #     DB_connector = postgre_connector()
            #     day1 = [datum_liste[0],datum_liste[1],datum_liste[2]]
            #     day2 = [datum_liste[0],datum_liste[1],datum_liste[2]]
            #     result = DB_connector.get_data(day1, day2, 'a', ['t1', 'rh_1'])
            #     result_gefiltert = result.loc[result['date'] == datum_liste[3] + '-' + datum_liste[4] + '-' + datum_liste[5] + ' ' + uhrzeit]
            #     print(result)
            #     print(result_gefiltert['date'])
            #     # print(list(result.columns.values))
            #      #for i in result:
            #       #   print(result["date"].)
            #      #print(x)
            #     print(type(result['t1']))
            #     return html.Div(className='colorcircle',
            #                     children=[
            #                                 html.Div(className='filled',
            #                                          id='bad-fill'),
            #                                 html.P(children=result_gefiltert['t1']),
            #                                 html.P(children=result_gefiltert['rh_1'])
            #                             ]
            #                     )
            
            
            # #html.Div(children=[
            #                                 #html.Div(children=date.strftime('%d.%m.%y')),
            #             #                    html.Div(children=value)
            #              #                 ])


@app.callback(
    dash.dependencies.Output('zimmer2', 'children'),
   [dash.dependencies.Input('my-date-picker-single', 'date'),
    dash.dependencies.Input('dropdown-uhrzeit', 'value')])

def dashboard_kugel_zimmer2(date, value):
            if date == None or value == None:
                return None
            else:
                
                datum_liste = dashboard_datum_gesplittet(date)
                uhrzeit = dashboard_uhrzeit_gesplittet(value)
                
                return dashboard_erstellung_zimmer_kugeln(datum_liste, uhrzeit, 't2', 'rh_2')
            
@app.callback(
    dash.dependencies.Output('zimmer3', 'children'),
   [dash.dependencies.Input('my-date-picker-single', 'date'),
    dash.dependencies.Input('dropdown-uhrzeit', 'value')])

def dashboard_kugel_zimmer3(date, value):
            if date == None or value == None:
                return None
            else:
                
                datum_liste = dashboard_datum_gesplittet(date)
                uhrzeit = dashboard_uhrzeit_gesplittet(value)
                
                return dashboard_erstellung_zimmer_kugeln(datum_liste, uhrzeit, 't3', 'rh_3')

@app.callback(
    dash.dependencies.Output('zimmer4', 'children'),
   [dash.dependencies.Input('my-date-picker-single', 'date'),
    dash.dependencies.Input('dropdown-uhrzeit', 'value')])

def dashboard_kugel_zimmer4(date, value):
            if date == None or value == None:
                return None
            else:
                
                datum_liste = dashboard_datum_gesplittet(date)
                uhrzeit = dashboard_uhrzeit_gesplittet(value)
                
                return dashboard_erstellung_zimmer_kugeln(datum_liste, uhrzeit, 't4', 'rh_4')

@app.callback(
    dash.dependencies.Output('zimmer5', 'children'),
   [dash.dependencies.Input('my-date-picker-single', 'date'),
    dash.dependencies.Input('dropdown-uhrzeit', 'value')])

def dashboard_kugel_zimmer5(date, value):
            if date == None or value == None:
                return None
            else:
                
                datum_liste = dashboard_datum_gesplittet(date)
                uhrzeit = dashboard_uhrzeit_gesplittet(value)
                
                return dashboard_erstellung_zimmer_kugeln(datum_liste, uhrzeit, 't5', 'rh_5')

@app.callback(
    dash.dependencies.Output('zimmer6', 'children'),
   [dash.dependencies.Input('my-date-picker-single', 'date'),
    dash.dependencies.Input('dropdown-uhrzeit', 'value')])

def dashboard_kugel_zimmer6(date, value):
            if date == None or value == None:
                return None
            else:
                
                datum_liste = dashboard_datum_gesplittet(date)
                uhrzeit = dashboard_uhrzeit_gesplittet(value)
                
                return dashboard_erstellung_zimmer_kugeln(datum_liste, uhrzeit, 't6', 'rh_6')

@app.callback(
    dash.dependencies.Output('zimmer7', 'children'),
   [dash.dependencies.Input('my-date-picker-single', 'date'),
    dash.dependencies.Input('dropdown-uhrzeit', 'value')])

def dashboard_kugel_zimmer7(date, value):
            if date == None or value == None:
                return None
            else:
                
                datum_liste = dashboard_datum_gesplittet(date)
                uhrzeit = dashboard_uhrzeit_gesplittet(value)
                
                return dashboard_erstellung_zimmer_kugeln(datum_liste, uhrzeit, 't7', 'rh_7')

@app.callback(
    dash.dependencies.Output('zimmer8', 'children'),
   [dash.dependencies.Input('my-date-picker-single', 'date'),
    dash.dependencies.Input('dropdown-uhrzeit', 'value')])

def dashboard_kugel_zimmer8(date, value):
            if date == None or value == None:
                return None
            else:
                
                datum_liste = dashboard_datum_gesplittet(date)
                uhrzeit = dashboard_uhrzeit_gesplittet(value)
                
                return dashboard_erstellung_zimmer_kugeln(datum_liste, uhrzeit, 't8', 'rh_8')

@app.callback(
    dash.dependencies.Output('zimmer9', 'children'),
   [dash.dependencies.Input('my-date-picker-single', 'date'),
    dash.dependencies.Input('dropdown-uhrzeit', 'value')])

def dashboard_kugel_zimmer9(date, value):
            if date == None or value == None:
                return None
            else:
                
                datum_liste = dashboard_datum_gesplittet(date)
                uhrzeit = dashboard_uhrzeit_gesplittet(value)
                
                return dashboard_erstellung_zimmer_kugeln(datum_liste, uhrzeit, 't9', 'rh_9')

def dashboard_datum_gesplittet(date):
    date_gesplittet = date.split('-',3)
    jahr = date_gesplittet[0]
    monat = date_gesplittet[1]                
    date_gesplittet_gesplittet = date_gesplittet[2].split(' ', 2)
    tag = date_gesplittet_gesplittet[0]
    # jahr_zahl = int(jahr)
    # monat_zahl = int(monat)
    # tag_zahl = int(tag)
    
    liste = []
    liste.append(jahr)
    liste.append(monat)
    liste.append(tag)

    return liste
                
def dashboard_uhrzeit_gesplittet(uhrzeit):
     uhrzeit_gesplittet = uhrzeit.split('T', 2)
     uhrzeit_gesplittet_gesplittet = uhrzeit_gesplittet[1].split(':',3)
     #print(uhrzeit_gesplittet_gesplittet)
     return uhrzeit_gesplittet_gesplittet
 
def dashboard_erstellung_zimmer_kugeln(datum_liste, uhrzeit, temp_zimmer, luftfeucht_zimmer):
    DB_connector = postgre_connector()
    # day1 = [datum_liste[0],datum_liste[1],datum_liste[2]]
    # day2 = [datum_liste[0],datum_liste[1],datum_liste[2]]
    # result = DB_connector.get_data(day1, day2, 'a', [temp_zimmer, luftfeucht_zimmer])
    # result_gefiltert = result.loc[result['date'] == datum_liste[3] + '-' + datum_liste[4] + '-' + datum_liste[5] + ' ' + uhrzeit]

    day1 = [int(datum_liste[0]),int(datum_liste[1]),int(datum_liste[2]),int(uhrzeit[0]),int(uhrzeit[1])]
    day2 = [int(datum_liste[0]),int(datum_liste[1]),int(datum_liste[2]),int(uhrzeit[0]),int(uhrzeit[1])]
    result = DB_connector.get_data(day1, day2, 'a', [temp_zimmer, luftfeucht_zimmer])
    #print(result)
    temp_zimmer_gesplittet = result[temp_zimmer].get(0).astype(str).split('.',2)
    luftfeucht_zimmer_gesplittet = result[luftfeucht_zimmer].get(0).astype(str).split('.',2)
    #print((result[temp_zimmer].get(0).astype(str).split('.',2)))
    #print(type(result[luftfeucht_zimmer].get(0).astype(str)))

    return html.Div(className='colorcircle',
                    children=[
                                html.Div(className='filled',
                                          id='bad-fill'),
                                html.P(children=temp_zimmer_gesplittet[0] + '°C'),
                                html.P(children=luftfeucht_zimmer_gesplittet[0] + '%')
                            ]
                    )

@app.callback(
    dash.dependencies.Output('luftfeuchte_wind_draussen', 'children'),
   [dash.dependencies.Input('my-date-picker-single', 'date'),
    dash.dependencies.Input('dropdown-uhrzeit', 'value')])

def dashboard_luftfeuchte_wind_draussen(date, value):
            if date == None or value == None:
                return None
            else:
                DB_connector = postgre_connector()
                datum_liste = dashboard_datum_gesplittet(date)
                uhrzeit = dashboard_uhrzeit_gesplittet(value)
                
                day1 = [int(datum_liste[0]),int(datum_liste[1]),int(datum_liste[2]),int(uhrzeit[0]),int(uhrzeit[1])]
                day2 = [int(datum_liste[0]),int(datum_liste[1]),int(datum_liste[2]),int(uhrzeit[0]),int(uhrzeit[1])]
                result = DB_connector.get_data(day1, day2, 'a', ['windspeed', 'rh_out'])
                #print(result)
                #print(type(result['windspeed']))
                
                windspeed_gesplittet = result['windspeed'].get(0).astype(str).split('.',2)
                rh_out_gesplittet = result['rh_out'].get(0).astype(str).split('.',2)
                
    
                return html.Div(className='col-12 text-center luft-wind',
                                children=[
                                           
                                            html.Div(children='Luftfeuchte: ' + rh_out_gesplittet[0] + '%' #result['rh_out'].astype(str)
                                                                        #<!-- Datensatz: Luftfeuchte draußen 'Luftfeuchte: '-->
                                                    ),
                                                     
                                                     
                                            html.Div('Wind: ' + windspeed_gesplittet[0] + ' m/s' #result['windspeed'].astype(str)
                                                     #<!-- Datensatz: Wind draußen 'Wind: 10 km/h'-->
                                                     )
                                            ]
                                )

@app.callback(
    dash.dependencies.Output('temp_draussen', 'children'),
   [dash.dependencies.Input('my-date-picker-single', 'date'),
    dash.dependencies.Input('dropdown-uhrzeit', 'value')])

def dashboard_temp_draussen(date, value):
            if date == None or value == None:
                return None
            else:
                DB_connector = postgre_connector()
                datum_liste = dashboard_datum_gesplittet(date)
                uhrzeit = dashboard_uhrzeit_gesplittet(value)
                
                day1 = [int(datum_liste[0]),int(datum_liste[1]),int(datum_liste[2]),int(uhrzeit[0]),int(uhrzeit[1])]
                day2 = [int(datum_liste[0]),int(datum_liste[1]),int(datum_liste[2]),int(uhrzeit[0]),int(uhrzeit[1])]
                result = DB_connector.get_data(day1, day2, 'a', ['t_out'])
                #print(result)
                #print(type(result['windspeed']))
                
                temp_draussen_gesplittet = result['t_out'].get(0).astype(str).split('.',2)
                
    
                
                return  html.Div(#className='col-4 text-right text-head',
                                 children=
                                             html.Div(children= temp_draussen_gesplittet[0] + '°C' #result['t_out'].astype(str) + '°C'
                                                      #<!-- Datensatz: Temperatur draußen -->
                                                      )
                                 ),          

@app.callback(
    dash.dependencies.Output('stromverbrauch_lichtverbrauch', 'children'),
   [dash.dependencies.Input('my-date-picker-single', 'date'),
    dash.dependencies.Input('dropdown-uhrzeit', 'value')])

def dashboard_stromverbrauch_lichtverbrauch(date, value):
            if date == None or value == None:
                return None
            else:
                DB_connector = postgre_connector()
                datum_liste = dashboard_datum_gesplittet(date)
                uhrzeit = dashboard_uhrzeit_gesplittet(value)
                
                day1 = [int(datum_liste[0]),int(datum_liste[1]),int(datum_liste[2]),int(uhrzeit[0]),int(uhrzeit[1])]
                day2 = [int(datum_liste[0]),int(datum_liste[1]),int(datum_liste[2]),int(uhrzeit[0]),int(uhrzeit[1])]
                result = DB_connector.get_data(day1, day2, 'a', ['appliances', 'lights'])
                #print(result)
                #print(type(result['windspeed']))
                
                appliances_gesplittet = result['appliances'].get(0).astype(str).split('.',2)
                licht_gesplittet = result['lights'].get(0).astype(str).split('.',2)
    
                
                return  html.Div(className='sidecard',
                                children=[
                                            html.Div(className='strom',
                                                     #<!-- Strom-Fläche -->
                                                     children=[
                                                                 html.Div(className='verbrauch-text',
                                                                          children='Stromverbrauch'
                                                                          ),
                                                                 html.Div(children=
                                                                                  html.I(className='mdi mdi-flash icons-verbrauch')
                                                                          ),
                                                                 html.Div(className='stromverbrauch verbrauch-zahl',
                                                                          children=appliances_gesplittet[0] + 'W' #result['appliances'].astype(str) + 'W'
                                                                          #<!-- Stromverbrauch eintragen -->
                                                                          )
                                                                ] 
                                                                 
                                                     ),
                                            html.Div(className='licht',
                                                     #<!-- Licht-Fläche -->
                                                     children=[
                                                                 html.Div(className='verbrauch-text',
                                                                          children='Lichtverbrauch'
                                                                          ),
                                                                 html.Div(children=
                                                                                      html.I(className='mdi mdi-lightbulb-on icons-verbrauch')
                                                                          ),
                                                                 html.Div(className='stromverbrauch verbrauch-zahl',
                                                                          children=licht_gesplittet[0] + 'W' #result['lights'].astype(str) + 'W'
                                                                          #<!-- Lichtverbrauch eintragen -->
                                                                          )
                                                                 ]
                                                     )
                                    ])
@app.callback(
    dash.dependencies.Output('Graph_Temperatur_Wohn', 'figure'),
   [dash.dependencies.Input('DatePickerWohn', 'date')])

def wohn_temperatur_tag(date):
            if date == None:
                return None
            else:
                return einzelzimmer_graph_tagesverlauf(date, 't2', 'Temperatur')
            
@app.callback(
    dash.dependencies.Output('Graph_Luftfeucht_Wohn', 'figure'),
   [dash.dependencies.Input('DatePickerWohn', 'date')])

def wohn_luftfeucht_tag(date):
            if date == None:
                return None
            else:
                return einzelzimmer_graph_tagesverlauf(date, 'rh_2', 'Luftfeuchtigkeit')            
            
@app.callback(
    dash.dependencies.Output('Graph_Temperatur_Wasch', 'figure'),
   [dash.dependencies.Input('DatePickerWasch', 'date')])

def wasch_temperatur_tag(date):
            if date == None:
                return None
            else:
                return einzelzimmer_graph_tagesverlauf(date, 't3', 'Temperatur')
            
@app.callback(
    dash.dependencies.Output('Graph_Luftfeucht_Wasch', 'figure'),
   [dash.dependencies.Input('DatePickerWasch', 'date')])

def wasch_luftfeucht_tag(date):
            if date == None:
                return None
            else:
                return einzelzimmer_graph_tagesverlauf(date, 'rh_3', 'Luftfeuchtigkeit')            
            
@app.callback(
    dash.dependencies.Output('Graph_Temperatur_Schlaf', 'figure'),
   [dash.dependencies.Input('DatePickerSchlaf', 'date')])

def schlaf_temperatur_tag(date):
            if date == None:
                return None
            else:
                return einzelzimmer_graph_tagesverlauf(date, 't9', 'Temperatur')
            
@app.callback(
    dash.dependencies.Output('Graph_Luftfeucht_Schlaf', 'figure'),
   [dash.dependencies.Input('DatePickerSchlaf', 'date')])

def schlaf_luftfeucht_tag(date):
            if date == None:
                return None
            else:
                return einzelzimmer_graph_tagesverlauf(date, 'rh_9', 'Luftfeuchtigkeit')            
            
@app.callback(
    dash.dependencies.Output('Graph_Temperatur_Kueche', 'figure'),
   [dash.dependencies.Input('DatePickerKueche', 'date')])

def kueche_temperatur_tag(date):
            if date == None:
                return None
            else:
                return einzelzimmer_graph_tagesverlauf(date, 't1', 'Temperatur')
            
@app.callback(
    dash.dependencies.Output('Graph_Luftfeucht_Kueche', 'figure'),
   [dash.dependencies.Input('DatePickerKueche', 'date')])

def kueche_luftfeucht_tag(date):
            if date == None:
                return None
            else:
                return einzelzimmer_graph_tagesverlauf(date, 'rh_1', 'Luftfeuchtigkeit')            
            
@app.callback(
    dash.dependencies.Output('Graph_Temperatur_Kinder', 'figure'),
   [dash.dependencies.Input('DatePickerKinder', 'date')])

def kinder_temperatur_tag(date):
            if date == None:
                return None
            else:
                return einzelzimmer_graph_tagesverlauf(date, 't8', 'Temperatur')
            
@app.callback(
    dash.dependencies.Output('Graph_Luftfeucht_Kinder', 'figure'),
   [dash.dependencies.Input('DatePickerKinder', 'date')])

def kinder_luftfeucht_tag(date):
            if date == None:
                return None
            else:
                return einzelzimmer_graph_tagesverlauf(date, 'rh_8', 'Luftfeuchtigkeit')
            
@app.callback(
    dash.dependencies.Output('Graph_Temperatur_Buegel', 'figure'),
   [dash.dependencies.Input('DatePickerBuegel', 'date')])

def buegel_temperatur_tag(date):
            if date == None:
                return None
            else:
                return einzelzimmer_graph_tagesverlauf(date, 't7', 'Temperatur')
            
@app.callback(
    dash.dependencies.Output('Graph_Luftfeucht_Buegel', 'figure'),
   [dash.dependencies.Input('DatePickerBuegel', 'date')])

def buegel_luftfeucht_tag(date):
            if date == None:
                return None
            else:
                return einzelzimmer_graph_tagesverlauf(date, 'rh_7', 'Luftfeuchtigkeit')            

@app.callback(
    dash.dependencies.Output('Graph_Temperatur_Bad', 'figure'),
   [dash.dependencies.Input('DatePickerBad', 'date')])

def bad_temperatur_tag(date):
            if date == None:
                return None
            else:
                return einzelzimmer_graph_tagesverlauf(date, 't5', 'Temperatur')
            
@app.callback(
    dash.dependencies.Output('Graph_Luftfeucht_Bad', 'figure'),
   [dash.dependencies.Input('DatePickerBad', 'date')])

def bad_luftfeucht_tag(date):
            if date == None:
                return None
            else:
                return einzelzimmer_graph_tagesverlauf(date, 'rh_5', 'Luftfeuchtigkeit')
            

@app.callback(
    dash.dependencies.Output('Graph_Temperatur_Arbeitzimmer', 'figure'),
   [dash.dependencies.Input('DatePickerArbeit', 'date')])

def arbeitszimmer_temperatur_tag(date):
            if date == None:
                return None
            else:
                return einzelzimmer_graph_tagesverlauf(date, 't4', 'Temperatur')
            
@app.callback(
    dash.dependencies.Output('Graph_Luftfeucht_Arbeitzimmer', 'figure'),
   [dash.dependencies.Input('DatePickerArbeit', 'date')])

def arbeitszimmer_luftfeucht_tag(date):
            if date == None:
                return None
            else:
                return einzelzimmer_graph_tagesverlauf(date, 'rh_4', 'Luftfeuchtigkeit')            

def einzelzimmer_graph_tagesverlauf(date, datenbankspalte, ueberschrift):
            if date == None:
               # if uhrzeit_datum.datum == None:
                    return None
               # else:
                    #date = uhrzeit_datum.datum
                
            else:
                dashboard_datum_liste = dashboard_datum_gesplittet(date)
                
                DB_connector = postgre_connector()
                
            
                day1 = [int(dashboard_datum_liste[0]),int(dashboard_datum_liste[1]),int(dashboard_datum_liste[2]),00,00]
                day2 = [int(dashboard_datum_liste[0]),int(dashboard_datum_liste[1]),int(dashboard_datum_liste[2]),23,50]
                result = DB_connector.get_data(day1, day2, 'a', [datenbankspalte])
                
                return {
                        'data': [
                                    {'x': result['datum'], 'y': result[datenbankspalte], 'type': 'scatter', 'name': 'SF'},
                                ],
                        'layout': {
                                    'title': ueberschrift
                           }
                        }                                                   
                        
                                          
                                           
                          
                    
                    
if __name__ == '__main__':
    app.run_server(debug=False)