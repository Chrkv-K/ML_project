import spacy
import re
import codecs
import stanfordnlp
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
# from spacy.lang.ru.examples import sentences
from spacy_stanfordnlp import StanfordNLPLanguage
nlp = spacy.load("ru_core_news_sm")
# stanfordnlp.download("ru")
snlp = stanfordnlp.Pipeline(lang="ru")
nlp = StanfordNLPLanguage(snlp)

twitter_one_word = codecs.open('C:/Users/ekate/Desktop/Project_ML/dataset/clean_twitter.txt', "r", "utf-8")
lemma = codecs.open('C:/Users/ekate/Desktop/Project_ML/dataset/lemmas_twitter.txt', "w", "utf-8")

lemmas = ""
for token in twitter_one_word:
    token = token.lower()
    pattern = r"\r\n"
    token = re.sub(pattern, "", token)
    lem = morph.parse(token)[0]
    lem = lem.normal_form
    lemmas = lemmas + "\n" + lem

lemma.write(lemmas)
lemma.close()
twitter_one_word.close()


