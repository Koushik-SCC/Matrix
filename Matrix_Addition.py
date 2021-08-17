#matrix operations using list of lists


A = [[1,2,-5,6],[5,1,9,7],[0,0,0,0]]
B = [[0,0,0,0],[1,5,1,1],[-7,-8,5.6,8.5]]
C = [[0,0,0,5],[0,0,0,0],[8,7,6,1]]
D = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]


row = len(A)
col = len(A[0])         #len(A[0]) will show len of 0th element([1,2,-5,6]) of A we can also use len(A[1]) 

#1st loop will go for 3 times for rows and 2nd loop will go for 4 times for colums 
# because the shape of matrix D will be 3,4
for i in range(row):
    for j in range(col):
        D[i][j] = A[i][j] + B[i][j] + C[i][j]        #replace values of D by A+B+C
        
        
        
print('Matrix D :')        
for r in D:      #printing the values of D one by one and not in same line
    print(r)        



print()             #for gap


#Matrix addition by list comprehension
E = [[1,2,-5,6],[5,1,9,7],[0,0,0,0]]
F = [[0,0,0,0],[1,5,1,1],[-7,-8,5.6,8.5]]
G = [[0,0,0,5],[0,0,0,0],[8,7,6,1]]

H = [[A[i][j] + B[i][j] + C[i][j] for j in range(col)] for i in range(row)]

print('Matrix H :')
for s in H:
    print(s) 

print()
        


# define matrix in numpy
from numpy import *

x = matrix('2 3 5;8 72 2; -1 -8 -1')
print(x)