import unittest
from challenge4 import misc_functions as mf


class challenge4fibo(unittest.TestCase):

    def test_challenge4fibonacci(self):
        for i in range(30):
            f = mf.Fibonacci()
            c = mf.ConvertNumbertoString()
            num = f.fibo(i)
            print(str(num) + " - " + str(c.num2words(num)))


if __name__ == '__main__':
    unittest.main()
