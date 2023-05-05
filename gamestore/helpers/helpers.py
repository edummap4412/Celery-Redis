import json

import requests
import subprocess

def my_requests():
    data = {'username': 'eduardo', 'password': '123'}
    json_data = json.dumps(data)

    # Execute o comando 'curl' com as opções desejadas
    output = subprocess.check_output(['curl', '-X', 'POST', '-H', 'Content-Type:application/json', '-d', json_data,
                                      'http://127.0.0.1:8000/api/token/'])

    # Faça algo com a saída retornada pelo comando curl
    return output
