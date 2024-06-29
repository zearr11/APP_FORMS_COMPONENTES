from PyQt5 import QtWidgets, uic

class MayorMenorController:
    
    def __init__(self):
        app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("view/frm_mym.ui")
        self.ventana.show()
        app.exec()