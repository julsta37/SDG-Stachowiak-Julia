import numpy as np
print("hello")

#ZADANIE 1
np_array = np.random.randint(1, 100, 15)
print(np_array)
print(np.min(np_array))
print(np.max(np_array))
print(np.std(np_array))

#ZADANIE 2
np_array2 = np.random.randint(100, size = (4,4))
print(np_array2)

print(np_array2.sum(axis = 0))
print(np_array2.sum(axis = 1))

#ZADANIE 3
np_array3 = np.arange(1, 76, 3)
print(np_array3)

print(np_array3.reshape(5,5))
indeksy = np.where((np_array3 % 2 == 0) & (np_array3 > 10))
print(indeksy)