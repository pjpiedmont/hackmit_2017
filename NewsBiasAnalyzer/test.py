import unittest
import paddleWrapper as paddle
import vectorize as vectorize

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
        #check at least part of the dictionary exists correctly
        result = paddle.getSentimentDictionary('word_dict.txt')
        self.assertDictContainsSubset({'limited': '1726', 'todays': '1638', 'shelf': '4437'}, result)
        
class TestVectorize(unittest.TestCase):
    def test_vectorize(self):
        test = vectorize.vectorize()
        vector = test.vectorizeArticle('Donald Trump asserted that he is powerful because his policies are fantastic. According to her, the police entered at 5 PM.')
        self.assertEqual(vector, [0.0, 0.5])

        
if __name__ == '__main__':
    unittest.main()