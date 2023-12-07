from Variable import Variable
from FuzzySet import FuzzySet
from FuzzySystem import FuzzySystem
from Rule import Rule
from math import inf
import re

def addRules(rules:list[Rule] , systemVariables:list[Variable]) -> None:
    print("Enter the rules in this format: (Press x to finish)\nIN_variable set operator IN_variable set => OUT_variable set")
    print("--------------------------------------------------------------------------------")

    in_variableName1 = ''
    in_variableName2 = ''
    in_variableSet1 = ''
    in_variableSet2 = ''
    operator = ''
    out_variableName = ''
    out_variableSet = ''

    while True:
        line = input()
        line = line.split(' ')
        if line == 'x':
            break
        in_variableName1 = line[0]
        in_variableSet1 = line[1]
        operator = line[2]
        in_variableName2 = line[3]
        in_variableSet2 = line[4]
        out_variableName = line[-2]
        out_variableSet = line[-1]

        matchedVar1 = list(filter(lambda x : x ==  in_variableName1 ,systemVariables))[0]
        matchedSet1 = list(filter(lambda x : x ==  in_variableSet1 ,matchedVar1.fuzzySets))[0]

        matchedVar2 = list(filter(lambda x : x ==  in_variableName2 ,systemVariables))[0]
        matchedSet2 = list(filter(lambda x : x ==  in_variableSet2 ,matchedVar2.fuzzySets))[0]

        out_variableName = list(filter(lambda x : x ==  out_variableName ,systemVariables))[0]
        out_variableSet = list(filter(lambda x : x ==  out_variableSet ,out_variableName.fuzzySets))[0]

        rule = Rule(matchedVar1, matchedVar2, operator, matchedSet1, matchedSet2, out_variableName, out_variableSet)
        rules.append(rule)



def createFuzzySets(names:list[str] , types:list[str] , valuesList:list[str] , varLower:float , varUpper:float)->list[FuzzySet]:
    res = []
    for i in range(len(names)):
        res.append(FuzzySet(names[i] , types[i] , valuesList[i] , varLower , varUpper))
    return res

def addFuzzySets(systemVariables:list[Variable])-> None:
    print("Enter the variable’s name:")
    print("--------------------------")
    variableName = input()

    var = list(filter(lambda x : x.name == variableName , systemVariables))[0]

    print("Enter the fuzzy set name, type (TRI/TRAP) and values: (Press x to finish)")
    print("-------------------------------------------------------------------------")


    names = []
    types = []
    valuesList = []

    line = None
    while True:
        line = input()
        if line == 'x':
            break
        line = line.split(' ')
        name = line[0]
        type = line[1]
        values = list(map(lambda x : int(x) , line[2:]))

        names.append(name)
        types.append(type)
        valuesList.append(values)
    
    for i in createFuzzySets(names , types , valuesList , var.lower , var.upper):
        var.addFuzzySet(i)
    
        


def parseVariables(line :str):
    pattern = r'(?P<variable>\w+)\s+(?P<type>[\w\s]+)\s+\[\s*(?P<lower>\d+)\s*,\s*(?P<upper>\d+)\s*\]'
    match = re.match(pattern, line)

    if match:
        variable = match.group('variable')
        type = match.group('type').strip()
        lower_limit = int(match.group('lower'))
        upper_limit = int(match.group('upper'))
        return variable, type, lower_limit, upper_limit
    else:
        return None


def createVariables(names:list[str] , types:list[str] , lowers:list[str] , uppers:list[str]) -> list[Variable]:
    res = []
    for i in range(len(names)):
        res.append(Variable(names[i] , types[i] , lowers[i] , uppers[i]))
    return res

def addVariables() -> list[Variable]:
    print("Enter the variable’s name, type (IN/OUT) and range ([lower, upper]):\n(Press x to finish)")
    print("-----------------------------------------------------------------------------------------")

    line = None
    names = []
    types = []
    lowers = []
    uppers = []

    while True:
        line = input()
        if line == 'x':
            break
        name , type , lower , upper = parseVariables(line)
        names.append(name)
        types.append(type)
        lowers.append(lower)
        uppers.append(upper)
    
    return createVariables(names , types , lowers , uppers)

def mainMenu():
    name = input("Enter the system’s name and a brief description:\n------------------------------------------------\n")
    desc = input()
    fuzzySystem = FuzzySystem(name = name , desc = desc)
    
    print("Main Menu:\n==========")
    while True:
        print("1- Add variables.")
        print("2- Add fuzzy sets to an existing variable.")
        print("3- Add rules.")
        print("4- Run the simulation on crisp values.")

        choice = int(input())
        if choice == 1:
            # add Variable
            for i in addVariables():
                fuzzySystem.addVariable(i)

        elif choice == 2:
            addFuzzySets(fuzzySystem.variables)
        elif choice == 3:
            addRules(fuzzySystem.rules , fuzzySystem.variables)
        else:
            pass

def main():
    print("Fuzzy Logic Toolbox\n===================")
    while True:
        choice = int(input("1- Create a new fuzzy system \n2- Quit\n"))
        if choice == 1:
            mainMenu()
            break
        else:
            break

    


if __name__ == '__main__':
    main()