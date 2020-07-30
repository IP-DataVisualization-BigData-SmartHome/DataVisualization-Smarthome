#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Lukas Schnittcher

Die Klasse repräsentiert die Schnittstelle zu der Datenbank

"""

import psycopg2
import pandas as pd
import datetime as dt
# Connect to the PostgreSQL database

class postgre_connector:
    
    #Initialisierung der Schnittstelle mit entsprechenden Server-Login
    def __init__(self):
        self.__host = '81.169.248.223'
        self.__dbname = 'ip_datavisualization'
        self.__user = 'dev'
        self.__password = 'dev'
        self.__connection = None
    
    #Verbindung zur Datenbank wird aufgebaut
    def connect(self):
        self.__connection = psycopg2.connect(host = self.__host, dbname = self.__dbname, user = self.__user, password = self.__password)
    
    #Verbindung der Datenbank wird geschlossen
    def close(self):
        if self.__connection != None:
            self.__connection.close()
        return
   
    #Berechnet das Zeitintervall zwischen 2 Messungen 
    def get_time_intervall(self):
        self.connect()
        query = 'SELECT datum FROM public.mat_view_all_data ORDER BY datum ASC LIMIT 2;'
        dataframe = self.create_pandas_table(query, [])
        return (dataframe['datum'][1] - dataframe['datum'][0]).total_seconds()/60
    
    #Gibt das erste Datum im Datensatz zurück, welches Smart-Home Daten enthält
    def get_first_date(self):
        self.connect()
        query = 'SELECT datum FROM public.mat_view_all_data ORDER BY datum ASC LIMIT 1;'
        dataframe = self.create_pandas_table(query, [])
        self.close()
        return dataframe
    
    #Gibt das letzte Datum im Datensatz zurück, welches Smart-Home Daten enthält
    def get_last_date(self):
        self.connect()
        query = 'SELECT datum FROM public.mat_view_all_data ORDER BY datum DESC LIMIT 1;'
        dataframe = self.create_pandas_table(query, [])
        self.close()
        return dataframe
     
    #Erzeugt aus SQL-Query ein Ergebnis und wandelt dieses in ein Pandas-DataFrame Objekt
    def create_pandas_table(self, sql_query, data):
        table = pd.read_sql_query(sql_query, self.__connection, params=data)
        return table
    
        """
        Data-Format day = [(int)Jahr, int(monat), int(day)] oder day1 und day2 sind datetime-Objekte
        Data-Format coloumns = ['t1', 'rh1', ...]
        Data-Format mode = { 'd' : tag, 'm' : Monat, 'h : stündlich, 'a' : Alle Daten'}
        """
    #Allgemeine Abfrage-Methode für die Daten, Argumente sind Start-/Enddatum, Zeitíntervall und Datenauswahl    
    def get_data(self, day1, day2, mode = 'd', coloums = ['t1']):
        
        if coloums == []:
            coloums = ['*']
        else:
            coloums = ['datum'] + coloums
        
        self.connect()
        if(type(day1) != dt.datetime and type(day2) != dt.datetime):
            start_day = dt.datetime(day1[0], day1[1], day1[2], day1[3], day1[4], 0)
            end_day = dt.datetime(day2[0], day2[1], day2[2], day2[3], day2[4], 0)
        else:
            start_day = day1
            end_day = day2
                
        query = 'SELECT '
        
        
        for col in coloums:
            query += col + ','
        
        query = query[:-1:] # Delete last ',' from Query
        
        
        if mode == 'a':
            #Grunddaten
            query += ' FROM public.mat_view_all_data WHERE datum >= %s AND datum <= %s ORDER BY datum ASC;'
            dataframe = self.create_pandas_table(query, [start_day, end_day])
        
        elif mode == 'h':
            #stunde
            query += ' FROM public.mat_view_avg_all_hour WHERE datum >= %s AND datum <= %s ORDER BY datum ASC;'
            dataframe = self.create_pandas_table(query, [start_day, end_day])
            
        elif mode == 'd':
            #mtag
            query += ' FROM public.mat_view_avg_all_days WHERE datum >= %s AND datum <= %s ORDER BY datum ASC;'
            dataframe = self.create_pandas_table(query, [start_day, end_day])
            
        elif mode == 'm':
            #month: Table: mat_view_avg_all_months
            query += ' FROM public.mat_view_avg_all_months WHERE EXTRACT("month" from datum) >= %s AND EXTRACT ("month" from datum) <= %s ORDER BY datum ASC;'
            dataframe = self.create_pandas_table(query, [start_day.month, end_day.month])
        self.close()
        return dataframe
    
    #Methode mit der theoretisch weitere Daten der Datenbank hinzugefügt werden können
    def add_data(self, data):
        # Einfüge-Funktion um den Datensatz zu erweitern
        pass
