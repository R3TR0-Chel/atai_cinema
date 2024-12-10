from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1600, 950)

        # Основной стиль
        Form.setStyleSheet("""
            QWidget {
                background-color: #1A2232;
                color: white;
            }
            QLabel {
                font-family: 'Arial';
                font-size: 14px;
                color: #E0E6ED;
            }
            QPushButton {
                background-color: #283046;
                border: 1px solid #3A4D6A;
                border-radius: 10px;
                color: white;
                font-weight: bold;
                font-size: 12px;
                min-width: 50px;
                min-height: 50px;
            }
            QPushButton:hover {
                background-color: #3A4D6A;
            }
            QPushButton:checked {
                background-color: #FF9500;
                color: #FFFFFF;
            }
        """)

        # Верхний контейнер (светлый)
        self.high_conteiner = QtWidgets.QFrame(Form)
        self.high_conteiner.setGeometry(QtCore.QRect(0, 0, 1600, 95))
        self.high_conteiner.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.high_conteiner.setFrameShadow(QtWidgets.QFrame.Raised)
        self.high_conteiner.setStyleSheet("""
            QFrame {
                background: qlineargradient(
                    spread:pad, x1:0, y1:0, x2:1, y2:1,
                    stop:0 rgba(18, 32, 47, 255), 
                    stop:1 rgba(44, 62, 80, 255)
                );
            }
        """)
        self.high_conteiner.setObjectName("high_conteiner")

        self.cinema_name_label = QtWidgets.QLabel(self.high_conteiner)
        self.cinema_name_label.setGeometry(QtCore.QRect(660, 10, 300, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.cinema_name_label.setFont(font)
        self.cinema_name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cinema_name_label.setObjectName("cinema_name_label")

        self.time_label = QtWidgets.QLabel(self.high_conteiner)
        self.time_label.setGeometry(QtCore.QRect(40, 35, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.time_label.setFont(font)
        self.time_label.setAlignment(QtCore.Qt.AlignCenter)
        self.time_label.setObjectName("time_label")

        # Полоса с изогнутым экраном
        self.screen_label = QtWidgets.QLabel(Form)
        self.screen_label.setGeometry(QtCore.QRect(550, 120, 500, 40))
        self.screen_label.setAlignment(QtCore.Qt.AlignCenter)
        self.screen_label.setObjectName("screen_label")
        self.screen_label.setStyleSheet("""
            QLabel {
                background-color: #283046;
                border: 2px solid #3A4D6A;
                border-radius: 20px;
                font-size: 16px;
                font-weight: bold;
                color: #E0E6ED;
                padding: 10px;
            }
            QLabel::before {
                content: '';
                display: block;
                width: 100%;
                height: 20px;
                border-top-left-radius: 50px;
                border-top-right-radius: 50px;
                background-color: #3A4D6A;
            }
        """)

        # Основной контейнер
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(550, 180, 500, 500))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # Сетка для мест
        self.seat_grid_layout = QtWidgets.QGridLayout(self.frame)
        self.seat_grid_layout.setContentsMargins(20, 20, 20, 20)
        self.seat_grid_layout.setSpacing(15)
        self.add_seats()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def add_seats(self):
        rows = 6  # Количество рядов
        cols = 8  # Количество мест в ряду

        for row in range(rows):
            for col in range(cols):
                seat_button = QtWidgets.QPushButton(f"{col + 1}")
                seat_button.setCheckable(True)
                seat_button.setFixedSize(50, 50)  # Размер кнопки (квадратная)
                self.seat_grid_layout.addWidget(seat_button, row, col)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Interactive Cinema Plan"))
        self.cinema_name_label.setText(_translate("Form", "Cinema Name"))
        self.time_label.setText(_translate("Form", "Time"))
        self.screen_label.setText(_translate("Form", "Screen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
