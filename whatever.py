# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 16:14:19 2017

@author: kyler
"""

import numpy as np

def gaussian(val, shift):
    return np.exp((-(val - shift))**2)

class BiasDeterminer:
    def __init__(self):
        # Order of Attributes: QuotationFrequency, 
        self.__weights = [0.2, 0.5, 0.3]
        self.__attributes = [0.0, 0.0, 0.0]     # Always initialized to 0.0
        
    def runAnalyis(self, articleStr):
        # Perform Tests
    
        # Return
        return self.calcScore()
    
    def calcScore(self):
        totalScore = 0.0        
        for score in range(len(self.__weights)):
            totalScore += self.__weights[score] * self.__attributes[score]
        return totalScore
    
    def calcQuoteF(self, articleStr):
        return float(articleStr.count("\"")) / len(articleStr)
    
    # Use Gaussian Distribution to determine score [0,1]
    # Optimal Frequency     
    def calcQuoteScore(self, optimal_f, articleStr):
        f = self.calcQuoteF(articleStr)
        return gaussian(f, optimal_f)
        
        
Peter = BiasDeterminer()
print Peter.calcQuoteF('\"hello\"')