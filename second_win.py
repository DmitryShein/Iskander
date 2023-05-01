from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import(
        QApplication, QWidget,
        QHBoxLayout, QVBoxLayout,
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)

#класс второго окна
class Second_win(QWidget):
    #инициализруем окошко и вызываем все его методы
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()
        self.show()
    
    #параметры окна
    def set_appear(self):
        self.setWindowTitle('Всем привет')
        self.resize(500, 300)
        self.move(500, 600)
    
    #контент на окне
    def initUI(self):
        self.text1 = QLabel('Вы вошли')
        self.v_line = QVBoxLayout()

        self.v_line.addWidget(self.text1, alignment=Qt.AlignCenter)

        self.setLayout(self.v_line)

    #Обработка нажатий на кнопки
    def connects(self):
        pass
