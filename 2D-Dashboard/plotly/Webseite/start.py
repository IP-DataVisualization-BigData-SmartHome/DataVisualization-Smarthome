#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 13:27:52 2020

@author: lukas
"""

import dash_html_components as html
import dash_core_components as dcc

class start:
    
    #HTML-Seite in Plotly übersetzt, gibt die aktuelle Version als Plotly-Objekt zurück
    def start_seite(self):
        return html.Div(children = [html.Nav(className = 'nav-abstand',
                                     children=
                                                 html.Div(className='container-fluid head-design',
                                                          children=
                                                                      html.Div(className='row',
                                                                               children=[
                                                                                           html.Div(className='col-3', children = html.Div(className='start-impressum', children = html.P(className='imp-link', children = html.A(href='impressum', children='Impressum', className = 'start-impressum'))) ) ,
                                                                                           html.Div(className='col-6 text-center head-optimization',
                                                                                                    children=
                                                                                                                html.A(children='IP-Datenvisualisierung')
                                                                                                    ),
                                                                                           html.Div(className='col-3 text-right logo', id = 'mydiv',
                                                                                                    children = html.A(children = html.Img(src='assets/logo.png', height=70, width='auto'), href='start'))
                                                                                       ]
                                                                               )
                                                          )
                                     ), 
                                    html.Div(className='container start-abstand',
                                              children = html.Div(className='row',
                                                                  children = [ html.Div(className='col-12',
                                                                                      children = html.Div(className='maindiv', 
                                                                                                          children = [ 
                                                                                                                       html.Div(className='abs abs1', children='Das interdisziplinäre Projekt "Datenvisualisierung für Big Data im Smart Home" ist ein Projekt der Fachhochschule Aachen, was in Zusammenarbeit von Studenten der Studiengänge Informatik und Media and Communications for Digital Business unter der Leitung von den Professoren Frank Hartung und Ingo Elsen im Sommersemester 2020 durchgeführt wurde.'),
                                                                                                                       html.Div(className='abs abs2', children='Ziel des Projektes war die übersichtliche Umsetzung von einem Smart Home Datensatz in ein 2D-Dashboard und eine 3D-Visualisierung.'),
                                                                                                                       html.Div(className='abs abs3', 
                                                                                                                                children = [ 'Beteiligte Studenten sind:', 
                                                                                                                                              html.Ul(children = [ html.Li(children='Lukas Schnittcher (Projektleiter)'),
                                                                                                                                                                   html.Li(children='Daniel Chinta'),
                                                                                                                                                                   html.Li(children='Max Conzen'),
                                                                                                                                                                   html.Li(children='Tobias Kordt'),
                                                                                                                                                                   html.Li(children='Erik Mues'),
                                                                                                                                                                   html.Li(children='Marc Oyen'),
                                                                                                                                                                   html.Li(children='Simon Waidner')
                                                                                                                                                                 ]
                                                                                                                                                      ) 
                                                                                                                                            ]
                                                                                                                                )
                                                                                                                      ]
                                                                                                          )
                                                                                      )
                                                                             ]
                                                                  )
                                              ),
                                     html.Nav(className='navbar fixed-bottom', 
                                              children =      html.Div(className= 'container-fluid navdiv',
                                                                       children =   [   html.Div(className='col navdiv', 
                                                                                                 children = html.A(className='nav-link', href='analytics', 
                                                                                                                   children =   [   html.I(className='mdi mdi-google-analytics navicon'),
                                                                                                                                    html.P(className='nav-text', children = 'Analytics')
                                                                                                                                ]
                                                                                                                   
                                                                                                                  )
                                                                                                 ),
                                                                                         html.Div(className='col navdiv', 
                                                                                                 children = html.A(className='nav-link', href='dashboard', 
                                                                                                                   children =   [   html.I(className='mdi mdi-home navicon'),
                                                                                                                                    html.P(className='nav-text', children = 'Dashboard')
                                                                                                                                ]
                                                                                                                   
                                                                                                                  )
                                                                                                 ),
                                                                                         html.Div(className='col navdiv', 
                                                                                                 children = html.A(className='nav-link', href='optimization', 
                                                                                                                   children =   [   html.I(className='mdi mdi-sync navicon'),
                                                                                                                                    html.P(className='nav-text', children = 'Optimization')
                                                                                                                                ]
                                                                                                                   
                                                                                                                  )
                                                                                                 )
                                                                                     
                                                                                     ]
                                                                       )
                                              ) 
                                    ]
                        )
            
           
