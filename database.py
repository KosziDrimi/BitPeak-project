# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 15:31:17 2021

@author: klimi
"""


from pathlib import Path
import sqlite3
import pandas as pd



Path('bitpeak.db').touch()


conn = sqlite3.connect('bitpeak.db')
c = conn.cursor()


c.execute('''CREATE TABLE programy (ID_PROGRAM INTEGER PRIMARY KEY, NAZWA TEXT)''')
c.execute('''CREATE TABLE osie (ID_PROGRAM INTEGER, ID_OS INTEGER PRIMARY KEY, 
          NAZWA TEXT, FOREIGN KEY(ID_PROGRAM) REFERENCES programy(ID_PROGRAM))''')
c.execute('''CREATE TABLE dzialania (ID_PROGRAM INTEGER, ID_OS INTEGER, 
          ID_DZL INTEGER PRIMARY KEY, NAZWA TEXT, FOREIGN KEY(ID_OS) 
          REFERENCES osie(ID_OS))''')

c.execute('''CREATE TABLE ftd (ID_FTD INTEGER PRIMARY KEY AUTOINCREMENT, 
          NAZWA TEXT, OPIS TEXT)''')
c.execute('''CREATE TABLE ftdelementy (ID_FTD_ELEMENT INTEGER PRIMARY KEY 
          AUTOINCREMENT, ID_FTD INTEGER, ID_DZL INTEGER, FOREIGN KEY(ID_FTD) 
          REFERENCES ftd(ID_FTD), FOREIGN KEY(ID_DZL) REFERENCES dzialania(ID_DZL))''')     


programy = pd.read_csv('programy.csv')
programy.to_sql('programy', conn, if_exists='append', index = False)

osie = pd.read_csv('osie.csv')
osie.to_sql('osie', conn, if_exists='append', index = False)

dzialania = pd.read_csv('dzialania.csv')
dzialania.to_sql('dzialania', conn, if_exists='append', index = False)
