from PyQt5 import QtWidgets, uic
from service import MayorMenorService

class MayorMenorController:
    
    def __init__(self):
        app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("view/frm_mym.ui")
        self.ventana.calcular_2.clicked.connect(self.onclickbtcalcular_2)
        self.ventana.show()
        app.exec()
        
    def onclickbtcalcular_2(self):
        resultado = 0
        try:
            val1 = int(self.ventana.n1.text())
            val2 = int(self.ventana.n2.text())
            val3 = int(self.ventana.n3.text())
            val4 = int(self.ventana.n4.text())
            
            if self.ventana.RB_mayor.isChecked():
                resultado = MayorMenorService.may(val1,val2,val3,val4)
            else:
                if self.ventana.RB_menor.isChecked():
                    resultado = MayorMenorService.men(val1,val2,val3,val4)
                else:
                    resultado = 0            
            
        except:
            resultado = 0
            
        finally:
            self.ventana.LB_resultado_2.setText(str(resultado))