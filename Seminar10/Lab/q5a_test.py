# DO NOT MODIFY THIS FILE
from q5a import get_matrix
    
# Test Case:

matrix = get_matrix('matrix.txt')
print("Expected: [[3.0, 9.0, 5.0], [2.0, 4.0, 1.0], [8.0, 2.0, 7.0]]")
print("Actual  : " + str(matrix))
print("Expected: <class 'float'>")
print("Actual  : " + str(type(matrix[0][0])))

