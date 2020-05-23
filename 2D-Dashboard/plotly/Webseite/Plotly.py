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




external_scripts = [
    'https://code.jquery.com/jquery-3.2.1.slim.min.js',
    'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js',
    'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js'
]

external_stylesheets = [
        dbc.themes.BOOTSTRAP,
        'https://cdn.materialdesignicons.com/5.1.45/css/materialdesignicons.min.css'
]


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



#erzeugt die Unterseiten
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])


def display_page(pathname):
    if pathname == '/dashboard.html':
        return Dashboard().dashboard_seite()
    elif pathname== '/optimization.html':
        return Optimization().optimization_seite()
    elif pathname== '/bad.html':
        return Bad().bad_seite()
    elif pathname== '/buegel.html':
        return Buegel().buegel_seite()
    elif pathname== '/kinder.html':
        return Kinder().kinder_seite()
    elif pathname== '/kueche.html':
        return Kueche().kueche_seite()
    elif pathname== '/schlaf.html':
        return Schlaf().schlaf_seite()
    elif pathname== '/wasch.html':
        return Wasch().wasch_seite()
    elif pathname== '/arbeit.html':
        return Arbeit().arbeit_seite()
    elif pathname== '/wohn.html':
        return Wohn().wohn_seite()
    else:
        return Dashboard().dashboard_seite()
    
@app.callback(
    dash.dependencies.Output('output-test-callback', 'children'),
   [dash.dependencies.Input('input-test-callback', 'value')])


def erzeuge_uhrzeit_dropdown(value):
            if value == None:
                return None
            else:
                return html.Div(children=value)


if __name__ == '__main__':
    app.run_server()
    