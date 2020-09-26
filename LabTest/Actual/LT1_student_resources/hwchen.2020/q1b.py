# Name: Nicholas Chen Han Wei
# Email ID: hwchen.2020

def is_compatible(patient_group, donor_group):
    return True if (patient_group == 'A' and (donor_group == "A" or donor_group == "AB")) or (
            patient_group == 'B' and (donor_group == "B" or donor_group == "AB")) or (
                           patient_group == 'AB' and donor_group == "AB") or (
                           patient_group == 'O' and (
                           donor_group == "O" or donor_group == "AB" or donor_group == "A" or donor_group == "B")) \
        else False
1