from Variable import Variable 
from FuzzySet import FuzzySet

class Rule():
    def __init__(self , variables:list[Variable] , fuzzySets:list[FuzzySet] , operators:list[str] ,outVariable:Variable , outSet:FuzzySet ):
        self.variables = variables
        self.fuzzySets = fuzzySets
        self.operators = operators
        self.outVariable = outVariable
        self.outSet = outSet
        self.fuzzyficationList = []
    
    def createFuzzificationList(self , variablesValues:dict)->None:
        for i in range(len(self.fuzzySets)):
            value = variablesValues[self.variables[i]]
            if self.fuzzySets[i].isInRange(value):
                self.fuzzyficationList.append(self.fuzzySets[i].fuzzyfication(value))
            else:
                self.fuzzyficationList.append(0)
    
    def applyNOT(self)->None:
        i = 0
        while i < len(self.operators):
            if self.operators[i] == 'not':
                self.fuzzyficationList[i] = 1 - self.fuzzyficationList[i]
                self.operators.pop(i)
                i -=1
            i+=1
    
    def applyAND(self)->None:
        i=0
        while i < len(self.operators):
            if self.operators[i] == 'and':
                value = min(self.fuzzyficationList[i] , self.fuzzyficationList[i+1])
                self.fuzzyficationList.pop(i)
                self.fuzzyficationList.pop(i)
                self.fuzzyficationList.insert(i , value)
                self.operators.pop(i)
                i -=1
            i+=1

    def applyOR(self)->None:
        i = 0
        while i < len(self.operators):
            if self.operators[i] == 'or':
                value = max(self.fuzzyficationList[i] , self.fuzzyficationList[i+1])
                self.fuzzyficationList.pop(i)
                self.fuzzyficationList.pop(i)
                self.fuzzyficationList.insert(i , value)
                self.operators.pop(i)
                i -=1
            i+=1

    def inference(self):
        self.applyNOT()
        self.applyAND()
        self.applyOR()
        return [self.outSet, self.fuzzyficationList[0]]
