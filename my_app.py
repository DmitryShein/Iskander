from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(
        QApplication, QWidget,
        QHBoxLayout, QVBoxLayout,
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit, QMessageBox)

#Имортирвешь класс второго окна
from second_win import *

#класс первого окна
class First_win(QWidget):

    #инициализруем окошко и вызываем все его методы
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()

    #параметры окна
    def set_appear(self):
        self.setWindowTitle('Авторизация')
        self.move(900,70)
        self.resize(250,50)

    #контент на окне
    def initUI(self):
        self.text1 = QLabel('Авторизация')
        self.text2 = QLabel('Имя пользователя')
        self.text3 = QLabel('Пароль')
        self.pas = QLineEdit()
        self.pas2 = QLineEdit()
        self.button = QPushButton('Войти')

        self.v_line = QVBoxLayout()

        self.v_line.addWidget(self.text2, alignment=Qt.AlignCenter)
        self.v_line.addWidget(self.pas, alignment=Qt.AlignCenter)

        self.v_line.addWidget(self.text2, alignment=Qt.AlignCenter)
        self.v_line.addWidget(self.text3, alignment=Qt.AlignCenter)

        self.v_line.addWidget(self.pas2, alignment=Qt.AlignCenter)

        self.v_line.addWidget(self.button, alignment=Qt.AlignCenter)

        self.setLayout(self.v_line)
    
    #Обработка нажатий на кнопки
    def connects(self):
        self.button.clicked.connect(self.autorithate)
    
    #когда кнопка нажата
    def autorithate(self):

        #проверяем
        if self.pas.text() == 'ogurec' and self.pas2.text() == '123':
            #Создаем новое окно от этого же приложения, скрывая первое окно
            self.second_win = Second_win()
            self.hide()

        else:
            #ошибка
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Не верный логин")
            msg.setIcon(QMessageBox.Warning)

            msg.exec_()

#создаем приложение + второе окно
app = QApplication([])
main_win = First_win()
app.exec_()


