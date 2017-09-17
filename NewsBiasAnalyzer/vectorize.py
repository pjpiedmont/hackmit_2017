# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 16:14:19 2017

@author: kyler
"""


# Create instance of object.
# Call vectorizeArticle. Pass in the entire article as a string.
    # sentimentFct should accept a string and return the 3-tuple of sentiment values
# vectorizeArticle returns the vector of the article.

class vectorize:
    def __init__(self):
        # Order of FeatureSet: QuotationFrequency, SentimentFrequency, 
        self.__featureset = []
        
    def vectorizeArticle(self, articleStr, sentimentFct):
        # Perform Tests
        self.calcQuoteF(articleStr)
        self.calcSentimentF(articleStr, sentimentFct)
        return self.__featureset;
    
    def calcQuoteF(self, articleStr):
        self.__featureset.append(float(articleStr.count("\"")) / len(articleStr))
     
    def calcSentimentF(self, articleStr, fct):    
        numSentiments = 0
        sentenceList = articleStr.split('\n')
        for sentence in sentenceList:
            if (len(sentence) > 1):         # in case of ellipses (...)
                sentence.append('.')
                sentimentVals = fct(sentence)       # Returns 3-tuple of probabilities of negative, neutral, positive respectively
                # If the highest probability is NOT 'neutral'
                if (sentimentVals.index(max(sentimentVals))) != 1:
                    numSentiments += 1
        return float(numSentiments) / len(sentenceList)