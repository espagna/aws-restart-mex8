userReply = input("Necesitas entregar un paquete? si o no").capitalize()
if userReply == "Si":
    print("podemos ayudarte con la entrega")
else:
    print("Ni modo, vuelve pronto")
    exit() #funcion pa salir de la ejecucion del programa

userReply = input("Que le gustaria comprar? estampas, sobres, hacer una fotocopia").lower()
if userReply == "stamps":
    print("tenemos muchos diseños")
elif userReply == "sobres":
    print("tenemos muchos sobres")
elif userReply == "copias":
    copias = input("cuantas quiere?")
    print("se sacara el num de copias", copias)