
import codecs
import pymorphy2
morph = pymorphy2.MorphAnalyzer()

A_good = ""
A_bad = ""
#A прилагательное
ADV_good = ""
ADV_bad = ""
#ADV наречие
CONJ_good = ""
CONJ_bad = ""
#CONJ союз
INTJ_good = ""
INTJ_bad = ""
#INTJ междометие
NUM_good = ""
NUM_bad = ""
#NUM числительное
PART_good = ""
PART_bad = ""
#PART частица
PR_good = ""
PR_bad = ""
#PR предлог
S_good = ""
S_bad = ""
#S существительное
SPRO_good = ""
SPRO_bad = ""
#SPRO местоимение-существительное
V_good = ""
V_bad = ""
#V глагол
just_my_good = ""
just_my_bad = ""
#неизвестно

A_file_bad = codecs.open('C:/Users/ekate/Desktop/ML/dataset/Final/bad/A_file.txt', "w", "utf-8")
ADV_file_bad = codecs.open('C:/Users/ekate/Desktop/ML/dataset/Final/bad/ADV_file.txt', "w", "utf-8")
CONJ_file_bad = codecs.open('C:/Users/ekate/Desktop/ML/dataset/Final/bad/CONJ_file.txt', "w", "utf-8")
INTJ_file_bad = codecs.open('C:/Users/ekate/Desktop/ML/dataset/Final/bad/INTJ_file.txt', "w", "utf-8")
NUM_file_bad = codecs.open('C:/Users/ekate/Desktop/ML/dataset/Final/bad/NUM_file.txt', "w", "utf-8")
PART_file_bad = codecs.open('C:/Users/ekate/Desktop/ML/dataset/Final/bad/PART_file.txt', "w", "utf-8")
PR_file_bad = codecs.open('C:/Users/ekate/Desktop/ML/dataset/Final/bad/PR_file.txt', "w", "utf-8")
S_file_bad = codecs.open('C:/Users/ekate/Desktop/ML/dataset/Final/bad/S_file.txt', "w", "utf-8")
SPRO_file_bad = codecs.open('C:/Users/ekate/Desktop/ML/dataset/Final/bad/SPRO_file.txt', "w", "utf-8")
V_file_bad = codecs.open('C:/Users/ekate/Desktop/ML/dataset/Final/bad/V_file.txt', "w", "utf-8")
just_my_file_bad = codecs.open('C:/Users/ekate/Desktop/ML/dataset/Final/bad/None_file.txt', "w", "utf-8")

with open('C:/Users/ekate/Desktop/ML/dataset/Final/bad.txt', 'r', encoding='utf-8-sig') as f:
    
    for line in f.readlines():
        line = line.split(';')
        word = line[0].strip() #слово
        tag = line[1].strip()
        new_line = morph.parse(word)[0]
        if new_line.tag.POS == "ADJF" or new_line.tag.POS == "ADJS":
            A_bad = A_bad + word + "_A;" + tag + "\n"
        elif new_line.tag.POS == "ADVB":
            ADV_bad = ADV_bad + word + "_ADV;" + tag + "\n"
        elif new_line.tag.POS == "NUMR":
            NUM_bad = NUM_bad + word + "_NUM;" + tag + "\n"
        elif new_line.tag.POS == "CONJ":
            CONJ_bad = CONJ_bad + word + "_CONJ;" + tag + "\n"
        elif new_line.tag.POS == "INTJ":
            INTJ_bad = INTJ_bad + word + "_INTJ;" + tag + "\n"
        elif new_line.tag.POS == "PRCL":
            PART_bad = PART_bad + word + "_PART;" + tag + "\n"
        elif new_line.tag.POS == "PREP":
            PR_bad = PR_bad + word + "_PR;" + tag + "\n"
        elif new_line.tag.POS == "NOUN":
            S_bad = S_bad + word + "_S;" + tag + "\n"
        elif new_line.tag.POS == "NPRO":
            SPRO_bad = SPRO_bad + word + "_SPRO;" + tag + "\n"
        elif new_line.tag.POS == "VERB" or new_line.tag.POS == "INFN":
            V_bad = V_bad + word + "_V;" + tag + "\n"
        else:
            just_my_bad = just_my_bad + word + ";" + tag + "\n"

A_file_bad.write(A_bad)
A_file_bad.close()

ADV_file_bad.write(ADV_bad)
ADV_file_bad.close()

CONJ_file_bad.write(CONJ_bad)
CONJ_file_bad.close()

INTJ_file_bad.write(INTJ_bad)
INTJ_file_bad.close()

