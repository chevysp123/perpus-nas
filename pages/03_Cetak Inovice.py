#Import Libary
import time
import sys
import os
import datetime
import streamlit as st

#Konfigurasi Halaman Streamlit
st.set_page_config(page_title="Menu Cetak Invoice", page_icon="🧾", layout="centered")

#Inisialisasi Variabel
arynama,aryjudul,arytglpinjam,arytglkembali = [],[],[],[]

#Elemen Halaman Streamlit
st.empty()
st.title("🧾 Invoice Generator")
st.write("Mohon isikan data dengan benar sesuai dengan struk peminjaman buku yang telah diberikan oleh petugas perpustakaan")

#Input Form
form3 = st.form(key="annotation3",clear_on_submit=True)
with form3:
    cols = st.columns((1,1))
    nama = cols[0].text_input("Nama Lengkap :")
    judul = cols[1].selectbox('Pilih Judul Buku',('','As A Man Thinketh by James Allen','The Metamorphosis by Franz Kafka','1984 by George Orwell','Manusia Setengan Salmon by Raditya Dika','Ubur Ubur Lembur by Raditya Dika','Sang Pemimpi by Andrea Hirata','The Little Prince by Antonie De Saint-Exupery','The Laws Of Human Nature by Robert Greene','The Art Of Being Alone by Renuka Gavrani','Steal Like An Artist by Austin Kleon'))
    cols = st.columns(2)
    tglpinjam = cols[0].date_input("Tanggal Peminjaman :")
    tglkembali = cols[1].date_input("Tanggal Deadline :")
    submitted = st.form_submit_button(label="Submit")
    #Menghitung Selisih Tanggal dan Denda
    tglskg = datetime.datetime.now()
    tglkembali = str(tglkembali)
    tglWajib = tglkembali.split('-')

    tglWajib[0] = int(tglWajib[0])
    tglWajib[1] = int(tglWajib[1])
    tglWajib[2] = int(tglWajib[2])
    
    selisihTahun = tglskg.year - tglWajib[0]
    selisihBulan = tglskg.month - tglWajib[1]
    selisihTanggal = tglskg.day - tglWajib[2]  

    totalHari = (selisihTahun*365 + selisihBulan*30 + selisihTanggal)
    
    denda = 0

    if(totalHari>0):
        denda = 5000 * totalHari
    
    #Menampilkan Output dan Membuat Invoice
    if submitted:
        st.success("Terimakasih sudah meminjam buku di perpustakaan Nasional! Jangan lupa ambil invoice-nya ya")
        st.balloons()
        for i in range(1):
            arynama.append(nama)
            aryjudul.append(judul)
            arytglpinjam.append(tglpinjam)
            arytglkembali.append(tglkembali)
            sys.stdout = open("invoice-"+nama+"-"+str(tglpinjam)+".txt", "w")
            print('''
                ************************  PERPUS NASIONAL  ************************
                ************ Sistem Peminjaman Buku Perpustakaan Digital ************
                ************************ Invoice Peminjaman *************************
                ''')
            print('\t\t\tTanggal : ',tglskg.day,"-",tglskg.month,"-",tglskg.year)
            print("\t\t\tNama Peminjam Buku : ",nama)
            print("\t\t\tJudul Buku : ",judul)
            print("\t\t\tTanggal Peminjaman : ",tglpinjam)
            print("\t\t\tTanggal Deadline : ",tglkembali)
            print("\t\t\tTanggal Kembali : ",tglskg.year,"-",tglskg.month,"-",tglskg.day)
            print("\t\t\tDenda : ",denda," Rupiah")
            print('''
                        ---Terima Kasih Telah Meminjam Buku Ditempat Kami---
                                            ---LUNAS---
                ''')
            sys.stdout.close()
            sys.stdout = sys.__stdout__
            time.sleep(1)
            os.system("invoice-"+nama+"-"+str(tglpinjam)+".txt")