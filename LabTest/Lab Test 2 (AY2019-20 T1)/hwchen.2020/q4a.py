# Name: Nicholas Chen Han Wei
# Email ID: hwchen.2020

def store_family_relations(family_file):
    res = {}
    # Modify the code below.
    with open(family_file) as families:
        for family in families:
            parents_data = family.split(':')[0]
            parents = parents_data[1:len(parents_data) - 1].split(',')
            children = family.split(':')[1].split(';')

            for i in range(len(parents)):
                rs = 'father' if i == 0 else 'mother'
                for child in children:
                    child_detail = child[1:len(child) - 1].split(',')
                    name = child_detail[0]
                    res[(parents[i], name)] = rs

            for child in children:
                child_detail = child[1:len(child) - 1].split(',')
                name = child_detail[0]
                gender = child_detail[1]
                for parent in parents:
                    res[(name, parent)] = 'daughter' if 'F' in gender else 'son'

    return res

