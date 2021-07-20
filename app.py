from tabulate import tabulate

# selamat datang
print(10*"-"+' SELAMAT DATANG',10*"-")

# daftar barang
table_daftar_brg = [['beras'],['bolpoin'],['wafer tango'],['jeruk'],['kecap']]
headers_daftar_brg = ['daftar barang']
print(tabulate(table_daftar_brg, headers_daftar_brg, tablefmt="pretty"))


## pilih barang
pilih_brg = input('Pilih barang yang ingin dibeli: ')
## daftar barang yg dipilih
table_pilih_brg = [[pilih_brg]]
headers_pilih_brg = ['barang yg dibeli']
hasil_pilih_brg = print(tabulate(table_pilih_brg, headers_pilih_brg, tablefmt="psql"))

# jumlah barang
jumlah_brg = int(input('Jumlah barang yang ingin dibeli: '))
## jumlah barang yg dipilih
table_jumlah_brg = [[pilih_brg,jumlah_brg]]
headers_jumlah_brg = ['barang yg dibeli','jumlah barang']
hasil_jumlah_brg = print(tabulate(table_jumlah_brg, headers_jumlah_brg, tablefmt="pretty"))

# daftar jenis barang
table_jenis_brg = [['kebutuhan pokok'],['alat tulis'],['snack'],['buah']]
headers_jenis_brg = ['daftar jenis barang']
print(tabulate(table_jenis_brg, headers_jenis_brg, tablefmt="pretty"))
## jenis barang
jenis_brg = input('Pilih jenis barang yang ingin dibeli: ')
## jenis barang yg dipilih
table_pilih_jenis_brg = [[pilih_brg,jumlah_brg,jenis_brg]]
headers_pilih_jenis_brg = ['barang yg dibeli','jumlah barang','jenis barang']
hasil_pilih_jenis_brg = print(tabulate(table_pilih_jenis_brg, headers_pilih_jenis_brg, tablefmt="psql"))


# berat barang
berat_brg = int(input('berat barang yang ingin dibeli(kg): '))
## jumlah barang yg dipilih
table_berat_brg = [[pilih_brg,jumlah_brg,jenis_brg,berat_brg]]
headers_berat_brg = ['barang yg dibeli','jumlah barang','jenis barang','berat barang(kg)']
hasil_berat_brg = print(tabulate(table_berat_brg, headers_berat_brg, tablefmt="pretty"))

# daftar harga barang
table_jenis_brg = [['kebutuhan pokok'],['alat tulis'],['snack'],['buah']]
headers_jenis_brg = ['daftar jenis barang']
print(tabulate(table_jenis_brg, headers_jenis_brg, tablefmt="pretty"))
## jenis barang
jenis_brg = input('Pilih jenis barang yang ingin dibeli: ')
## jenis barang yg dipilih
table_pilih_jenis_brg = [[pilih_brg,jumlah_brg,jenis_brg]]
headers_pilih_jenis_brg = ['barang yg dibeli','jumlah barang','jenis barang']
hasil_pilih_jenis_brg = print(tabulate(table_pilih_jenis_brg, headers_pilih_jenis_brg, tablefmt="psql"))

