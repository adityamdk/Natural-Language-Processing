import pickle
from pprint import pprint
import string
from collections import Counter
import math
import os


def ClassConditionalProbablity(Dict, prior, Freq):
    LogProb = math.log(prior)
    try:
        for i in Dict:
            if i in Freq:
                LogProb = LogProb + math.log(Freq[i])
    except Exception, e:
        pass
    return LogProb


	







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


with open('nbmodel.txt', 'r') as f:
    Classcontents = pickle.load(f)


PPD = Classcontents[5]
PND = Classcontents[6]
PNT = Classcontents[7]
PPT = Classcontents[8]



posDeceptive = Classcontents[0]
negDeceptive = Classcontents[1]
negTruth = Classcontents[2]
posTruth = Classcontents[3]
vocabulary = Classcontents[4]








import os, sys
import string
from sys import argv
from collections import Counter
script, input = argv
FirstLabel = 'truthful'
SecondLabel = 'positive'
try:

    path = input
    FreqFile = open('nboutput.txt', 'w')

    Files = []
    rootDir = '.'
    for dirName, subdirList, fileList in os.walk(input):
        for fname in fileList:
            if fname.endswith(".txt"):
                if(fname=="README.txt"):
                    continue
                fn = os.path.join(dirName,fname)
                Files.append(fn)

    for fname in Files:

        with open(fname, 'r') as filename:
            line = filename.read().replace('\n', '')


        line = line.translate(string.maketrans("", ""), string.punctuation)
        line = line.lower().strip()
        filter(lambda x: x.isalpha(), line)
        WordSplit = line.split(' ')
        WordSplit = filter(None, WordSplit)
        TheList = dict(Counter(WordSplit))
        FinalList = TheList
        FinalList = dict(
            (key, value)
            for key, value in TheList.iteritems()
            if key not in set(SkipWordList)
        )





        negreal = ClassConditionalProbablity(FinalList, PNT, negTruth)




        posdeceptive = ClassConditionalProbablity(FinalList, PPD, posDeceptive)
        postrue = ClassConditionalProbablity(FinalList, PPT, posTruth)
        negdeceptive = ClassConditionalProbablity(FinalList, PND, negDeceptive)




        probablity = [posdeceptive,negdeceptive,negreal,postrue]

        max = 0
        count = 0
        mcount = 0
        for i in probablity:
            if max<i:
                max = i
                mcount = count
            count+=1





        if mcount ==0:
            FirstLabel = 'deceptive'
            SecondLabel = 'positive'
        elif mcount == 1:
            FirstLabel = 'deceptive'
            SecondLabel = 'negative'
        elif mcount == 2:
            FirstLabel = 'truthful'
            SecondLabel = 'negative'
        else:
            FirstLabel = 'truthful'
            SecondLabel = 'positive'
        FreqFile.write(FirstLabel + ' ' + SecondLabel + ' ' + fname + '\n')





    FreqFile.close()
except Exception, e:
    pass
