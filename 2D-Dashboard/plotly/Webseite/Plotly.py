# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:41:53 2020

@author: Mues
"""


import dash
import dash_core_components as dcc
import dash_html_components as html
from Dashboard import Dashboard




external_scripts = [
    'https://code.jquery.com/jquery-3.2.1.slim.min.js',
    'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js',
    'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js'
]

external_stylesheets = [
        'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css',
        'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css',
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
        <div>My Custom header</div>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
        <div>My Custom footer</div>
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
    if pathname == '/startseite':
        return Dashboard().dashboard_seite()
    else:
        return Dashboard().dashboard_seite()
        



if __name__ == '__main__':
    app.run_server()
    