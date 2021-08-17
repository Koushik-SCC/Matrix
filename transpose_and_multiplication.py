'''
Transpose of matrices
'''
x = [[1,2,3],[1,2,2],[0,0,0]]

trans1 = [[x[i][j] for i in range(len(x))]for j in range(len(x[0]))]
print('Transpose of the matrix: ')
for v in trans1:
    print(v)

# another method of the transpose
trans2 = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(x)):
    for j in range(len(x[0])):
        trans2[i][j] = x[j][i]
print('Transpose of the matrix:')
for p in trans2:
    print(p)
'''
matrix multiplication
'''
x = [[1,2,3],[1,2,2],[0,0,0]]
y = [[1,0,0],[0,1,0],[0,0,1]]
z = [[0,0,0],[0,0,0],[0,0,0]]

print('1st Matrix is')
for q in x:
    print(q)

print()

print('Second Matrix is')
for w in y:
    print(w)
    
    
print()

for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            z[i][j]= z[i][j] + x[i][k] * y[k][j]
        
print('Result of Multiplication is')        
for s in z:
    print(s)
    
    
