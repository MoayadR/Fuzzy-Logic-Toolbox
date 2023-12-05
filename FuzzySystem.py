from Variable import Variable

class FuzzySystem():
    def __init__(self , name:str , desc:str , rules , variables:Variable)->None:
        self.name = name
        self.desc = desc
        self.rules = rules
        self.variables = variables