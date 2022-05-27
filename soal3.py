import string
# file1 = input('Masukkan nama file 1 : ')
# file2 = input('Masukkan nama file 2 : ')

try:
    handle1 = open('berita1.txt')
    handle2 = open('berita2.txt')

except:
    print('File eror atau tidak ditemukan !!')
    exit()

unik1 = set()
unik2 = set()


for line in handle1:
    line = line.replace(".",'')
    line = line.replace(',','')
    line = line.lower().strip().split()
    for i in line:
        unik1.add(i)

    

for line in handle2:
    line = line.replace('.','')
    line = line.replace(',','')
    line = line.lower().strip().split()
    for j in line:
        unik2.add(j)
    
    

print(unik1 & unik2)