import movies_utility

movie_list = [("The Shawshank Redemption", "drama", 142), 
        ("The Godfather", "drama", 175), 
        ("The Lord of the Rings: The Return of the King", "fantasy", 201), 
        ("Forrest Gump", "comedy", 142), 
        ("The Lord of the Rings: The Fellowship of the Ring", "fantasy", 178), 
        ("Star Wars: Episode IV - A New Hope", "fantasy", 121), 
        ("The Lion King", "animation", 88)]
       
    
# Test cases used to test your functions

print('\nTesting : get_average_duration()')
print('================================')
print('\nTestcase 1')
print('-' * 10)
print('Expected: 0.0')
print('Actual:   ' + str(movies_utility.get_average_duration([])))

print('\nTestcase 2')
print('-' * 10)
print('Expected: 149.6')
print('Actual:   ' + str(round(movies_utility.get_average_duration(movie_list),1)))


print('\nTesting : get_num_movies_of_genre()')
print('===================================')
print('\nTestcase 1')
print('-' * 10)
print('Expected: 2')
print('Actual:   ' + str(movies_utility.get_num_movies_of_genre(movie_list, "drama")))

print('\nTestcase 2')
print('-' * 10)
print('Expected: 3')
print('Actual:   ' + str(movies_utility.get_num_movies_of_genre(movie_list, "fantasy")))


print('\nTesting : get_title_of_longest_movie()')
print('======================================')
print('\nTestcase 1')
print('-' * 10)
print('Expected: The Lord of the Rings: The Return of the King')
print('Actual:   ' + str(movies_utility.get_title_of_longest_movie(movie_list)))


print('\nTesting : get_movies_with_keyword()')
print('===================================')
print('\nTestcase 1')
print('-' * 10)
print("Expected: [('The Lord of the Rings: The Return of the King', 'fantasy', 201), ('The Lion King', 'animation', 88)]")
print('Actual:   ' + str(movies_utility.get_movies_with_keyword(movie_list, "King")))

print('\nTestcase 2')
print('-' * 10)
print("Expected: [('The Lord of the Rings: The Return of the King', 'fantasy', 201), ('The Lord of the Rings: The Fellowship of the Ring', 'fantasy', 178)]")
print('Actual:   ' + str(movies_utility.get_movies_with_keyword(movie_list, "Lord")))

print('\nTestcase 3')
print('-' * 10)
print("Expected: []")
print('Actual:   ' + str(movies_utility.get_movies_with_keyword(movie_list, "Hello")))












