from PyQt5 import QtWidgets
import database


from MainUi import Ui_MainWindow
from dialog import Ui_Dialog
from dialog2 import  Ui_Dialog2     # Ładujemy główną stronę




class MyWindows(QtWidgets.QMainWindow):
    """
    QMainWindows - Klasa rodzica, która służy do obsługi głownego okna aplikacji
    """
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

class Register(QtWidgets.QDialog, Ui_Dialog2):
    def __init__(self, parent=None):
        super(Register, self).__init__(parent)
        self.setupUi(self)
        self.db_register.clicked.connect(self.enterData)

    def enterData(self):
        email = self.lineEdit.text()
        username = self.lineEdit_2.text()
        password = self.lineEdit_3.text()
        if password != "" and username != "" and email != "":
            self.sendData(email, username, password)
        else:
            return QtWidgets.QMessageBox.warning(self, 'Warning', "Input all data!")

    def sendData(self, email, username, password):
        if database.addToDb(email, username, password) == True:
            QtWidgets.QMessageBox.information(self, 'Rejestracja', 'Pomyslnie zarejestrowano!')
            self.hide()



class Logowanie(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(Logowanie, self).__init__(parent)
        self.setupUi(self)
        self.logujBtn.clicked.connect(self.handleLogin)
        self.register_2.clicked.connect(self.RegisterSite)


    def handleLogin(self):
        username = self.Login.text()
        password = self.password.text()
        if username == "" or password == "":
           return QtWidgets.QMessageBox.warning(self, 'Error', "Input some data")

        if database.dane(username) == False:
            return QtWidgets.QMessageBox.warning(self, 'Error', 'Bad user or password')

        self.username_db = database.dane(username)[0]
        self.password_db = database.dane(username)[1]

        if username == self.username_db and password == self.password_db:
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Bad user or password')

    def RegisterSite(self):
        self.dialog = Register(self)
        self.dialog.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = Logowanie()
    register = Register()

    if login.exec_() == QtWidgets.QDialog.Accepted:
        window = MyWindows()
        window.show()
        window.resize(1300, 1000)
        sys.exit(app.exec_())





