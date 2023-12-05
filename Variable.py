from FuzzySet import FuzzySet

class Variable():
    def __init__(self , name:str ,lower:int , upper:int) -> None:
        self.name = name
        self.upper = upper
        self.lower = lower
        self.fuzzySets = []
    
    def addFuzzySet(self , fuzzySet:FuzzySet)->None:
        self.fuzzySets.append(fuzzySet)