
def printDatos (c1,c2,c3,c4):
    nota1=float(input('ingrese nota de '+c1+" : "))
    nota2=float(input('ingrese nota de '+c2+" : "))
    nota3=float(input('ingrese nota de '+c3+" : "))
    nota4=float(input('ingrese nota de '+c4+" : "))
    imprimir='=============================================='+"\n"
    imprimir+="CURSO 1 "+c1+" tiene nota: "+str(nota1)+"\n"
    imprimir+="CURSO 2 "+c2+" tiene nota: "+str(nota2)+"\n"
    imprimir+="CURSO 3 "+c3+" tiene nota: "+str(nota3)+"\n"
    imprimir+="CURSO 4 "+c4+" tiene nota: "+str(nota4)+"\n"
    promedio=notas(nota1,nota2,nota3,nota4)
    imprimir+="El promedio del estudiante es: "+str(promedio)+"\n"
    if promedio <6:
        observacion='bajo rendimiento'
    elif promedio<10:
        observacion='malo'
    elif promedio<15:
        observacion='rendimiento Regular'
    elif promedio<18:
        observacion='rendimiento Bueno'
    else:
        observacion='Rendimiento excelente'
    imprimir+='OBSERVACION DEL ALUMNO ES: '+observacion

    print(imprimir)

def notas (n1,n2,n3,n4):
    promedio=(n1+n2+n3+n4)/4
    return promedio

def datos ():
    codigo=input('Ingrese su codigo: ')
    nombre = input('Ingrese nombre del alumno: ')
    apellidos= input('Ingrese sus apellidos: ')
    ciclo=int(input('Ingrese su ciclo \n1.-I\n2.-II\n3.-III\n4.-IV\n5.-V\n6.-VI\n'))
    
    if ciclo==1 or ciclo==2 or ciclo==3 or ciclo==4 or ciclo==5 or ciclo==6:
        if ciclo==1:
            printDatos('WINDOWS','WORD','EXCEL','ACCES')
        elif ciclo==2:
            printDatos('Power Point','Internet','Extranet','Acces')
        elif ciclo==3:
            printDatos('Visual Basic 6.0','.net 2019-I','SQL-I','Analisis -I')
        elif ciclo==4:
            printDatos('Java I','.net 2019-II','SQL-II','Analisis -II')
        elif ciclo==5:
            printDatos('Java II','Asp .net 2019-II','Oracle-I','Proyectos')
        else:
            printDatos('Java III','Linux','Php','Sistemas')
    
    else:
        print ('Ciclo no valido')

datos ()