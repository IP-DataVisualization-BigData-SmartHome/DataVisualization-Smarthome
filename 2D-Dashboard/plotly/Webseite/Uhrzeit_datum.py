# -*- coding: utf-8 -*-
"""
Created on Wed May 27 16:44:24 2020

@author: Mues
"""
from datetime import datetime as dt2
import psycopg2
from postgre import postgre_connector, pd

class Uhrzeit_datum:
    uhrzeit = None
    datum = None
    
    def __init__(self):
        self.aktuelleUhrzeit()

    def aktuelleUhrzeit(self):
        aktuelleUhrzeit = dt2.now()

        aktuelle_stunde = aktuelleUhrzeit.hour
        aktuelle_minute = aktuelleUhrzeit.minute
        
        DB_connector = postgre_connector()
        
        letzter_eintrag = DB_connector.get_last_date()
        letzter_eintrag_timestamp = letzter_eintrag['datum'][0]
        
        while True:
            day1 = [letzter_eintrag_timestamp.year,letzter_eintrag_timestamp.month,letzter_eintrag_timestamp.day, aktuelle_stunde, aktuelle_minute]
            day2 = [letzter_eintrag_timestamp.year,letzter_eintrag_timestamp.month,letzter_eintrag_timestamp.day, aktuelle_stunde, aktuelle_minute]
            result = DB_connector.get_data(day1, day2, 'a', ['t1'])
            print(result)
            
            if result['datum'].count() == 0:
                aktuelle_minute += 1
                if(aktuelle_minute == 60):
                    aktuelle_minute = 0
                    if(aktuelle_stunde <23):
                        aktuelle_stunde += 1
                    else:
                        aktuelle_stunde = 0
                print(aktuelle_minute)
                
            else:
                print(aktuelle_minute)
                break
        
        if(aktuelle_minute < 10 and aktuelle_stunde < 10):
            self.uhrzeit = ['0' + str(aktuelle_stunde), '0' + str(aktuelle_minute)]
            self.datum = [str(letzter_eintrag_timestamp.year), str(letzter_eintrag_timestamp.month), str(letzter_eintrag_timestamp.day)]
        
        elif (aktuelle_minute < 10):
            self.uhrzeit = [str(aktuelle_stunde), '0' + str(aktuelle_minute)]
            self.datum = [str(letzter_eintrag_timestamp.year), str(letzter_eintrag_timestamp.month), str(letzter_eintrag_timestamp.day)]
            
        elif (aktuelle_stunde < 10):
            self.uhrzeit = ['0' + str(aktuelle_stunde), str(aktuelle_minute)]
            self.datum = [str(letzter_eintrag_timestamp.year), str(letzter_eintrag_timestamp.month), str(letzter_eintrag_timestamp.day)]
        else:
            self.uhrzeit = [str(aktuelle_stunde), str(aktuelle_minute)]
            self.datum = [str(letzter_eintrag_timestamp.year), str(letzter_eintrag_timestamp.month), str(letzter_eintrag_timestamp.day)]