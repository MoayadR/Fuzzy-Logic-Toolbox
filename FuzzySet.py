from Line import Line
from Point import Point
from math import inf

class FuzzySet():
    def __init__(self , name:str , type:str , values:list , variableLower:int , variableUpper:int) -> None:
        self.name = name
        self.type = type
        self.values = values
        self.variableUpper = variableUpper
        self.variableLower = variableLower
        self.points = self.generatePoints()
        self.lines = self.generateLines()

    def generatePoints(self)->list:
        res = []
        for i in range(len(self.values)):
            if self.values[i] > self.variableUpper:
                self.values[i] = self.variableUpper
            
            if i == 0 or i == len(self.values) -1:
                point = Point(self.values[i] , 0)
            else:
                point = Point(self.values[i] , 1)
            res.append(point)
        return res

    def generateLines(self) ->list:
        res = []
        for i in range(len(self.points)-1):
            res.append(Line(self.points[i] , self.points[i+1]))
        return res

    def isInRange(self , x:int) ->bool: # upper and lower for the fuzzySet
        return True if x>= self.values[0] and x<= self.values[-1] else False
    
    def getInRangeLines(self , x:int)->list[Line]:
        res = []
        for line in self.lines:
            if line.isInRange(x):
                res.append(line)
        return res
    
    def fuzzyfication(self , value) -> float:
        lines = list(filter(lambda x : x.isInRange(value) == True , self.lines))
        return lines[0].predict(value)

    def calcCentroid (self):
        return sum(self.values)/len(self.values)

    
        