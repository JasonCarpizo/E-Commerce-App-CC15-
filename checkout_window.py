import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox
from checkout import Ui_CheckoutWindow

class CheckoutWindow(QtWidgets.QMainWindow, Ui_CheckoutWindow):
    def __init__(self, buyer_ID):
        super().__init__()
        self.setupUi(self)  
        self.backButton.clicked.connect(self.goBack)
        self.removeButton.clicked.connect(self.remove)
        self.CheckoutButton.clicked.connect(self.checkout)

    def remove(self):
        selected_items = self.cartList.selectedItems()
        if not selected_items:
            QMessageBox.warning(self, "No Selection", "Please select an item to remove.")
            return

        for item in selected_items:
            self.cartList.takeItem(self.cartList.row(item))
        
    def checkout(self):
        name = self.name.text()
        number = self.number.text()
        address = self.address.text()

        items = []
        for index in range(self.cartList.count()):
            item = self.cartList.item(index).text()
            items.append(item)

        cart_contents = "\n".join(items) if items else "No items in cart."

        message = (
            f"Name: {name}\n"
            f"Contact Number: {number}\n"
            f"Address: {address}\n\n"
            f"Items:\n{cart_contents}"
        )

        QMessageBox.information(self, "Checkout Details", message)
        
    def goBack(self):
        from buyer_window import BuyerApp
        self.buyer_window = BuyerApp(self.buyer_ID)  
        self.buyer_window.show()


