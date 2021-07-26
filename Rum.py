# Autor: Ricardo Antonello
import requests
import json

veiculos = requests.get('https://maps.googleapis.com/maps/api/distancematrix/json?origins=-22.782307222222222,-47.18768138888889&destinations=Contagem,MG&key=AIzaSyDuUm5AoarbQslI0GK5Q-751SwDNaNJQyM')
data1 = veiculos.json()
autorizados = json.dumps(data1)
veiculos_json = autorizados.replace('[', "").replace(']', "")

aList = json.loads(veiculos_json)
#numeros = json.loads(aList['rows'])

print(aList[''])




