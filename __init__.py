from Variable import Variable
from FuzzySet import FuzzySet
from math import inf

def main():
    
    var = Variable("temp" , 0 , 110)
    var.addFuzzySet(FuzzySet("freezing" , "TRO" , [0 , 0 , 30 , 50] ,0 , 110))
    var.addFuzzySet(FuzzySet("cool" , "TRI" , [30 , 50 , 70],0 , 110))
    var.addFuzzySet(FuzzySet("warm" , "TRI" , [50 , 70 , 90],0 , 110))
    var.addFuzzySet(FuzzySet("hot" , "TRO" , [70 , 90 , inf , inf ],0 , 110))

    value = 65
    for s in var.fuzzySets:
        if s.isInRange(value):
            print(s.name)
            print(s.getInRangeLines(value)[0].predict(value))

    


if __name__ == '__main__':
    main()