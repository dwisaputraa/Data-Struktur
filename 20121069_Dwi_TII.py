# Tugas Terstruktur

# soal pertama
print('Jawaban Pertama')
print('')
data_mahasiswa = {
    'NIM':'20121069',
    'Nama':'Dwi Saputra',
    'Kelas':'TI3A',
    'Alamat':'Pecalungan'
}
print("data_mahasiswa = ",data_mahasiswa)

# soal kedua
print('Jawaban Kedua')
print('')
print('------------------------------------------------')
print('Aplikasi Sederhana Menggunakan String Dan Array')
print('------------------------------------------------')
print('NIM    : ',data_mahasiswa['NIM'])
print('Nama   : ',data_mahasiswa['Nama'])
print('Kelas  : ',data_mahasiswa['Kelas'])
print('Alamat : ',data_mahasiswa['Alamat'])
print('------------------------------------------------')

# soal ketiga
print('Jawaban Ketiga')
print('')
kalimat = ['UNISS','di','belajar','pada','Mahasiswa','data','ruang','lab','struktur','semester','tema','Array','String','dan','di','dengan','Batang','3']

print(kalimat[4],kalimat[9],kalimat[17],kalimat[1],kalimat[0],kalimat[16],kalimat[2],kalimat[8],kalimat[5],kalimat[3],kalimat[6],kalimat[7],kalimat[15],kalimat[10],kalimat[12],kalimat[13],kalimat[11])

# soal keempat
print('Jawaban Keempat')
print('')
from array import *
Nilai = array('i',[1,3,4,5,10,15,20])

print('-------------------------------------------------')
print('    Aplikasi Sederhan menggunakan Array          ')
print('-------------------------------------------------')
print(Nilai[4], ' + ',Nilai[1], ' x ', Nilai[5], ' = ',Nilai[4]+Nilai[1]*Nilai[5])
print(Nilai[1], ' x ',Nilai[2], ' : 2 = ',Nilai[1]*Nilai[2]/2)
print(Nilai[5], '^2 x ',Nilai[1], ' + ',Nilai[3],' = ',Nilai[5]**2 *Nilai[1]+Nilai[3])
print(Nilai[5], ' - ',Nilai[3], ' x ', Nilai[2], ' = ',Nilai[5]-Nilai[3]*Nilai[2])