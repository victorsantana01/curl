import requests
import json
#https://aapi.autotrac-online.com.br/aticapi/v1/accounts

headers = {
    'Ocp-Apim-Subscription-Key': '64aba33b1e084de3bd2bd397b0f7b43d',
    'Authorization': 'Basic administrador@goldbrasil:auto.sup',
}

#Lista de Contas
print('====== Bloco: Listar Contas ======')
conta = requests.get('https://aapi3.autotrac-online.com.br/aticapi/v1/accounts/', headers=headers)
data = conta.json()
y = json.dumps(data)
aList = json.loads(y)
print("Contas")
for i in aList:
    print(i)
code = y[10:14]
#print("codConta: "+code)


#Lista veiculos ativos
print('\n====== Bloco: Listar Veiculos Ativos ======')
veiculos = requests.get('https://aapi3.autotrac-online.com.br/aticapi/v1/accounts/'+code+'/vehicles?_limit=500', headers=headers)
data = veiculos.json()
v = json.dumps(data)
veiculos_json = v.replace('{"Data": ', "").replace(', "Limit": 500, "Offset": 1, "IsLastPage": false}', "")
aList = json.loads(veiculos_json)
for i in aList:
    print(i)
#print(len(aList))
#veiculos = requests.get('https://aapi.autotrac-online.com.br/aticapi/v1/accounts/6064/vehicles/833622/positions', headers=headers)




#Lista Veiculos autorizados
print('\n====== Bloco: Veiculos autorizados ======')
veiculosAutorizados = requests.get('https://aapi3.autotrac-online.com.br/aticapi/v1/accounts/'+code+'/authorizedvehicles', headers=headers)
data1 = veiculos.json()
autorizados = json.dumps(data1)
veiculos_json = autorizados.replace('{"Data": ', "").replace(', "Limit": 500, "Offset": 1, "IsLastPage": false}', "")
#print(veiculos_json)
aList = json.loads(veiculos_json)
for i in aList:
    print(i)
print(len(aList))


#POSITIONS
print('\n====== Bloco: Listar Posições ======')
veiculos = requests.get('https://aapi3.autotrac-online.com.br/aticapi/v1/accounts/6064/vehicles/844616/positions?_limit=10',headers=headers)
data1 = veiculos.json()
autorizados = json.dumps(data1)
veiculos_json = autorizados.replace('{"Data": ', "").replace(', "Limit": 10, "Offset": 0, "IsLastPage": false}', "")
aList = json.loads(veiculos_json)
for i in aList:
    placa = i['VehicleName']
    ignicao = i['VehicleIgnition']
    if ignicao == 1:
        ignicao = "On"
    else:
        ignicao = "Off"

    odometro = i['Odometer']
    odometro = str(odometro)
    hora = i['PositionTime']
    hora = str(hora)
    hora = hora.replace("T", " ").replace("+", ":")
    print(placa + '| Ignição: ' + ignicao + '| Odometro: ' + odometro + '| Horario: ' + hora)
    # print("Placa: "+placa+" Ignicao: "+ignicao+" Odometro: "+odometro+" Horario: "+hora)
#print(len(aList))



