def promedio(n1,n2,n3,n4):
    suma=n1+n2+n3+n4
    promedio=suma/4
    return promedio

def situacion(n1,n2,n3,n4):
    prom=promedio(n1,n2,n3,n4)
    if prom <6:
        observacion='BAJO RENDIMIENTO'
    elif prom<10:
        observacion='MALO'
    elif prom<15:
        observacion='RENDIMIENTO REGULAR'
    elif prom<18:
        observacion='RENDIIENTO BUENO'
    else:
        observacion='RENDIMIENTO EXCELENTE'
    return observacion