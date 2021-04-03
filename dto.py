# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 18:11:04 2021

@author: klimi
"""


from typing import List
  

class DzialanieDTO():
    
    def __init__(self, id, nazwa):
        self.id = id
        self.nazwa = nazwa
  
  
class OsDTO():
    
    def __init__(self, id, nazwa, dzialanie_list: List[DzialanieDTO]):
        self.id = id
        self.nazwa = nazwa
        self.dzialanie_list = dzialanie_list
  
  
class ProgramDTO():
   
    def __init__(self, id, nazwa, os_list: List[OsDTO]):
        self.id = id
        self.nazwa = nazwa
        self.os_list = os_list

    
class FTDElementDTO():
    
    def __init__(self, id_ftd, id_dzl):
      
        self.id_ftd = id_ftd
        self.id_dzl = id_dzl  
        
  
class FTDDTO():
    
    def __init__(self, nazwa, opis, element_list: List[FTDElementDTO]):
      
        self.nazwa = nazwa
        self.opis = opis
        self.element_list = element_list


