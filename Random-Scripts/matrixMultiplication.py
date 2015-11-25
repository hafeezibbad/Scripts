

import random
import time

# make python arrays
matrix=[[random.randint(1,100) for x in range(100)] for x in range (10000)]
#print matrix
#number of rows
mat_rows=len(matrix)
#number of columns
mat_columns=len(matrix[1])
#declare array for transpose
matrix_transpose=[[0 for x in range(mat_rows)] for x in range(mat_columns)]
#number of rows
transpose_rows=len(matrix_transpose)
#number of columns
transpose_col=len(matrix_transpose[1])
#for each row in matrix
for i in range(mat_rows):
    for j in range(mat_columns):
        matrix_transpose[j][i]= matrix[i][j]
#print matrix_transpose


#matrix_2=[[random.randint(1,5) for x in range(3)] for x in range (3)]
#print matrix_2
operations=0
time_before= time.time()
#check matrix multiplication limits
if (mat_columns!=transpose_rows):
    #matrix multiplication not possible
    print "Sorry, mismatching dimensions for multiplication"
    exit(-1)
else:
    #matrix multiplication possible
    # set a result matrix
    matrix_result=[[0 for x in range(mat_rows)] for x in range(transpose_col)]
    #for each row in matrix A
    for i in range(mat_rows):
        # for all columns in matrix A
        for j in range(mat_columns):
            #for all rows in matrix B
            for k in range(transpose_col):
                matrix_result[i][k]+=(matrix[i][j]*matrix_transpose[j][k])
                operations+=2

    #print matrix_result
    time_after= time.time()
    time_taken=time_after-time_before
    print "time taken : ", time_taken
    print "total operations: ", operations
