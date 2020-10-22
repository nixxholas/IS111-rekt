### Q2c: Universities 
# Write your code below:
def search_with_keyword(file_name, keyword):
    file = open(file_name, 'r')
    acronyms = []

    for line in file:
        uni_datum = line.rstrip().split('\t')

        if keyword.lower() in uni_datum[0].lower():
            acronyms.append(uni_datum[1])

    return acronyms

