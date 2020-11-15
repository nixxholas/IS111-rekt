def get_n_top_words(filename, n=3):
    word_counter = {}

    with open(filename) as article_1:
        for line in article_1:
            words = line.rstrip().split(' ')

            for word in words:
                word = ''.join([i for i in word if i.isalpha()]).lower()

                if word != '':
                    if word in word_counter.keys():
                        word_counter[word] += 1
                    else:
                        word_counter[word] = 1

    top_n = []

    while len(top_n) < n:
        cur_key = word_counter.popitem()
        top_n.append((cur_key[0], cur_key[1]))
    top_n.sort(key=lambda x: x[1])
    while len(word_counter.keys()) > 0:
        word = word_counter.popitem()
        for i in range(len(top_n)):
            if top_n[i][1] < word[1]:
                top_n[i] = (word[0], word[1])
                top_n.sort(key=lambda x: x[1])
                break

    return top_n[::-1]


print(get_n_top_words('article-1.txt'))
print(get_n_top_words('article-2.txt'))