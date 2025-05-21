import sys
from PyQt6 import QtWidgets
from login import Ui_Dialog
from database import validate_user, register_user 

class LoginApp(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.loginButton.clicked.connect(self.login)
        self.ui.registerButton.clicked.connect(self.register)

    def login(self):
        username = self.ui.username.toPlainText()
        password = self.ui.password.toPlainText()
        role = self.ui.usertype.currentText().lower()
        
        user_id = self.validate_user(username, password, role)

        if user_id:  
            QtWidgets.QMessageBox.information(self, "Login Success", f"Welcome {role.title()} {username}!")

            if role == "customer":
                from buyer_window import BuyerApp
                self.buyer_window = BuyerApp(user_id)  
                self.buyer_window.show()
            else:
                from sellerui import SellerWindow
                self.seller_window = SellerWindow(user_id)  
                self.seller_window.show()

            self.close()  
        else:
            QtWidgets.QMessageBox.warning(self, "Login Failed", "Invalid username or password.")

    def register(self):
        username = self.ui.username.toPlainText()
        password = self.ui.password.toPlainText()
        role = self.ui.usertype.currentText().lower()

        user_id = self.register_user(username, password, role)

        if user_id:
            QtWidgets.QMessageBox.information(self, "Registration Success", f"Welcome {role.title()} {username}!")
        else:
            QtWidgets.QMessageBox.warning(self, "Registration Failed", "Username Already Exists.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = LoginApp()
    window.show()
    sys.exit(app.exec())