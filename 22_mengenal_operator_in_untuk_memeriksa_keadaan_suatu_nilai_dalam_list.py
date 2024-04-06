print(f'\n{15*'*'} Tidak Pythonic {15*'*'}')

my_list = [10,20,30,40,50]
search = 40
status = False

for data in my_list:
    if data == search:
        status = True
        break

if status:
    print('angka di temukan')
else:
    print('angka tidak di temukan')
    

print(f'\n{15*'*'} Pythonic {15*'*'}')

if search in my_list:
    print('angka di temukan')
else: 
    print('angka tidak di temukan')