# -*- coding: utf-8 -*-
"""


@author: Mues
Diese Datei beinhaltet alle Plotly Callback-Funktionen und ihre Hilffunktionen. 
Außerdem werden hier die einzelen Objekte der Webseiten-Klassen erstellt und aufgerufen. 
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
from postgre import postgre_connector, pd
#from datetime import datetime as dt2
import datetime as dt
from Uhrzeit_datum import Uhrzeit_datum
from Analytics import analytics
from impressum import impressum
from start import start
import numpy  as np

#Sktipt-Einbindung für die Webseite(n)
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
    }
]

#CSS-Einbindung für die Webseite(n) Bootstrap
external_stylesheets = [
        dbc.themes.BOOTSTRAP,
        'https://cdn.materialdesignicons.com/5.1.45/css/materialdesignicons.min.css'
]

#Diese Funktion erstellt eine Liste, die alle Uhrzeiten des Datensatzes enthält.
#Diese Liste wird wird für die Uhrzeiten-Dropdown-Leiste der Dashboard-Webseite genutzt.
def erzeuge_uhrzeiten():
    DB_connector = postgre_connector()
    uhrzeiten_liste = []
    time_intervall = int(DB_connector.get_time_intervall())
    
    for i in range(0,24):
        minutenzaehler = time_intervall * -1
        for j in range(0, int(60/time_intervall)):
            minutenzaehler += time_intervall
            uhrzeiten_liste.append(dt.datetime(year = 9999, month = 1, day = 1, hour=i, minute=minutenzaehler))
    
    return uhrzeiten_liste      

#Dictionary-Abbildung der Räume auf die einzelnen Temperatur- und Luftfeuchtesensoren
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

uhrzeiten = erzeuge_uhrzeiten()

uhrzeit_datum = Uhrzeit_datum()

#Liste für die Auswahl der FH-Farben
color_dict = ['#33C1B1', '#000000', '#093D40', '#CECFD1', '#65666D', '#28988E', '#9B9C9F', '#192331', '#1A6C68' ]

def get_color(i):
    return color_dict[i]
    

app = dash.Dash(external_stylesheets=external_stylesheets, external_scripts=external_scripts)
app.title = 'Dashboard'

#Meta-Tags der Webseite
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

#Erstellung der Webseiten-Objekte
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
analytics = analytics()
start = start()
impressum = impressum()


#erzeugt die Unterseiten
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname'),
               ])
#Call-Back Methode zum Naviǵieren der einzelnen Seiten
def display_page(pathname):
    
    if pathname == '/dashboard':
        uhrzeit_datum.aktuelleUhrzeit()
        return dashboard.dashboard_seite(uhrzeiten, uhrzeit_datum.uhrzeit)
    elif pathname == '/analytics':
        return analytics.get_site()
    elif pathname == '/optimization':
         site = Optimization(dt.datetime(int(uhrzeit_datum.datum[0]), int(uhrzeit_datum.datum[1]) , int(uhrzeit_datum.datum[2])))
         site.case_check()
         return site.optimization_seite()
    elif pathname == '/bad':
        return bad.bad_seite(uhrzeiten, uhrzeit_datum.datum, uhrzeit_datum.uhrzeit)
    elif pathname == '/buegel':
        return buegel.buegel_seite(uhrzeiten, uhrzeit_datum.datum, uhrzeit_datum.uhrzeit)
    elif pathname == '/kinder':
        return kinder.kinder_seite(uhrzeiten, uhrzeit_datum.datum, uhrzeit_datum.uhrzeit)
    elif pathname == '/kueche':
        return kueche.kueche_seite(uhrzeiten, uhrzeit_datum.datum, uhrzeit_datum.uhrzeit)
    elif pathname == '/schlaf':
        return schlaf.schlaf_seite(uhrzeiten, uhrzeit_datum.datum, uhrzeit_datum.uhrzeit)
    elif pathname == '/wasch':
        return wasch.wasch_seite(uhrzeiten, uhrzeit_datum.datum, uhrzeit_datum.uhrzeit)
    elif pathname == '/arbeit':
        return arbeit.arbeit_seite(uhrzeiten,  uhrzeit_datum.datum, uhrzeit_datum.uhrzeit)
    elif pathname == '/wohn':
        return wohn.wohn_seite(uhrzeiten, uhrzeit_datum.datum, uhrzeit_datum.uhrzeit)
    elif pathname == '/impressum':
        return impressum.impressum_seite()
    elif pathname == '/start':
        return start.start_seite()
    else:        
        return start.start_seite() 
    
    
#Callback-Funktion, um die Uhrzeit, die auf der Dashboard-Webseite gewählt wurde abzuspeichern.
@app.callback(
    dash.dependencies.Output('variablen_abspeichern','children'),
   [dash.dependencies.Input('my-date-picker-single', 'date'),
    dash.dependencies.Input('dropdown-uhrzeit', 'value')])

def dashboard_uhrzeit_tage_abspeichern(date, value):
            if(date != None and value == None):
                uhrzeit_datum.datum = dashboard_datum_gesplittet(date)
            if(date != None and value != None):
                uhrzeit_datum.uhrzeit = dashboard_uhrzeit_gesplittet(value)
                uhrzeit_datum.datum = dashboard_datum_gesplittet(date)
            
    
#Callback-Funktion des Dashboards, die mit Hilfe der "dashboard_erstellung_zimmer_kugeln" Funktion die Temperatur/Luftfeuchtigkeitskugel
#des ersten Zimmers erstellt.
@app.callback(
    dash.dependencies.Output('zimmer1', 'children'),
   [dash.dependencies.Input('my-date-picker-single', 'date'),
    dash.dependencies.Input('dropdown-uhrzeit', 'value')])

def kugel_zimmer1(date, value):
            if date == None or value == None:
                datum_liste = uhrzeit_datum.datum
                uhrzeit = uhrzeit_datum.uhrzeit
            else:                
                datum_liste = dashboard_datum_gesplittet(date)
                uhrzeit = dashboard_uhrzeit_gesplittet(value)
                
            return dashboard_erstellung_zimmer_kugeln(datum_liste, uhrzeit, 't1', 'rh_1')
                
           

#Callback-Funktion des Dashboards, die mit Hilfe der "dashboard_erstellung_zimmer_kugeln" Funktion die Temperatur/Luftfeuchtigkeitskugel
#des zweiten Zimmers erstellt.
@app.callback(
    dash.dependencies.Output('zimmer2', 'children'),
   [dash.dependencies.Input('my-date-picker-single', 'date'),
    dash.dependencies.Input('dropdown-uhrzeit', 'value')])

def dashboard_kugel_zimmer2(date, value):
            if date == None or value == None:
                datum_liste = uhrzeit_datum.datum
                uhrzeit = uhrzeit_datum.uhrzeit
            else:            
                datum_liste = dashboard_datum_gesplittet(date)
                uhrzeit = dashboard_uhrzeit_gesplittet(value)
                
            return dashboard_erstellung_zimmer_kugeln(datum_liste, uhrzeit, 't2', 'rh_2')
            
#Callback-Funktion des Dashboards, die mit Hilfe der "dashboard_erstellung_zimmer_kugeln" Funktion die Temperatur/Luftfeuchtigkeitskugel
#des dritten Zimmers erstellt.        
@app.callback(
    dash.dependencies.Output('zimmer3', 'children'),
   [dash.dependencies.Input('my-date-picker-single', 'date'),
    dash.dependencies.Input('dropdown-uhrzeit', 'value')])

def dashboard_kugel_zimmer3(date, value):
            if date == None or value == None:
                datum_liste = uhrzeit_datum.datum
                uhrzeit = uhrzeit_datum.uhrzeit
            else:            
                datum_liste = dashboard_datum_gesplittet(date)
                uhrzeit = dashboard_uhrzeit_gesplittet(value)
                
            return dashboard_erstellung_zimmer_kugeln(datum_liste, uhrzeit, 't3', 'rh_3')

#Callback-Funktion des Dashboards, die mit Hilfe der "dashboard_erstellung_zimmer_kugeln" Funktion die Temperatur/Luftfeuchtigkeitskugel
#des vierten Zimmers erstellt.
@app.callback(
    dash.dependencies.Output('zimmer4', 'children'),
   [dash.dependencies.Input('my-date-picker-single', 'date'),
    dash.dependencies.Input('dropdown-uhrzeit', 'value')])

def dashboard_kugel_zimmer4(date, value):
            if date == None or value == None:
                datum_liste = uhrzeit_datum.datum
                uhrzeit = uhrzeit_datum.uhrzeit
            else:
            
                datum_liste = dashboard_datum_gesplittet(date)
                uhrzeit = dashboard_uhrzeit_gesplittet(value)
                
            return dashboard_erstellung_zimmer_kugeln(datum_liste, uhrzeit, 't4', 'rh_4')

#Callback-Funktion des Dashboards, die mit Hilfe der "dashboard_erstellung_zimmer_kugeln" Funktion die Temperatur/Luftfeuchtigkeitskugel
#des fünften Zimmers erstellt.
@app.callback(
    dash.dependencies.Output('zimmer5', 'children'),
   [dash.dependencies.Input('my-date-picker-single', 'date'),
    dash.dependencies.Input('dropdown-uhrzeit', 'value')])

def dashboard_kugel_zimmer5(date, value):
            if date == None or value == None:
                datum_liste = uhrzeit_datum.datum
                uhrzeit = uhrzeit_datum.uhrzeit
            else:            
                datum_liste = dashboard_datum_gesplittet(date)
                uhrzeit = dashboard_uhrzeit_gesplittet(value)
                
            return dashboard_erstellung_zimmer_kugeln(datum_liste, uhrzeit, 't5', 'rh_5')

#Callback-Funktion des Dashboards, die mit Hilfe der "dashboard_erstellung_zimmer_kugeln" Funktion die Temperatur/Luftfeuchtigkeitskugel
#des sechsten Zimmers erstellt.
@app.callback(
    dash.dependencies.Output('zimmer6', 'children'),
   [dash.dependencies.Input('my-date-picker-single', 'date'),
    dash.dependencies.Input('dropdown-uhrzeit', 'value')])

def dashboard_kugel_zimmer6(date, value):
            if date == None or value == None:
                datum_liste = uhrzeit_datum.datum
                uhrzeit = uhrzeit_datum.uhrzeit
            else:            
                datum_liste = dashboard_datum_gesplittet(date)
                uhrzeit = dashboard_uhrzeit_gesplittet(value)
                
            return dashboard_erstellung_zimmer_kugeln(datum_liste, uhrzeit, 't6', 'rh_6')

#Callback-Funktion des Dashboards, die mit Hilfe der "dashboard_erstellung_zimmer_kugeln" Funktion die Temperatur/Luftfeuchtigkeitskugel
#des siebten Zimmers erstellt.
@app.callback(
    dash.dependencies.Output('zimmer7', 'children'),
   [dash.dependencies.Input('my-date-picker-single', 'date'),
    dash.dependencies.Input('dropdown-uhrzeit', 'value')])

def dashboard_kugel_zimmer7(date, value):
            if date == None or value == None:
                datum_liste = uhrzeit_datum.datum
                uhrzeit = uhrzeit_datum.uhrzeit
            else:
            
                datum_liste = dashboard_datum_gesplittet(date)
                uhrzeit = dashboard_uhrzeit_gesplittet(value)
                
            return dashboard_erstellung_zimmer_kugeln(datum_liste, uhrzeit, 't7', 'rh_7')

#Callback-Funktion des Dashboards, die mit Hilfe der "dashboard_erstellung_zimmer_kugeln" Funktion die Temperatur/Luftfeuchtigkeitskugel
#des achten Zimmers erstellt.
@app.callback(
    dash.dependencies.Output('zimmer8', 'children'),
   [dash.dependencies.Input('my-date-picker-single', 'date'),
    dash.dependencies.Input('dropdown-uhrzeit', 'value')])

def dashboard_kugel_zimmer8(date, value):
            if date == None or value == None:
                datum_liste = uhrzeit_datum.datum
                uhrzeit = uhrzeit_datum.uhrzeit

            else:

                datum_liste = dashboard_datum_gesplittet(date)
                uhrzeit = dashboard_uhrzeit_gesplittet(value)
                
            return dashboard_erstellung_zimmer_kugeln(datum_liste, uhrzeit, 't8', 'rh_8')

#Callback-Funktion des Dashboards, die mit Hilfe der "dashboard_erstellung_zimmer_kugeln" Funktion die Temperatur/Luftfeuchtigkeitskugel
#des neunten Zimmers erstellt.
@app.callback(
    dash.dependencies.Output('zimmer9', 'children'),
   [dash.dependencies.Input('my-date-picker-single', 'date'),
    dash.dependencies.Input('dropdown-uhrzeit', 'value')])

def dashboard_kugel_zimmer9(date, value):
            if date == None or value == None:
                datum_liste = uhrzeit_datum.datum
                uhrzeit = uhrzeit_datum.uhrzeit
            else:            
                datum_liste = dashboard_datum_gesplittet(date)
                uhrzeit = dashboard_uhrzeit_gesplittet(value)
                
            return dashboard_erstellung_zimmer_kugeln(datum_liste, uhrzeit, 't9', 'rh_9')

#Funktion die den Datums-String, den der Date-Picker zurückgibt in Jahr, Monat und Tag splittet
def dashboard_datum_gesplittet(date):    
    date_gesplittet = date.split('-',3)
    jahr = date_gesplittet[0]
    monat = date_gesplittet[1]                
    date_gesplittet_gesplittet = date_gesplittet[2].split(' ', 2)
    tag = date_gesplittet_gesplittet[0]
    
    liste = []
    liste.append(jahr)
    liste.append(monat)
    liste.append(tag)

    return liste
                
#Funktion die den Uhrzeit-String, die die Uhrzeit-Dropdown-Leiste zurückgibt in Stunden und Minuten splittet
def dashboard_uhrzeit_gesplittet(uhrzeit):
     uhrzeit_gesplittet = uhrzeit.split('T', 2)
     uhrzeit_gesplittet_gesplittet = uhrzeit_gesplittet[1].split(':',3)
     return uhrzeit_gesplittet_gesplittet
 
#erstellt den Plotly-HTML-Code für die Kugeln der einzelnen Zimmer der Dashboard-Webseite.
def dashboard_erstellung_zimmer_kugeln(datum_liste, uhrzeit, temp_zimmer, luftfeucht_zimmer):
    DB_connector = postgre_connector()

    day1 = [int(datum_liste[0]),int(datum_liste[1]),int(datum_liste[2]),int(uhrzeit[0]),int(uhrzeit[1])]
    day2 = [int(datum_liste[0]),int(datum_liste[1]),int(datum_liste[2]),int(uhrzeit[0]),int(uhrzeit[1])]
    result = DB_connector.get_data(day1, day2, 'a', [temp_zimmer, luftfeucht_zimmer])
    temp_zimmer_gesplittet = result[temp_zimmer].get(0).astype(str).split('.',2)
    luftfeucht_zimmer_gesplittet = result[luftfeucht_zimmer].get(0).astype(str).split('.',2)

    return html.Div(className='colorcircle',
                    children=[
                                html.Div(className='filled',
                                          id='bad-fill'),
                                html.P(children=temp_zimmer_gesplittet[0] + '°C'),
                                html.P(children=luftfeucht_zimmer_gesplittet[0] + '%')
                            ]
                    )

#Callback Funktion der Dasboard-Webseite, die den Plotly-HTML-Code erzeugt, um die Luftfeuchte und die Windgeschwindigkeit
#außerhalb des Hauses dynamisch je nach gewähltem Tageszeitpunkt anzuzeigen.
@app.callback(
    dash.dependencies.Output('luftfeuchte_wind_draussen', 'children'),
   [dash.dependencies.Input('my-date-picker-single', 'date'),
    dash.dependencies.Input('dropdown-uhrzeit', 'value')])

def dashboard_luftfeuchte_wind_draussen(date, value):
            if date == None or value == None:
                datum_liste = uhrzeit_datum.datum
                uhrzeit = uhrzeit_datum.uhrzeit
            else:                
                datum_liste = dashboard_datum_gesplittet(date)
                uhrzeit = dashboard_uhrzeit_gesplittet(value)

            DB_connector = postgre_connector()                
            day1 = [int(datum_liste[0]),int(datum_liste[1]),int(datum_liste[2]),int(uhrzeit[0]),int(uhrzeit[1])]
            day2 = [int(datum_liste[0]),int(datum_liste[1]),int(datum_liste[2]),int(uhrzeit[0]),int(uhrzeit[1])]
            result = DB_connector.get_data(day1, day2, 'a', ['windspeed', 'rh_out'])
            
            windspeed_gesplittet = result['windspeed'].get(0).astype(str).split('.',2)
            rh_out_gesplittet = result['rh_out'].get(0).astype(str).split('.',2)
            

            return html.Div(className='luft-wind',
                            children=[
                                        html.Div(children='Luftfeuchte: ' + rh_out_gesplittet[0] + '%' 
                                                              
                                                ),
                                                 
                                                 
                                        html.Div(children='Wind: ' + windspeed_gesplittet[0] + ' m/s' 
                                                 
                                                 )
                                        ]
                            )
#Callback Funktion der Dasboard-Webseite, die den Plotly-HTML-Code erzeugt, um die Temperatur außerhalb des Hauses
#dynamisch je nach gewähltem Tageszeitpunkt anzuzeigen.
@app.callback(
    dash.dependencies.Output('temp_draussen', 'children'),
   [dash.dependencies.Input('my-date-picker-single', 'date'),
    dash.dependencies.Input('dropdown-uhrzeit', 'value')])

def dashboard_temp_draussen(date, value):
            if date == None or value == None:
                datum_liste = uhrzeit_datum.datum
                uhrzeit = uhrzeit_datum.uhrzeit
            else:                
                datum_liste = dashboard_datum_gesplittet(date)
                uhrzeit = dashboard_uhrzeit_gesplittet(value)

            DB_connector = postgre_connector()                
            day1 = [int(datum_liste[0]),int(datum_liste[1]),int(datum_liste[2]),int(uhrzeit[0]),int(uhrzeit[1])]
            day2 = [int(datum_liste[0]),int(datum_liste[1]),int(datum_liste[2]),int(uhrzeit[0]),int(uhrzeit[1])]
            result = DB_connector.get_data(day1, day2, 'a', ['t_out'])                
            
            temp_draussen_gesplittet = result['t_out'].get(0).astype(str).split('.',2)
            

            
            return  html.Div(
                             children=
                                         html.Div(children= temp_draussen_gesplittet[0] + '°C'                                                   
                                                  )
                             ),          

#Callback Funktion der Dasboard-Webseite, die den Plotly-HTML-Code erzeugt, um den Stromverbrauch und Lichtverbrauch
#dynamisch je nach gewähltem Tageszeitpunkt anzuzeigen.
@app.callback(
    dash.dependencies.Output('stromverbrauch_lichtverbrauch', 'children'),
   [dash.dependencies.Input('my-date-picker-single', 'date'),
    dash.dependencies.Input('dropdown-uhrzeit', 'value')])

def dashboard_stromverbrauch_lichtverbrauch(date, value):
            if date == None or value == None:
                datum_liste = uhrzeit_datum.datum
                uhrzeit = uhrzeit_datum.uhrzeit
            else:                
                datum_liste = dashboard_datum_gesplittet(date)
                uhrzeit = dashboard_uhrzeit_gesplittet(value)

            DB_connector = postgre_connector()                
            day1 = [int(datum_liste[0]),int(datum_liste[1]),int(datum_liste[2]),int(uhrzeit[0]),int(uhrzeit[1])]
            day2 = [int(datum_liste[0]),int(datum_liste[1]),int(datum_liste[2]),int(uhrzeit[0]),int(uhrzeit[1])]
            result = DB_connector.get_data(day1, day2, 'a', ['appliances', 'lights'])
            
            appliances_gesplittet = result['appliances'].get(0).astype(str).split('.',2)
            licht_gesplittet = result['lights'].get(0).astype(str).split('.',2)
        
            
            return  html.Div(className='sidecard',
                            children=[
                                        html.Div(className='strom',
                                                 children=[
                                                             html.Div(className='verbrauch-text',
                                                                      children='Stromverbrauch'
                                                                      ),
                                                             html.Div(children=
                                                                              html.I(className='mdi mdi-48px mdi-flash icons-verbrauch')
                                                                      ),
                                                             html.Div(className='stromverbrauch verbrauch-zahl',
                                                                      children=appliances_gesplittet[0] + 'W'                                                                       
                                                                      )
                                                            ] 
                                                             
                                                 ),
                                        html.Div(className='licht',
                                                 children=[
                                                             html.Div(className='verbrauch-text',
                                                                      children='Lichtverbrauch'
                                                                      ),
                                                             html.Div(children=
                                                                                  html.I(className='mdi mdi-48px mdi-lightbulb-on icons-verbrauch')
                                                                      ),
                                                             html.Div(className='stromverbrauch verbrauch-zahl',
                                                                      children=licht_gesplittet[0] + 'W'                                                                       
                                                                      )
                                                             ]
                                                 )
                                ])
#Callback-Funktion der Wohnzimmer-Seite, um den Temperatur-Graph dynamisch je nach gewähltem Datum anzuzeigen.
@app.callback(
    dash.dependencies.Output('Graph_Temperatur_Wohn', 'figure'),
   [dash.dependencies.Input('DatePickerWohn', 'date')])

def wohn_temperatur_tag(date):
            if date == None:
                return None
            else:
                return einzelzimmer_graph_tagesverlauf(date, 't2', 'Temperatur')

#Callback-Funktion der Wohnzimmer-Seite, um den Luftfeuchtigkeits-Graph dynamisch je nach gewähltem Datum anzuzeigen.            
@app.callback(
    dash.dependencies.Output('Graph_Luftfeucht_Wohn', 'figure'),
   [dash.dependencies.Input('DatePickerWohn', 'date')])

def wohn_luftfeucht_tag(date):
            if date == None:
                return None
            else:
                return einzelzimmer_graph_tagesverlauf(date, 'rh_2', 'Luftfeuchtigkeit')            
            
#Callback-Funktion der Waschraum-Seite, um den Temperatur-Graph dynamisch je nach gewähltem Datum anzuzeigen.            
@app.callback(
    dash.dependencies.Output('Graph_Temperatur_Wasch', 'figure'),
   [dash.dependencies.Input('DatePickerWasch', 'date')])

def wasch_temperatur_tag(date):
            if date == None:
                return None
            else:
                return einzelzimmer_graph_tagesverlauf(date, 't3', 'Temperatur')

#Callback-Funktion der Waschraum-Seite, um den Luftfeuchtigkeits-Graph dynamisch je nach gewähltem Datum anzuzeigen.
@app.callback(
    dash.dependencies.Output('Graph_Luftfeucht_Wasch', 'figure'),
   [dash.dependencies.Input('DatePickerWasch', 'date')])

def wasch_luftfeucht_tag(date):
            if date == None:
                return None
            else:
                return einzelzimmer_graph_tagesverlauf(date, 'rh_3', 'Luftfeuchtigkeit')            
            
#Callback-Funktion der Schlafzimmer-Seite, um den Temperatur-Graph dynamisch je nach gewähltem Datum anzuzeigen.            
@app.callback(
    dash.dependencies.Output('Graph_Temperatur_Schlaf', 'figure'),
   [dash.dependencies.Input('DatePickerSchlaf', 'date')])

def schlaf_temperatur_tag(date):
            if date == None:
                return None
            else:
                return einzelzimmer_graph_tagesverlauf(date, 't9', 'Temperatur')

#Callback-Funktion der Schlafzimmer-Seite, um den Luftfeuchtigkeits-Graph dynamisch je nach gewähltem Datum anzuzeigen.            
@app.callback(
    dash.dependencies.Output('Graph_Luftfeucht_Schlaf', 'figure'),
   [dash.dependencies.Input('DatePickerSchlaf', 'date')])

def schlaf_luftfeucht_tag(date):
            if date == None:
                return None
            else:
                return einzelzimmer_graph_tagesverlauf(date, 'rh_9', 'Luftfeuchtigkeit')            

#Callback-Funktion der Küchen-Seite, um den Temperatur-Graph dynamisch je nach gewähltem Datum anzuzeigen.
@app.callback(
    dash.dependencies.Output('Graph_Temperatur_Kueche', 'figure'),
   [dash.dependencies.Input('DatePickerKueche', 'date')])

def kueche_temperatur_tag(date):
            if date == None:
                return None
            else:
                return einzelzimmer_graph_tagesverlauf(date, 't1', 'Temperatur')
        
#Callback-Funktion der Küchen-Seite, um den Luftfeuchtigkeits-Graph dynamisch je nach gewähltem Datum anzuzeigen.        
@app.callback(
    dash.dependencies.Output('Graph_Luftfeucht_Kueche', 'figure'),
   [dash.dependencies.Input('DatePickerKueche', 'date')])

def kueche_luftfeucht_tag(date):
            if date == None:
                return None
            else:
                return einzelzimmer_graph_tagesverlauf(date, 'rh_1', 'Luftfeuchtigkeit')            

#Callback-Funktion der Kinderzimmer-Seite, um den Temperatur-Graph dynamisch je nach gewähltem Datum anzuzeigen.
@app.callback(
    dash.dependencies.Output('Graph_Temperatur_Kinder', 'figure'),
   [dash.dependencies.Input('DatePickerKinder', 'date')])

def kinder_temperatur_tag(date):
            if date == None:
                return None
            else:
                return einzelzimmer_graph_tagesverlauf(date, 't8', 'Temperatur')

#Callback-Funktion der Kinderzimmer-Seite, um den Luftfeuchtigkeits-Graph dynamisch je nach gewähltem Datum anzuzeigen.            
@app.callback(
    dash.dependencies.Output('Graph_Luftfeucht_Kinder', 'figure'),
   [dash.dependencies.Input('DatePickerKinder', 'date')])

def kinder_luftfeucht_tag(date):
            if date == None:
                return None
            else:
                return einzelzimmer_graph_tagesverlauf(date, 'rh_8', 'Luftfeuchtigkeit')
            
#Callback-Funktion der Bügelzimmer-Seite, um den Temperatur-Graph dynamisch je nach gewähltem Datum anzuzeigen.            
@app.callback(
    dash.dependencies.Output('Graph_Temperatur_Buegel', 'figure'),
   [dash.dependencies.Input('DatePickerBuegel', 'date')])

def buegel_temperatur_tag(date):
            if date == None:
                return None
            else:
                return einzelzimmer_graph_tagesverlauf(date, 't7', 'Temperatur')

#Callback-Funktion der Bügelzimmer-Seite, um den Luftfeuchtigkeits-Graph dynamisch je nach gewähltem Datum anzuzeigen.        
@app.callback(
    dash.dependencies.Output('Graph_Luftfeucht_Buegel', 'figure'),
   [dash.dependencies.Input('DatePickerBuegel', 'date')])

def buegel_luftfeucht_tag(date):
            if date == None:
                return None
            else:
                return einzelzimmer_graph_tagesverlauf(date, 'rh_7', 'Luftfeuchtigkeit')            

#Callback-Funktion der Badezimmer-Seite, um den Temperatur-Graph dynamisch je nach gewähltem Datum anzuzeigen.
@app.callback(
    dash.dependencies.Output('Graph_Temperatur_Bad', 'figure'),
   [dash.dependencies.Input('DatePickerBad', 'date')])

def bad_temperatur_tag(date):
            if date == None:
                return None
            else:
                return einzelzimmer_graph_tagesverlauf(date, 't5', 'Temperatur')
            
#Callback-Funktion der Badezimmer-Seite, um den Luftfeuchtigkeits-Graph dynamisch je nach gewähltem Datum anzuzeigen.
@app.callback(
    dash.dependencies.Output('Graph_Luftfeucht_Bad', 'figure'),
   [dash.dependencies.Input('DatePickerBad', 'date')])

def bad_luftfeucht_tag(date):
            if date == None:
                return None
            else:
                return einzelzimmer_graph_tagesverlauf(date, 'rh_5', 'Luftfeuchtigkeit')
            
#Callback-Funktion der Arbeitszimmer-Seite, um den Temperatur-Graph dynamisch je nach gewähltem Datum anzuzeigen.
@app.callback(
    dash.dependencies.Output('Graph_Temperatur_Arbeitzimmer', 'figure'),
   [dash.dependencies.Input('DatePickerArbeit', 'date')])

def arbeitszimmer_temperatur_tag(date):
            if date == None:
                return None
            else:
                return einzelzimmer_graph_tagesverlauf(date, 't4', 'Temperatur')
            
#Callback-Funktion der Arbeitszimmer-Seite, um den Luftfeuchtigkeits-Graph dynamisch je nach gewähltem Datum anzuzeigen.            
@app.callback(
    dash.dependencies.Output('Graph_Luftfeucht_Arbeitzimmer', 'figure'),
   [dash.dependencies.Input('DatePickerArbeit', 'date')])

def arbeitszimmer_luftfeucht_tag(date):
            if date == None:
                return None
            else:
                return einzelzimmer_graph_tagesverlauf(date, 'rh_4', 'Luftfeuchtigkeit')            

#Funtion, die Plotly-HTML-Code erzeugt, um die Tagesverlaufgraphen der einzelnen Zimmer anzuzeigen.
def einzelzimmer_graph_tagesverlauf(date, datenbankspalte, ueberschrift):
            if date == None:
                    return None
                
            else:
                dashboard_datum_liste = dashboard_datum_gesplittet(date)
                
                DB_connector = postgre_connector()
                
                if ueberschrift == 'Temperatur':
                    title = 'Temperatur [°C]'
                
                else:
                    title = 'Luftfeuchte [%]'
                
            
                day1 = [int(dashboard_datum_liste[0]),int(dashboard_datum_liste[1]),int(dashboard_datum_liste[2]),00,00]
                day2 = [int(dashboard_datum_liste[0]),int(dashboard_datum_liste[1]),int(dashboard_datum_liste[2]),23,50]
                result = DB_connector.get_data(day1, day2, 'a', [datenbankspalte])
                
                return {
                        'data': [
                                    {'x': result['datum'], 'y': result[datenbankspalte], 'type': 'scatter', 'name': title, 'textposition' : 'bottom center' ,'marker' : { 'color' : '#33C1B1'}},
                                ],
                        'layout': {
                                    'title': ueberschrift,
                                    'yaxis' : {'title' : title}
                           }
                        }           
                                        
#Callback-Funktion der Arbeitszimmer-Webseite, um die Durchschnitts Luftfeuchtigkeit und Temperatur dynamisch je nach Datum anzuzeigen.
@app.callback(
    dash.dependencies.Output('Durchschnitt_Temp_Luftfeuchte_Arbeitszimmer', 'children'),
   [dash.dependencies.Input('DatePickerArbeit', 'date')])

def arbeitszimmer_durchschnitt_temp_luftfeuchte(date):
            if date == None:
                return None
            else:
                return einzelzimmer_durchschnitt_temp_luftfeuchte(date, 't4', 'rh_4')   

#Callback-Funktion der Badezimmer-Webseite, um die Durchschnitts Luftfeuchtigkeit und Temperatur dynamisch je nach Datum anzuzeigen.
@app.callback(
    dash.dependencies.Output('Durchschnitt_Temp_Luftfeuchte_Bad', 'children'),
   [dash.dependencies.Input('DatePickerBad', 'date')])

def bad_durchschnitt_temp_luftfeuchte(date):
            if date == None:
                return None
            else:
                return einzelzimmer_durchschnitt_temp_luftfeuchte(date, 't5', 'rh_5')  

#Callback-Funktion der Bügelzimmer-Webseite, um die Durchschnitts Luftfeuchtigkeit und Temperatur dynamisch je nach Datum anzuzeigen.            
@app.callback(
    dash.dependencies.Output('Durchschnitt_Temp_Luftfeuchte_Buegel', 'children'),
   [dash.dependencies.Input('DatePickerBuegel', 'date')])

def buegel_durchschnitt_temp_luftfeuchte(date):
            if date == None:
                return None
            else:
                return einzelzimmer_durchschnitt_temp_luftfeuchte(date, 't7', 'rh_7')

#Callback-Funktion der Kinderzimmer-Webseite, um die Durchschnitts Luftfeuchtigkeit und Temperatur dynamisch je nach Datum anzuzeigen.            
@app.callback(
    dash.dependencies.Output('Durchschnitt_Temp_Luftfeuchte_Kinder', 'children'),
   [dash.dependencies.Input('DatePickerKinder', 'date')])

def kinder_durchschnitt_temp_luftfeuchte(date):
            if date == None:
                return None
            else:
                return einzelzimmer_durchschnitt_temp_luftfeuchte(date, 't8', 'rh_8')   
            
#Callback-Funktion der Küchen-Webseite, um die Durchschnitts Luftfeuchtigkeit und Temperatur dynamisch je nach Datum anzuzeigen.            
@app.callback(
    dash.dependencies.Output('Durchschnitt_Temp_Luftfeuchte_Kueche', 'children'),
   [dash.dependencies.Input('DatePickerKueche', 'date')])

def kueche_durchschnitt_temp_luftfeuchte(date):
            if date == None:
                return None
            else:
                return einzelzimmer_durchschnitt_temp_luftfeuchte(date, 't1', 'rh_1')   

#Callback-Funktion der Schlafzimmer-Webseite, um die Durchschnitts Luftfeuchtigkeit und Temperatur dynamisch je nach Datum anzuzeigen.                    
@app.callback(
    dash.dependencies.Output('Durchschnitt_Temp_Luftfeuchte_Schlaf', 'children'),
   [dash.dependencies.Input('DatePickerSchlaf', 'date')])

def schlaf_durchschnitt_temp_luftfeuchte(date):
            if date == None:
                return None
            else:
                return einzelzimmer_durchschnitt_temp_luftfeuchte(date, 't9', 'rh_9')   

#Callback-Funktion der Waschraum-Webseite, um die Durchschnitts Luftfeuchtigkeit und Temperatur dynamisch je nach Datum anzuzeigen.                        
@app.callback(
    dash.dependencies.Output('Durchschnitt_Temp_Luftfeuchte_Wasch', 'children'),
   [dash.dependencies.Input('DatePickerWasch', 'date')])

def wasch_durchschnitt_temp_luftfeuchte(date):
            if date == None:
                return None
            else:
                return einzelzimmer_durchschnitt_temp_luftfeuchte(date, 't3', 'rh_3')   
            
#Callback-Funktion der Wohnzimmer-Webseite, um die Durchschnitts Luftfeuchtigkeit und Temperatur dynamisch je nach Datum anzuzeigen.                        
@app.callback(
    dash.dependencies.Output('Durchschnitt_Temp_Luftfeuchte_Wohn', 'children'),
   [dash.dependencies.Input('DatePickerWohn', 'date')])

def wohn_durchschnitt_temp_luftfeuchte(date):
            if date == None:
                return None
            else:
                return einzelzimmer_durchschnitt_temp_luftfeuchte(date, 't2', 'rh_2')   
            
#Funktion, die den Plotly-HTML-Code erzeugt, um die durchschnittliche Luftfeuchtigkeit und Temperatur der Einzelzimmer-Webseiten anzuzeigen.
def einzelzimmer_durchschnitt_temp_luftfeuchte(date, temp_datenbankspalte, luftfeucht_datenbankspalte):
                dashboard_datum_liste = dashboard_datum_gesplittet(date)
                
                DB_connector = postgre_connector()
                
            
                day1 = [int(dashboard_datum_liste[0]),int(dashboard_datum_liste[1]),int(dashboard_datum_liste[2]),00,00]
                day2 = [int(dashboard_datum_liste[0]),int(dashboard_datum_liste[1]),int(dashboard_datum_liste[2]),23,50]
                result = DB_connector.get_data(day1, day2, 'a', [temp_datenbankspalte, luftfeucht_datenbankspalte])
                
                durchschnitt_temp = np.array(result[temp_datenbankspalte]).mean().round(2)
                durchschnitt_luftfeucht = np.array(result[luftfeucht_datenbankspalte]).mean().round(2)                                
                return html.Div(className='row',
                               children=[
                
                                            html.Div(className='col',
                                                     children=
                                                                html.P(className='data temp',
                                                                       children=[
                                                                                   durchschnitt_temp,
                                                                                   html.I(className='mdi mdi-temperature-celsius kreis-icon')
                                                                               ]
                                                                       )
                                                    ),
                                            html.Div(className='col',
                                                     children=
                                                                html.P(className='data temp',
                                                                       children=[
                                                                                   durchschnitt_luftfeucht,
                                                                                   html.I(className='mdi mdi-water-percent kreis-icon')
                                                                               ]
                                                                       )
                                                    )
                                            ]
                                ) 
                         #)                                      
#----------------------------------------------------------------- Analytics

#Callback-Methoden zum handeln der Auswahl der aktuellen Zimmer/Räume in Analytics.py

@app.callback(
    dash.dependencies.Output('Arbeitszimmer', 'style'),
    [dash.dependencies.Input('Arbeitszimmer', 'n_clicks')])
def click_az(value):
    if(value == None):
        return analytics.set_active_room('Arbeitszimmer')
    if analytics.active_rooms['Arbeitszimmer'] == False:
        analytics.active_rooms['Arbeitszimmer'] = True
        return analytics.set_active_room('Arbeitszimmer')
    else:
        analytics.active_rooms['Arbeitszimmer'] = False
        return analytics.set_active_room('Arbeitszimmer')
    
@app.callback(
    dash.dependencies.Output('Badezimmer', 'style'),
    [dash.dependencies.Input('Badezimmer', 'n_clicks')])
def click_baz(value):
    if(value == None):
        return analytics.set_active_room('Badezimmer') 
    if analytics.active_rooms['Badezimmer'] == False:
        analytics.active_rooms['Badezimmer'] = True
        return analytics.set_active_room('Badezimmer')
    else:
        analytics.active_rooms['Badezimmer'] = False
        return analytics.set_active_room('Badezimmer')

@app.callback(
    dash.dependencies.Output('Bügelzimmer', 'style'),
    [dash.dependencies.Input('Bügelzimmer', 'n_clicks')])
def click_büz(value):
    if(value == None):
        return analytics.set_active_room('Bügelzimmer')
    if analytics.active_rooms['Bügelzimmer'] == False:
        analytics.active_rooms['Bügelzimmer'] = True
        return analytics.set_active_room('Bügelzimmer')
    else:
        analytics.active_rooms['Bügelzimmer'] = False
        return analytics.set_active_room('Bügelzimmer')

@app.callback(
    dash.dependencies.Output('Kinderzimmer', 'style'),
    [dash.dependencies.Input('Kinderzimmer', 'n_clicks')])
def click_kz(value):
    if(value == None):
        return analytics.set_active_room('Arbeitszimmer')
    if analytics.active_rooms['Kinderzimmer'] == False:
        analytics.active_rooms['Kinderzimmer'] = True
        return analytics.set_active_room('Kinderzimmer')
    else:
        analytics.active_rooms['Kinderzimmer'] = False
        return analytics.set_active_room('Kinderzimmer')

@app.callback(
    dash.dependencies.Output('Küche', 'style'),
    [dash.dependencies.Input('Küche', 'n_clicks')])
def click_kü(value):
    if(value == None):
        return analytics.set_active_room('Küche')
    if analytics.active_rooms['Küche'] == False:
        analytics.active_rooms['Küche'] = True
        return analytics.set_active_room('Küche')
    else:
        analytics.active_rooms['Küche'] = False
        return analytics.set_active_room('Küche') 

@app.callback(
    dash.dependencies.Output('Schlafzimmer', 'style'),
    [dash.dependencies.Input('Schlafzimmer', 'n_clicks')])
def click_sz(value):
    if(value == None):
        return analytics.set_active_room('Schlafzimmer')
    if analytics.active_rooms['Schlafzimmer'] == False:
        analytics.active_rooms['Schlafzimmer'] = True
        return analytics.set_active_room('Schlafzimmer')
    else:
        analytics.active_rooms['Schlafzimmer'] = False
        return analytics.set_active_room('Schlafzimmer') 
    
@app.callback(
    dash.dependencies.Output('Waschküche', 'style'),
    [dash.dependencies.Input('Waschküche', 'n_clicks')])
def click_wk(value):
    if(value == None):
        return analytics.set_active_room('Waschküche')
    if analytics.active_rooms['Waschküche'] == False:
        analytics.active_rooms['Waschküche'] = True
        return analytics.set_active_room('Waschküche')
    else:
        analytics.active_rooms['Waschküche'] = False
        return analytics.set_active_room('Waschküche') 

@app.callback(
    dash.dependencies.Output('Wohnzimmer', 'style'),
    [dash.dependencies.Input('Wohnzimmer', 'n_clicks')])
def click_wz(value):
    if(value == None):
        return analytics.set_active_room('Wohnzimmer')
    if analytics.active_rooms['Wohnzimmer'] == False:
        analytics.active_rooms['Wohnzimmer'] = True
        return analytics.set_active_room('Wohnzimmer')
    else:
        analytics.active_rooms['Wohnzimmer'] = False
        return analytics.set_active_room('Wohnzimmer') 

#Call-Back Methode: Initialisiert den Graphen der ausgewählten Zimmer 
    
@app.callback(
    dash.dependencies.Output('analytics_graph', 'children'),  
    [dash.dependencies.Input('Arbeitszimmer', 'n_clicks'),
      dash.dependencies.Input('Badezimmer', 'n_clicks'),
      dash.dependencies.Input('Bügelzimmer', 'n_clicks'),
      dash.dependencies.Input('Kinderzimmer', 'n_clicks'),
      dash.dependencies.Input('Küche', 'n_clicks'),
      dash.dependencies.Input('Schlafzimmer', 'n_clicks'),
      dash.dependencies.Input('Waschküche', 'n_clicks'),
      dash.dependencies.Input('Wohnzimmer', 'n_clicks'),
      dash.dependencies.Input('daterange', 'start_date'),
      dash.dependencies.Input('daterange', 'end_date'),
      dash.dependencies.Input('mode_data', 'value'),
      dash.dependencies.Input('mode_time', 'value')])
def graph_cb(value1, value2, value3, value4, value5, value6, value7, value8, start_date, end_date, mode_data, mode_time):
    
    DB_conn = postgre_connector()
    retDiv = html.Div(children = [])
    graph = dcc.Graph(config = {'responsible' : True})
    start_date = dt.datetime.strptime(start_date[:10], '%Y-%m-%d')
    end_date = dt.datetime.strptime(end_date[:10], '%Y-%m-%d')
                      
    unit = None
    
    analytics.start_date = start_date
    analytics.end_date = end_date
    analytics.data = mode_data
    analytics.mode = mode_time

    room_list = []
    gath = []
    
    analytics.rooms = [k for k in analytics.active_rooms.keys() if analytics.active_rooms[k] == True]
    
    if mode_data == 'temp':
        room_list += [room_dict[x][0] for x in analytics.rooms]
        result = DB_conn.get_data(start_date, end_date, mode_time, room_list)
        unit = '[°C]'
    
    elif mode_data == 'tempd':
        room_list += [room_dict[x][0] for x in analytics.rooms] 
        room_list += ['t_out']
        analytics.rooms += ['Temperatur Draußen']
        result = DB_conn.get_data(start_date, end_date, mode_time, room_list)
        unit = '[°C]'
        
    elif mode_data == 'hum':
        room_list += [room_dict[x][1] for x in analytics.rooms]
        result = DB_conn.get_data(start_date, end_date, mode_time, room_list)
        unit = '[%]'
    
    elif mode_data == 'humd':
        room_list += [room_dict[x][1] for x in analytics.rooms]
        room_list += ['rh_out']
        analytics.rooms += ['Luftfeuchtigkeit Draußen']
        result = DB_conn.get_data(start_date, end_date, mode_time, room_list)
        unit = '[%]'
        
    data_col = list(result.columns).copy()
    data_col.remove('datum')
    
    col_n = 0
        
    for col,name in zip(data_col, analytics.rooms):
        if col != 'datum':
            fig_data = {'x' : result['datum'], 'y' : result[col], 'type' : 'line', 'textposition' : 'bottom center' , 'name' : name + ' ' + unit, 'marker' : { 'color' : get_color(col_n)}}
            gath.append(fig_data)
            col_n += 1
        
    if mode_data == 'tempd':
        analytics.rooms.remove('Temperatur Draußen')
    elif mode_data == 'humd':
        analytics.rooms.remove('Luftfeuchtigkeit Draußen')
        
    if mode_data == 'temp' or mode_data == 'tempd':
        unit = 'Temperatur ' + unit
    else:
        unit = 'Luftfeuchte ' + unit
    
    fig = { 'data' : gath, 'layout': {'title': 'Analytics Graph', 'height' : '600', 'yaxis' : {'title' : unit}}}
    graph = dcc.Graph(figure=fig)
    
    retDiv.children = graph
    
    analytics.graph.children = graph
    retDiv.className = 'graph'
    
    return retDiv                                           
                          
 # <------------------------------------------> Optimazation Callback

#Ändert das Ausgewählte Datum auf der Optimization.py
@app.callback(
    dash.dependencies.Output('url', 'pathname'),
    [dash.dependencies.Input('datepicker-optimization', 'date')])
def date_callback(date):
    optimization.set_date(dt.datetime.strptime(date[:10], '%Y-%m-%d'))
    uhrzeit_datum.datum[0] = str(optimization.date.year)
    uhrzeit_datum.datum[1] = str(optimization.date.month)
    uhrzeit_datum.datum[2] = str(optimization.date.day)
    return '/optimization'

#Call-Back Methode, welche den Text des Light-Cases übergibt    
@app.callback(
    dash.dependencies.Output('lightstext', 'children'),
    [dash.dependencies.Input('lightsbt', 'n_clicks')]) 
def lights_inf(click):
    if click != None:
        return 'Haben Sie letzte Nacht eventuell vergessen das Licht in einem der Räume auszuschalten?'
    
#Call-Back Methode, welche den Text des Appliances-Cases übergibt       
@app.callback(
    dash.dependencies.Output('appliancestext', 'children'),
    [dash.dependencies.Input('appliancesbt', 'n_clicks')]) 
def appliances_inf(click):
    if click != None:
        return 'Haben Sie letzte Nacht eventuell vergessen laufende Elektrische Geräte wie z.B. den Fernseher auszuschalten?'

#Call-Back Methode, welche den Text des Windspeed-Cases übergibt    
@app.callback(
    dash.dependencies.Output('windspeedtext', 'children'),
    [dash.dependencies.Input('windspeedbt', 'n_clicks')]) 
def windspeed_inf(click):
    if click != None:
        return 'Heute war es besonders windig, in Zukunft könnte sich ein Windrad lohnen! Die Energie die erzeugt würde, berechnet sich aus einem Windrad mit 3m Rotorblattlänge und 20% Energieeffizienz.'

#Call-Back Methode, welche den Text des Sichtbarkeits-Cases übergibt    
@app.callback(
    dash.dependencies.Output('visibilitytext', 'children'),
    [dash.dependencies.Input('visibilitybt', 'n_clicks')]) 
def visibility_inf(click):
    if click != None:
        return 'Heute war es kaum bewölkt, gehen Sie doch Morgen spatzieren!'

#Call-Back Methode, welche den Text des Schimmel-Cases übergibt    
@app.callback(
    dash.dependencies.Output('schimmeltext', 'children'),
    [dash.dependencies.Input('schimmelbt', 'n_clicks')]) 
def schimmel_inf(click):
    if click != None:
        return 'Der Graph zeigt für den ausgewählten Tag, den Raum mit der aus den Daten errechneten höchsten Tauwerttemperatur.\n Temperaturen an Wänden oder Bauteilen die unter dem angegebenen Taupunkt liegen, sind Schimmel gefährdet!'                               
                          
                    
                    
if __name__ == '__main__':    app.run_server(debug=False)