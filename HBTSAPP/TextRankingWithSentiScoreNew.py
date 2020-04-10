import re
from polyglot.text import Text, Word
import glob
from polyglot.text import Text, Word
import errno
import os
pattern = re.compile(u'[\u0980-\u09FF]+', re.UNICODE)
f = open('Documents/TrainingData/%s.txt', encoding="utf-8")
sens=f.read()
totaltext=Text(sens)
scoresht=0;
storescore=[]
sentencecount=0
eachsentu=[]
for eachsent in totaltext.sentences:
    sentencecount=sentencecount+1
    eachsentu.append(eachsent)
    scoresht=0.0
    for wordsi in eachsent.words:
        if (wordsi == "," or wordsi=="'"):
              continue
        if wordsi.polarity == 0:
              scoresht = scoresht + .0001
    storescore.append(scoresht)
n = sentencecount
for i in range(n):
    for j in range(0, n - i - 1):
        if storescore[j] < storescore[j + 1]:
            storescore[j], storescore[j + 1] = storescore[j + 1], storescore[j]
            eachsentu[j],eachsentu[j+1]=eachsentu[j+1],eachsentu[j]
            totaltext.sentences[j],totaltext.sentences[j+1] = totaltext.sentences[j+1],totaltext.sentences[j]


for k in range(0,int(sentencecount*.40)):
    if int(len(eachsentu[k]))<10:
        continue
    print(eachsentu[k], file=open("Documents/Testing/SummaryBasedOnSentiment/%s.txt" % pot, "a", encoding='utf8'))
    print(eachsentu[k], file=open("Documents/Testing/SummaryWithScoreBasedOnSentiment/%s.txt" % pot, "a", encoding='utf8'))
    print(storescore[k], file=open("Documents/Testing/SummaryWithScoreBasedOnSentiment/%s.txt" % pot, "a", encoding='utf8'))