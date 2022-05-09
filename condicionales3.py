#Realice un programa que lea dos numeros a y b y diga si a es mayor que b, o a es menor que b, o si son iguales.
a = int(input("Digite el numero 1: "))
b = int(input("Digite el numero 2: "))
if a > b:
    print(f"{a} es mayor a {b}")
elif a < b:
    print(f"{a} es menor a {b}")
else:
    print(f"{a} es igual a {b}")
    
'''
a == b igualdad
a != b diferente
a < b  menor que
a > b  mayor que
a <= b menor o igual que
a >= b mayor o igual que

'''