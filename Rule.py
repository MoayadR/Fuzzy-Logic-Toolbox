from Variable import Variable 
from FuzzySet import FuzzySet

class Rule():
    def __init__(self , variables:list[Variable] , fuzzySets:list[FuzzySet] , operators:list[str] ,outVariable:Variable , outSet:FuzzySet ):
        self.variables = variables
        self.fuzzySets = fuzzySets
        self.operators = operators
        self.outVariable = outVariable
        self.outSet = outSet