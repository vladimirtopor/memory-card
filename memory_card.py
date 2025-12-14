from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QButtonGroup, QPushButton, QHBoxLayout, QVBoxLayout, QRadioButton, QGroupBox, QLabel, QWidget) 
from random import shuffle, randint

class Question():
    def __init__(self, question, correct, wrong1, wrong2, wrong3):   #класс для вопросов
        self.question = question
        self.correct = correct
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

quest_list = [] #список с вопросами
quest_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Английский'))
quest_list.append(Question('У какого животного самые большие\n      глаза относительно тела?', 'У долгопята', 'У летучей мыши', 'У тупайи', 'У лемура'))
quest_list.append(Question('Цветы какого из этих растений не голубого цвета?', 'Лютик', 'Незабудка', 'Цикорий', 'Василек'))
quest_list.append(Question('Что в японском ресторане называется «осибори»?', 'Влажное полотенце', 'Палочки для еды', 'Соевый соус', 'Тарелка для суши'))
quest_list.append(Question('Как называется логически верная ситуация,\nкоторая не может существовать в реальности?', 'Апория', 'Парадокс', 'Антиномия', 'Гипербола'))
quest_list.append(Question('Какой национальности не существует?', 'Смурфы', 'Энцы', 'Чулымцы', 'Алеуты'))

app = QApplication([]) #начало программы

#####

btn_ok = QPushButton('Ответить')
lb_question = QLabel('Какой национальности не существует?') #написать вопрос

radiogroupbox = QGroupBox('Варианты ответов') #+группа кнопок

rbtn1 = QRadioButton('Энцы')  #написать варианты ответов
rbtn2 = QRadioButton('Смурфы')
rbtn3 = QRadioButton('Чулымцы')
rbtn4 = QRadioButton('Алеуты')

radiogroup = QButtonGroup() #коробка с радиокнопками

radiogroup.addButton(rbtn1)
radiogroup.addButton(rbtn2)
radiogroup.addButton(rbtn3)
radiogroup.addButton(rbtn4)

layout_ans1 = QHBoxLayout()  #линии
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn1)
layout_ans2.addWidget(rbtn2)
layout_ans3.addWidget(rbtn3)
layout_ans3.addWidget(rbtn4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

radiogroupbox.setLayout(layout_ans1) #привязали линии к группе

ansgroupbox = QGroupBox('Результат теста') #группа результата
lb_result = QLabel('Правильно/Неправильно')
lb_correct = QLabel('Правильный ответ') #ответ на вопрос

layout_res = QVBoxLayout()
layout_res.addWidget(lb_result, alignment=(Qt.AlignLeft | Qt.AlignTop)) #подредактировал правильный ответ
layout_res.addWidget(lb_correct, alignment=Qt.AlignHCenter, stretch=2)
ansgroupbox.setLayout(layout_res)

layout_line1 = QHBoxLayout() #вопрос
layout_line2 = QHBoxLayout() #варианты ответов и результат
layout_line3 = QHBoxLayout() #кнопка 'ответить'

layout_line1.addWidget(lb_question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(radiogroupbox)
layout_line2.addWidget(ansgroupbox)
ansgroupbox.hide() #прячем группу результата

layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok, stretch=2) #настраиваем размеры кнопки ответить
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2) #присоединяем линии к главной и настраиваем их
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)




#################################

def show_result():
    radiogroupbox.hide() #скрывает группу кнопок, показывает группу результата
    ansgroupbox.show()
    btn_ok.setText('Следующий вопрос')

def show_question():
    radiogroupbox.show() #скрывает группу результата, показывает группу кнопок
    ansgroupbox.hide()
    btn_ok.setText('Ответить')
    radiogroup.setExclusive(False) #Нет ограничений. Возможен сброс кнопок
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    radiogroup.setExclusive(True) #Установлено ограничение. Нельзя сбросить кнопки

answer = [rbtn1, rbtn2, rbtn3, rbtn4] #список с кнопками

'''def test(): #переключатель
    if btn_ok.text() == 'Ответить':  #для теста работы программы (можно удалить)
        show_result()
    else:
        show_question()'''

def ask(q: Question): #устанавливаем новые позиции ответов
    shuffle(answer)
    answer[0].setText(q.correct)
    answer[1].setText(q.wrong1) 
    answer[2].setText(q.wrong2)
    answer[3].setText(q.wrong3)
    lb_question.setText(q.question)
    lb_correct.setText(q.correct)
    show_question()

def check_ans(): #проверка на верность ответа
    if answer[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n-Всего вопросов:', window.total, '\n-Правильных ответов:', window.score)
        print(f'Рейтинг: {window.score/window.total*100}%')

    else:
        if answer[1].isChecked() or answer[2].isChecked() or answer[3].isChecked():
            show_correct('Неверно!')
            print('Статистика\n-Всего вопросов:', window.total, '\n-Правильных ответов:', window.score)
            print(f'Рейтинг: {window.score/window.total*100}%')

def show_correct(res): #показывает результат
    lb_result.setText(res)
    show_result()

def next_quest():   #новый вопрос
    window.total += 1
    
    cur_question = randint(0, len(quest_list) - 1)
    #if cur_question = window.number:
    while cur_question == window.number:
        cur_question = randint(0, len(quest_list) - 1)
    number = cur_question
    window.number = number
    q = quest_list[cur_question]
    ask(q)

def click_ok():
    if btn_ok.text() == 'Ответить': 
        check_ans()
    else:
        next_quest()

#################################
window = QWidget()
window.total = 0
window.score = 0
window.number = 0
window.setWindowTitle('Memo card')
next_quest()
window.resize(396,200)
window.setLayout(layout_card)
q = Question('Какой национальности не существует?', 'Смурфы', 'Энцы', 'Чулымцы', 'Алеуты')
ask(q)


btn_ok.clicked.connect(click_ok)

window.show()

app.exec()
