from Variable import Variable
from FuzzySet import FuzzySet
from FuzzySystem import FuzzySystem
from Rule import Rule
from math import inf
import re

def createRule(fuzzySystem:FuzzySystem , variableNames:list , operatorNames:list  , setNames:list,  outVariableName:str , outSetName:str ) -> Rule:
    variables = []
    fuzzySets = []
    for i in range(len(variableNames)):
        matchedVar = list(filter(lambda x : x.name ==  variableNames[i] ,fuzzySystem.variables))[0]
        matchedSet = list(filter(lambda x : x.name ==  setNames[i] , matchedVar.fuzzySets))[0]
        variables.append(matchedVar)
        fuzzySets.append(matchedSet)
    
    out_variable = list(filter(lambda x : x.name ==  outVariableName ,fuzzySystem.variables))[0]
    out_variableSet = list(filter(lambda x : x.name ==  outSetName ,out_variable.fuzzySets))[0]

    return Rule(variables , fuzzySets , operatorNames , out_variable , out_variableSet)


def addRules(fuzzySystem:FuzzySystem) -> None:
    print("Enter the rules in this format: (Press x to finish)\nIN_variable set operator IN_variable set => OUT_variable set")
    print("--------------------------------------------------------------------------------")

    while True:
        line = input()
        variableNames = []
        operatorNames = []
        setNames = []
        outVariableName = None
        outSetName = None
        if line == 'x':
            break
        line = line.split(' ')
        

        if line[0] == 'not': # fix this later
            operatorNames.append(line[0])
            variableNames.append(line[1])
            setNames.append(line[2])
            if "not" in line[3]:
                operatorNames.append(line[3].split('_')[0])
                operatorNames.append('not')
            else:
                operatorNames.append(line[3])
                
            variableNames.append(line[4])
            setNames.append(line[5])
            i = 6
        else:
            variableNames.append(line[0])
            setNames.append(line[1])

            if "not" in line[2]:
                operatorNames.append(line[2].split('_')[0])
                operatorNames.append('not')
            else:
                operatorNames.append(line[2])

            variableNames.append(line[3])
            setNames.append(line[4])
            i = 5

        while i < len(line):
            if line[i] == '=>':
                break

            if "not" in line[i]:
                operatorNames.append(line[i].split('_')[0])
                operatorNames.append('not')
            else:
                operatorNames.append(line[i])

            variableNames.append(line[i+1])
            setNames.append(line[i+2])
            i+=3

        outVariableName = line[-2]
        outSetName = line[-1]
        fuzzySystem.addRule(createRule(fuzzySystem , variableNames , operatorNames , setNames , outVariableName ,outSetName ))



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
            addRules(fuzzySystem)
        elif choice == 4:
            if fuzzySystem.rules == 0 or fuzzySystem.variables == 0:
                continue
            
            inputVariables = fuzzySystem.getInputVariables()
            variablesValues = {}
            for var in inputVariables:
                print(f"{var.name}:")
                value = int(input())
                variablesValues[var] = value
            
            outFuzzySetsValues = []
            for rule in fuzzySystem.rules:
                rule.createFuzzificationList(variablesValues)
                outFuzzySetsValues.append(rule.inference())

            finalResult = fuzzySystem.defuzzyfication(outFuzzySetsValues)
            print(finalResult)
                
        else:
            break
            
def main():
    print("Fuzzy Logic Toolbox\n===================")
    while True:
        choice = int(input("1- Create a new fuzzy system \n2- Quit\n"))
        if choice == 1:
            mainMenu()
        else:
            break

    


if __name__ == '__main__':
    main()