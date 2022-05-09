#Realice un programa que lea un numero entero y diga si es mayor o igual a 100
respuesta = "S"
while respuesta == "S":
    numero = int(input("Digite un número entero: "))
    if numero >= 100:
        print("El número es mayor o igual a 100")
    else:
        print("El numero es menor a 100")
    respuesta = input('Presiones "S" para continuar o cualquier tecla para salir \n')
    
