import numpy as np

m = int(input('number of rows, m = '))
n = int(input('number of columns, n = '))
#matrix1 = [[0 for j in range(n)] for i in range(m)]
#matrix2 = [[0 for j in range(n)] for i in range(m)]
matrix1=np.arange(m*n).reshape(m,n)
matrix2=np.arange(m*n).reshape(m,n)

print ('INPUT FOR 1st MATRIX')

for i in range (0,m):
    for j in range (0,n):
        print ('entry in row: ',i+1,' column: ',j+1)
        matrix1[i][j] = int(input())

print ('INPUT FOR 2nd MATRIX')

for i in range (0,m):
    for j in range (0,n):
        print ('entry in row: ',i+1,' column: ',j+1)
        matrix2[i][j] = int(input())

    
#result=[[0 for j in range(n)] for i in range(m)]
result=np.arange(m*n).reshape(m,n)

for i in range (0,m):
    for j in range (0,n):
        for k in range (0,n):
            result[i][j] = result[i][j] + matrix1[i][k] * matrix2[k][j];

   	 

print (result)
