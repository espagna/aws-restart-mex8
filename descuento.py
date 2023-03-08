precio = float(input("ingresa el precio original de tu producto: "))

if precio <= 0:
    print("ingresa valores positivos!")
else:
    print("el precio mas el descuento agregado es de: ", (precio - precio * 0.15))

