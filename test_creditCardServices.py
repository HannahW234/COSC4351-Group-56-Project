import unittest
import creditCardServices as cs


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        name = "Hin Pham"
        cardNumberTrue = "4569215487956321"
        cardNumberFalse = "3244232543"
        expDate = "2023-11"
        cvv = 317

        self.sampleCardTrue = cs.CreditCard(name, cardNumberTrue, expDate, cvv)
        self.sampleCardFalse = cs.CreditCard(name, cardNumberFalse, expDate, cvv)

    def test_canary(self):
        self.assertTrue(True)

    def test_is_card_valid_true(self):
        self.assertTrue(self.sampleCardTrue.is_card_valid())

    def test_is_card_valid_false(self):
        self.assertFalse(self.sampleCardFalse.is_card_valid())





if __name__ == '__main__':
    unittest.main()
