import unittest

from yomi.main import convert


class YomiTestCase(unittest.TestCase):
    def setUp(self):
        print("setUp!!")

    def tearDown(self):
        print("tearDown!!")

    def test_yakiniku(self):
        self.assertEqual(convert('焼肉定食'), ['ヤ', 'キ', 'ニ', 'k', 'テ', 'イ', 'シ', 'ョ', 'k'])
