
print(f'\n{15*'*'} Tidak Pythonic - Tanpa Context Manager {15*'*'}')

access_file = open('./resource/file.txt','w')
access_file.write('belajar pemrograman python\n')
access_file.write('untuk keperluan bidang data science\n')
access_file.close()



print(f'\n{15*'*'} Tidak Pythonic - Dengan Context Manager {15*'*'}')

with open('./resource/file.txt','w') as my_file:
    my_file.write('saya belajar python\n')
    my_file.write('untuk mengelola resources dengan context manager\n')


with open('./resource/file.txt', 'r') as read_my_file:
    for index,line in enumerate(read_my_file.readlines()):
        print(f'\ndata index ke-{index} = {line}')
