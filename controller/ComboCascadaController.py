from PyQt5 import QtWidgets, uic

class ComboCascadaController:
    
    def __init__(self):
        app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("view/frm_combo_cascada.ui")
        self.ventana.show()
        app.exec()