# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 16:14:19 2017

@author: kyler
"""

from paddleWrapper import getSentimentDictionary, getSentiment
import re

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
        sentenceList = articleStr.split('\n')
        Dict = getSentimentDictionary('word_dict.txt')
        for sentence in sentenceList:
            if (len(sentence) > 1):         # in case of ellipses (...)
                wordList = re.sub("[^\w]", " ", sentence).split()
                keyList = []                
                for word in wordList:
                    if word in Dict:
                        keyList.append(Dict[word])    
                sentimentVals = getSentiment(keyList)       # Returns 2-tuple of probabilities of positive, negative respectively                
                thresholdDifference = 0.2
                if (abs(sentimentVals[0] - sentimentVals[1]) > thresholdDifference):
                    numSentiments += 1
        return float(numSentiments) / len(sentenceList)
        
test = vectorize()
vector = test.vectorizeArticle('My name is kyler. I like cookies.')
print('Expected result: 0.5')
print('Actual result:' + vector[1])
