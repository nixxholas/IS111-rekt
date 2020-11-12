def get_document_pair(filename):  # Load, iterate, replace
    sub_pairs = []
    with open(filename) as doc:
        for line in doc:
            data = line.rstrip().split('\t')
            sub_pairs.append(data)

    best_pair = None
    while len(sub_pairs) > 0:
        cur_key = sub_pairs.pop()
        # Create n - 1 number of pairs where n = length of sub_pairs
        for kvp in sub_pairs:
            matches = len(set(cur_key[1].split(' ')).intersection(set(kvp[1].split(' '))))
            if best_pair is None or best_pair[2] < matches:
                best_pair = (cur_key[0], kvp[0], matches)

    return best_pair


# Debugging function for nCr
def combination(n):
    val = 0
    for i in range(n - 1, 0, -1):
        val += i
    return val


    # You'll never know if you need to interact with more pairs in time to come.
    # pairs = {}
    # combinations = combination(len(sub_pairs.keys()))
    # while combinations > len(pairs.keys()) and len(sub_pairs.keys()) > 0:
    #     cur_key = sub_pairs.popitem()
    #     # Create n + 1 number of pairs with n as the first key
    #     for key in sub_pairs.keys():
    #         matches = 0
    #         # Traverse pairs, convert them to sets then back to lists to make them unique.
    #         cur_key_words = list(set(cur_key[1].split(' ')))
    #         comp_key_str_words = list(set(sub_pairs[key].split(' ')))
    #
    #         for cur_key_word in cur_key_words:
    #             if cur_key_word in comp_key_str_words:
    #                 matches += 1
    #
    #         if (cur_key, key) not in pairs.keys():
    #             pairs[(cur_key[0], key)] = matches
    #         if best_pair is None or best_pair[2] < matches:
    #             best_pair = (cur_key[0], key, matches)

