import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QWidget, QDialog, QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor


class NoneUnEror(Exception):
    pass


class SecUnError(Exception):
    pass


class ClearLineError(Exception):
    pass


class AddWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui_files/add_win.ui', self)
        self.pushButton.clicked.connect(self.add_university)
        self.label_9.hide()
        self.exec()

    def add_university(self):
        try:
            con = sqlite3.connect('db_files/project_db.db')
            cur = con.cursor()
            universities = list(cur.execute("""SELECT Университет FROM universities"""))
            l_un = []
            for i in universities:
                l_un.append(i[0])
            university = self.lineEdit.text()
            city = self.lineEdit_2.text()
            if university in l_un:
                raise SecUnError('Такой университет уже есть в списке')
            if university and city:
                bal = [self.essay.value(), self.gto.value(), self.medal.value(), self.spo.value(),
                       self.portfolio.value(),
                       self.volunteering.value()]

                cur.execute(
                    """INSERT INTO universities(Университет, Город, Сочинение, ГТО, Медаль, СПО, Портфолио, Волонтёрство) 
                    VALUES(?,?,?,?,?,?,?,?)""",
                    (university, city, *bal))
                con.commit()
                con.close()
                self.label_9.setText("Университет добавлен")
                self.label_9.setStyleSheet('color: green')
                self.label_9.show()
            elif university and not city:
                raise ClearLineError('Введите город')
            elif city and not university:
                raise ClearLineError('Введите университет')
            elif not city and not university:
                raise ClearLineError('Введите университет и город')

        except Exception as e:
            self.label_9.setText(str(e))
            self.label_9.setStyleSheet('color: red')
            self.label_9.show()


class DeleteWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui_files/delete_win.ui', self)
        self.pushButton.clicked.connect(self.delete_university)
        self.label.hide()
        self.exec()

    def delete_university(self):
        try:
            con = sqlite3.connect('db_files/project_db.db')
            cur = con.cursor()
            university = self.lineEdit.text()
            universities = list(cur.execute("""SELECT Университет FROM universities"""))
            l_un = []
            for i in universities:
                l_un.append(i[0])
            if university in l_un:
                cur.execute("""DELETE FROM universities WHERE Университет = ?""", (university,))
                con.commit()
                con.close()

                self.label.setText('Университета удалён')
                self.label.setStyleSheet('color: green')
                self.label.show()

            else:
                raise NoneUnEror('Университет не в списке')

        except Exception as e:
            self.label.setText(str(e))
            self.label.setStyleSheet('color: red')
            self.label.show()

        return self.label.show()


class UpdateWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui_files/update_win.ui', self)
        self.pushButton.clicked.connect(self.update_university)
        self.label.hide()
        self.exec()

    def update_university(self):
        try:
            con = sqlite3.connect('db_files/project_db.db')
            cur = con.cursor()
            university = self.lineEdit.text()
            universities = list(cur.execute("""SELECT Университет FROM universities"""))
            l_un = []
            for i in universities:
                l_un.append(i[0])
            if university in l_un:
                bal = [self.essay.value(), self.gto.value(), self.medal.value(), self.spo.value(),
                       self.portfolio.value(),
                       self.volunteering.value()]

                cur.execute("""UPDATE universities SET Сочинение = ?, ГТО = ?, Медаль = ?, СПО = ?, Портфолио = ?, Волонтёрство = ? 
                WHERE Университет = ?""", (*bal, university))
                con.commit()
                con.close()
                self.label.setText('Параметры университета изменены')
                self.label.setStyleSheet('color: green')
            else:
                raise NoneUnEror('Университет не в списке')
        except Exception as e:
            self.label.setText(str(e))
            self.label.setStyleSheet('color: red')
            self.label.show()

        return self.label.show()
