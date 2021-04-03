# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 14:20:18 2021

@author: klimi
"""


from flask import request, jsonify
from flask_api import status
import logging

from funkcje import programs_json, add_filtr, update_filtr
from models import app, Programy
    


if __name__ == "__main__":
    logging.basicConfig(filename='web_api.log', level=logging.DEBUG)

    
    @app.route('/api/v1/programs')
    def programs():
        logging.info('ładowanie programów')
        try:
            programy_all = Programy.query.all()
        except:
            logging.error('błąd odczytu z bazy')
            return jsonify({'result': False, 'description': 'błąd odczytu z bazy'}), status.HTTP_500_INTERNAL_SERVER_ERROR
        try:
            programy_json = programs_json(programy_all)
        except:
            logging.error('błąd generowania json')
            return jsonify({'result': False, 'description': 'błąd generowania json'}), status.HTTP_500_INTERNAL_SERVER_ERROR
        return programy_json

    
    @app.route('/api/v1/add_filtr', methods = ['POST'])
    def add():
        logging.info('dodawanie filtru')
        try:
            new_filtr = request.get_json()
        except:
            logging.error('niepoprawny json')
            return jsonify({'result': False, 'description': 'niepoprawny json'}), status.HTTP_400_BAD_REQUEST
        try:
            add_filtr(new_filtr) 
        except:
            logging.error('błąd zapisu do bazy')
            return jsonify({'result': False, 'description': 'błąd zapisu do bazy'}), status.HTTP_500_INTERNAL_SERVER_ERROR
        return jsonify({'result': True})

        
    @app.route('/api/v1/update_filtr', methods = ['PUT'])
    def update():
        logging.info('aktualizowanie filtru')
        try:
            updated_filtr = request.get_json()
        except:
            logging.error('niepoprawny json')
            return jsonify({'result': False, 'description': 'niepoprawny json'}), status.HTTP_400_BAD_REQUEST
        try:
            update_filtr(updated_filtr) 
        except:
            logging.error('błąd zapisu do bazy')
            return jsonify({'result': False, 'description': 'błąd zapisu do bazy'}), status.HTTP_500_INTERNAL_SERVER_ERRO
        return jsonify({'result': True})

        
    app.run(debug=True)