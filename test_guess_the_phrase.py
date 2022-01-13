import enum
import unittest
import guess_the_phrase

class TestGuessThePhrase(unittest.TestCase):

    def test_my_answer_equals_my_dictionary(self):
        # Make sure my_answer is created correctly
        dict_answer = ""
        for i, (k, v) in enumerate(guess_the_phrase.my_answer_dictionary.items()):
            dict_answer += v
        print(f'dict: {dict_answer}')
        if guess_the_phrase.count > 0:
            self.assertEqual(guess_the_phrase.my_answer, dict_answer)