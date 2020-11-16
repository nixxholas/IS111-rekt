def get_num_common_words(doc1, doc2):
    
    # each doc is a tuple of (doc_id, word_list)
    word_list1 = doc1[1]
    word_list2 = doc2[1]
    
    common_word_list = []
    for word in word_list1:
        if word not in common_word_list and word in word_list2:
            common_word_list.append(word)
    return len(common_word_list)

def get_document_pair(filename):
    doc_list = []
    with open(filename, 'r') as input_file:
        for line in input_file:
            line = line.rstrip('\n')
            columns = line.split('\t')
            doc_id = columns[0]
            words = columns[1].split(' ')
            # each doc is a tuple: (doc_id, word_list)
            doc_list.append( (doc_id, words) )


    max_tuple = ('', '', -1)
    
    
    for index1 in range(len(doc_list) - 1):
        doc1 = doc_list[index1]
        for index2 in range(index1 + 1, len(doc_list)):
            doc2 = doc_list[index2]

            num_common_words = get_num_common_words(doc1, doc2)

            if num_common_words > max_tuple[2]:
                max_tuple = (doc1[0], doc2[0], num_common_words)

    return max_tuple

