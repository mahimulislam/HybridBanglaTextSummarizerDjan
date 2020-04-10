import re
from polyglot.text import Text, Word
import glob
import re
import numpy as np
from numpy import dot
from polyglot.text import Text, Word
import errno
import os
from numpy.linalg import norm
from gensim.models import Word2Vec
from nltk import word_tokenize
import glob

import nltk
class Sentence2Vec:
    def __init__(self, model_file):
        self.load(model_file)

    def load(self, model_file):
        self.model = Word2Vec.load(model_file)

    def get_vector(self, sentence):
        # convert to lowercase, ignore all special characters - keep only
        # alpha-numericals and spaces

        vectors = [self.model.wv[w] for w in word_tokenize(sentence)
                   if w in self.model.wv]

        v = np.zeros(self.model.vector_size)

        if (len(vectors) > 0):
            v = (np.array([sum(x) for x in zip(*vectors)])) / v.size

        return v

    def similarity(self, x, y):
        xv = self.get_vector(x)
        yv = self.get_vector(y)

        score = 0

        if xv.size > 0 and yv.size > 0 and norm(xv)!=0 and norm(yv)!=0:
            lp=(norm(xv) * norm(yv))
            lx=np.dot(xv, yv)
            score = lx / lp

        return score/10

cur_path = os.path.dirname(__file__)

def main(textarea):
    s=""
    pattern = re.compile(u'[\u0980-\u09FF]+', re.UNICODE)
    new_path1 = cur_path + '/economicswordswithscore.txt'
    totaltext=Text(textarea)
    sample_file2 = open(new_path1, 'r', encoding='utf8')
    text = sample_file2.read()
    textual = Text(text)

    model = Sentence2Vec(cur_path + '/trainedsentence.model')
    scoresht = 0
    storescore = []
    sentencecount = 0
    eachsentu = []
    normfactortextr=0.0
    normfactorsenti=0.0
    normfactorkey=0.0
    ll=0

    for eachsent in totaltext.sentences:
        sentencecount = sentencecount + 1
        for wordsi in eachsent.words:
            if (wordsi == "," or wordsi=="'"):
                continue
            strings = wordsi
            try:
                answer = textual.find(strings)
                sd = len(strings)
                dot = ""
                for i in range(0, 12):
                    dot = dot + textual[answer + sd + 4 + i]
                normfactorkey = normfactorkey + (float(dot))
            except:
                print("S")
            if wordsi.polarity == 0:
                    normfactorsenti = normfactorsenti + .0001

        strings = ""
        for wordssx in eachsent.words:
            strings += wordssx + ' '
        for xx in range(0,len(totaltext.sentences)):
            if xx==sentencecount-1:
                continue
            stringx=""
            for words2x in totaltext.sentences[xx].words:
                stringx+=words2x+' '
            simscore = 0.0
            simscore = model.similarity(stringx, strings)
            normfactortextr = normfactortextr + (float(simscore))
    sentencecount = 0

    for eachsent in totaltext.sentences:
        sentencecount = sentencecount + 1
        eachsentu.append(eachsent)
        scoresht = 0.0
        scoresht2=0.0

        for wordsi in eachsent.words:
            if (wordsi == "," or wordsi=="'"):
                continue
            strings = wordsi
            try:
                answer = textual.find(strings)
                sd = len(strings)
                dot = ""
                for i in range(0, 12):
                    dot = dot + textual[answer + sd + 4 + i]
                    scoresht = scoresht + (float(dot))
            except:
                print("S")
            if wordsi.polarity == 0:
                    scoresht2 = scoresht2 + .0001

        scoresht3=0.0

        strings = ""
        for wordssx in eachsent.words:
            strings += wordssx + ' '
        for xx in range(0,len(totaltext.sentences)):
            if xx==sentencecount-1:
                continue
            stringx=""
            for words2x in totaltext.sentences[xx].words:
                stringx+=words2x+' '
            simscore = 0.0
            simscore = model.similarity(stringx, strings)
            scoresht3 = scoresht3 + (float(simscore))
        mixedscore = .5*(scoresht3/normfactortextr) +.3 * (scoresht/normfactorkey) + .2 * (scoresht2/normfactorsenti)
        storescore.append(mixedscore)

    n = sentencecount

    for i in range(n):
        for j in range(0, n - i - 1):
            if storescore[j] < storescore[j + 1]:
                storescore[j], storescore[j + 1] = storescore[j + 1], storescore[j]
                eachsentu[j], eachsentu[j + 1] = eachsentu[j + 1], eachsentu[j]
                totaltext.sentences[j], totaltext.sentences[j + 1] = totaltext.sentences[j + 1], totaltext.sentences[j]

    for k in range(0, int(sentencecount * .40)):
        if int(len(eachsentu[k])) < 10:
            continue
        s = s + str(eachsentu[k])+'\n'
    return s
