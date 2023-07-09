from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(400, 400)
        MainWindow.setStyleSheet(".QWidget {background-image: url(D:/Python/weather/background.jpg);}")
        MainWindow.setWindowIcon(QIcon('D:/Python/weather/sunny.ico'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 360, 60))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(22)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius: 0;\n"
                                    "border: 2px solid rgba(255, 255, 255, 80);\n"
                                    "color: white;\n"
                                    "background-color: rgba(255, 255, 255, .4)")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 90, 360, 50))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(22)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "color: white;"
                                      "background-color: rgb(0,126,210)\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "background-color: rgb(0,180,250)\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 150, 360, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QtCore.QRect(20, 170, 361, 191))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("border: 2px solid rgba(255, 255, 255, 0);\n"
                                    "color: white;\n"
                                    "background-color: rgba(255, 255, 255,0)")
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "УЗНАТЬ ПОГОДУ"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
