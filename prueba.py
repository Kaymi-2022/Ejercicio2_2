import sys
from PyQt6.QtWidgets import QMainWindow,QApplication,QDialog
from PyQt6 import uic
import metodo as operar


class Ejemplo01(QMainWindow):
    dato=""
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("Principal.ui",self)
        self.b_borrar.clicked.connect(self.reset)
        self.b_salir.clicked.connect(self.exit)
        self.b_ciclo1.clicked.connect(self.ciclo1)
        self.b_ciclo2.clicked.connect(self.ciclo2)
        self.b_ciclo3.clicked.connect(self.ciclo3)
        self.b_ciclo4.clicked.connect(self.ciclo4)
        self.b_ciclo5.clicked.connect(self.ciclo5)
        self.b_ciclo6.clicked.connect(self.ciclo6)

    def dato(self):
        nombre=self.txt_nombres.text()
        apellido=self.txt_apellidos.text()
        dato=nombre+apellido



    def reset(self):
        self.txt_codigo.setText("")
        self.txt_apellidos.setText("")
        self.txt_nombres.setText("")
    
    def exit(self):
        self.close()
        
    
    def ciclo1(self):
        self.seg1=Ventana1()
        self.close()
        self.seg1.show()
    
    def ciclo2(self):
        self.seg1=Ventana2()
        self.close()
        self.seg1.show()
    
    def ciclo3(self):
        self.seg1=Ventana3()
        self.close()
        self.seg1.show()
    
    def ciclo4(self):
        self.seg1=Ventana4()
        self.close()
        self.seg1.show()

    def ciclo5(self):
        self.seg1=Ventana5()
        self.close()
        self.seg1.show()

    def ciclo6(self):
        self.seg1=Ventana6()
        self.close()
        self.seg1.show()


class Ventana1(QDialog):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("seg1.ui",self)
        self.b_calcular.clicked.connect(self.calcular)
        self.b_salir.clicked.connect(self.salir)
        self.lb_curso1.setText("WINDOWS")
        self.lb_curso2.setText("WORD")
        self.lb_curso3.setText("EXCEL")
        self.lb_curso4.setText("ACCES")
    super.__class__
    
    def salir(self):
        self.close()

    def calcular(self):
        n1=float(self.txt_nota1.text())
        n2=float(self.txt_nota2.text())
        n3=float(self.txt_nota3.text())
        n4=float(self.txt_nota4.text())
        self.lb_alumno.setText(Ejemplo01.dato(self))
        self.lb_promedio.setText(str(round(operar.promedio(n1,n2,n3,n4),2)))
        self.lb_observacion.setText(operar.situacion(n1,n2,n3,n4))

class Ventana2(QDialog):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("seg1.ui",self)
        self.b_calcular.clicked.connect(self.calcular)
        self.b_salir.clicked.connect(self.salir)
        self.lb_curso1.setText("POWER POINT")
        self.lb_curso2.setText("INTERNET")
        self.lb_curso3.setText("EXTRANET")
        self.lb_curso4.setText("ACCESS")

    def salir(self):
        self.close()

    def calcular(self):
        n1=float(self.txt_nota1.text())
        n2=float(self.txt_nota2.text())
        n3=float(self.txt_nota3.text())
        n4=float(self.txt_nota4.text())
        self.lb_promedio.setText(str(round(operar.promedio(n1,n2,n3,n4),2)))
        self.lb_observacion.setText(operar.situacion(n1,n2,n3,n4))

class Ventana3(QDialog):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("seg1.ui",self)
        self.b_calcular.clicked.connect(self.calcular)
        self.b_salir.clicked.connect(self.salir)
        self.lb_curso1.setText("VISUAL BASIC 6.0")
        self.lb_curso2.setText(".net 2019-I")
        self.lb_curso3.setText("SQL-I")
        self.lb_curso4.setText("Analisis -I")
        
    def salir(self):
        self.close()

    def calcular(self):
        n1=float(self.txt_nota1.text())
        n2=float(self.txt_nota2.text())
        n3=float(self.txt_nota3.text())
        n4=float(self.txt_nota4.text())
        self.lb_promedio.setText(str(round(operar.promedio(n1,n2,n3,n4),2)))
        self.lb_observacion.setText(operar.situacion(n1,n2,n3,n4))

class Ventana4(QDialog):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("seg1.ui",self)
        self.b_calcular.clicked.connect(self.calcular)
        self.b_salir.clicked.connect(self.salir)
        self.lb_curso1.setText("Java I")
        self.lb_curso2.setText(".net 2019-II")
        self.lb_curso3.setText("SQL-II")
        self.lb_curso4.setText("Analisis -II")
        
    def salir(self):
        self.close()

    def calcular(self):
        n1=float(self.txt_nota1.text())
        n2=float(self.txt_nota2.text())
        n3=float(self.txt_nota3.text())
        n4=float(self.txt_nota4.text())
        self.lb_promedio.setText(str(round(operar.promedio(n1,n2,n3,n4),2)))
        self.lb_observacion.setText(operar.situacion(n1,n2,n3,n4))

class Ventana5(QDialog):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("seg1.ui",self)
        self.b_calcular.clicked.connect(self.calcular)
        self.b_salir.clicked.connect(self.salir)
        self.lb_curso1.setText("Java II")
        self.lb_curso2.setText("Asp .net 2019-II")
        self.lb_curso3.setText("Oracle-I")
        self.lb_curso4.setText("Proyectos")
        
    def salir(self):
        self.close()

    def calcular(self):
        n1=float(self.txt_nota1.text())
        n2=float(self.txt_nota2.text())
        n3=float(self.txt_nota3.text())
        n4=float(self.txt_nota4.text())
        self.lb_promedio.setText(str(round(operar.promedio(n1,n2,n3,n4),2)))
        self.lb_observacion.setText(operar.situacion(n1,n2,n3,n4))

class Ventana6(QDialog):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi("seg1.ui",self)
        self.b_calcular.clicked.connect(self.calcular)
        self.b_salir.clicked.connect(self.salir)
        self.lb_curso1.setText("Java III")
        self.lb_curso2.setText("Linux")
        self.lb_curso3.setText("Php")
        self.lb_curso4.setText("Sistemas")
        
    def salir(self):
        self.close()

    def calcular(self):
        n1=float(self.txt_nota1.text())
        n2=float(self.txt_nota2.text())
        n3=float(self.txt_nota3.text())
        n4=float(self.txt_nota4.text())
        self.lb_promedio.setText(str(round(operar.promedio(n1,n2,n3,n4),2)))
        self.lb_observacion.setText(operar.situacion(n1,n2,n3,n4))


app = QApplication(sys.argv)
Principal=Ejemplo01()
Principal.show()
sys.exit(app.exec())