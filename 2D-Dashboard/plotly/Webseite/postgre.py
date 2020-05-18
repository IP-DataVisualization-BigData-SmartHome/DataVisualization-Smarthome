#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 12:53:03 2020

@author: lukas

Host: 81.169.248.223
Username: dev
Passwort: dev
DB-Name: ip_datavisualization

"""

import psycopg2
import pandas as pd
import time
# Connect to the PostgreSQL database

conn = psycopg2.connect(host="81.169.248.223", dbname="ip_datavisualization", user="dev", password="dev")

# Create a new cursor
cur = conn.cursor()

# A function that takes in a PostgreSQL query and outputs a pandas database 
def create_pandas_table(sql_query, data, database = conn):
    table = pd.read_sql_query(sql_query, database, params=data)
    return table

# Utilize the create_pandas_table function to create a Pandas data frame
# Store the data as a variable

day1 = psycopg2.Timestamp(2016, 2, 14, 0,0,0) #2016-02-14 00:00:00
day2 = psycopg2.Timestamp(2016, 4, 3, 0,0,0) #2016-04-03 00:00:00 
data = (day1,day2)
    
query = 'SELECT t1,t2,date FROM "public"."Energyuseage" WHERE date::date >= (%s) AND date::date <= (%s);'
query2 = 'SELECT * FROM "public"."mat_view_avg_all_months";' 
start = time.time()    
result = create_pandas_table(query2, [])
stop = time.time()

print(result)
print("Anweisung dauerte " + str(stop-start) + " Sekunden")

# Close the cursor and connection to so the server can allocate
# bandwidth to other requests
cur.close()
conn.close()