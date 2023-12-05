class Rule():
    def __init__(self , rule:str):
        self.parse(rule)

        self.inVariable1 = None
        self.inVariable2 = None

        self.set1 = None
        self.set2 = None
        
        self.outVariable = None
        self.outSet = None

    def parse(rule:str)->None:
        pass