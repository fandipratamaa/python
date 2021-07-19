from tabulate import tabulate

# selamat datang
print(10*"#"+' SELAMAT DATANG',10*"#")

# daftar barang
table_daftar_brg = [['beras'],['bolpoin'],['wafer tango'],['jeruk'],['kecap']]
headers_daftar_brg = ['daftar barang']
print(tabulate(table_daftar_brg, headers_daftar_brg, tablefmt="pretty"))

## pilih barang
pilih_brg = input('Pilih barang yang ingin dibeli: ')

## tampilkan daftar barang yg dipilih
table_pilih_brg = [[pilih_brg]]
headers_pilih_brg = ['barang yg dibeli']
hasil_pilih_brg = print(tabulate(table_pilih_brg, headers_pilih_brg, tablefmt="psql"))

## cek barang ada / tidak





