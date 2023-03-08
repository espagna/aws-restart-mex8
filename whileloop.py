import random

print("pensaré en un num y lo adivinarás!")
number = random.randint(1,10)

isGuessRight = False

while isGuessRight != True:
    guess = int(input("Adivina un num del 1 al 10: "))
    
    if guess == number:
        print("cool, lo adivinaste!")
        isGuessRight = True
    else:
        print("no era ese, sigue intentando!")

