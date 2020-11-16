def get_document_pair(filename):
    documents = {}
    with open(filename) as file:
        for line in file:
            cols = line.rstrip().split('\t')
            documents[cols[0]] = set(cols[1].split(' '))

    pair_data = {}
    for main_key in documents.keys():
        main_sub_pair = documents[main_key]
        for sub_key in documents.keys():
            if main_key != sub_key:
                key = (main_key, sub_key)
                if (key not in pair_data.keys()) and ((sub_key, main_key) not in pair_data.keys()):
                    counter_sub_pair = documents[sub_key]
                    intersect_count = len(set(main_sub_pair).intersection(set(counter_sub_pair)))
                    pair_data[key] = intersect_count

    tuple_list = []
    for key in pair_data:
        # tuple_list.append((key[0], key[1], pair_data[key]))
        tuple_list = push_and_check(tuple_list, (key[0], key[1], pair_data[key]))
    return tuple_list


def push_and_check(collection, incoming_tuple):
    if len(collection) == 0:
        collection.append(incoming_tuple)
    else:
        new_collection = []
        for c in collection:
            if c[2] >= incoming_tuple[2]:
                new_collection.append(c)

        if len(new_collection) == 0:
            new_collection.append(incoming_tuple)
        elif new_collection[0][2] == incoming_tuple[2]:
            new_collection.append(incoming_tuple)

        collection = new_collection

    return collection
