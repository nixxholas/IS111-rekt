def get_max_of_min(list_of_num_tuples):
    largestNum = None
    
    for numberTuple in list_of_num_tuples:
        tupleSmallestNum = None
        
        for number in numberTuple:
            if tupleSmallestNum == None or number < tupleSmallestNum:
                tupleSmallestNum = number

        if largestNum == None or tupleSmallestNum > largestNum:
            largestNum = tupleSmallestNum

    return largestNum
