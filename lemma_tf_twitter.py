import re
from nltk.tokenize import word_tokenize, wordpunct_tokenize
import codecs
import pymorphy2
morph = pymorphy2.MorphAnalyzer()
import nltk
import collections

lemmas_twitter = codecs.open('C:/Users/ekate/Desktop/Project_ML/dataset/lemmas_twitter.txt', "r", "utf-8")
tf_lemma = codecs.open('C:/Users/ekate/Desktop/Project_ML/dataset/lemma_tf_twitter.txt', "w", "utf-8")

counter_le = str(collections.Counter(lemmas_twitter))

pattern = r", '"
clean_counter = re.sub(pattern, "\n", counter_le)
pattern = r"\\n'"
clean_counter = re.sub(pattern, "", clean_counter)

tf_lemma.write(clean_counter)
tf_lemma.close()
lemmas_twitter.close()


