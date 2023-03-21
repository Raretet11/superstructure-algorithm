from superstructure_algorithm import SuperstructureAlgorithm
from typing import List

class FastSuperstructureAlgorithm(SuperstructureAlgorithm):
    def __init__(self) -> None:
        super().__init__()
        self._s: List[str] = []
        self._len_s: int = 0
        self._result: str = ""

    def compute_superstructure(self, s: List[str]) -> str:
        self._s = s
        self._len_s = len(s)
        self._result = self._s[0]
        self._s.pop(0)
        while len(self._s) != 0:
            self._update_result()
        return self._result

    def _update_result(self) -> None:
        t_ind: int = -1
        l_ind: int = -1
        for ind, el in enumerate(self._s):
            if t_ind == -1 or len(self._overlap(self._s[t_ind], self._result)) < len(self._overlap(el, self._result)):
                t_ind = ind
        for ind, el in enumerate(self._s):
            if l_ind == -1 or len(self._overlap(self._result, self._s[l_ind])) < len(self._overlap(self._result, el)):
                l_ind = ind

        if len(self._overlap(self._s[t_ind], self._result)) > len(self._overlap(self._result, self._s[l_ind])):
            self._result = self._combine(self._s[t_ind], self._result)
            self._s.pop(t_ind)
        else:
            self._result = self._combine(self._result, self._s[l_ind])
            self._s.pop(l_ind)
    
    def _overlap(self, s: str, t: str) -> str:
        for overlap_start_ind in range(len(s)):
            if s[overlap_start_ind:] == t[:len(s) - overlap_start_ind]:
                return s[overlap_start_ind:]
        return ""
    
    def _combine(self, s: str, t: str) -> str:
        for overlap_start_ind in range(len(s)):
            if s[overlap_start_ind:] == t[:len(s) - overlap_start_ind]:
                return s + t[len(s) - overlap_start_ind:]
        return s + t
    