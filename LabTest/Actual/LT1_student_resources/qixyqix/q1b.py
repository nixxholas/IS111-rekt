def is_compatible(patient_group, donor_group):
    grpAB = "AB"
    grpO = "O"

    #AB can be accepted by ALL groups
    if donor_group == grpAB:
        return True
    #O can accept ALL groups
    elif patient_group == grpO:
        return True
    #Otherwise, check if patient and donor is the same grp
    elif patient_group == donor_group:
        return True
    #No match
    else:
        return False
    
    
