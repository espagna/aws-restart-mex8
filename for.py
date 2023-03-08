students = ["Luis", "Lidia", "Lalo"]

"""
for student in students:
    if student == "Luis":
        print("Chao")
        continue
    print("Hola", student)
    
"""

#rango con un solo argumento va de 0 hasta n, sumando de a 1 salto
#rango con dos args va de n1 a n2, sumando de a 1 salto
#3 argumentos va de n1 a n2 con saltos de a 3
"""
for i in range(10):
    print(i)

for j in range(3,10):
    print(j)

for k in range(3, 10, 3):
    print(k)
"""
    
#numeros pares del 0 al 100
for i in range(2,102,2):
    print(i)

#otra forma    
for i in range(101):
    if(i%2==0):
        print(i)