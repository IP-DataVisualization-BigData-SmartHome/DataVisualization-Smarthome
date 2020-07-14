#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 13:28:09 2020

@author: lukas
"""

import dash_html_components as html
import dash_core_components as dcc

class impressum:
    
    def impressum_seite():
        return html.Div(children = [ html.Div(className='container',
                                              children =      html.Div(className='maindiv', 
                                                                       children =     [    html.H1(children='Impressum'),
                                                                                           html.Div(className='abs abs1', 
                                                                                                    children = 'Die FH Aachen ist eine vom Land getragene, rechtsfähige Körperschaft des öffentlichen Rechts. Der Betrieb der FH Aachen erfolgt auf der Grundlage des Gesetzes über die Hochschulen des Landes Nordrhein-Westfalen. Sie wird durch den Rektor nach außen vertreten. In Rechts- und Verwaltungsangelegenheiten wird er durch den Kanzler vertreten.'),
                                                                                           html.Div(className='abs abs2',
                                                                                                    children =    [    html.H3(children='Zuständige Aufsichtsbehörde'),
                                                                                                                       html.P(children = 'Ministerium für Kultur und Wissenschaft des Landes Nordrhein-Westfalen'),
                                                                                                                       html.P(children = 'Völklinger Straße 49'),
                                                                                                                       html.P(children = '40221 Düsseldorf '),
                                                                                                                       html.P(children = 'T +49.211.896 04 '),
                                                                                                                       html.P(children = 'T +49.211.896 45 55 '),
                                                                                                                       html.P(children = html.A(href='https://www.mkw.nrw', children = 'https://www.mkw.nrw'))
                                                                                                                  ]   
                                                                                                    )
                                                                                     ]
                                                                       )
                                              ),
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
    
    
    
    
    
    
    