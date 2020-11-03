from q5a import count_words_in_file

file = 'spam_sms.txt'
my_dict = count_words_in_file(file)

for word in my_dict:
    if len(word) >= 4 and my_dict[word] > 50:
        print(word + ' : ' + str(my_dict[word]))
