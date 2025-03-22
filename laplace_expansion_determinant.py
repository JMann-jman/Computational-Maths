def _2x2_determinant(matrix):
    if len(matrix) != 2:
        return Exception("Dimension Error")

def laplace_expansion_determinant(matrix):
    if len(matrix) != len(matrix[0]):
        return Exception("Dimension Error") # Checking matrix is square before taking determinant
    
    list_of_submatrices = []                # Initialise list of submatrices 
    list_of_associated_coefficients = []
    sign = 1
    for a in range(len(matrix[0])):         # Choose top row for laplace formula, so go through each column in the matrix
        list_of_associated_coefficients.append(matrix[0][a]*sign)
        sign *= -1

        sub_matrix = []                     # Create an empty submatrix. Naturally, this will have dimensions of n-1.
        for b in range(len(matrix)-1):      
            sub_matrix.append([])

        c = 0                                   # Form the matrix's submatrices - matrices of values from the original matrix which do
        for i in range(len(matrix)):            # not share the same column or row as the chosen value, in the chosen row.
            for j in range(len(matrix[0])):
                if((i != 0) and (j != a)):
                    sub_matrix[c].append(matrix[i][j])
            if(i != 0):
                c+=1        
        list_of_submatrices.append(sub_matrix)
        
    if len(list_of_submatrices[0]) != 2:        # All submatrices will have the same dimensions, if the submatrices are not 2x2, then this algorithm should repeat,
                                                # recursively, until the base case is reached.
        accumulated_determinant = 0
        coefficent_list_counter = 0
        for submatrix in list_of_submatrices:                                        
            accumulated_determinant += laplace_expansion_determinant(submatrix) * list_of_associated_coefficients[coefficent_list_counter]
            coefficent_list_counter += 1

        return accumulated_determinant

    else:                                       # This is for the base case, if the dimensions are 2x2, then the normal ad-bc formula is used.
        return_determinant = 0
        coefficent_list_counter = 0
        for submatrix in list_of_submatrices:
            return_determinant += _2x2_determinant(submatrix) * list_of_associated_coefficients[coefficent_list_counter]
            coefficent_list_counter += 1

        return return_determinant