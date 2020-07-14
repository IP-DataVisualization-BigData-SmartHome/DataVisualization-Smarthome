#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 13:27:52 2020

@author: lukas
"""

import dash_html_components as html
import dash_core_components as dcc

class start:
    
    def start_seite():
        return html.Div(children = [ html.Div(className='container',
                                              children = html.Div(className='row',
                                                                  children = [ html.Div(className='col-12',
                                                                                      children = html.Div(className='maindiv', 
                                                                                                          children = [ html.H1(className='h1main', children='IP-Datenvisualisierung'),
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
                                                                                      ),
                                                                               html.Div(className='logo', children = html.Img(src='logo.png', width='100%', alt='Logo FH Aachen'))
                                                                             ]
                                                                  )
                                              ),
                                     html.Footer(children = html.Div(className='foot', children = html.P(className='imp-link', children = html.A(href='impressum.html', children='Impressum')))),
                                     html.Nav(className='navbar fixed bottom', 
                                              children =      html.Div(className= 'container-fluid navdiv',
                                                                       children =   [   html.div(className='col navdiv', 
                                                                                                 children = html.A(classname='nav-link', href='analytics.html', 
                                                                                                                   children =   [   html.I(className='mdi mdi-google-analytics navicon'),
                                                                                                                                    html.P(className='nav-text', children = 'Analytics')
                                                                                                                                ]
                                                                                                                   
                                                                                                                  )
                                                                                                 ),
                                                                                         html.div(className='col navdiv', 
                                                                                                 children = html.A(classname='nav-link nav-link-active', href='#', 
                                                                                                                   children =   [   html.I(className='mdi mdi-home navicon'),
                                                                                                                                    html.P(className='nav-text', children = 'Dashboard')
                                                                                                                                ]
                                                                                                                   
                                                                                                                  )
                                                                                                 ),
                                                                                         html.div(className='col navdiv', 
                                                                                                 children = html.A(classname='nav-link nav-link-active', href='optimazation.html', 
                                                                                                                   children =   [   html.I(className='mdi mdi-sync navicon'),
                                                                                                                                    html.P(className='nav-text', children = 'Optimazation')
                                                                                                                                ]
                                                                                                                   
                                                                                                                  )
                                                                                                 )
                                                                                     
                                                                                     ]
                                                                       )
                                              ) 
                                    ]
                        )
            
           
