kms = float(input("ingresa los kms recorridos: "))
combustible = float(input("ingresa el combustible gastado en el recorrido: "))

if kms <= 0 and combustible <= 0:
    print("debes ingresar valores positivos!")
else:
    print("los kms recorridos por litro de combustible son: ", kms/combustible)

"""
kms = input("ingrese los kms recorridos \n")
gas = input("ingrese el consumo de gas \n")

kms = float(kms)
gas = float(gas)

while (kms <= 0) """