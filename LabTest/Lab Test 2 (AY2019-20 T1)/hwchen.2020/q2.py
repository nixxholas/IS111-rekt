# Name: Nicholas Chen Han Wei
# Email ID: hwchen.2020

def get_longer_words(file_name):
    res = []
    # Modify the code below.
    with open(file_name) as lines:
        for line in lines:
            words = line.strip().split('&')
            res.append(words[0] if len(words[0]) > len(words[1]) else words[1])

    return res

