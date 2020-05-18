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

class AnalysePage:
    
     def analyse_seite(self):
         return html.Div([
                        dcc.Link('Startseite', href='/startseite'),
                        html.Br(),
                        dcc.Link('Optimierungsseite', href='/optimieren'),
                        ])
    
    