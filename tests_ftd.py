# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 14:59:21 2021

@author: klimi
"""


import unittest
import json

from models import FTD
from funkcje import add_filtr, update_filtr


class TestAddingFilter(unittest.TestCase):
    

    def test_ftd_is_added(self):
        
        with open('filtr1.json', 'r') as file:
            filtr = json.load(file)
        add_filtr(filtr) 
        last = FTD.query.order_by(FTD.id_ftd.asc()).all()[-1]
        
        self.assertEqual(last.nazwa, 'nazwa 1')
        self.assertEqual(last.opis, 'opis 11') 
   
    def test_ftd_elements_are_correct(self):
        
        with open('filtr2.json', 'r') as file:
            filtr = json.load(file)
        add_filtr(filtr) 
        last = FTD.query.order_by(FTD.id_ftd.asc()).all()[-1]
        elements = []
        for element in last.elementy:
            elements.append(element)
        
        self.assertEqual(len(elements), 3)
        self.assertEqual(elements[2].id_dzl, 4760)   


class TestUpdatingFilter(unittest.TestCase):
    

    def test_ftd_is_updated(self):
        
        with open('filtr3.json', 'r') as file:
            filtr = json.load(file)
        update_filtr(filtr) 
        updated = FTD.query.filter_by(id_ftd=filtr['id_ftd']).first()
        
        self.assertEqual(updated.nazwa, 'nazwa sto')
        self.assertEqual(updated.opis, 'opis trzy') 
   
    def test_ftd_elements_are_updated(self):
        
        with open('filtr4.json', 'r') as file:
            filtr = json.load(file)
        update_filtr(filtr) 
        updated = FTD.query.filter_by(id_ftd=filtr['id_ftd']).first()
        
        elements = []
        for element in updated.elementy:
            elements.append(element)
        
        self.assertEqual(len(elements), 2)
        self.assertEqual(elements[1].id_dzl, 4755) 
      
        
if __name__ == "__main__":
    unittest.main()             