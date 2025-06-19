from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(482, 359)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 10, 431, 311))
        self.frame.setStyleSheet("background-color: #FFB6B9;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 30, 411, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(70, 80, 411, 61))
        font.setPointSize(9)
        font.setUnderline(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(240, 80, 411, 61))
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(40, 120, 171, 41))
        self.lineEdit.setObjectName("lineEdit")
        
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 120, 171, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(90, 170, 241, 41))
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(50, 230, 350, 41))  # digeser lebih ke bawah
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # koneksi tombol ke fungsi
        self.pushButton.clicked.connect(self.hitung_imt)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "APLIKASI CEK INDEKS MASSA TUBUH (IMT)"))
        self.label_2.setText(_translate("Form", "Input Berat Badan"))
        self.label_3.setText(_translate("Form", "Input Tinggi Badan"))
        self.pushButton.setText(_translate("Form", "HITUNG INDEKS MASSA TUBUH"))
        self.label_4.setText(_translate("Form", ""))  # kosongkan dulu

    def hitung_imt(self):
        try:
            berat = float(self.lineEdit.text())
            tinggi = float(self.lineEdit_2.text()) / 100  # konversi cm ke meter
            imt = berat / (tinggi * tinggi)

            if imt < 18.5:
                hasil = "Kurus"
            elif 18.5 <= imt < 25:
                hasil = "Normal"
            elif 25 <= imt < 30:
                hasil = "Kelebihan Berat Badan"
            else:
                hasil = "Obesitas"

            self.label_4.setText(f"Hasil: {hasil} ({imt:.2f})")

        except ValueError:
            self.label_4.setText("Input tidak valid!")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
