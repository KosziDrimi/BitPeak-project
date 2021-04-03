# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 14:27:15 2021

@author: klimi
"""


import unittest
import json

from models import Programy, Osie, Dzialania
from funkcje import programs_json


class TestJsonGenerationFromProgramy(unittest.TestCase):
    

    def test_program_data_is_in_json(self):
        
        programy = [Programy(1, 'nazwa programu')]
        result = json.loads(programs_json(programy))
        
        id = result[0]['id']
        name = result[0]['nazwa']
            
        self.assertEqual(id, 1)
        self.assertEqual(name, 'nazwa programu')
        
    def test_os_data_is_in_json(self):
        
        program_1 = Programy(1, 'nazwa programu')
        os_1 = Osie(1, 1, 'pierwsza os')
        os_2 = Osie(1, 2, 'druga os')
        program_1.osie.append(os_1)
        program_1.osie.append(os_2)
        programy = [program_1]
        result = json.loads(programs_json(programy))
        
        id_2 = result[0]['os_list'][1]['id']
        name_1 = result[0]['os_list'][0]['nazwa']
            
        self.assertEqual(id_2, 2)
        self.assertEqual(name_1, 'pierwsza os')
        
    def test_dzialania_data_is_in_json(self):
        
        program_1 = Programy(1, 'nazwa programu')
        os_1 = Osie(1, 1, 'pierwsza os')
        os_2 = Osie(1, 2, 'druga os')
        dzialanie_1 = Dzialania(1, 1, 1, 'dzialanie 1')
        dzialanie_2 = Dzialania(1, 1, 2, 'dzialanie 2')
        dzialanie_3 = Dzialania(1, 2, 3, 'dzialanie 3')
        dzialanie_4 = Dzialania(1, 2, 4, 'dzialanie 4')
        os_1.dzialania.append(dzialanie_1)
        os_1.dzialania.append(dzialanie_2)
        os_2.dzialania.append(dzialanie_3)
        os_2.dzialania.append(dzialanie_4)
        program_1.osie.append(os_1)
        program_1.osie.append(os_2)
        
        programy = [program_1]
        result = json.loads(programs_json(programy))
        
        id_1 = result[0]['os_list'][0]['dzialanie_list'][0]['id']
        name_2 = result[0]['os_list'][0]['dzialanie_list'][1]['nazwa']
        id_3 = result[0]['os_list'][1]['dzialanie_list'][0]['id']
        name_4 = result[0]['os_list'][1]['dzialanie_list'][1]['nazwa']
            
        self.assertEqual(id_1, 1)
        self.assertEqual(name_2, 'dzialanie 2')   
        self.assertEqual(id_3, 3)
        self.assertEqual(name_4, 'dzialanie 4')
        
        
if __name__ == "__main__":
    unittest.main()     



        
        