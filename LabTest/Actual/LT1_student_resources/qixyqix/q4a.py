def trace_contacts(patient, history):
    infectedList = []

    for contactCase in history:
        if patient in contactCase and contactCase[2] > -6:
            newlyInfected = None
            if contactCase[0] == patient:
                newlyInfected = contactCase[1]
            else:
                newlyInfected = contactCase[0]

            infectionDay = contactCase[2]

            infectedList.append(newlyInfected)
            print(infectedList)

            #AHH TOO LAZY DO IT AGAIN NEXT TIME LEL

##            updatedHistoryList = []
##            for case in history:
##                updatedHistoryList.append((case[0],case[1],case[2]-infectionDay))
##
##            addedInfections = trace_contacts(newlyInfected, updatedHistoryList)
##            for newInfection in addedInfctions:
##                if newInfection not in infectedList:
##                    infectedList.append(newInfection)

    return infectedList
            
        
    
    
