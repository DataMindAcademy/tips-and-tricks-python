
print(f'\n{15*'*'} Tidak Pythonic {15*'*'}')

a = [10,20,30]
b = [40,50,60]
c = [None]*(len(a) + len(b))

for i in range(len(a)):
    c[i] = a[i]
for j in range(len(b)):
    c[j + len(a)] = b[j]

print(f'hasil c = {c}')

'''
list = sequence data types yang dapat menampung sekumpulan nilai tanpa mengharuskan keseragaman dalam tipe data 
'''


print(f'\n{15*'*'} Pythonic {15*'*'}')

c = a + b

print(f'hasil c = {c}')

