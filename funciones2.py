def operacion(a:int,b:int,c:str):
    if c=="+":
        return a+b
    else:
        if c=="-":
            return a-b
        else:
            return f"Digite + o -, como operador"
        
def operacion2(a:int,b:int,c:str):
    if c=="+":
        resultado = a+b
    else:
        resultado = a-b
    return resultado
        
print(operacion(5,6,"*"))
print(operacion(9,3,"-"))
print(operacion2(5,6,"+"))
print(operacion2(9,3,"-"))