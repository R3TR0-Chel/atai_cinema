from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)

        # Установка фона формы с масштабированием
        Form.setStyleSheet("""
            #Form {
                background-image: url('wallpaper.jpg');  /* Укажите путь к вашему изображению */
                background-repeat: no-repeat;
                background-position: center;
                background-size: cover;  /* Масштабирование под размер виджета */
            }
        """)

        # QR-код
        self.qr_image = QtWidgets.QLabel(Form)
        self.qr_image.setGeometry(QtCore.QRect(300, 50, 200, 200))
        self.qr_image.setAlignment(QtCore.Qt.AlignCenter)
        self.qr_image.setObjectName("qr_image")
        self.qr_image.setStyleSheet("""
            QLabel {
                border: 2px solid #3A4D6A;
                border-radius: 10px;
                background-color: rgba(0, 0, 0, 50%);
            }
        """)

        # Загрузка и масштабирование изображения
        pixmap = QtGui.QPixmap('qr.jpg')  # Укажите путь к вашему изображению
        scaled_pixmap = pixmap.scaled(self.qr_image.width(), self.qr_image.height(), QtCore.Qt.KeepAspectRatio)
        self.qr_image.setPixmap(scaled_pixmap)

        # Название фильма
        self.Movie_title = QtWidgets.QLabel(Form)
        self.Movie_title.setGeometry(QtCore.QRect(20, 300, 760, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.Movie_title.setFont(font)
        self.Movie_title.setAlignment(QtCore.Qt.AlignCenter)
        self.Movie_title.setObjectName("Movie_title")
        self.Movie_title.setStyleSheet("""
            QLabel {
                color: #E0E6ED;
                background-color: rgba(0, 0, 0, 0%);
                border-radius: 5px;
            }
        """)

        # Время
        self.time_label = QtWidgets.QLabel(Form)
        self.time_label.setGeometry(QtCore.QRect(20, 350, 760, 30))
        font.setPointSize(12)
        self.time_label.setFont(font)
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label.setObjectName("time_label")
        self.time_label.setStyleSheet("""
            QLabel {
                color: #E0E6ED;
                background-color: rgba(0, 0, 0, 0%);
                border-radius: 5px;
            }
        """)

        # Место
        self.seat_label = QtWidgets.QLabel(Form)
        self.seat_label.setGeometry(QtCore.QRect(20, 400, 760, 30))
        self.seat_label.setFont(font)
        self.seat_label.setAlignment(QtCore.Qt.AlignCenter)
        self.seat_label.setObjectName("seat_label")
        self.seat_label.setStyleSheet("""
            QLabel {
                color: #E0E6ED;
                background-color: rgba(0, 0, 0, 0%);
                border-radius: 5px;
            }
        """)

        # Цена
        self.price_title = QtWidgets.QLabel(Form)
        self.price_title.setGeometry(QtCore.QRect(20, 450, 760, 30))
        self.price_title.setFont(font)
        self.price_title.setAlignment(QtCore.Qt.AlignCenter)
        self.price_title.setObjectName("price_title")
        self.price_title.setStyleSheet("""
            QLabel {
                color: #E0E6ED;
                background-color: rgba(0, 0, 0, 0%);
                border-radius: 5px;
            }
        """)

        # Первая кнопка
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(200, 520, 180, 40))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet("""
            QPushButton {
                background-color: #FF9500;
                border: 2px solid #3A4D6A;
                border-radius: 10px;
                color: white;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #3A4D6A;
            }
        """)

        # Вторая кнопка
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(420, 520, 180, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("""
            QPushButton {
                background-color: #FF9500;
                border: 2px solid #3A4D6A;
                border-radius: 10px;
                color: white;
                font-weight: bold;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #3A4D6A;
            }
        """)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Movie Ticket"))
        self.qr_image.setText(_translate("Form", ""))
        self.Movie_title.setText(_translate("Form", "Movie Title: Example Movie"))
        self.time_label.setText(_translate("Form", "Time: 18:00"))
        self.seat_label.setText(_translate("Form", "Seat: A12"))
        self.price_title.setText(_translate("Form", "Price: $12.99"))
        self.pushButton.setText(_translate("Form", "Buy"))
        self.pushButton_2.setText(_translate("Form", "Refund"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
