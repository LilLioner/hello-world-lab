import numpy as np
lista = [1,2,3]
lista2 = [4,5,6]

print(lista*2) #output = [1,2,3,1,2,3]
print(lista+lista2) #output = [1,2,3,4,5,6]

array = np.array([1,2,3])
array2 = np.array([4,5,6])

print(array*2) #output = [2,4,6]
print(array+array2) # output = [5,7,9]

           #A          0                1               2
alf = np.array([["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]])
           #B     0    1    2      0    1    2      0    1    2

print(alf[1,2]) # Output = [F]
# No caso de uma array bidimensional (apenas duas dimensões), 
# ficaria algo como print(alf[A,B])
              #A          0                1               2             C
tridm = np.array([[["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]], # 0 
                  [["J", "K", "L"], ["M", "N", "O"], ["P", "Q", "R"]], # 1
                  [["S", "T", "U"], ["V", "W", "X"], ["Y", "Z", " "]]])# 2
              #B     0    1    2      0    1    2      0    1    2
print(tridm[1 , 0 , 1]) # Output = [K]
# No caso da Tridimensional fica print(tridm[C,A,B])

np.mean()   # média
np.sum()    # soma
np.max()    # máximo
np.min()    # mínimo
np.std()    # desvio padrão