import sys
from PyQt6 import QtWidgets
from buyerui import Ui_MainWindow
#from database import 

class BuyerApp(QtWidgets.QMainWindow):
    def __init__(self, buyerID):
        super().__init__()
        self.buyer_ID = buyerID
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.categories_dropdownButton.clicked.connect(self.dropdown)
        self.ui.settings_pushButton.clicked.connect(self.settings)
        self.ui.booksStationary_pushButton.clicked.connect(self.booksStationery)
        self.ui.clothingFashion_pushButton.clicked.connect(self.clothingFashion)
        self.ui.electronicsGadgets_pushButton.clicked.connect(self.electronicsGadgets)
        self.ui.foodSnacks_pushButton.clicked.connect(self.foodSnacks)
        self.ui.healthBeauty_pushButton.clicked.connect(self.healthBeauty)
        self.ui.homeLiving_pushButton.clicked.connect(self.homeLiving)
        self.ui.homeLiving_pushButton_2.clicked.connect(self.others)

        self.ui.search_pushButton.clicked.connect(self.search)

        self.ui.addCart_pushButton.clicked.connect(self.addCart)
        

    def dropdown(self):
        pass

    def settings(self):
        pass

    def booksStationery(self):
        pass

    def clothingFashion(self):
        pass

    def electronicsGadgets(self):
        pass

    def foodSnacks(self):
        pass

    def healthBeauty(self):
        pass

    def homeLiving(self):
        pass
    
    def others(self):
        pass


    def search(self):
        searchText = self.ui.searchBar_lineEdit.toPlainText()

    
    def addCart(self):
        from checkout_window import CheckoutWindow
        self.checkout_window = CheckoutWindow(self.buyer_ID)  
        self.checkout_window.show()
