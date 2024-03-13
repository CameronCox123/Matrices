# File: Matrices
# Author: Cameron Cox
# UT EID: cpc2526
# Course: cs303E

import random



def make_matrix(num_rows, num_cols):
    """
    Generrates a matrix of variable length filled with random 1s and 0s.  

    :num_rows: Int. Determines the number of rows that will be generated in the matrix

    :num_cols: Int. Determines the number of rows that will be generated in the matrix

    :matrix: returns the generated matrix
    """

    # initalizes the matrix and other variables
    matrix = []
    random_num_list = []
    length = num_cols

    # loops through the rows and columns
    while num_rows > 0:
        while num_cols > 0:
            
            # For each number of column a random 1 or 0 is generated and appended to our temporary list
            randomNum = random.randint(0,1)
            random_num_list.append(randomNum)
            num_cols -= 1

        # appends temporary our list of random 1s and 0s to matrix  
        # typecasting to a list to make matrix point to unique object in memory instead of the same list for 
        # each row
        # moves through while loop
        matrix.append(list(random_num_list))
        random_num_list.clear()

        num_rows -= 1
        num_cols = length
    
    return(matrix)



def even_cols(matrix):
    """
    Takes a matrix and loops through it, appending the position of each column with an even number of 1s.

    :matrix: List. The matrix we will loop through.

    :even_col_list: List. Holds the positions of columns in the inputed matrix that have an even number of 1s
    """

    one_counter = 0
    even_col_list = []

    # loops through our matrix by column. Sums the number of 1s in a column.
    for k in range(len(matrix[0])):
        for j in range(len(matrix)):

            if matrix[j][k] == 1:
                one_counter += 1

        # if there is an even number of 1s in the column we append the index of the column to our returned list
        if one_counter % 2 == 0:
            even_col_list.append(k)

        one_counter = 0
    
    return(even_col_list)


def even_rows(matrix):
    """
    Takes a matrix and loops through it, appending the position of each row with an even number of 1s.

    :matrix: List. The matrix we will loop through.

    :even_row_list: List. Holds the positions of columns in the inputed matrix that have an even number of 1s
    """

    one_counter = 0
    even_row_list = []

    # loops through our matrix by row. Sums the number of 1s in a row.
    for k in range(len(matrix[0])):
        for j in range(len(matrix)):

            if matrix[k][j] == 1:
                one_counter += 1

        # if there is an even number of 1s in the row we append the index of the row to our returned list
        if one_counter % 2 == 0:
            even_row_list.append(k)

        one_counter = 0
    
    return(even_row_list)

"""
Driver Code
"""

def main():
    # Example variables for matrix
    num_rows = 5
    num_cols = 5

    matrix = make_matrix(num_rows, num_cols)
    print(matrix)
    print()
    print(f'Columns with an even number of 1s: {even_cols(matrix)}')
    print(f'Rows with an even number of 1s: {even_rows(matrix)}')
    
if __name__ == '__main__':
    main()