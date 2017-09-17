import unittest
import paddleWrapper as paddle

class TestWrapper(unittest.TestCase):
    def test_sentiment_wrapper_01(self):
        #positive connotation
        result = paddle.getSentiment([8, 37, 7])
        self.assertAlmostEqual(result[0], 0.9999890327453613)
        self.assertAlmostEqual(result[1], 1.0963042768707965e-05)
        
    def test_sentiment_wrapper_02(self):
        #negative connotation
        result = paddle.getSentiment([436, 2345, 73])
        self.assertAlmostEqual(result[0], 0, 2)
        self.assertAlmostEqual(result[1], 1, 2)
        
    def test_get_sentiment_dictionary(self):
        result = paddle.getSentimentDictionary('word_dict.txt')
        self.assertDictContainsSubset({'limited': '1726', 'todays': '1638', 'shelf': '4437'}, result)
        
class TestVectorize(unittest.TestCase):
    
    

        
if __name__ == '__main__':
    unittest.main()