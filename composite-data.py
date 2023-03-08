#para importar un modulo uso import + nombre de modulo
#puedo usar un alias: importacion + as + alias

# ejemplo: import csv as c

import csv #csv sirve pa manejo de archivos de formato csv 
import copy #Hacer copias de colecciones

#Definiendo un diccionario
myVehicle = {
    "vin": "<empty>",
    "make": "<empty>",
    "model": "<empty>",
    "year": 0,
    "range":0,
    "topSpeed":0,
    "zeroSixty": 0.0,
    "mileage": 0
}

#print(myVehicle.values())

for key, value in myVehicle.items():
    print(key, value) #al colocar coma se separan
    
#lista de diccionarios que se declara vacia
myInventoryList = []


#manejo de archivos 
#que archivo abrir, como lo abro, que codificacion tiene, etc
#default el modo de abrirlo es de lectura
with open('car-fleet.csv') as csvFile:
    #Hago lectura del csv
    csvReader = csv.reader(csvFile, delimiter=',')
    
    lineCount = 0
    
    for row in csvReader:
        if lineCount == 0:
            print(f"las columnas son: {', '.join(row)}\n)
        else:
            lineCount += 1