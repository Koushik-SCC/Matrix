
L = [53,52,1,2,0,4]
# ascending

def bubble(L):
    n = len(L)
    for i in range(n):
        for j in range(n-i-1):
            if L[j] > L[j+1]:
                L[j+1],L[j] = L[j],L[j+1]
    return L
print('Sorted list(ascending):-',bubble(L))

# desceding       

def bubble(L):
    n = len(L)
    for i in range(n):
        for j in range(n-i-1):
            if L[j] < L[j+1]:
                L[j+1],L[j] = L[j],L[j+1]
    return L
print('Sorted list(descending):-',bubble(L))


# list of list 

a = [[1,10,2,4],[2,1,8,52],[0,4,7,9,6]]

def bubble(a):
    n = len(a)
    for i in range(n):
        m = len(a[i])
        for j in range(m):
            for k in range(m-j-1):
                if a[i][k] > a[i][k+1]:
                    a[i][k],a[i][k+1] = a[i][k+1],a[i][k]
    return a
print('Sorted list(ascending):-',bubble(a))