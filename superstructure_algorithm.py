from typing import List
from abc import abstractmethod

class SuperstructureAlgorithm:    
    @abstractmethod
    def compute_superstructure(self, s: List[str]):
        pass
