import unittest
from src.grammar.grammar_corrector import correct_grammar

class TestGrammar(unittest.TestCase):
    def test_correct_grammar(self):
        input_text = "This are a test."
        corrected_text = correct_grammar(input_text)
        self.assertEqual(corrected_text, "This is a test.")

if __name__ == "__main__":
    unittest.main()
