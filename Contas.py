import requests
import json


class Conta:
    def getContas(self):
        url = 'https://aapi3.autotrac-online.com.br/aticapi/v1/accounts'
        headers = {
            'Ocp-Apim-Subscription-Key': '64aba33b1e084de3bd2bd397b0f7b43d',
            'Authorization': 'Basic administrador@goldbrasil:auto.sup',
        }

        # Lista de Contas
        print("Iniciando Consulta de Conta !!!!! ")
        conta = requests.get(url, headers=headers)
        data = conta.json()
        y = json.dumps(data)
        aList = json.loads(y)
        #print("Conta: "+aList)
        code = y[10:14]
        print("codConta: " + y)
        return code

contas = Conta()

print("Consulta de Conta com SUCESSO: " + contas.getContas())











