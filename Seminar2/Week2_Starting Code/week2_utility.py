def get_insurance_premium(age, gender):
    """
    This function takes in the age and gender of a person.
    It returns the health insurance premium this person has
    to pay based on his/her age and gender. 
    Parameters:
        age (int): This is the age of the person.
        gender (str, either 'M' or 'F'): This is the gender
                of the person.
    Return:
        the insurance premium of the person
    """
    if gender == 'M':
        if age >= 50:
            return 300
        elif age >= 35:
            return 250
        else:
            return 150
    else:
        if age >= 50:
            return 320
        elif age >= 35:
            return 270
        else:
            return 160