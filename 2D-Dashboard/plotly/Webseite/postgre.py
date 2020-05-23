#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: lukas
"""

import psycopg2
import pandas as pd
import datetime as dt
# Connect to the PostgreSQL database

class postgre_connector:
    
    def __init__(self):
        self.__host = '81.169.248.223'
        self.__dbname = 'ip_datavisualization'
        self.__user = 'dev'
        self.__password = 'dev'
        self.__connection = None
    
    def connect(self):
        self.__connection = psycopg2.connect(host = self.__host, dbname = self.__dbname, user = self.__user, password = self.__password)
        
    def close(self):
        if self.__connection != None:
            self.__connection.close()
        return
    
    def get_first_date(self):
        self.connect()
        query = 'SELECT date FROM "public"."energyusage" ORDER BY DATE ASC LIMIT 1;'
        dataframe = self.create_pandas_table(query, [])
        self.close()
        return dataframe
    
    def get_last_date(self):
        self.connect()
        query = 'SELECT date FROM "public"."energyusage" ORDER BY DATE DESC LIMIT 1;'
        dataframe = self.create_pandas_table(query, [])
        self.close()
        return dataframe
        
    def create_pandas_table(self, sql_query, data):
        table = pd.read_sql_query(sql_query, self.__connection, params=data)
        return table
    
        """
        Data-Format day = [(int)Jahr, int(monat), int(day)]
        Data-Format coloumns = ['t1', 'rh1', ...]
        """
    def get_data(self, day1, day2, mode = 'd', coloums = ['t1']):
        
        coloums = ['date'] + coloums
        
        self.connect()
        
        start_day = dt.datetime(day1[0], day1[1], day1[2], day1[3], day1[4], 0)
        end_day = dt.datetime(day2[0], day2[1], day2[2], day2[3], day2[4], 0)
        
        print(start_day)
        print(end_day)
        
        query = 'SELECT '
        
        for col in coloums:
            query += col + ','
        
        query = query[:-1:] # Delete last ',' from Query
        
        if mode == 'a':
            #Grunddaten
            query += ' FROM "public"."energyusage" WHERE date >= (%s) AND date <= (%s);'
            dataframe = self.create_pandas_table(query, [start_day, end_day])
        
        elif mode == 'h':
            #stunde
            query += ' FROM "public"."mat_view_avg_all_hour" WHERE date >= (%s) AND date <= (%s);'
            dataframe = self.create_pandas_table(query, [start_day, end_day])
            
        elif mode == 'd':
            #mtag
            query += ' FROM "public"."mat_view_avg_all_days" WHERE date >= (%s) AND date <= (%s);'
            dataframe = self.create_pandas_table(query, [start_day, end_day])
            
        elif mode == 'm':
            #month: Table: mat_view_avg_all_months
            query += ' FROM "public"."mat_view_avg_all_months" WHERE date >= (%s) AND date <= (%s);'
            dataframe = self.create_pandas_table(query, [start_day, end_day])
        
        self.close()
        return dataframe
    
    def add_data(self, data):
        # Einfüge-Funktion um den Datensatz zu erweitern
        pass


DB_connector = postgre_connector()
day1 = [2016,4,12,3,30]
day2 = [2016,4,16,8,30]
result = DB_connector.get_data(day1, day2, 'd', ['t1, t2, rh_1'])
#result = DB_connector.get_first_date()
print(result)

    