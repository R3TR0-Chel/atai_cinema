#python -m PyQt5.uic.pyuic -x log_window.ui -o my_ui.py
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1600, 950)

        # Установка основного стиля для всего окна
        Form.setStyleSheet("""
            QWidget {
                background: qlineargradient(
                    spread:pad, x1:0, y1:0, x2:1, y2:1,
                    stop:0 rgba(18, 32, 47, 255), 
                    stop:1 rgba(44, 62, 80, 255)
                );
                color: white;
            }
            QPushButton {
                background-color: #34495e;
                border: 1px solid #2c3e50;
                color: white;
                font-weight: bold;
                padding: 8px 16px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #2c3e50;
            }
            QLabel {
                font-size: 14px;
            }
        """)

        # Верхний фрейм
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 10, 1560, 61))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.login_button = QtWidgets.QPushButton(self.frame)
        self.login_button.setGeometry(QtCore.QRect(1470, 10, 81, 41))
        self.login_button.setObjectName("login_button")
        self.login_button.setStyleSheet(
            """
            #login_button {
                background-color: #FF9500;
                background-position: center;
                background-repeat: no-repeat;
            }
            """
        )

        self.logo_label = QtWidgets.QLabel(self.frame)
        self.logo_label.setGeometry(QtCore.QRect(10, 10, 47, 41))
        self.logo_label.setPixmap(QtGui.QPixmap("path_to_logo.png"))
        self.logo_label.setScaledContents(True)
        self.logo_label.setObjectName("logo_label")
        self.logo_label.setPixmap(QtGui.QPixmap("logo.jpg").scaled(self.logo_label.width(), self.logo_label.height(),  QtCore.Qt.KeepAspectRatio,  QtCore.Qt.SmoothTransformation))
        self.logo_label.setScaledContents(True)
        

        # Основной контейнер (QScrollArea)
        self.Main_conteiner = QtWidgets.QScrollArea(Form)
        self.Main_conteiner.setGeometry(QtCore.QRect(20, 85, 1560, 850))
        self.Main_conteiner.setWidgetResizable(True)
        self.Main_conteiner.setObjectName("Main_conteiner")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1229, 599))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        # Основной макет для содержимого
        self.main_layout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.main_layout.setObjectName("main_layout")

        # Добавляем фильмы в контейнер
        self.add_movies()

        # Устанавливаем содержимое ScrollArea
        self.Main_conteiner.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.login_button.setText(_translate("Form", "Log in"))

    def add_movies(self):
        # Пример данных о фильмах
        movies = [
            {"title": "The Batman", "genre": "Action", "rating": "8.1", "image": "batman.jpg"},
            {"title": "Uncharted", "genre": "Adventure", "rating": "7.2", "image": "unchartedwebp.webp"},
            {"title": "The Exorcism of God", "genre": "Horror", "rating": "5.6", "image": "The-Exorcism-of-God.jpg"},
            {"title": "Turning Red", "genre": "Comedy", "rating": "7.1", "image": "turning-red.jpg"},
            {"title": "Spider-Man: No Way Home", "genre": "Action", "rating": "8.3", "image": "spider-man.jpg"},
            {"title": "Blade runner", "genre": "Action", "rating": "8.3", "image": "blade runner.jpg"}
        ]

        # Сетка для фильмов
        grid_layout = QtWidgets.QGridLayout()
        row = 0
        col = 0

        for movie in movies:
            # Виджет для фильма
            movie_widget = QtWidgets.QWidget()
            movie_widget.setStyleSheet("background-color: rgba(52, 73, 94, 45); border-radius: 10px; padding: 10px;")
            movie_layout = QtWidgets.QVBoxLayout(movie_widget)

            # Изображение фильма
            movie_image = QtWidgets.QLabel()
            movie_image.setPixmap(QtGui.QPixmap(movie["image"]).scaled(450, 300, QtCore.Qt.KeepAspectRatio))
            movie_image.setAlignment(QtCore.Qt.AlignCenter)
            movie_layout.addWidget(movie_image)

            # Название фильма
            title_label = QtWidgets.QLabel(movie["title"])
            title_label.setAlignment(QtCore.Qt.AlignCenter)
            title_label.setStyleSheet("font-size: 16px; font-weight: bold;")
            movie_layout.addWidget(title_label)

            # Жанр фильма
            genre_label = QtWidgets.QLabel(movie["genre"])
            genre_label.setAlignment(QtCore.Qt.AlignCenter)
            genre_label.setStyleSheet("color: lightgray;")
            movie_layout.addWidget(genre_label)

            # Рейтинг фильма
            rating_label = QtWidgets.QLabel(movie["rating"])
            rating_label.setAlignment(QtCore.Qt.AlignCenter)
            rating_label.setStyleSheet("color: orange; font-size: 14px;")
            movie_layout.addWidget(rating_label)

            # Добавляем фильм в сетку
            grid_layout.addWidget(movie_widget, row, col)

            col += 1
            if col > 2:  # По три фильма в ряд
                col = 0
                row += 1

        # Добавляем сетку в основной макет
        self.main_layout.addLayout(grid_layout)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
#test
