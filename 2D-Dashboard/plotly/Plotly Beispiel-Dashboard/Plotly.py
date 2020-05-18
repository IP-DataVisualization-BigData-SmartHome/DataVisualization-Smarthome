# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 13:36:06 2020

@author: Mues
"""

import numpy as np
import plotly_express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import base64
from dash.dependencies import Input, Output
import pandas
from IndexSeite import IndexPage
from Analyse import AnalysePage
from Optimieren import OptimierenPage

#csv einlesen
df = pandas.read_excel(r'D:\Downloads\IP-Projekt2020\Kaddle-Dataset-Energyuseage.xlsx')

#print(type(series_daten))
#datetime
series_daten = df['date']

liste_ohne_doppelte=[]

#with open('D:\Downloads\IP-Projekt2020\Plotly\Optimieren.html', 'r') as f:
 #   html_string = f.read()

for i in series_daten.index:
    if i == 0:
        liste_ohne_doppelte.append(series_daten[i].date())
    elif series_daten[i].date() != series_daten[i-1].date():
        liste_ohne_doppelte.append(series_daten[i].date())



image_filename = 'nur_gebaeude.png' 
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

external_scripts = [
    'https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js',
    'https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js'
]

external_stylesheets = [
        'https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css',
        'D:\Downloads\IP-Projekt2020\Plotly\Optimieren.py'
        
]

app = dash.Dash(external_stylesheets=external_stylesheets, external_scripts=external_scripts)
app.title = 'Dashboard'

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


#erzeugt die Unterseiten
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])

def display_page(pathname):
    if pathname == '/analyse':
        return AnalysePage().analyse_seite()
    elif pathname == '/startseite':
        return IndexPage().index_seite(liste_ohne_doppelte)
        #return index_page
    elif pathname == '/optimieren':
        return OptimierenPage().optimieren_seite()
    else:
        return IndexPage().index_seite(liste_ohne_doppelte)
        #return index_page

#erzeugt die Grad-Zahl Ausgabe des ersten Zimmers
@app.callback(
     dash.dependencies.Output('max-Temp-Raum1', 'children'),
    [dash.dependencies.Input('dropdown-zeit', 'value'),
     dash.dependencies.Input('dropdown-tag', 'value')])

def erzeuge_gradzahl(value1, value2):
   # temperatur_raum = None
   if(value1 == None or value2 == None):
       return None
   else:
        for i in df.index:
            if (value2 == df['date'][i].date().strftime("%Y-%m-%d") and 
               value1 == df['date'][i].time().strftime("%H:%M:%S")):
                    temperatur_raum_1 = df['T1'][i]/1000000000000000
               
        return html.Center(children=(
                                    'Die Temperatur im ersten Raum beträgt um ' + 
                                    value1 + 
                                    ' Uhr ' + 
                                    np.array2string(temperatur_raum_1) + 
                                    ' Grad.'
                                    )
                          )   
    #return 'You have selected "{}"'.format(value1)

 #erzeugt das Uhrzeit Dropdown Menu
@app.callback(
    dash.dependencies.Output('dropdown-liste-zeiten', 'children'),
   [dash.dependencies.Input('dropdown-tag', 'value')])


def erzeuge_uhrzeit_dropdown(value1):
    liste_zeiten=[]
    if value1 == None:
        return None
    else:        
        #erstellt liste fuer die Uhrzeiten des entsprechenden Tages
        for i in series_daten.index:
            if value1 == series_daten[i].date().strftime("%Y-%m-%d"):
                liste_zeiten.append(series_daten[i].time())
                
        return html.Center(children=(dcc.Dropdown(
                                                id='dropdown-zeit', 
                                                style={'text-align': 'left'},  
                                                options=[
                                                            {
                                                                    'label': i.strftime("%H:%M Uhr"), 
                                                                    'value': i
                                                            } 
                                                            for i in liste_zeiten
                                                        ]
                                                )
                                    )
                            )
    
#erzeugt den Graphen
@app.callback(
    dash.dependencies.Output('dd-output-container', 'children'),
   [dash.dependencies.Input('dropdown-tag', 'value')])


def erzeuge_strom_graphen(value1):
    liste_zeiten=[]
    liste_appliances=[]
    if value1 == None:
        return None
    else:
        #erstellt liste fuer den Stromverbrauchsgraphen
        for j in df.index:
            if value1 == df['date'][j].date().strftime("%Y-%m-%d"):
                liste_appliances.append(df['Appliances'][j])
                aktueller_tag = df['date'][j].date().strftime("%d/%m/%y")
        
        #erstellt liste fuer die Uhrzeiten des entsprechenden Tages
        for i in series_daten.index:
            if value1 == series_daten[i].date().strftime("%Y-%m-%d"):
                aktueller_tag = series_daten[i].date().strftime("%d/%m/%y")
                liste_zeiten.append(series_daten[i].time())
                
        return html.Center(children=(
                                    dcc.Graph(
                                            id='example Graph2',
                                            figure = {
                                                'data': [
                                                            {'x': liste_zeiten, 'y': liste_appliances, 'type': 'scatter', 'name': 'SF'},
                                                        ],
                                                'layout': {
                                                            'title': 'Stromverbrauch vom ' + 
                                                                     aktueller_tag + 
                                                                     ' über den Tag verteilt'
                                                          }
                                                    }
                                            ),
                                    )
                            )

if __name__ == '__main__':
    app.run_server()
    