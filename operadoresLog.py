#Realizar un programa que indique si una persona debe presentar 
#la declacion de renta. Las condiciones para presentar este impuesto son:
#Ser mayor de edad y
#Tener ingresos anuales superiores o iguales a $50.831.000
edad = int(input("Digite su edad: \n")) #es un salto de línea 
ingresos = int(input("Digite sus ingresos anuales sin puntos ni comas: \n"))
if edad >= 18 and ingresos >= 50831000:
    print("Usted debe presentar la declaración de renta")
else:
    print("Usted no debe presentar la declaración de renta")
    