from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MovieDetailsForm(object):
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
                color: #E0E6ED;
            }
            QPushButton {
                background-color: #283046;
                border: 1px solid #3A4D6A;
                border-radius: 10px;
                color: white;
                font-weight: bold;
                font-size: 14px;
                min-height: 40px;
            }
            QPushButton:hover {
                background-color: #3A4D6A;
            }
            QComboBox {
                background-color: #283046;
                border: 1px solid #3A4D6A;
                border-radius: 5px;
                color: white;
                padding: 5px;
            }
            QListWidget {
                background-color: #283046;
                border: 1px solid #3A4D6A;
                border-radius: 10px;
                color: white;
                font-size: 16px;
            }
        """)

        # Верхний контейнер
        self.high_conteiner = QtWidgets.QFrame(Form)
        self.high_conteiner.setGeometry(QtCore.QRect(20, 10, 1560, 91))
        self.high_conteiner.setStyleSheet("""
            QFrame {
                background-color: #2C3E50;
                border-radius: 15px;
            }
        """)
        self.high_conteiner.setObjectName("high_conteiner")

        self.movie_title_label = QtWidgets.QLabel(self.high_conteiner)
        self.movie_title_label.setGeometry(QtCore.QRect(600, 20, 400, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.movie_title_label.setFont(font)
        self.movie_title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.movie_title_label.setObjectName("movie_title_label")

        # Левый контейнер
        self.left_frame = QtWidgets.QFrame(Form)
        self.left_frame.setGeometry(QtCore.QRect(20, 120, 780, 600))
        self.left_frame.setStyleSheet("""
            QFrame {
                background-color: #283046;
                border-radius: 15px;
            }
        """)
        self.left_frame.setObjectName("left_frame")

        # Постер
        self.movie_poster_label = QtWidgets.QLabel(self.left_frame)
        self.movie_poster_label.setGeometry(QtCore.QRect(20, 20, 740, 400))
        self.movie_poster_label.setStyleSheet("""
            QLabel {
                background-color: #1A2232;
                border: 2px solid #3A4D6A;
                border-radius: 10px;
            }
        """)
        self.movie_poster_label.setAlignment(QtCore.Qt.AlignCenter)
        self.movie_poster_label.setObjectName("movie_poster_label")

        # Информация о фильме (текст под постером)
        self.movie_info_label = QtWidgets.QLabel(self.left_frame)
        self.movie_info_label.setGeometry(QtCore.QRect(20, 430, 740, 150))
        self.movie_info_label.setStyleSheet("font-size: 16px;")
        self.movie_info_label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.movie_info_label.setWordWrap(True)
        self.movie_info_label.setObjectName("movie_info_label")

        # Правый контейнер
        self.right_frame = QtWidgets.QFrame(Form)
        self.right_frame.setGeometry(QtCore.QRect(820, 120, 760, 600))
        self.right_frame.setStyleSheet("""
            QFrame {
                background-color: #283046;
                border-radius: 15px;
            }
        """)
        self.right_frame.setObjectName("right_frame")

        # Расписание в правом контейнере
        self.schedule_list_widget = QtWidgets.QListWidget(self.right_frame)
        self.schedule_list_widget.setGeometry(QtCore.QRect(20, 20, 720, 560))
        self.schedule_list_widget.setObjectName("schedule_list_widget")
        self.schedule_list_widget.setStyleSheet("font-size: 18px; padding: 10px;")

        # Кнопка "Buy"
        self.buy_button = QtWidgets.QPushButton(Form)
        self.buy_button.setGeometry(QtCore.QRect(650, 750, 300, 60))
        self.buy_button.setText("Buy Ticket")
        self.buy_button.setObjectName("buy_button")
        self.buy_button.setStyleSheet(
            """
            QPushButton {
                background-color: #FF9500;
                background-position: center;
                background-repeat: no-repeat;
            }
            """
        )

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def set_movie_details(self, title, poster_path, year, duration, actors, schedule):
        """
        Устанавливает данные о фильме.

        :param title: Название фильма
        :param poster_path: Путь к изображению постера
        :param year: Год выпуска
        :param duration: Продолжительность
        :param actors: Список актеров
        :param schedule: Расписание (список строк)
        """
        self.movie_title_label.setText(title)
        self.movie_poster_label.setPixmap(QtGui.QPixmap(poster_path).scaled(740, 400, QtCore.Qt.KeepAspectRatio))
        self.movie_info_label.setText(
            f"Year: {year}\nDuration: {duration}\nActors: {', '.join(actors)}"
        )
        self.schedule_list_widget.clear()
        self.schedule_list_widget.addItems(schedule)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Movie Details"))
        self.movie_title_label.setText(_translate("Form", "Movie Title"))
        self.movie_poster_label.setText(_translate("Form", "Poster"))
        self.movie_info_label.setText(_translate("Form", "Year: 2024\nDuration: 120 min\nActors: Actor 1, Actor 2"))
        self.schedule_list_widget.addItems(["15:30", "18:00", "20:30"])  # Пример расписания


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_MovieDetailsForm()
    ui.setupUi(Form)
    # Пример вызова метода set_movie_details
    ui.set_movie_details(
        title="Example Movie",
        poster_path="path/to/poster.jpg",
        year=2024,
        duration="120 min",
        actors=["Actor 1", "Actor 2", "Actor 3"],
        schedule=["15:30", "18:00", "20:30"]
    )
    Form.show()
    sys.exit(app.exec_())
