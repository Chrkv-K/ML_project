import re
from nltk.tokenize import word_tokenize, wordpunct_tokenize
import codecs
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
import nltk
import collections

twitter = codecs.open('C:/Users/ekate/Desktop/Project_ML/dataset/dataset_twitter.txt', 'r', encoding='utf-8-sig')
final_twitter = codecs.open('C:/Users/ekate/Desktop/Project_ML/dataset/clean_twitter.txt', "w", "utf-8")

phrases = ""
for line in twitter:

                #          убираем смалики, упоминания людей и ссылки

    pattern = r'((@[a-zA-Z\d\-\_]+)|(https?:\/\/t\.co\/[a-zA-Z\d]+)|([\;\:(\;\-)(\:\-)]?(\)|\(|\|)+))'
    clean_phrase = re.sub(pattern, "", line)
    phrases = phrases + clean_phrase

pattern_2 = r" +"
phrases = re.sub(pattern_2, " ", phrases)
pattern_3 = r"(^ *)"
phrases = re.sub(pattern_3, "", phrases)
pattern_4 = r"\.(?=\b)"
clean_date = re.sub(pattern_4, ". ", phrases)
pattern_5 = r"(\,|\.|\?|\!|\;|\:|\=|\(|\)|\'|\"|RT|\#|\—|\-)"
clean_date = re.sub(pattern_5, "", clean_date)

words = ""
nltk_tokens = nltk.word_tokenize(clean_date)
for i in nltk_tokens:
    words = words + "\n" + i
final_twitter.write(words)
final_twitter.close()
twitter.close()



