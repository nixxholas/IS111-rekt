book_author_dict = {"Harry Potter and the Sorcerer's Stone":'J.K. Rowling',
               "Turtles All the Way Down":'John Green',
               "Animal Farm and 1984":'George Orwell',
               "The Da Vinci Code":'Dan Brown',
               "Harry Potter and the Goblet of Fire":'J.K. Rowling',
               "Origin":'Dan Brown'}

search = input('Do you want to search for the author of a book? [Y|N]') == 'Y'
while search:
    book_title = input('Please enter a book title :')

    if book_title in book_author_dict:
        print('The author of the book is', book_author_dict[book_title])
    else:
        print('Not found!')

    print()

    search = input('Do you want to continue? [Y|N]') == 'Y'

print('Good-bye!')