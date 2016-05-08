import sys
import os
import math
import codecs


#global variables

unigram_dict_ref = {}
bigram_dict_ref = {}
trigram_dict_ref = {}
quadgram_dict_ref = {}

unigram_dict = {}
bigram_dict = {}
trigram_dict = {}
quadgram_dict = {}


unigram_list_ref = []
bigram_list_ref = []
trigram_list_ref = []
quadgram_list_ref = []

unigram_list = []
bigram_list = []
trigram_list = []
quadgram_list = []




candidate_data = []
reference_data = []
brevity_penality = 0



global_unigram_count = 0
global_bigram_count = 0
global_trigram_count = 0
global_quadgram_count = 0

global_unigram_count_denom = 0
global_bigram_count_denom = 0
global_trigram_count_denom = 0
global_quadgram_count_denom = 0


unigram_dict_num = {}
bigram_dict_num = {}
trigram_dict_num = {}
quadgram_dict_num = {}



#global functions
def compute_document_word_count(input):
    """
    computes the word count of document
    """
    count = 0
    #file=codecs.open(input, "r", "utf-8")
    file=open(input, "r")
    wordcount={}
    for word in file.read().split():
        count+=1
    file.close()
    return count

def GetFilesInFolder(input):
    '''
    stores the files in the given path to a structure and returns this structure
    '''
    ref = []
    for dirName, subdirList, fileList in os.walk(input):
            for fname in fileList:
                    fn = os.path.join(dirName,fname)
                    ref.append(fn)
    return ref


def gather_input_data():
    '''
    gathers the data from input files and writes to global list
    '''
    global brevity_penality
    candidate_path= sys.argv[1]
    reference_path= sys.argv[2]
    global candidate_data,reference_data

    candidate_word_count = compute_document_word_count(candidate_path)
    reference_word_count = compute_document_word_count(reference_path)
    #print "reference file:"+reference_path
    #print "candidate file:"+candidate_path
    #print "candidate word Count: "+str(candidate_word_count)
    #print "reference word Count: "+str(reference_word_count)

    #computing brevity penality
    if(candidate_word_count>reference_word_count):
        brevity_penality = 1.0
    else:
        fraction = 1-(reference_word_count/float(candidate_word_count))
        brevity_penality = math.exp(fraction)
    #print "brevity_penality value is "+str(brevity_penality)


   #opening file and writing the file lines in a list
   # with codecs.open(candidate_path, "r", "utf-8") as myfile:
    with open(candidate_path, "r") as myfile:
        candidate_data = myfile.readlines()
    candidate_data = [x.rstrip() for x in candidate_data]
    #print"current candidate file content is : \n"+str(candidate_data)
    #print "\n"
    myfile.close()

    #with codecs.open(reference_path, "r", "utf-8") as myfile1:
    with open(reference_path, "r") as myfile1:
        reference_data= myfile1.readlines()
    reference_data = [x.rstrip() for x in reference_data]


    #print"current reference file content is : "+str(reference_data)
    myfile1.close()
    #print "\n"

def compute_unigrams_list(string,flag):
    """
    generates unigram and adds them to a list
    if flag is 1 then ref else candidate
    """
    global unigram_list,unigram_list_ref
    string = string.lower()
    unigram = []
    token = string.split()

    for i in token:
        unigram.append(i)

    if flag == 1:
        unigram_list_ref.extend(unigram)
    elif flag == 2:
        return unigram
    else:
        unigram_list.extend(unigram)

def compute_bigram_list(string,flag):
    """
    generates bigrams and adds them to a list
    flag is 1 if ref else candidate
    """
    global bigram_list,bigram_list_ref
    stri = " "
    bigram = []
    string = string.lower()
    token = string.split()
    prev = "start"
    cur = "start"
    count = 0
    for i in token:
        prev = cur
        cur = i
        if (count>=1)  :
            ##print "count is "+str(count)
            stri = prev+" "+cur
            bigram.append(stri)
            stri =""
        count+=1
    if flag == 1:
        bigram_list_ref.extend(bigram)
    elif flag == 2:
        return bigram
    else:
        bigram_list.extend(bigram)



    #return bigram

