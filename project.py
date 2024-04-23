import csv
import sys
import sqlite3

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QApplication, QWidget, QDialog, QPushButton
from second_win import AddWindow, DeleteWindow, UpdateWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui_files/project_ui.ui', self)
        self.loadTable('csv_files/project_csv.csv')

        self.essay1.clicked.connect(self.essay)
        self.gto1.clicked.connect(self.gto)
        self.medal1.clicked.connect(self.medal)
        self.spo1.clicked.connect(self.spo)
        self.portfolio1.clicked.connect(self.portfolio)
        self.volunteering1.clicked.connect(self.volunteering)
        self.MainPage.clicked.connect(self.tblwdgt)
        self.sorting.clicked.connect(self.get_result)
        self.text1.hide()
        self.picture.hide()
        self.MainPage.hide()

        self.pushButton.clicked.connect(AddWindow)
        self.pushButton_2.clicked.connect(DeleteWindow)
        self.pushButton_3.clicked.connect(UpdateWindow)

    def loadTable(self, table_name):
        with open(table_name, encoding="utf8") as csvfile:
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            title = next(reader)
            self.tableWidget.setColumnCount(len(title))
            self.tableWidget.setHorizontalHeaderLabels(title)
            self.tableWidget.setRowCount(0)
            for i, row in enumerate(reader):
                self.tableWidget.setRowCount(
                    self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    self.tableWidget.setItem(
                        i, j, QTableWidgetItem(elem))
        self.tableWidget.resizeColumnsToContents()

    def optim(self, text, name):
        self.text1.setText(text)
        self.text1.setFont(QFont("Times", 12))
        self.tableWidget.hide()
        self.text1.show()
        self.MainPage.show()

        self.label_3.hide()
        self.sorting.hide()
        self.verticalWidget.hide()
        self.lineEdit.hide()

        self.pixmap = QPixmap(f'img/{name}.png')
        self.picture.setPixmap(self.pixmap)
        self.picture.show()

    def essay(self):
        text = '''  С 2014 году по поручению президента в российских школах было введено обязательное
итоговое сочинение (изложение) для 11-классников. Старшеклассники уже свыклись с
мыслью о том, что допуск к ЕГЭ по русскому языку невозможен без прохождения
дополнительного испытания, однако немногие знают, что успешное написание
итогового сочинения может принести до 10 дополнительных баллов к результатам ЕГЭ
при поступлении в вуз. Вот что надо учесть, чтобы набрать максимум баллов. Цель
итогового сочинения—выявление умения мыслить, анализировать, обосновывать и
доказывать свою позицию, опираясь на самостоятельно выбранные произведения
отечественной и мировой литературы. 
  
  Работа оценивается по системе «зачет-незачет». Успешное выполнение заданий является допуском
к обязательному ЕГЭ по русскому языку. При оценке прежде всего учитываются объем (от 250 слов) и 
самостоятельность написания. Кроме того, как и любой другой экзамен, итоговое сочинение 
оценивается по критериям: соответствие теме, аргументация и привлечение литературного материала, композиция и логика 
рассуждения, качество письменной речи, грамотность. С 2022 года в итоговое сочинение внесены изменения. 
  
  Теперь комплекты тем будут формировать из закрытого банка тем итогового сочинения. Это значит, что на сочинении 
2022 года будут только те темы, которые уже использовались в прошлые годы. Никаких новых тем не появится. 
Всего в закрытом банке тем итогового сочинения хранится порядка 1500 вариантов тем. Хорошо написанное итоговое 
сочинение может принести до 10 дополнительных баллов к результатам ЕГЭ при поступлении в вуз. С каждым годом все 
больше вузов рассматривают сочинение в качестве индивидуального достижения абитуриентов.
        '''
        self.optim(text, 'essay')

    def gto(self):
        text = ''' Если в академических дисциплинах выдающихся успехов вы не достигли, есть и другие
способы заработать бонусные баллы. Например, отличиться в спортивной деятельности. 
Особенно это полезно, если поступаете на специальность, связанную со спортом или в целом
требующую хорошей физической подготовки.
  
  Знак отличия ГТО — награда, которую можно получить за успешное выполнение комплекса 
спортивных упражнений на силу, быстроту, гибкость и выносливость. Нормативы разделены
на три уровня сложности, соответствующие золотому, серебряному и бронзовому знакам.
В числе обязательных испытаний комплекса ГТО — бег на короткие и длинные дистанции, 
подтягивания/отжимания и наклоны. Участники также могут пройти дополнительные тесты
по плаванию, лыжному бегу, прыжкам, метанию, стрельбе, самозащите без оружия или
проверке туристических знаний в турпоходе.
  
  За наличие золотого знака ГТО абитуриент при поступлении в вуз может рассчитывать до 4 дополнительных баллов. 
ГТО — это система физической подготовки, которую проходят школьники по всей России. Для получения золотого знака 
необходимо пройти спортивные состязания на определённый результат. Спортивные нормативы включают в себя бег, подтягивания,
прыжки и другие упражнения. Итоговое спортивное соревнование определяет то, насколько участник соответствует статусу 
победителя. 
        '''
        self.optim(text, 'gto')

    def medal(self):
        text = '''Дополнительные баллы также начисляются за медаль «За особые успехи в учении», 
выдаваемую школьникам, отличившимся в освоении ряда предметов школьной программы
и занимающимся научными разработками. 
  
  За наличие медали поступающий в вуз абитуриент может получить до 6 дополнительных 
баллов. Это награда, которую получают выпускники средней школы за отличную учебную 
успеваемость. Для получения медали необходимо набрать определённое количество 
баллов по всем предметам, указанным в учебном плане. Для приёмной комиссии в 
университете золото дополнительно говорит о серьёзности абитуриента и его 
жажде знаний. 
  
  Кроме того, медаль нужна при конкуренции с другими поступающими. Например, если у вас одинаковое количество баллов
за ЕГЭ с другим абитуриентом, но у него нет медали, а у вас есть, то преимущество будет именно у вас. Это плюс при 
поступлении в вузы с большим конкурсом на место.
        '''
        self.optim(text, 'medal')

    def spo(self):
        text = '''
                      Диплом с отличием об окончании колледжа, 
профессионального училища может принести до 10 баллов в профильном вузе.
        '''
        self.optim(text, 'spo')

    def portfolio(self):
        text = '''Участники и победители интеллектуальных конкурсов, не относящихся к предметным
олимпиадам, также получают право на получение 5-ти дополнительных баллов.

  Школьники могут участвовать в научно-исследовательской деятельности, презентовать
авторские разработки на всероссийских и международных технических выставках и 
форумах, заниматься внедрением и продвижением своих проектов с подтвержденным 
патентными документами авторством-все это поможет получить доп (баллы).

  Отдельный вид конкурсов охватывает творческие специальности.

Будущие дизайнеры и архитекторы могут поучить дополнительные баллы, участвуя в проектных соревнования по созданию и 
презентации авторских чертежей и макетов.

Талантливые музыканты, вокалисты и танцоры подтверждают уровень своей квалификации наличие дипломов и сертификатов за 
участие и победу в конкурсах талантов по всей стране или на международном уровне.

Решение о присвоении дополнительных баллов наиболее одаренным абитуриентам принимают педагоги, входящие в приемную 
комиссию вуза.
        '''
        self.optim(text, 'portfolio')

    def volunteering(self):
        text = ''' Волонтерская деятельность – это добровольное участие в различных мероприятиях для тех, 
кто нуждается в помощи. Такой труд, как правило, не оплачивается. 
  
  Если вы поступаете в вуз в этом году, то получить баллы за волонтерство уже не 
удастся − вузы учитывают стаж, полученный не менее 3 месяцев назад от срока подачи 
документов. В остальных случаях вы можете позаботиться о своем будущем заранее и 
завести волонтерскую книжку уже сейчас.

  Для получения дополнительных баллов по этому параметру понадобится книжка волонтёра. 
Этот документ доказывает, что его хозяин участвовал в мероприятии в роли добровольца. 
Некоторые вузы смотрят, сколько часов абитуриент отработал, другие – дают всем волонтерам фиксированное количество 
баллов. Также есть знак отличия «Доброволец России». Его можно получить, подав заявку на одноименный конкурс 
волонтерских проектов. Кстати, обладателями этого знака могут стать не только абитуриенты и студенты, но и СМИ. 
  
  Узнать подробнее, как стать добровольцем, можно в районном волонтерском центре. 
В некоторых школах тоже есть такое отделение или даже отряд добровольцев. 
        '''
        self.optim(text, 'volunteering')

    def tblwdgt(self):
        self.tableWidget.show()
        self.MainPage.hide()
        self.text1.hide()
        self.picture.hide()
        self.label_3.show()
        self.sorting.show()
        self.verticalWidget.show()
        self.lineEdit.show()

    def get_result(self):
        DBSample.select_data(self)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter:
            self.get_result()

        if int(event.modifiers()) == Qt.ShiftModifier:
            if event.key() == Qt.Key_A:
                AddWindow()
        if int(event.modifiers()) == Qt.ShiftModifier:
            if event.key() == Qt.Key_D:
                DeleteWindow()
        if int(event.modifiers()) == Qt.ShiftModifier:
            if event.key() == Qt.Key_U:
                UpdateWindow()


class DBSample(MainWindow):
    def select_data(self):
        bal = ['0', '0', '0', '0', '0', '0']
        self.connection = sqlite3.connect("db_files/project_db.db")
        city = self.lineEdit.text().lower().capitalize()
        if city == 'Введите город':
            city = ''
        elif city == 'Санкт-петербург':
            city = 'Санкт-Петербург'

        if not self.essay2.isChecked() and bal[0] == '1':
            bal[0] = '0'
        elif self.essay2.isChecked() and bal[0] == '0':
            bal[0] = '1'
        if not self.gto2.isChecked() and bal[1] == '1':
            bal[1] = '0'
        elif self.gto2.isChecked() and bal[1] == '0':
            bal[1] = '1'
        if not self.medal2.isChecked() and bal[2] == '1':
            bal[2] = '0'
        elif self.medal2.isChecked() and bal[2] == '0':
            bal[2] = '1'
        if not self.spo2.isChecked() and bal[3] == '1':
            bal[3] = '0'
        elif self.spo2.isChecked() and bal[3] == '0':
            bal[3] = '1'
        if not self.portfolio2.isChecked() and bal[4] == '1':
            bal[4] = '0'
        elif self.portfolio2.isChecked() and bal[4] == '0':
            bal[4] = '1'
        if not self.volunteering2.isChecked() and bal[5] == '1':
            bal[5] = '0'
        elif self.volunteering2.isChecked() and bal[5] == '0':
            bal[5] = '1'
        if city:
            res = self.connection.cursor().execute("""SELECT * FROM universities 
                            WHERE Город = ? AND Сочинение >= ?  AND ГТО >= ? AND Медаль >= ? 
                            AND СПО >= ? AND Портфолио >= ? AND Волонтёрство >= ?""", (city, *bal)).fetchall()
        else:
            res = self.connection.cursor().execute("""SELECT * FROM universities 
                                       WHERE Сочинение >= ?  AND ГТО >= ? AND Медаль >= ? 
                                       AND СПО >= ? AND Портфолио >= ? AND Волонтёрство >= ?""", (bal)).fetchall()
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)

        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def closeEvent(self, event):
        self.connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec())
