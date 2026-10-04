import sys
import os
import unittest

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src import morse


class TestMorse(unittest.TestCase):

    def test_encode(self):
        self.assertEqual(morse.encode("SOS"), "... --- ...")
        self.assertEqual(morse.encode("sos"), "... --- ...")
        self.assertEqual(morse.encode("HI THERE"), ".... .. / - .... . .-. .")
        self.assertEqual(morse.encode("123"), ".---- ..--- ...--")
        self.assertEqual(morse.encode(""), "")

    def test_encode_invalid(self):
        with self.assertRaises(ValueError):
            morse.encode(123)
        with self.assertRaises(ValueError):
            morse.encode("HELLO!")

    def test_decode(self):
        self.assertEqual(morse.decode("... --- ..."), "SOS")
        self.assertEqual(morse.decode(".... .. / - .... . .-. ."), "HI THERE")
        self.assertEqual(morse.decode(".---- ..--- ...--"), "123")
        self.assertEqual(morse.decode(""), "")

    def test_decode_invalid(self):
        with self.assertRaises(ValueError):
            morse.decode(None)
        with self.assertRaises(ValueError):
            morse.decode("...---...")

    def test_round_trip(self):
        self.assertEqual(morse.decode(morse.encode("Hello World 2026")), "HELLO WORLD 2026")

    def test_count_signals(self):
        self.assertEqual(morse.count_signals("... --- ..."), (6, 3))
        self.assertEqual(morse.count_signals(""), (0, 0))
        self.assertEqual(morse.count_signals(".-"), (1, 1))

    def test_add_morse(self):
        self.assertEqual(morse.add_morse("..---", "...--"), ".....")
        self.assertEqual(morse.add_morse(".---- -----", "-----"), ".---- -----")
        self.assertEqual(morse.add_morse("---..", "--..."), ".---- .....")

    def test_add_morse_invalid(self):
        with self.assertRaises(ValueError):
            morse.add_morse(".-", "..---")


if __name__ == '__main__':
    unittest.main()