def compute_trigram_list(string,flag):
    """
    generates trigrams and adds them to a list
    flag is 1 if ref else candidate
    """
    global trigram_list,trigram_list_ref
    str = " "
    trigram = []
    string = string.lower()
    token = string.split()
    prev = "start"
    cur = "start"
    next = "start"
    count = 0
    for i in token:
        prev = cur
        cur = next
        next = i
        if count>=2:
            str = prev+" "+cur+" "+next
            trigram.append(str)
            str =""
        count+=1
    #return trigram
    if flag == 1:
        trigram_list_ref.extend(trigram)
    elif flag == 2:
        return trigram
    else:
        trigram_list.extend(trigram)



def compute_quadgram_list(string,flag):
    """
    generates trigrams and adds them to a list
    flag is 1 if ref else candidate
    """
    global quadgram_list,quadgram_list_ref
    str = " "
    quadgram = []
    string = string.lower()
    token = string.split()
    prev = "start"
    cur = "start"
    next = "start"
    final = "start"
    count = 0
    for i in token:
        prev = cur
        cur = next
        next = final
        final = i
        if count>=3:
            str = prev+" "+cur+" "+next+" "+final
            quadgram.append(str)
            str =""
        count+=1
    #return quadgram
    if flag == 1:
        quadgram_list_ref.extend(quadgram)
    elif flag == 2:
        return quadgram
    else:
        quadgram_list.extend(quadgram)

def compute_ngram_lists():
    global candidate_data,reference_data
    for i in candidate_data:
        compute_unigrams_list(i,0)
        compute_bigram_list(i,0)
        compute_trigram_list(i,0)
        compute_quadgram_list(i,0)

    # for i in reference_data:
    #     compute_unigrams_list(i,1)
    #     compute_bigram_list(i,1)
    #     compute_trigram_list(i,1)
    #     compute_quadgram_list(i,1)


def print_list():

    global unigram_dict,bigram_dict,trigram_dict,quadgram_dict,unigram_dict_ref,bigram_dict_ref,trigram_dict_ref,quadgram_dict_ref#,global_dict,global_dict_ref

    #print "#########################################################################"

    #print "candidate "
    #print "unigram"+str(unigram_list)
    #print "bigram"+str(bigram_list)
    #print "trigram"+str(trigram_list)
    #print "quadgram"+str(quadgram_list)

    #print "#########################################################################"

    #print "\n"

    #print "#########################################################################"

    #print "reference "
    #print "unigram"+str(unigram_list_ref)
    #print "bigram"+str(bigram_list_ref)
    #print "trigram"+str(trigram_list_ref)
    #print "quadgram"+str(quadgram_list_ref)

    #print "#########################################################################"
    #print  "\n"


def update_reference_counts(list):
    """
    updates the counts in  dict
    """
    dict = {}
    for word in list :
        if word in dict:
            dict[word] +=1
        else:
            dict[word] = 1
    return  dict


def convert_list_to_dict():
    '''
    converts lists to dict
    '''
    global unigram_list,unigram_list_ref,bigram_list_ref,bigram_list,trigram_list,trigram_list_ref,quadgram_list_ref,quadgram_list,unigram_dict,unigram_dict_ref,bigram_dict_ref,bigram_dict,trigram_dict_ref,trigram_dict,quadgram_dict,quadgram_dict_ref
    unigram_dict= update_reference_counts(unigram_list)
    bigram_dict = update_reference_counts(bigram_list)
    trigram_dict = update_reference_counts(trigram_list)
    quadgram_dict = update_reference_counts(quadgram_list)

    # unigram_dict_ref = update_reference_counts(unigram_list_ref)
    # bigram_dict_ref = update_reference_counts(bigram_list_ref)
    # trigram_dict_ref= update_reference_counts(trigram_list_ref)
    # quadgram_dict_ref= update_reference_counts(quadgram_list_ref)




