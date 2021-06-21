#-*- coding: utf8 -*-
#project
import pymorphy2
import re
morph = pymorphy2.MorphAnalyzer()
import codecs
import time
import random
import sys
from PyQt5 import (QtWidgets, QtGui, QtCore)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

def filthy_language(inputedText):

    """ Функция заменяет мат на синоним """

    #создаем словарь со словами, которые будем искать
    with open('C:/Users/ekate/Desktop/Project_ML/dictionaries/curse_dictionary.txt', 'r', encoding='utf-8-sig') as f:

        filthy_words = {}
        for line in f.readlines():
            line = line.split(':')
            key = line[0].strip()
            value = line[1].strip()
            if key in filthy_words:
                filthy_words[key].append(value)
            else:
                filthy_words[key] = value

    your_phrase = inputedText

    with open('C:/Users/ekate/Desktop/Project_ML/dictionaries/tf_3grams_twitter.txt', 'r', encoding='utf-8-sig') as first_thr:
        thr_dict = {}
        for line in first_thr.readlines():
                line = line.split(':')
                key = line[0].strip()
                value = line[1].strip()
                if key in thr_dict:
                    thr_dict[key].append(value)
                else:
                    thr_dict[key] = value

    for key in thr_dict:
        your_phrase = re.sub(key, thr_dict.get(key), your_phrase)
    

    with open('C:/Users/ekate/Desktop/Project_ML/dictionaries/tf_bi_twitter.txt', 'r', encoding='utf-8-sig') as first_bi:
        bi_dict = {}
        for line in first_bi.readlines():
                line = line.split(':')
                key = line[0].strip()
                value = line[1].strip()
                if key in bi_dict:
                    bi_dict[key].append(value)
                else:
                    bi_dict[key] = value

    for key in bi_dict:
        your_phrase = re.sub(key, bi_dict.get(key), your_phrase)

    with open('C:/Users/ekate/Desktop/Project_ML/dictionaries/one_word.txt', 'r', encoding='utf-8-sig') as first_one:
        one_dict = {}
        for line in first_one.readlines():
                line = line.split(':')
                key = line[0].strip()
                value = line[1].strip()
                if key in one_dict:
                    one_dict[key].append(value)
                else:
                    one_dict[key] = value

    for key in one_dict:
        your_phrase = re.sub(key, one_dict.get(key), your_phrase)

    #разбиваем на токены
    from nltk.tokenize import word_tokenize, wordpunct_tokenize
    split_your_phrase = wordpunct_tokenize(your_phrase)
    final_phrase = ""
    
    #проверяем, есть ли во фразе нецензурная лексика (ключами словаря являются слова (мат) в инфинитиве, поэтому слова сначала нужно привести в начальную форму)

    for word_from_phrase in split_your_phrase:
        new_a = morph.parse(word_from_phrase)[0]  
        key_inf = new_a.normal_form       
        good_word_origin = filthy_words.get(key_inf)
        
        new_test_b = ""

        
        #если слово найдено в словаре, то мы берем значение ключа и даем ему (значением является слово) грамматические характеристики слова из предложения (не инфинитива!)

        if good_word_origin is not None:

            new_a = morph.parse(word_from_phrase)[0]
            new_b = morph.parse(good_word_origin)[0]
            

            if new_a.tag.POS is not None:
                    
                try:
                    new_test_b = new_b.inflect({new_a.tag.POS}).word #часть речи
                    new_test_b = morph.parse(new_test_b)[0]
                except AttributeError:
                    new_test_b = new_b.word
                    new_test_b = morph.parse(new_test_b)[0]
            if new_a.tag.case is not None:
                try:
                    new_test_b = new_test_b.inflect({new_a.tag.case}).word # падеж
                    new_test_b = morph.parse(new_test_b)[0]
                except AttributeError:
                    new_test_b = new_test_b.word
                    new_test_b = morph.parse(new_test_b)[0]
            if new_a.tag.gender is not None:
                try:
                    new_test_b = new_test_b.inflect({new_a.tag.gender}).word # род
                    new_test_b = morph.parse(new_test_b)[0]
                except AttributeError:
                    new_test_b = new_test_b.word
                    new_test_b = morph.parse(new_test_b)[0]
            if new_a.tag.mood is not None:
                try:
                    new_test_b = new_test_b.inflect({new_a.tag.mood}).word # наклонение
                    new_test_b = morph.parse(new_test_b)[0]
                except AttributeError:
                    new_test_b = new_test_b.word
                    new_test_b = morph.parse(new_test_b)[0]
            if new_a.tag.number is not None:
                try:
                    if new_a.tag.POS == "NOUN":
                        if new_a.tag.number == 'plur':
                            new_test_b = new_test_b.inflect({'plur'}).word
                        else:
                            new_test_b = new_test_b.inflect({'sing'}).word
                    else:
                        new_test_b = new_test_b.inflect({new_a.tag.number}).word # число
                    new_test_b = morph.parse(new_test_b)[0]
                except AttributeError:
                    new_test_b = new_test_b.word
                    new_test_b = morph.parse(new_test_b)[0]
            if new_a.tag.person is not None:
                try:
                    new_test_b = new_test_b.inflect({new_a.tag.person}).word # лицо
                    new_test_b = morph.parse(new_test_b)[0]
                except AttributeError:
                    new_test_b = new_test_b.word
                    new_test_b = morph.parse(new_test_b)[0]
            if new_a.tag.tense is not None:
                try:
                    new_test_b = new_test_b.inflect({new_a.tag.tense}).word # время
                    new_test_b = morph.parse(new_test_b)[0]
                except AttributeError:
                    new_test_b = new_test_b.word
                    new_test_b = morph.parse(new_test_b)[0]
            if new_a.tag.voice is not None:
                try:
                    new_test_b = new_test_b.inflect({new_a.tag.voice}).word  # залог
                    new_test_b = morph.parse(new_test_b)[0]
                except AttributeError:
                    new_test_b = new_test_b.word
                    new_test_b = morph.parse(new_test_b)[0]
            
            new_test_b = new_test_b.word

            final_phrase = final_phrase + " " + new_test_b
        
        else:
            final_phrase = final_phrase + " " + word_from_phrase

        # ^ если слово без ошибок проходит все возможные этапы изменения, то оно записывается в новой нужной форме в предложение.
        # ^ если слову невозможно дать нужную характеристику, мы пропускаем эту грамматическую характеристику и переходим к следующей
        # ^ если слово не было найдено в словаре, то мы записываем его без изменений.


    #убираем лишние символы, которые появились после токенизации и записи изменений

    pattern = r"(((?<=\'), )|\s(?=[(\,)(\.)(\?)(\!)(\s)(\-)])|^(\s)|\'|\[|\]|(?<=\-)\s|\\ n)"
    pattern_2 = r"(((?<=\s)\s)|(^\s))"
    
    new_final_phrase = re.sub(pattern, "", final_phrase)
    new_final_phrase = re.sub(pattern_2, "", new_final_phrase)
    
    # длинное регулярное выражение позволяет найти нецензурные слова, которые по причине их отсутствия в словаре были записаны без изменений.
    # регулярное выражение позволяет найти слова с одним из четырех матерных корней (за счет просмотра вперед и назад мы уменьшаем процент ошибочного исправления цензурных слов)
    pattern_3 = r"((?<=^)|(?<=\s)|(?<=\-)|(?<=без)|(?<=четырежд.)|(?<=бес)|(?<=во)|(?<=воз)|(?<=воc)|(?<=возо)|(?<=вз)|(?<=вс)|(?<=вы)|(?<=до)|(?<=за)|(?<=ис)|(?<=из)|(?<=изо)|(?<=на)|(?<=не)|(?<=наи)|(?<=надо)|(?<=недо)|(?<=над)|(?<=нис)|(?<=низ)|(?<=низо)|(?<=о)|(?<=от)|(?<=об)|(?<=обо)|(?<=обез)|(?<=обес)|(?<=по)|(?<=па)|(?<=ото)|(?<=пра)|(?<=про)|(?<=при)|(?<=пре)|(?<=раз)|(?<=рас)|(?<=роз)|(?<=рос)|(?<=под)|(?<=подо)|(?<=пере)|(?<=пред)|(?<=предо)|(?<=разо)|(?<=су)|(?<=со)|(?<=черес)|(?<=через)|(?<=чрез)|(?<=а)|(?<=ана)|(?<=анти)|(?<=архи)|(?<=гипер)|(?<=гипо)|(?<=де)|(?<=дез)|(?<=дес)|(?<=ин)|(?<=интер)|(?<=у)|(?<=инфра)|(?<=квази)|(?<=кило)|(?<=контр)|(?<=макро)|(?<=микро)|(?<=мега)|(?<=мата)|(?<=мета)|(?<=мульти)|(?<=орто)|(?<=пан)|(?<=пара)|(?<=пост)|(?<=прото)|(?<=ре)|(?<=суб)|(?<=супер)|(?<=транс)|(?<=ультра)|(?<=экстра)|(?<=экс)|(?<=взо)|(?<=ко)|(?<=среди))(ъ|о|)(сху[яиеёю]|ху[яиеёю]|вху[яиеёю]|схуй|хуй|вхуй|спизд|пизд|впизд|сбля|бля|вбля|съеб|еб|въеб|въёб|съёб|ёб|сбляд|бляд|сблядь|блядь|вблядь)((?=)|(?=к)|(?=ок)|(?=ик)|(?=ек)|(?=ёк)|(?=оньк)|(?=еньк)|(?=очк)|(?=ечк)|(?=ушк)|(?=юшк)|(?=ышк)|(?=ник)|(?=чик)|(?=щик)|(?=тель)|(?=ниц)|(?=ист)|(?=ск)|(?=ов)|(?=ев)|(?=ёв)|(?=н)|(?=и)|(?=е)|(?=ова)|(?=ева)|(?=ть)|(?=ти)|(?=чь)|(?=л)|(?=ся)|(?=сь)|(?=ец)|(?=я)|(?=а)|(?=ы)|(?=у)|(?=ю)|(?=ом)|(?=ой)|(?=ое)|(?=ых)|(?=их)|(?=ем)|(?=ая)|(?=яя)|(?=юю)|(?=ую)|(?=ее)|(?=ие)|(?=ые)|(?=ого)|(?=его)|(?=ому)|(?=ему)|(?=ыми)|(?=ими)|(?=им)|(?=ым)|(?=ий)|(?=ый)|(?=ям)|(?=ём))"
    new_final_phrase = re.sub(pattern_3, "***", new_final_phrase)
    
    from nltk.tokenize import word_tokenize, wordpunct_tokenize
    import nltk
    import collections
    import gensim
    import pickle
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from collections import Counter
    from sklearn import feature_extraction, model_selection, naive_bayes, metrics, svm
    import logging
    import urllib.request
    from gensim.models import word2vec
    import joblib

    fasttext_model = gensim.models.KeyedVectors.load('C:/Users/ekate/Desktop/Project_ML/model/214/model.model')
    classifer = joblib.load("C:/Users/ekate/Desktop/Project_ML/model/my_model_svm.pkl")
    final_ml_phrase = ""
    nltk_tokens = nltk.word_tokenize(new_final_phrase)
    for i in nltk_tokens:
        lem = morph.parse(i)[0]
        lem = lem.normal_form
        X = []
        vector = fasttext_model[lem]
        X.append(vector)
        result = classifer.predict(X)
        if result == [0]:
            final_ml_phrase = final_ml_phrase + " " + i
        elif result == [1]:
            final_ml_phrase = final_ml_phrase + " " + "<b><u>" + i + "</u></b>"
    
    pattern = r"(((?<=\'), )|\s(?=[(<b><u>\,</u></b>)(\.)(\?)(\!)(\s)(\-)])|^(\s)|\'|\[|\]|(?<=\-)\s|\\ n)"
    final_ml_phrase = re.sub(pattern, " ", final_ml_phrase)
    pattern = r"\s<b><u>\,</u></b>"
    final_ml_phrase = re.sub(pattern, ", ", final_ml_phrase)
    pattern = r"\s<b><u>\.</u></b>"
    final_ml_phrase = re.sub(pattern, ". ", final_ml_phrase)
    pattern = r"\s<b><u>\?</u></b>"
    final_ml_phrase = re.sub(pattern, "? ", final_ml_phrase)
    pattern = r"\s<b><u>\!</u></b>"
    final_ml_phrase = re.sub(pattern, "! ", final_ml_phrase)
    pattern = r"(((?<=\'), )|\s(?=[(\,)(\.)(\?)(\!)(\s)(\-)])|^(\s)|\'|\[|\]|(?<=\-)\s|\\ n)"
    final_ml_phrase = re.sub(pattern, " ", final_ml_phrase)
    pattern = r"^\s"
    final_ml_phrase = re.sub(pattern, "", final_ml_phrase)
    
    return (final_ml_phrase)

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
        
    def initUI(self):
        
        self.setToolTip('здесь исправляют похабные выражения')
        self.setWindowTitle('Icon')
        self.setGeometry(600, 100, 600, 1100)
        self.setWindowTitle('color: rgba(10, 10, 10, 10)')
        self.setWindowIcon(QIcon('C:/Users/ekate/Desktop/Project_ML/images_for_gui/12345.jpg'))
        self.fon = QLabel(self)
        self.fon.setAlignment(QtCore.Qt.AlignCenter)
        self.fon.setGeometry(0, -300, 635, 1100)
        self.pic = QLabel(self)
        self.pic.setWordWrap(True)
        self.pic.setAlignment(QtCore.Qt.AlignCenter)
        self.pic.setGeometry(0, 0, 1000, 1000)
        self.pic.setStyleSheet('background-color: rgba(255, 255, 255, 10)')
        self.setStyleSheet('background-color: #000000; color: #FFFFFF; border-radius: 10px')        
        self.input = QLineEdit(self)
        self.input.setGeometry(50, 50, 500, 100)
        self.input.setStyleSheet('background-color: #000000; color: #FFFFFF; border-radius: 10px')        
        font_check = QFont()
        font_check.setFamily("Courier New")
        font_check.setPointSize(19)
        self.input.setFont(font_check)
        btn = QPushButton('Обработать', self)
        btn.resize(btn.sizeHint())
        btn.move(185, 200)
        btn.setFont(QFont('century schoolbook', 23))        
        btn.setIconSize(QSize(1000, 50))
        btn_back = QPushButton('Ещё раз', self)    
        btn_back.setFont(QFont('century schoolbook', 30))
        btn.resize(btn.sizeHint())        
        btn_back.move(190, 600)
        btn_back.setIconSize(QSize(100, 50))
        self.label = QLabel(self)
        self.label.setGeometry(20, 20, 500, 100)
        self.show()
        btn.setStyleSheet("QPushButton {background-color: #800000; color: #FFEBCD; border-radius: 10px;}"
                          "QPushButton:pressed {background-color:#A0522D}")
        btn_back.setStyleSheet("QPushButton {background-color: #800000; color: #FFEBCD; border-radius: 10px;}"
                          "QPushButton:pressed {background-color:#A0522D}")
        app.setStyleSheet("btn{font-size: 100pt;}")
        self.movie = QMovie("C:/Users/ekate/Desktop/Project_ML/images_for_gui/333.jpg")
        self.fon.setMovie(self.movie)
        self.movie.start()
        btn.setToolTip('нажми <b>кнопку "ПРОВЕРИТЬ ФРАЗУ"</b>, чтобы исправить мат и выделить оскорбления')

        def on_click_check():
            if (self.input.text() == ""): return
            self.movie = QMovie("C:/Users/ekate/Desktop/Project_ML/images_for_gui/444.jpg")
            self.fon.setMovie(self.movie)
            self.movie.start()
            self.label.setText(filthy_language(self.input.text()))
            self.label.setFont(QFont('gabriola', 30))
            self.label.setGeometry(0, 0, 510, 500)
            self.label.setStyleSheet('background:transparent; color: #000000')
            self.label.setWordWrap(True) 
            self.label.move(50, 20)
            self.input.setVisible(False)
            btn_back.setVisible(True)
            btn.setVisible(False) 
            self.label.setVisible(True)
            self.pic.setFont(QFont('Courier New', 100))
            self.pic.setAlignment(QtCore.Qt.AlignCenter)
            self.pic.setGeometry(150, 101, 3000, 300)
            self.pic.setStyleSheet('background-color: rgba(255, 255, 255, 10)')
    
        def on_click_back():
            self.movie = QMovie("C:/Users/ekate/Desktop/Project_ML/images_for_gui/333.jpg")
            self.fon.setMovie(self.movie)
            self.movie.start()
            self.input.setVisible(True)
            btn_back.setVisible(False)
            self.label.setVisible(False)
            btn.setVisible(True)
            self.input.clear()
        btn.clicked.connect(on_click_check)
        btn_back.clicked.connect(on_click_back)
        btn.resize(btn.sizeHint())
        btn_back.setVisible(False)
        self.label.setVisible(False)
        self.setFixedSize(600, 725)
        self.setWindowTitle('Карманный редактор')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())