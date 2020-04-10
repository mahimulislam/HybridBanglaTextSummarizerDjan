import re
from polyglot.text import Text, Word
import glob
from polyglot.text import Text, Word
import errno
import os
from .Summarizer.Accident import TextRankingWithHybridTesting1
from .Summarizer.Economics import TextRankingWithHybridTesting2
from .Summarizer.Entertainment import TextRankingWithHybridTesting3
from .Summarizer.Politics import TextRankingWithHybridTesting4
def main(textarea):
    cur_path = os.path.dirname(__file__)
    new_path1=cur_path+'/Summarizer/Accident/accidentwordswithscore.txt'
    new_path2=cur_path+'/Summarizer/Economics/economicswordswithscore.txt'
    new_path3=cur_path+'/Summarizer/Entertainment/entertainmentwordswithscore.txt'
    new_path4=cur_path+'/Summarizer/Politics/politicswordswithscore.txt'

    sample_file1 = open(new_path1, 'r', encoding='utf8')
    sample_file2 = open(new_path2, 'r', encoding='utf8')
    sample_file3 = open(new_path3, 'r', encoding='utf8')
    sample_file4 = open(new_path4, 'r', encoding='utf8')

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

    totaltext=Text(textarea)

    sentencecount = 0
    classent = 0.0
    classeco = 0.0
    classpol = 0.0
    classacc = 0.0
    for eachsent in totaltext.sentences:
        sentencecount = sentencecount + 1
        words = eachsent.split(' ')
        for k in range(0, len(words)):
            strings = words[k]
            if (words[k] == "," or words[k] == "'"):
                continue
            try:
                answer = textual1.find(strings)
                sd = len(strings)
                dot = ""
                for i in range(0, 12):
                    dot = dot + textual1[answer + sd + 4 + i]
                classacc = classacc + (float(dot))
            except:
                print("S")
            try:
                answer = textual2.find(strings)
                sd = len(strings)
                dot = ""
                for i in range(0, 12):
                    dot = dot + textual2[answer + sd + 4 + i]
                classeco = classeco + (float(dot))
            except:
                print("S")
            try:
                answer = textual3.find(strings)
                sd = len(strings)
                dot = ""
                for i in range(0, 12):
                    dot = dot + textual3[answer + sd + 4 + i]
                classent = classent + (float(dot))
            except:
                print("S")
            try:
                answer = textual4.find(strings)
                sd = len(strings)
                dot = ""
                for i in range(0, 12):
                    dot = dot + textual4[answer + sd + 4 + i]
                classacc = classacc + (float(dot))
            except:
                print("S")
    if classacc>classeco and classacc>classent and classacc>classpol:
        pk= TextRankingWithHybridTesting1.main(textarea)
        print(pk)
        return(pk)
    if classeco > classacc and classeco > classent and classeco > classpol:
        pk = TextRankingWithHybridTesting2.main(textarea)
        print(pk)
        return(pk)
    if classent>classeco and classent>classacc and classent>classpol:
        pk = TextRankingWithHybridTesting3.main(textarea)
        print(pk)
        return(pk)
    if classpol > classeco and classpol > classacc and classpol > classent:
        pk = TextRankingWithHybridTesting4.main(textarea)
        print(pk)
        return(pk)
    else:
        return("missclassified")