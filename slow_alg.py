from superstructure_algorithm import SuperstructureAlgorithm
from typing import List, Set

class SlowSuperstructureAlgorithm(SuperstructureAlgorithm):
    def __init__(self) -> None:
        super().__init__()
        self._s: List[str] = []
        self._len_s: int = 0
        self._order: List[int] = []
        self._result: str = ""

    def compute_superstructure(self, s: List[str]) -> str:
        self._s = s
        self._len_s = len(s)
        self._order = [-1 for _ in range(self._len_s)]
        self._result = ""
        self._brute_recursion(0)
        return self._result
        
    def _brute_recursion(self, current_ind: int) -> None:
        if current_ind == self._len_s:
            current_result: str = ""
            reordered_strings: List[str] = ["" for _ in range(self._len_s)]
            for i, new_i in enumerate(self._order):
                reordered_strings[new_i] = self._s[i]
            current_result = reordered_strings[0]
            for next_string in reordered_strings[1:]:
                current_result = self._combine(current_result, next_string)
            if self._result == "" or len(current_result) < len(self._result):
                self._result = current_result
        else:
            possible_ind: Set[int] = set()
            for i in range(self._len_s):
                possible_ind.add(i)
            for el in self._order[:current_ind]:
                possible_ind.discard(el)
            for ind in possible_ind:
                self._order[current_ind] = ind
                self._brute_recursion(current_ind + 1)
    
    def _combine(self, s: str, t: str) -> str:
        for overlap_start_ind in range(len(s)):
            if s[overlap_start_ind:] == t[:len(s) - overlap_start_ind]:
                return s + t[len(s) - overlap_start_ind:]
        return s + t
    