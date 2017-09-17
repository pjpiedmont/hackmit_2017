# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 16:14:19 2017

@author: kyler
"""

from paddleWrapper import getSentimentDictionary, getSentiment
import string

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
                sentimentVals = getSentiment(keyList)       # Returns 2-tuple of probabilities of positive, negative respectively                
                thresholdDifference = 0.5
                if (abs(sentimentVals[0] - sentimentVals[1]) > thresholdDifference):
                    numSentiments += 1
                numSentences += 1
        try:
            self.__featureset.append(float(numSentiments) / numSentences)
        except ZeroDivisionError:
            print("Error. No strings to parse.")
        
test = vectorize()
vector = test.vectorizeArticle('Donald Trump asserted that he is powerful because his policies are fantastic. According to her, the police entered at 5 PM.')
print('Expected result: 0.5')
print('Actual result: ' + str(vector[1]))
