import requests

def getSentimentDictionary(filePath):
    d = {}
    with open(filePath) as wordDict:
        for line in wordDict:
            k, v = line.strip().split()
            d[k] = v
    return d

def getSentiment(wordList):
    r = requests.post('http://127.0.0.1:8001', json = {"word": wordList} )
    return r.json()['data'][0]
