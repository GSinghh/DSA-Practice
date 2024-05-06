def create_matrix(rows, columns):
    # This function will create a matrix of n length
    # Each row will be of length m
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            row.append(0)
        matrix.append(row)
    print(matrix)
    assert len(matrix) == rows
    assert len(matrix[0]) == columns
    
        
create_matrix(3, 4)