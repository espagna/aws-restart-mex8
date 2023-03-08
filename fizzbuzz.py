"""
dado un rango de numeros indica fizz cuando el numero impreso sea multiplo de 3, buzz cuando sea de 5, fizzbump cuando sea de ambos

"""

for i in range(1, 51):
    if(i % 3 == 0 and i % 5 == 0):
        print(i, "fizzbuzz")
    elif(i % 3 == 0):
        print(i, "fizz")
    elif(i % 5 == 0):
        print(i, "buzz")
    else:
        print(i)
    #elif(i % 3 == 0 and i % 5 == 0):
        #print("fizzbuzz")
    