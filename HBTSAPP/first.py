'''x = 5
myVars = {'x': x}
exec(open('second.py').read(), myVars)'''

import re
from polyglot.text import Text, Word
import glob
from polyglot.text import Text, Word
import errno
import os
def main(textarea):
    try:
        totaltext = Text(textarea)
    except:
        print("s")
    s = ""
    scoresht = 0;
    storescore = []
    sentencecount = 0
    eachsbentu = []
    eachsentu = []
    try:

        for eachsent in totaltext.sentences:
            sentencecount = sentencecount + 1
            eachsentu.append(eachsent)
            scoresht = 0.0
            for wordsi in eachsent.words:
                if (wordsi == "," or wordsi == "'"):
                    continue
                if wordsi.polarity == 0:
                    scoresht = scoresht + .0001
            storescore.append(scoresht)
        n = sentencecount
        for i in range(n):
            for j in range(0, n - i - 1):
                if storescore[j] < storescore[j + 1]:
                    storescore[j], storescore[j + 1] = storescore[j + 1], storescore[j]
                    eachsentu[j], eachsentu[j + 1] = eachsentu[j + 1], eachsentu[j]
                    totaltext.sentences[j], totaltext.sentences[j + 1] = totaltext.sentences[j + 1], \
                                                                            totaltext.sentences[j]
        sop=""
        for k in range(0, int(sentencecount * .40)):
            if int(len(eachsentu[k])) < 10:
                continue
        s=sop
        args = {}
        text = "hello world"
        args['mytext'] = text
    except:
            print("S")

    for k in range(0, int(sentencecount * .40)):
        if int(len(eachsentu[k])) < 10:
            continue
        print(eachsentu[k])
        s = s + str(eachsentu[k])
    return s