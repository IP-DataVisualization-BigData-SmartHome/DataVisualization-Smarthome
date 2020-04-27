# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 17:17:54 2020

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

class IndexPage:
    
    image_filename = 'nur_gebaeude.png' 
    encoded_image = base64.b64encode(open(image_filename, 'rb').read())
    
    #def __init__(self):
        
    def index_seite(self, liste_ohne_doppelte):
        return html.Div([
                        html.Center(
                                children=(
                                        html.Div(className='Container', 
                                                 style={'width': '350px'}, 
                                                 children=(
                                                        html.Div(className='row', 
                                                                 children=[
                                                                         (html.Div(className='col-md-6', 
                                                                                   children=(
                                                                                               dcc.Dropdown(id='dropdown-tag', 
                                                                                                            style={'text-align': 'left'},  
                                                                                                            options=[{'label': i.strftime("%d/%m/%y"), 'value': i} for i in liste_ohne_doppelte],
                                                                                                            )
                                                                                             )
                                                                                   )
                                                                          ),
                                                                          (html.Div(className='col-md-6', 
                                                                                     children=(
                                                                                             html.Div(id='dropdown-liste-zeiten')
                                                                                             )
                                                                                     )
                                                                            ) 
                                                                            ]
                                                                )   
                                                            )
                                                )
                                        )
                                    ),
                        html.Div(id='max-Temp-Raum1'),
                        html.Div(id='dd-output-container'),
                       
                                         
                        html.Center(children=
                                            html.Img(src='data:image/png;base64,{}'.format(self.encoded_image.decode()), style={'align': 'center'}),
                                    ),
                        
                        html.Nav(className='navbar navbar-inverse', 
                                 children=
                                          html.Ul(className='nav navbar-nav',
                                                  children=[
                                                          html.Li(children=
                                                                  dcc.Link('Analyse', href='/analyse')
                                                                  ),
                                                          html.Li(children=
                                                                  dcc.Link('Gebäude', href='/gebaeude')
                                                                  ),
                                                          html.Li(children=
                                                                  dcc.Link('Optimieren', href='/optimieren')
                                                                  ),
                                                          ]
                                                  )
                                  )
                ])