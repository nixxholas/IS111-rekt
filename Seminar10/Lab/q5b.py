### Q5b: Matrix
import copy
from q5a import get_matrix

# Write your code below:
def get_matrix_transpose(file_name):
    orig_matrix = get_matrix(file_name)
    new_matrix = copy.deepcopy(orig_matrix)

    # For every row in the matrix
    for i in range(len(orig_matrix)):
        # For every column in the row
        for j in range(len(orig_matrix[i])):
            # i.e. 0,0 becomes 0,0; 1,0 becomes 0,1
            new_matrix[j][i] = orig_matrix[i][j]


    return new_matrix
