# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 16:19:52 2021

@author: klimi
"""


import json

from funkcje import programs_json, add_filtr, update_filtr
from models import Programy
   
    

if __name__ == "__main__":
    
    
    programy_all = Programy.query.all()
    programy_json = programs_json(programy_all)
    with open('programs.json', 'w') as f:
        f.write(programy_json)
      
    
    with open('filtr1.json', 'r') as file:
        filtr = json.load(file)
    add_filtr(filtr)     
    
        
    with open('filtr3.json', 'r') as file:
        filtr = json.load(file)
    update_filtr(filtr)
    