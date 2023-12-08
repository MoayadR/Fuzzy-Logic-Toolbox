from Variable import Variable
from Rule import Rule

class FuzzySystem():
    def __init__(self , name:str = None , desc:str = None , rules:list[Rule] = [] , variables:list[Variable] = [])->None:
        self.name = name
        self.desc = desc
        self.rules = rules
        self.variables = variables
    
    def addVariable(self , variable:Variable) -> None:
        self.variables.append(variable)
    
    def addRule(self , rule:Rule )->None:
        self.rules.append(rule)

    def getInputVariables(self)->list[Variable]:
        return list(filter(lambda x : x.type == 'IN' , self.variables))

    def defuzzyfication(self, outSetsValues : list[list]) -> float :
        result =0
        sum =0 
        for L in outSetsValues:
           mul = L[0].calcCentroid() * L[1]
           result += mul
           sum += L[1]
        return result/sum

        
