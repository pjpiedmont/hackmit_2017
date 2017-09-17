# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 16:14:19 2017

@author: kyler
"""

from paddleWrapper import getSentimentDictionary, getSentiment
import string
import random
import csv
import os
import numpy as np
random.seed(0)



# Create instance of object.
# Call vectorizeArticle. Pass in the entire article as a string.
    # sentimentFct should accept a string and return the 3-tuple of sentiment values
# vectorizeArticle returns the vector of the article.

class vectorize:
    def __init__(self):
        # Order of FeatureSet: QuotationFrequency, SentimentFrequency... 
        self.__featureset = []
        
    def vectorizeArticle(self, articleStr):
        # Perform Tests
        self.calcQuoteF(articleStr)
        self.calcSentimentF(articleStr)
        return self.__featureset;
    
    def calcQuoteF(self, articleStr):
        try:
            self.__featureset.append(float(articleStr.count("\"")) / len(articleStr))
        except:
            self.__featureset.append(0.0)
     
    def calcSentimentF(self, articleStr):    
        numSentiments = 0
        numSentences = 0
        sentenceList = articleStr.split('.')
        Dict = getSentimentDictionary('word_dict.txt')
        keyList = []
        for sentence in sentenceList:
            if (len(sentence) > 1):         # in case of ellipses (...)
                wordList = [word.strip(string.punctuation) for word in sentence.split()]
                
                for word in wordList:
                    if word in Dict:
                        keyList.append(int(Dict[word]))
        if keyList != []:

               # print(keyList)
               sentimentVals = getSentiment(keyList)       # Returns 2-tuple of probabilities of positive, negative respectively                

        else:
            sentimentVals = [0.0,0.0]
        try:
            self.__featureset.append((len(articleStr) / len(sentenceList))/ 50)
        except:
            self.__featureset.append(0)
               #                sentimentVals = [0,1]
#                thresholdDifference = 0.5
#                if (abs(sentimentVals[0] - sentimentVals[1]) > thresholdDifference):
#                    numSentiments += 1
#                numSentences += 1
        try:
            self.__featureset.append(sentimentVals[0])
            self.__featureset.append(sentimentVals[1])
        except ZeroDivisionError:
           # print(articleStr)
            print("Error. No strings to parse.")
            self.__featureset.append(0.0)
            self.__featureset.append(0.0)

def getFake():   
    
    fakes = open('fake.csv')
    reader = csv.reader(fakes)
    for line in reader:
        yield line[5] # the element containing the article text
    
def getReal():
    for file in os.listdir("bbc/business"):
        #print("testtest2")
        if file.endswith(".txt"):
         #   print("testtest1")
            openF = open("bbc/business/"+file, "r")
          #  print("testtest")
            yield openF.read()
            
            
def myGen(n):
    yield n
    yield n + 1
            
def tester():
    fake = getFake()
    real = getReal()
    for i in range(300):
        articleType = random.choice([0,1])
        try:
            if(articleType == 0):
                articleText = next(fake)
            else:
                articleText = next(real)
        except:
            break
        v = vectorize()
        featureVector = np.array(v.vectorizeArticle(articleText))
        #print((featureVector,articleType))
        yield featureVector,[articleType]
            