def print_dict():

    global unigram_dict,bigram_dict,trigram_dict,quadgram_dict,unigram_dict_ref,bigram_dict_ref,trigram_dict_ref,quadgram_dict_ref#,global_dict,global_dict_ref

    #print "#########################################################################"

    #print " #printing candidate dict "
    #print "unigram"
    #print unigram_dict
    #print "bigram"
    #print bigram_dict
    #print "trigram"
    #print trigram_dict
    #print "quadgram"
    #print quadgram_dict
    #print "num dict"

    #print "unigram"
    #print unigram_dict_num

    #print "bigram"
    #print bigram_dict_num
    #print "trigram"
    #print trigram_dict_num

    #print "quadgram"
    #print quadgram_dict_num


    #print "#########################################################################"

    #print "\n"

    #print "#########################################################################"

    #print "reference "
    #print "unigram"+str(unigram_dict_ref)
    #print "bigram"+str(bigram_dict_ref)
    #print "trigram"+str(trigram_dict_ref)
    #print "quadgram"+str(quadgram_dict_ref)

    #print "#########################################################################"
    #print  "\n"


def update_bleu_counts(dict,dict_ref,flag):

    global unigram_dict_num,bigram_dict_num,trigram_dict_num,quadgram_dict_num

    value = 0.0
    length_of_dict = len(dict)

    #print "candidate dict being used is"
    #print dict
    #print "reference dict being used is"
    #print dict_ref
    tempd = {}
    if length_of_dict!=0:
        for k, v in dict.iteritems():
                    clip_count = 0
                    count = v
                    if k in dict_ref.keys():
                        max_ref_count = dict_ref[k]
                        clip_count = min(count,max_ref_count)
                        #print "current key is "+k
                        #print "max count in reference is "+str(max_ref_count)
                        #print "max count in candidate is "+str(count)
                        #print "clip count is "+str(clip_count)

                    else:
                        clip_count = 0

                    tempd[k]=clip_count
    #print "tempd"+str(tempd)
    val = 0
    if flag==1:
        #unigram_dict_num.update(tempd)

        for me in tempd:
                val = tempd[me]
                if me in unigram_dict_num:

                    unigram_dict_num[me] +=val
                else:
                    unigram_dict_num[me] = val


        #print "$$$$$$$$$$$$ updated unigram dict is "+str(unigram_dict_num)

    elif flag==2:
        #bigram_dict_num.update(tempd)

        for me in tempd:
                val = tempd[me]
                if me in bigram_dict_num:

                    bigram_dict_num[me] +=val
                else:
                    bigram_dict_num[me] = val

        #print "$$$$$$$$$$$$  updated bigram dict is "+str(bigram_dict_num)
    elif flag==3:
        #trigram_dict_num.update(tempd)

        for me in tempd:
                val = tempd[me]
                if me in trigram_dict_num:

                    trigram_dict_num[me] +=val
                else:
                    trigram_dict_num[me] = val

        #print "$$$$$$$$$$$$ updated trigram dict is "+str(trigram_dict_num)
    elif flag==4:
        #quadgram_dict_num.update(tempd)

        for me in tempd:
                val = tempd[me]
                if me in quadgram_dict_num:
                    quadgram_dict_num[me] +=val
                else:
                    quadgram_dict_num[me] = val

        #print "$$$$$$$$$$$$ updated quadgram dict is "+str(quadgram_dict_num)





def construct_global_dict():
       '''
       constructs global dict for each line in both reference and candidate files
       '''
       global candidate_data,reference_data

       for i in range(0,len(candidate_data)):
            #print "current candidate line"+str(candidate_data[i])
            #print "\n"
            #print "current ref line"+str(reference_data[i])

            #print "\n"
            #print "##############unigram#############################################"
            cand_list = compute_unigrams_list(candidate_data[i],2)
            cand_dict =update_reference_counts(cand_list)
            #print "cand_dict:"+str(cand_dict)

            ref_list = compute_unigrams_list(reference_data[i],2)
            ref_dict =update_reference_counts(ref_list)
            #print "ref_dict:"+str(ref_dict)

            update_bleu_counts(cand_dict,ref_dict,1)
            #print "##############bigram#############################################"
            cand_list = compute_bigram_list(candidate_data[i],2)
            cand_dict =update_reference_counts(cand_list)
            #print "cand_dict:"+str(cand_dict)

            ref_list = compute_bigram_list(reference_data[i],2)
            ref_dict =update_reference_counts(ref_list)
            #print "ref_dict:"+str(ref_dict)



            update_bleu_counts(cand_dict,ref_dict,2)
            #print "##############trigram#############################################"
            cand_list = compute_trigram_list(candidate_data[i],2)
            cand_dict =update_reference_counts(cand_list)
            #print "cand_dict:"+str(cand_dict)

            ref_list = compute_trigram_list(reference_data[i],2)
            ref_dict =update_reference_counts(ref_list)
            #print "ref_dict:"+str(ref_dict)


            update_bleu_counts(cand_dict,ref_dict,3)
            #print "##############quadgram#############################################"
            cand_list = compute_quadgram_list(candidate_data[i],2)
            cand_dict =update_reference_counts(cand_list)
            #print "cand_dict:"+str(cand_dict)

            ref_list = compute_quadgram_list(reference_data[i],2)
            ref_dict =update_reference_counts(ref_list)
            #print "ref_dict:"+str(ref_dict)


            update_bleu_counts(cand_dict,ref_dict,4)


