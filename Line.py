from Point import Point
from math import inf

class Line():
    def __init__(self , startPoint:Point , endPoint:Point) -> None:
        self.startPoint = startPoint
        self.endPoint = endPoint
        self.slope = self.calculateSlope()
        self.bias = self.caculateBias()
    
    def calculateSlope(self) -> float:
        return (self.endPoint.y - self.startPoint.y) / (self.endPoint.x - self.startPoint.x) if (self.endPoint.x - self.startPoint.x) != 0 else inf

    def caculateBias(self) ->float:
        return (self.startPoint.y - (self.slope * self.startPoint.x)) if self.slope != inf else inf

    def isInRange(self, x:int) -> int:
        return True if x >= self.startPoint.x and x<= self.endPoint.x else False
    
    def predict(self , x:int)-> int:
        return max(self.startPoint.y , self.endPoint.y) if self.slope == inf else (self.slope * x) + self.bias # math notation for return 1

        