from Variable import Variable 
from FuzzySet import FuzzySet

class Rule():
    def __init__(self , inVariable1:Variable = None , inVariable2:Variable = None , operator:str = None , set1:FuzzySet = None,
                 set2:FuzzySet = None , outVariable:Variable = None , outSet:FuzzySet = None):
        self.inVariable1 = inVariable1
        self.inVariable2 = inVariable2

        self.operator = operator

        self.set1 = set1
        self.set2 = set2
        
        self.outVariable = outVariable
        self.outSet = outSet
