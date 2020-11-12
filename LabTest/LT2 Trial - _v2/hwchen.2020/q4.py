def get_document_pair(filename):
    # Modify the code below.
    subpairs = {}
    with open(filename) as doc:
        for subpair in doc:
            data = subpair.rstrip().split('\t')
            subpairs[data[0]] = data[1]

    best_pair = None
    pairs = {}
    combinations = combination(len(subpairs.keys()))
    while combinations > len(pairs.keys()) and len(subpairs.keys()) > 0:
        cur_key = subpairs.popitem()
        # Create n + 1 number of pairs with n as the first key
        for key in subpairs.keys():
            matches = 0
            # Traverse pairs, convert them to sets then back to lists to make them unique.
            cur_key_words = list(set(cur_key[1].split(' ')))
            comp_key_str_words = list(set(subpairs[key].split(' ')))

            for cur_key_word in cur_key_words:
                if cur_key_word in comp_key_str_words:
                    matches += 1

            if (cur_key, key) not in pairs.keys():
                pairs[(cur_key[0], key)] = matches
            if best_pair is None or best_pair[2] < matches:
                best_pair = (cur_key[0], key, matches)

    return best_pair


def combination(n):
    val = n
    for i in range(n - 1, 0, -1):
        val += i
    return val
