import json
import os
import re

SkipWordList = ['a','about','above','across','after','afterwards','again','against','all','almost','alone','along','already',
             'also','although','always','am','among','amongst','amoungst','amount','an','and','another','any','anyhow','anyone','anything',
             'anyway','anywhere','are','around','as','at','back','be','became','because','become','becomes','becoming','been','before','beforehand',
             'behind','being','below','beside','besides','between','beyond','bill','both','bottom','but','by','call','can','cannot','cant','co','computer',
             'con','could','couldnt','cry','de','describe','detail','do','done','down','due','during','each','eg','eight','either','eleven','else',
             'elsewhere','empty','enough','etc','even','ever','every','everyone','everything','everywhere','except','few','fifteen','fify','fill','find',
             'fire','first','five','for','former','formerly','forty','found','four','from','front','full','further','get','give','go','had','has','hasnt',
             'have','he','hence','her','here','hereafter','hereby','herein','hereupon','hers','herse"','him','himse"','his','how','however','hundred','i',
             'ie','if','in','inc','indeed','interest','into','is','it','its','itse"','keep','last','latter','latterly','least','less','ltd','made','many',
             'may','me','meanwhile','might','mill','mine','more','moreover','most','mostly','move','much','must','my','myse"','name','namely','neither',
             'never','nevertheless','next','nine','no','nobody','none','noone','nor','not','nothing','now','nowhere','of','off','often','on','once','one',
             'only','onto','or','other','others','otherwise','our','ours','ourselves','out','over','own','part','per','perhaps','please','put','rather','re',
             'same','see','seem','seemed','seeming','seems','serious','several','she','should','show','side','since','sincere','six','sixty','so','some',
             'somehow','someone','something','sometime','sometimes','somewhere','still','such','system','take','ten','than','that','the','their','them',
             'themselves','then','thence','there','thereafter','thereby','therefore','therein','thereupon','these','they','thick','thin','third','this',
             'those','though','three','through','throughout','thru','thus','to','together','too','top','toward','towards','twelve','twenty','two','un',
             'under','until','up','upon','us','very','via','was','we','well','were','what','whatever','when','whence','whenever','where','whereafter',
             'whereas','whereby','wherein','whereupon','wherever','whether','which','while','whither','who','whoever','whole','whom','whose','why','will',
             'with','within','without','would','yet','you','your','yours','yourself','yourselves']


path = []
wordList = []




fakeTrueReview = {}
fakeFalseReview = {}
realTrueReview = {}
realFalseReview = {}


DecPosDocCount = 0
DecNegDocCount = 0

TruNegDocCount = 0
TruPosDocCount = 0
TotalWordCount = 0




def GetCountAndDictFromFile(file):
    global DecPosDocCount
    global DecNegDocCount
    global TruNegDocCount
    global TruPosDocCount
    #print "here7"
    global SkipWordList
    with open(file, 'r') as filename:
        line = filename.read().replace('\n', '')
    #print "here8"
    line = line.translate(string.maketrans("", ""), string.punctuation)
    line = re.sub("[~!?,.'\"-:;\n]",'',line)
    line = line.lower().strip()
    filter(lambda x: x.isalpha(), line)
    SplitWord = line.split(' ')
    SplitWord = filter(None, SplitWord)
    WordListed = dict(Counter(SplitWord))
    CounterDict = WordListed
    CounterDict = dict(
        (key, value)
        for key, value in WordListed.iteritems()
			if key not in set(SkipWordList))

    #print CounterDict

    #print "here9"

    if file.find('deceptive') != -1 and file.find('negative') !=-1 :
       # print "here11"
        DecNegDocCount = DecNegDocCount + 1
        for i in CounterDict:
            if i in fakeFalseReview:
                fakeFalseReview[i] = fakeFalseReview[i] + 1
       #         print "here12"
            else:
                fakeFalseReview[i] = 1
        #        print "here12"

   # print "here10"
    if file.find('deceptive') != -1 and file.find('positive') != -1 :
            DecPosDocCount = DecPosDocCount + 1

            for i in CounterDict:
                if i in fakeTrueReview:
                    fakeTrueReview[i] = fakeTrueReview[i] + 1
                else:
                    fakeTrueReview[i] = 1



    if file.find('truthful') != -1 and file.find('positive') != -1 :
            TruPosDocCount = TruPosDocCount + 1
            for i in CounterDict:
                if i in realTrueReview:
                    realTrueReview[i] = realTrueReview[i] + 1
                else:
                    realTrueReview[i] = 1


    if file.find('truthful') != -1 and file.find('negative') != -1 :
            TruNegDocCount = TruNegDocCount + 1
            for i in CounterDict:
                if i in realFalseReview:
                    realFalseReview[i] = realFalseReview[i] + 1
                else:
                    realFalseReview[i] = 1


import os,sys
import string
from collections import Counter
from sys import argv
script, input = argv

try:
    for dirName, subdirList, fileList in os.walk(input):
        #print "here"
        for file in fileList:
         #   print "here1"
            if file.endswith(".txt"):
              #  print "here2"
                if(file=="README.txt"):
                 #   print "here3"
                    continue
              #  print "here4"
                fpath = os.path.join(dirName,file)
              #  print "here5"
                GetCountAndDictFromFile(fpath)
               # print "here6"
                AdderToVoc = {}

                for word in fakeTrueReview:
                    if word in AdderToVoc:
                        AdderToVoc[word] = AdderToVoc[word] + 1
                    else:
                        AdderToVoc[word] = 1
                for word in fakeFalseReview:
                    if word in AdderToVoc:
                        AdderToVoc[word] = AdderToVoc[word] + 1
                    else:
                        AdderToVoc[word] = 1

                for word in realTrueReview:
                    if word in AdderToVoc:
                        AdderToVoc[word] = AdderToVoc[word] + 1
                    else:
                        AdderToVoc[word] = 1

                for word in realFalseReview:
                    if word in AdderToVoc:
                        AdderToVoc[word] = AdderToVoc[word] + 1
                    else:
                        AdderToVoc[word] = 1


#    AdderToVoc.update(fakeTrueReview)
#     AdderToVoc.update(fakeFalseReview)
#     AdderToVoc.update(realTrueReview)
#     AdderToVoc.update(realFalseReview)


    for l in AdderToVoc:
     wordList.append(l)

except Exception, e:
    print 'error occured'


def countWords(input):
    mysum = 0
    for i in input:
        mysum = mysum + input[i]
    return mysum




#DecPosDocCount = 0
#DecNegDocCount = 0

#TruNegDocCount = 0
#TruPosDocCount = 0

TotalWordCount = TruPosDocCount+TruNegDocCount+DecNegDocCount+DecPosDocCount


#PriorProbablityPositiveClass
PriorProbablityPosDecClass = DecPosDocCount/(float)(TotalWordCount )#pos dec
#PriorProbablityNegativeClass
PriorProbablityNegDecClass = DecNegDocCount/(float)(TotalWordCount) #neg dec
#PriorProbablityDeceptiveClass
PriorProbablityPosTruClass= TruPosDocCount/(float)(TotalWordCount)  #pos tru
#PriorProbablityRealClass
PriorProbablityNegTruClass= TruNegDocCount/(float)(TotalWordCount) #neg tru



outfile = open('nbmodel.txt', 'w')

import pickle

dumpList = [fakeTrueReview, fakeFalseReview, realFalseReview, realTrueReview, wordList, PriorProbablityPosDecClass,
            PriorProbablityNegDecClass, PriorProbablityNegTruClass, PriorProbablityPosTruClass]

pickle.dump(dumpList, outfile)
outfile.close()

