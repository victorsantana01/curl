from cgitb import reset

import requests
import json

from urllib3.util import timeout

#from Contas import Conta
import mysql.connector
#import schedule
import time
from sys import exit
import asyncio
url = 'https://aapi3.autotrac-online.com.br/aticapi/v1/accounts'
class Coletas:
    
    def getVeiculos(self):
        #contas = Conta()
        headers = {
            'Ocp-Apim-Subscription-Key': '64aba33b1e084de3bd2bd397b0f7b43d',
            'Authorization': 'Basic administrador@goldbrasil:auto.sup',
        }
        # Lista veiculos ativos
        try:
            print("Iniciando Consulta Veiculo .............. ")
            veiculos = requests.get('https://aapi3.autotrac-online.com.br/aticapi/v1/accounts/6064/vehicles?_limit=500',
            headers=headers, timeout = 5)

            data = veiculos.json()
            v = json.dumps(data)
            tags = ['{"Data": ', ', "Limit": 500, ', ' "Offset": 1, ', ' "IsLastPage": ', 'false}']
            veiculos_json = v.replace('{"Data": ', "").replace(', "Limit": 500, "Offset": 1, "IsLastPage": false}', "")
            # veiculos_json = v.replace(tags, "")
            aList = json.loads(veiculos_json)
            print(aList)

            for i in aList:
                code = i['Code']
            print("\nConsulta Veiculos Ativos Realizada COM SUCESSO!!!!! \n")
        except:
            print('Tempo Esgotado para Consulta Ativos: ')
            aList = ""

        return aList

    def getPosition(self,code):

        #contas = Conta()
        headers = {
            'Ocp-Apim-Subscription-Key': '64aba33b1e084de3bd2bd397b0f7b43d',
            'Authorization': 'Basic administrador@goldbrasil:auto.sup',
        }
        # POSITIONS
        try:
            print("Iniciando Consulta position ......... ")
            veiculos = requests.get('https://aapi3.autotrac-online.com.br/aticapi/v1/accounts/6064/vehicles/'+ code + '/positions?_limit=200',headers=headers, timeout=5)

            data1 = veiculos.json()
            autorizados = json.dumps(data1)
            #print("======================== "+autorizados)
            tags = [', "Limit": 200, "Offset": 0, "IsLastPage": true}']
            veiculos_json = autorizados.replace('{"Data": ', "").replace(
                ', "Limit": 200, ', "").replace('"Offset": 0, "IsLastPage": true}', "").replace(
                '"Offset": 0, "IsLastPage": false}', "")
            # veiculos_json = autorizados.replace(tags, "")
            aList = json.loads(veiculos_json)
            for i in aList:
                placa = i['VehicleName']
                ignicao = i['VehicleIgnition']
                if ignicao == 1:
                    ignicao = "On"
                else:
                    ignicao = "Off"
                referencia = i['Landmark']
                equipamento = i['VehicleAddress']
                odometro = i['Odometer']
                odometro = str(odometro)
                hora = i['PositionTime']
                hora = str(hora)
                hora = hora.replace("T", " ").replace("+", ":")
                #print(placa + '| Ignição: ' + ignicao + '| Odometro: ' + odometro + '| Horario: ' + hora)
            print("Consulta de position com SUCESSO PLACA: "+placa)


        except:
            print('Tempo Esgotado para busca do Codigo: ' + code)
            aList = ""

        return aList




    def coleta(self,code):
        for i in colet.getPosition(code):

            placa = i['VehicleName']
            ignicao = i['VehicleIgnition']
            if ignicao == 1:
                ignicao = "On"
            else:
                ignicao = "Off"

            odometro = i['Odometer']
            if odometro == "None":
                odometro = "0"
            odometro = str(odometro)
            hora = i['PositionTime']
            hora = str(hora)
            hora = hora.replace("T", " ").replace("+", ":")
            referencia = i['Landmark']
            referencia = referencia.replace("'","")
            equipamento = i['VehicleAddress']
            distancia = str(i['Distance'])
            latitude = str(i['Latitude'])
            longitude = str(i['Longitude'])
            connection = mysql.connector.connect(
                host='localhost', user='root', password='auto.sup', database='autotrac_bd', charset='utf8')
            cursor = connection.cursor(dictionary=True)

            print(placa + '| Ignição: ' + ignicao + '| Odometro: ' + odometro + '| Horario: ' + hora+ '| referencia: ' + referencia+ '| Equipamento: ' + equipamento+ '| lat: ' + latitude+ '| Long: ' + longitude)
            cursor.execute("INSERT IGNORE INTO `autotrac_bd`.`position` (`placa`, `equipamento`, `odomentro`, `ignicao`,`position_time`, `referencia`, `latitude`,`longitude`,`distancia`) VALUES ('"+placa+"', '"+equipamento+"', '"+odometro+"', '"+ignicao+"', '"+hora+"', '"+referencia+"', '"+latitude+"', '"+longitude+"', '"+distancia+"')")
            connection.commit()

colet = Coletas()
def rodar():

    for i in colet.getVeiculos():
        code = str(i['Code'])
        colet.coleta(code)
        print("\n")

def  contador():
    async def main(timeout=1):
        # Abre um loop de duração indeterminada...
        while True:

            tarefa = asyncio.create_task(rodar())
            print('Fazendo uma tentativa...')
            # Abre um bloco de tratamento de exceções...
            try:
                await asyncio.wait_for(tarefa, timeout)
            except asyncio.TimeoutError:
                tarefa.cancel()
                print('Time out...')
            else:
                return tarefa.result()

    asyncio.run(main(4))
i = 1
while 1:

    print("============================  BUSCA DE NUMERO: " + str(i) + "  ====================================")
    rodar()
    i += 1












