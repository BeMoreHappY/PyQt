from PyQt5 import QtWidgets
import database
from datetime import datetime
import time
from Main_window import Ui_MainWindow
from dialog import Ui_Dialog
from dialog2 import  Ui_Dialog2     # Ładujemy główną stronę




class MyWindows(QtWidgets.QMainWindow, Ui_MainWindow):
    """
    QMainWindows - Klasa rodzica, która służy do obsługi głownego okna aplikacji
    """
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.Append_btn.clicked.connect(self.enter_data)

    def enter_data(self):

        if self.pet_name_unknow.checkState() == 0:
            pet_name = self.pet_name.text()
            if pet_name == "":
                return QtWidgets.QMessageBox.warning(self, 'Warning', 'Enter the name or check the box!')

        else:
            pet_name = "Unknown"

        if self.breed_unknow.checkState() == 0:
            breed = self.breed.currentText()
        else:
            breed = "Unknown"

        if self.date_born_unknow.checkState() == 0:
            born_date = self.date_born.text()
            today = datetime.today().strftime("%d.%m.%Y")
            set_data = time.strptime(born_date, "%d.%m.%Y")
            new_today = time.strptime(today, "%d.%m.%Y")
            if new_today < set_data:
                return QtWidgets.QMessageBox.warning(self, 'Warning', 'Invalid date!')



        else:
            born_date = "Unknown"


        sex = self.sex.currentText()

        if database.addToDbAnimals(pet_name, breed, born_date, sex) == True:
            QtWidgets.QMessageBox.information(self, "Information", "Zwierzak został dodany!")

class Baza(MyWindows):
    def __init__(self):
        super().__init__()

class Status(MyWindows):
    def __init__(self):
        super().__init__()












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
        window.resize(800, 600)
        sys.exit(app.exec_())





