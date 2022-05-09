def CDT(usuario:str,capital:int,tiempo:int):
    Intereses = (capital*0.03*tiempo)/12
    total = capital + Intereses
    return f"Para  el  usuario  {usuario}  La  cantidad  de  dinero  a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es:{total}"

print(CDT("AB1012",1000000,3))

