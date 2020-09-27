def check_math(list_of_equations):
    correct = True

    operators = ["+","-","*","//","%"]
    equivalence = "="

    for equation in list_of_equations:
        equationHolds = True
        
        operatorIndex = 0
        equivalenceIndex = 0
        operation = ""

        equivalenceIndex = equation.index(equivalence)
        
        for operator in operators:
            if operator in equation:
                operation = operator
                operatorIndex = equation.index(operator)
                break

        #obtain numbers
        firstNum = int(equation[:operatorIndex])
        
        if operation == "//":
            secondNum = int(equation[operatorIndex+2:equivalenceIndex])
        else:
            secondNum = int(equation[operatorIndex+1:equivalenceIndex])

        resultant = int(equation[equivalenceIndex+1:])

        #evaluate
        if operator == "+":
            equationHolds = firstNum+secondNum == resultant
            
        elif operator == "-":
            equationHolds = firstNum-secondNum == resultant
            
        elif operator == "*":
            equationHolds = firstNum*secondNum == resultant
            
        elif operator == "//":
            equationHolds = firstNum//secondNum == resultant
            
        elif operator == "%":
            equationHolds = firstNum%secondNum == resultant

        if not equationHolds:
            return False

    return True
            
