#data type list diubah ke type set
data_list = [21,34,99,100,88,99]
ubah_set = set(data_list)

#data type set diubah lagi ke type list
ubah_list = list(ubah_set)

#menampilkan output
print('Data awal (list)             :', data_list)
print('Data setelah diubah ke set   :',ubah_set)
print('Data dikembalikan ke list    :', ubah_list,'\n')

#data type tuple diubah ke type set
data_tuple = ('nila', 'lele', 'patin', 'gurame', 'hiu', 'lele','nilai')
ubah_set2 = set(data_tuple)

#mengubah typenya ke tuple lagi
ubah_tuple = tuple(ubah_set2)

#menampilkan output
print('Data awal (tuple)            :',data_tuple)
print('Data setelah diubah ke set   :', ubah_set2)
print('Data dikembalikan ke tuple   :', ubah_tuple)