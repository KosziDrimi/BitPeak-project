# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 18:14:25 2021

@author: klimi
"""


import json

from dto import DzialanieDTO, OsDTO, ProgramDTO, FTDElementDTO, FTDDTO
from models import db, Programy, Osie, Dzialania, FTD, FTDElementy


def programs_json(programy):
    programy_new = []
    for program in programy:
        programDTO = ProgramDTO(program.id_program, program.nazwa, [])
        programy_new.append(programDTO)
        for os in program.osie:
            osDTO = OsDTO(os.id_os, os.nazwa, [])
            programDTO.os_list.append(osDTO)
            for dzialanie in os.dzialania:
                dzialanieDTO = DzialanieDTO(dzialanie.id_dzl, dzialanie.nazwa)
                osDTO.dzialanie_list.append(dzialanieDTO)

    json_data = json.dumps(programy_new, default=lambda o: o.__dict__, indent=4)
    return json_data 
        

# %%

def add_filtr(filtr):   
    
    new_filtr = FTDDTO(nazwa = filtr['nazwa'], opis = filtr['opis'], 
                      element_list = filtr['element_list'])
    nazwa = new_filtr.nazwa
    opis = new_filtr.opis
        
    filtr_added = FTD(nazwa, opis)
    db.session.add(filtr_added)
    db.session.commit()
    
    elementy_list = []
    for element in new_filtr.element_list:
        new_element = FTDElementDTO(filtr_added.id_ftd, element['id_dzl'])
        elementy_list.append(new_element)
                        
    for element in elementy_list:
        element_added = FTDElementy(element.id_ftd, element.id_dzl) 
        db.session.add(element_added)
        db.session.commit()
    

# %%

def update_filtr(filtr):
    
    filter_id = filtr['id_ftd']
    filter_nazwa = filtr['nazwa']
    filter_opis = filtr['opis']
    elementy = filtr['element_list']
        
    filtr_to_update = FTD.query.filter_by(id_ftd=filter_id).first()  
    filtr_to_update.nazwa = filter_nazwa
    filtr_to_update.opis = filter_opis
    
    for old_item in filtr_to_update.elementy:
        db.session.delete(old_item)
        db.session.commit()
         
    elementy_list = []
    for element in elementy: 
        new_element = FTDElementDTO(filtr_to_update.id_ftd, element['id_dzl'])
        elementy_list.append(new_element)
       
    for element in elementy_list:
        element_added = FTDElementy(element.id_ftd, element.id_dzl) 
        db.session.add(element_added)
   
    db.session.commit()
   