def compute_bleu():
    '''
    computes bleu score
    '''

    global  brevity_penality,unigram_dict,unigram_dict_num,bigram_dict,bigram_dict_num,trigram_dict,trigram_dict_num,quadgram_dict,quadgram_dict_num
    bleu = 0
    tbleu = 0
    myunigram_candidate_count = 0
    mybigram_clip_count = 0
    myunigram_clip_count = 0
    mybigram_candidate_count = 0
    mytrigram_clip_count = 0
    mytrigram_candidate_count = 0
    myquadgram_candidate_count = 0
    myquadgram_clip_count = 0

    for k,v in unigram_dict_num.iteritems():
        myunigram_clip_count = myunigram_clip_count+v
    for k,v in unigram_dict.iteritems():
        myunigram_candidate_count = myunigram_candidate_count+v

    for k,v in bigram_dict_num.iteritems():
        mybigram_clip_count = mybigram_clip_count+v
    for k,v in bigram_dict.iteritems():
        mybigram_candidate_count = mybigram_candidate_count+v

    for k,v in trigram_dict_num.iteritems():
        mytrigram_clip_count = mytrigram_clip_count+v
    for k,v in trigram_dict.iteritems():
        mytrigram_candidate_count = mytrigram_candidate_count+v

    for k,v in quadgram_dict_num.iteritems():
        myquadgram_clip_count = myquadgram_clip_count+v
    for k,v in quadgram_dict.iteritems():
        myquadgram_candidate_count = myquadgram_candidate_count+v

    #print "uni values "+str(myunigram_clip_count)+" and "+str(myunigram_candidate_count)

    #print "bi values "+str(mybigram_clip_count)+" and "+str(mybigram_candidate_count)

    #print "tri values "+str(mytrigram_clip_count)+" and "+str(mytrigram_candidate_count)

    #print "quad values "+str(myquadgram_clip_count)+" and "+str(myquadgram_candidate_count)


    uni = myunigram_clip_count/float(myunigram_candidate_count)
    if uni!=0:
        temp =math.log(uni)
        tbleu+= temp/float(4)
    #print "uni value"+str(uni)

    bi = mybigram_clip_count/float(mybigram_candidate_count)
    if bi!=0:
        temp =math.log(bi)
        tbleu+= temp/float(4)
    #print "bi value"+str(bi)
    tri = mytrigram_clip_count/float(mytrigram_candidate_count)
    if tri != 0:
        temp =math.log(tri)
        tbleu+= temp/float(4)
    #print "tri value"+str(tri)
    quad = myquadgram_clip_count/float(myquadgram_candidate_count)
    if quad != 0:
        temp =math.log(quad)
        tbleu+= temp/float(4)
    #print "quad value"+str(quad)

    bleu += math.exp(tbleu)
    bleu = bleu *brevity_penality
    return bleu







#main
gather_input_data()
compute_ngram_lists()
##print_list()
convert_list_to_dict()
##print_dict()
construct_global_dict()
#print_dict()
bleu_score =compute_bleu()
#print "bleu score is"+str(bleu_score)

result = open('bleu_out.txt', 'w')

result.write('%s' % bleu_score)

result.close()


#remove dot
# do reference.
