import re
from polyglot.text import Text, Word
import glob
from polyglot.text import Text, Word
import errno
import os

def run(runfile):
  with open(runfile,"r") as rnf:
    exec(rnf.read())

def split_sentences(text):
    """
    Utility function to return a list of sentences.
    @param text The text that must be split in to sentences.
    """
    # sentence_delimiters = re.compile(u'[\\[\\]\n.!?,;:\t\\-\\"\\(\\)\\\'\u2019\u2013]')
    sentence_delimiters = re.compile(
        u'[৷\u002f\u0053\u0056\u00a0\u00ad\u00d0\u00da\u00e6\u00f2\u00f3\u2013\u2014\\[\\]\n!?,;:\।\t\\"\\(\\)\\\'\‘\‘‘]')
    sentences = sentence_delimiters.split(text)
    # print(sentences, file=open("bangla_splitted_sentence.txt", "a", encoding='utf8'))
    return sentences

sample_file1 = open('Accident/Codes For Accident/Documents/accidentwordswithscore.txt', 'r', encoding='utf8')
sample_file2 = open('Economics/Codes For Economics/Documents/economicswordswithscore.txt', 'r', encoding='utf8')
sample_file3 = open('Entertainment/Codes For Entertainment/Documents/entertainmentwordswithscore.txt', 'r', encoding='utf8')
sample_file4 = open('Politics/Codes For Politics/Documents/politicswordswithscore.txt', 'r', encoding='utf8')

text1 = sample_file1.read()
textual1 = Text(text1)
scoresht1 = 0

text2 = sample_file2.read()
textual2 = Text(text2)
scoresht2 = 0

text3 = sample_file3.read()
textual3 = Text(text3)
scoresht3 = 0

text4 = sample_file4.read()
textual4 = Text(text4)
scoresht4 = 0

countacc=0
countpol=0
counteco=0
countent=0
for rot in range(1,101):
    classent=0.0
    classeco=0.0
    classpol=0.0
    classacc=0.0
    pattern = re.compile(u'[\u0980-\u09FF]+', re.UNICODE)
    #print(os.listdir())

    f = open("Mazharul Docs/Document_%s.txt"%rot, encoding="utf-8")
    sens=f.read()
    totaltext=split_sentences(sens)

    scoresht=0
    storeindex=[]
    storescore=[]
    indo=0
    sentencecount=0



    for eachsent in totaltext:
        sentencecount = sentencecount + 1
        words = eachsent.split(' ')
        for k in range(0, len(words)):
            for i in range(0, len(textual1.words)):
                    # print(word)
                    if textual1.words[i] == words[k]:
                        dot = textual1.words[i + 4]
                        dot = dot[:12]
                        classacc = classacc +(float(dot))
            for i in range(0, len(textual2.words)):
                    # print(word)
                    if textual2.words[i] == words[k]:
                        dot = textual2.words[i + 4]
                        dot = dot[:12]
                        classeco = classeco + (float(dot))

            for i in range(0, len(textual3.words)):
                    if textual3.words[i] == words[k]:
                        dot = textual3.words[i + 4]
                        dot = dot[:12]
                        classent = classent + float(dot)

            for i in range(0, len(textual4.words)):
                    # print(word)
                    if textual4.words[i] == words[k]:
                        dot = textual4.words[i + 4]
                        dot = dot[:12]
                        classpol = classpol + float(dot)

    if classacc>classeco and classacc>classent and classacc>classpol:
        countacc+=1
        print(sens, file=open("Accident/Codes For Accident/Documents/MazharulDocs/%s.txt" % rot, "a", encoding='utf8'))

        print("Acident ",rot)
    if classeco > classacc and classeco > classent and classeco > classpol:
        counteco+=1
        print(sens, file=open("Economics/Codes For Economics/Documents/MazharulDocs/%s.txt" % rot, "a", encoding='utf8'))

    print("Eco ", rot)
    if classent>classeco and classent>classacc and classent>classpol:
        countent+=1
        print(sens, file=open("Entertainment/Codes For Entertainment/Documents/MazharulDocs/%s.txt" % rot, "a", encoding='utf8'))

    print("Ent ", rot)
    if classpol > classeco and classpol > classacc and classpol > classent:
        countpol+=1
        print(sens, file=open("Politics/Codes For Politics/Documents/MazharulDocs/%s.txt" % rot, "a", encoding='utf8'))

    print("Politics ", rot)
print(countacc)
print(countent)
print(counteco)
print(countpol)

countacc=str(countacc)
countent=str(countent)
counteco=str(counteco)
countpol=str(countpol)

print("Out of 100  Mazharul Docs ,Classifier Says", file=open("DocClassifierMazharulClass.txt", "a", encoding='utf8'))
print('Accident '+countacc, file=open("DocClassifierMazharulClass.txt", "a", encoding='utf8'))
print('Economics '+counteco, file=open("DocClassifierMazharulClass.txt", "a", encoding='utf8'))
print('Entertainment '+countent, file=open("DocClassifierMazharulClass.txt", "a", encoding='utf8'))
print('Politics '+countpol, file=open("DocClassifierMazharulClass.txt", "a", encoding='utf8'))
