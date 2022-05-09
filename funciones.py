print("inicio")
def saludo():
    print("Hola mundo")
    
for i in range(5):
    saludo()

def suma(a, b): #función con parámetros
    resultado = a + b
    print(resultado)
#a= int(input("Digite num1: "))
#b= int(input("Digite num2: "))
#suma(a, b) #función que tiene argumentos
suma(23,90)
suma(15,20)

def resta(a:int,b:int):
    return a-b

print("La resta es:", resta(50,20))

# format
totales = "La resta1 es {} y la resta2 es {}" 
print(totales.format(resta(80,20),resta(40,60))) 
print(totales.format(4,8))

# f-strings
edad = 20
naionalidad = "Colombiana"
print(f"La persona tiene {resta(50,10)} años y es {naionalidad}")
   
