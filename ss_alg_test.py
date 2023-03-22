import unittest
from typing import List
import random
from slow_alg import SlowSuperstructureAlgorithm
from fast_alg import FastSuperstructureAlgorithm

class EasyTest(unittest.TestCase):
    def get_ratio(self, s: List[str]) -> float:
        a = SlowSuperstructureAlgorithm()
        b = FastSuperstructureAlgorithm()
        optimal_len = len(a.compute_superstructure(s))
        greedy_len = len(b.compute_superstructure(s))
        return greedy_len / optimal_len
    
    def random_string(self, len: int) -> str:
        result: str = ""
        for _ in range(len):
            result += chr(ord('a') + random.randrange(0, 26))
        return result

    def test_1(self):
       s = ['abc', 'bcf', 'gfr', 'tyu', 'qwe', 'gdshe']
       self.assertLess(self.get_ratio(s), 2.0)
    
    def test_one_string(self):
        s = ['abc']
        self.assertLess(self.get_ratio(s), 2.0)
    
    def test_two_equal_string(self):
        s = ['abc', 'abc']
        self.assertLess(self.get_ratio(s), 2.0)
    
    def test_multi(self):
        for _ in range(10):
            s = []
            for x in range(4):
                t = self.random_string(16)
                s.append(t)
            self.assertLess(self.get_ratio(s), 2.0)

    def test_many_overlaps(self):
        s = ['eabc', 'abcd', 'eaqbcf', 'afv', 'fq', 'vrt']
        self.assertLess(self.get_ratio(s), 2.0)
    
    def test_2(self):
        s = ['eabc', 'abcd', 'eac', 'hyt', 'iwgh', 'utd', 'utd']
        self.assertLess(self.get_ratio(s), 2.0)

