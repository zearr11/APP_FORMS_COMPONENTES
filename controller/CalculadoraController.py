from PyQt5 import QtWidgets, uic
#from service.CalculadoraService import suma, restar, multiplicado, divisor
from service import CalculadoraService
class CalculadoraController:
    
    def __init__(self):
        app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("view/frm_calculadora.ui")
        self.ventana.calcular.clicked.connect(self.onclickbtcalcular)
        self.ventana.show()
        app.exec()
        
    def onclickbtcalcular(self):
        valor = False
        resultado = 0
        op = ""
        try:
            num1 = int(self.ventana.numero1.text())
            num2 = int(self.ventana.numero2.text())
            if self.ventana.RB_suma.isChecked():
                resultado = CalculadoraService.suma(num1,num2)
                op = "Suma"
            else:
                if self.ventana.RB_resta.isChecked():
                    resultado = CalculadoraService.restar(num1,num2)
                    op = "Resta"
                else:
                    if self.ventana.RB_divide.isChecked():
                        resultado = CalculadoraService.divisor(num1,num2)
                        op = "Divide"
                    else:
                        if self.ventana.RB_multi():
                            resultado = CalculadoraService.multiplicado(num1,num2)
                            op = "Multiplica"
                        else:
                            resultado = 0
                            op = "Elegir Operacion"
            valor = True
        except:
            op = "¡Ingresa valores numéricos!"
        finally:
            if valor == True:
                self.ventana.LB_resultado.setText(op+"="+str(resultado))
            else:
                if valor == False:
                    self.ventana.LB_resultado.setText(op)
                    