NUM_file_bad.write(NUM_bad)
NUM_file_bad.close()

PART_file_bad.write(PART_bad)
PART_file_bad.close()

PR_file_bad.write(PR_bad)
PR_file_bad.close()

S_file_bad.write(S_bad)
S_file_bad.close()

SPRO_file_bad.write(SPRO_bad)
SPRO_file_bad.close()

V_file_bad.write(V_bad)
V_file_bad.close()

just_my_file_bad.write(just_my_bad)
just_my_file_bad.close()

A_file_good = codecs.open('C:/Users/ekate/Desktop/ML/dataset/Final/good/A_file.txt', "w", "utf-8")
ADV_file_good = codecs.open('C:/Users/ekate/Desktop/ML/dataset/Final/good/ADV_file.txt', "w", "utf-8")
CONJ_file_good = codecs.open('C:/Users/ekate/Desktop/ML/dataset/Final/good/CONJ_file.txt', "w", "utf-8")
INTJ_file_good = codecs.open('C:/Users/ekate/Desktop/ML/dataset/Final/good/INTJ_file.txt', "w", "utf-8")
NUM_file_good = codecs.open('C:/Users/ekate/Desktop/ML/dataset/Final/good/NUM_file.txt', "w", "utf-8")
PART_file_good = codecs.open('C:/Users/ekate/Desktop/ML/dataset/Final/good/PART_file.txt', "w", "utf-8")
PR_file_good = codecs.open('C:/Users/ekate/Desktop/ML/dataset/Final/good/PR_file.txt', "w", "utf-8")
S_file_good = codecs.open('C:/Users/ekate/Desktop/ML/dataset/Final/good/S_file.txt', "w", "utf-8")
SPRO_file_good = codecs.open('C:/Users/ekate/Desktop/ML/dataset/Final/good/SPRO_file.txt', "w", "utf-8")
V_file_good = codecs.open('C:/Users/ekate/Desktop/ML/dataset/Final/good/V_file.txt', "w", "utf-8")
just_my_file_good = codecs.open('C:/Users/ekate/Desktop/ML/dataset/Final/good/None_file.txt', "w", "utf-8")

with open('C:/Users/ekate/Desktop/ML/dataset/Final/good.txt', 'r', encoding='utf-8-sig') as f:
    
    for line in f.readlines():
        line = line.split(';')
        word = line[0].strip() #слово
        tag = line[1].strip()
        new_line = morph.parse(word)[0]
        if new_line.tag.POS == "ADJF" or new_line.tag.POS == "ADJS":
            A_good = A_good + word + "_A;" + tag + "\n"
        elif new_line.tag.POS == "ADVB":
            ADV_good = ADV_good + word + "_ADV;" + tag + "\n"
        elif new_line.tag.POS == "NUMR":
            NUM_good = NUM_good + word + "_NUM;" + tag + "\n"
        elif new_line.tag.POS == "CONJ":
            CONJ_good = CONJ_good + word + "_CONJ;" + tag + "\n"
        elif new_line.tag.POS == "INTJ":
            INTJ_good = INTJ_good + word + "_INTJ;" + tag + "\n"
        elif new_line.tag.POS == "PRCL":
            PART_good = PART_good + word + "_PART;" + tag + "\n"
        elif new_line.tag.POS == "PREP":
            PR_good = PR_good + word + "_PR;" + tag + "\n"
        elif new_line.tag.POS == "NOUN":
            S_good = S_good + word + "_S;" + tag + "\n"
        elif new_line.tag.POS == "NPRO":
            SPRO_good = SPRO_good + word + "_SPRO;" + tag + "\n"
        elif new_line.tag.POS == "VERB" or new_line.tag.POS == "INFN":
            V_good = V_good + word + "_V;" + tag + "\n"
        else:
            just_my_good = just_my_good + word + ";" + tag + "\n"

A_file_good.write(A_good)
A_file_good.close()

ADV_file_good.write(ADV_good)
ADV_file_good.close()

CONJ_file_good.write(CONJ_good)
CONJ_file_good.close()

INTJ_file_good.write(INTJ_good)
INTJ_file_good.close()

NUM_file_good.write(NUM_good)
NUM_file_good.close()

PART_file_good.write(PART_good)
PART_file_good.close()

PR_file_good.write(PR_good)
PR_file_good.close()

S_file_good.write(S_good)
S_file_good.close()

SPRO_file_good.write(SPRO_good)
SPRO_file_good.close()

V_file_good.write(V_good)
V_file_good.close()

just_my_file_good.write(just_my_good)
just_my_file_good.close()