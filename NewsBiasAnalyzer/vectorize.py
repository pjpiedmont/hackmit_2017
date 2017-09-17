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
        self.__featureset.append(float(articleStr.count("\"")) / len(articleStr))
     
    def calcSentimentF(self, articleStr):    
        numSentiments = 0
        numSentences = 0
        sentenceList = articleStr.split('.')
        Dict = getSentimentDictionary('word_dict.txt')
        for sentence in sentenceList:
            if (len(sentence) > 1):         # in case of ellipses (...)
                wordList = [word.strip(string.punctuation) for word in sentence.split()]
                keyList = []                
                for word in wordList:
                    if word in Dict:
                        keyList.append(int(Dict[word]))    
#                sentimentVals = getSentiment(keyList)       # Returns 2-tuple of probabilities of positive, negative respectively                
                sentimentVals = [0,1]
                thresholdDifference = 0.5
                if (abs(sentimentVals[0] - sentimentVals[1]) > thresholdDifference):
                    numSentiments += 1
                numSentences += 1
        try:
            self.__featureset.append(float(numSentiments) / numSentences)
        except ZeroDivisionError:
            print("Error. No strings to parse.")

def getFake():   
    
    fakes = open('fake.csv')
    reader = csv.reader(fakes)
    for line in reader:
        yield line[5] # the element containing the article text
    
def getReal():
    for file in os.listdir("bbc"):
        if file.endswith(".txt"):
            openF = open(file, "r")
            yield openF.read()
            
def test():    
    def test_generator():
        fake = getFake()
        real = getReal()
        while True:
            articleType = random.choice([0,1])
            if(articleType == 0):
                articleText = next(fake)
            else:
                articleText = next(real)
            v = vectorize()
            featureVector = v.vectorizeArticle(articleText)
            print(featureVector)
            yield featureVector#, articleType
    return test_generator

def train():
    def test_generator():
        fake = getFake()
        real = getReal()
        while True:
            articleType = random.choice([0,1])
            if(articleType == 0):
                articleText = next(fake)
            else:
                articleText = next(real)
            v = vectorize()
            featureVector = v.vectorizeArticle(articleText)
            print(featureVector)
            yield featureVector#, articleType
    return test_generator
