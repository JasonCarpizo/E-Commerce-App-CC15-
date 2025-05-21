from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from database import checkout_items

class CheckoutWindow(QtWidgets.QMainWindow):
    def __init__(self, buyer_ID):
        super().__init__()
        from checkout import Ui_CheckoutWindow
        self.ui = Ui_CheckoutWindow()
        self.ui.setupUi(self)

        self.buyer_ID = buyer_ID 

        self.ui.backButton.clicked.connect(self.goBack)
        self.ui.removeButton.clicked.connect(self.remove)
        self.ui.CheckoutButton.clicked.connect(self.checkout)

    def remove(self):
        selected_items = self.ui.cartList.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "No Selection", "Please select an item to remove.")
            return

        for item in selected_items:
            self.ui.cartList.takeItem(self.ui.cartList.row(item))

    def checkout(self):
        name = self.ui.name.text()
        number = self.ui.number.text()
        address = self.ui.address.text()

        if not name or not number or not address:
            QMessageBox.warning(self, "Missing Fields", "Please fill in all fields.")
            return

        success = checkout_items(self.buyer_ID)

        if success:
            QMessageBox.information(self, "Checkout Complete", "Your order has been placed.")
            self.ui.cartList.clear()
        else:
            QMessageBox.critical(self, "Checkout Failed", "Unable to complete checkout. Please try again.")

    def goBack(self):
        from buyer_window import BuyerApp
        self.buyer_window = BuyerApp(self.buyer_ID)
        self.buyer_window.show()
        self.close()
