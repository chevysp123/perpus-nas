#Import Libary
import time
import sys
import os
import streamlit as st
from Array_Buku import buku
from Array_Peminjam import peminjam
from Array_Peminjam import key_peminjam
import datetime
import qrcode
from PIL import Image


#Konfigurasi Halaman Streamlit
st.set_page_config(page_title="Menu Peminjaman Buku", page_icon="📖", layout="centered")

#Inisialisasi Variabel
arynama,aryjudul,arytglpinjam,arytglkembali,aryaktif = [],[],[],[],[]

#Elemen Halaman Streamlit
st.empty()
st.title("📖 Menu Peminjaman Buku")
st.write("Silahkan Masukkan Data Diri Anda")


#Input Form
form1 = st.form(key="annotation1",clear_on_submit=False)
with form1:
        #cols = st.columns((1,1))
        nama = form1.text_input("Nama Lengkap :")
        judul = form1.selectbox('Pilih Judul Buku',('','0 - As A Man Thinketh by James Allen','1 - The Metamorphosis by Franz Kafka','2 - 1984 by George Orwell','3 - Manusia Setengan Salmon by Raditya Dika','4 - Ubur Ubur Lembur by Raditya Dika','5 - Sang Pemimpi by Andrea Hirata','6 - The Little Prince by Antonie De Saint-Exupery','7 - The Laws Of Human Nature by Robert Greene','8 - The Art Of Being Alone by Renuka Gavrani'))
        # judul = cols[1].selectbox('Pilih Judul Buku',list_buku)
        #cols = st.columns(2)
        tglpinjam = value=datetime.date.today()
        tglkembali = form1.date_input("Tanggal Kembali :")
        #aktif = form1=="0"
        max_tglkembali = tglpinjam + datetime.timedelta(days=7)
        # if tglkembali > max_tglkembali:
        #     st.error("Tanggal kembali tidak boleh lebih dari 7 hari dari tanggal pinjam.")
        submitted = st.form_submit_button(label="Submit")
        
        #Pengiriman Data
        if submitted:
            index = int(judul.split(" - ")[0]) 
            judul = str(judul.split(" - ")[1]) 
            if buku[index][1] == 0:
                st.error("Maaf, Buku yang Anda Pilih Sedang Tidak Tersedia")
            elif tglkembali > max_tglkembali:
                st.error("Tanggal kembali tidak boleh lebih dari 7 hari dari tanggal pinjam.")
            else:
                
                #buku[index][1] = buku[index][1] - 1
                st.success("Silahkan simpan QR Code Peminjaman Buku Anda untuk pengambilan dan penyerahan buku")
                # st.balloons()
                
                id = time.strftime("%d%m%y%H%M%S")
                
                peminjam.append(
                    [
                        id,
                        nama,
                        judul,
                        tglpinjam.strftime("%Y-%m-%d"),
                        tglkembali.strftime("%Y-%m-%d"),
                        '0',
                        index
                    ]
                )
                
                key_peminjam.append( id + ' - ' + nama + " - " + judul)

                # Generate QR code
                qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
                qr.add_data(id + ' - ' + nama + " - " + judul)
                qr.make(fit=True)
                img = qr.make_image(fill='black', back_color='white')
                img_path = "qrcode-" + id + ".png"
                img.save(img_path)

                # Center the QR code on the page
                qr_col1, qr_col2, qr_col3 = st.columns([1, 2, 1])
                with qr_col2:
                    st.image(img_path, caption="QR Code Peminjaman Buku")
                    st.write("ID Peminjaman: ", id + ' - ' + nama + " - " + judul)


                st.success("Terimakasih sudah meminjam buku di perpustakaan Nasional!")    
                            
                # Menyimpan Data dan Membuat Struk
                # for i in range(1):
                #     arynama.append(nama)
                #     aryjudul.append(judul)
                #     arytglpinjam.append(tglpinjam.strftime("%Y-%m-%d"))
                #     arytglkembali.append(tglkembali)
                #     #Membuat File Struk
                #     sys.stdout = open("struk-"+nama+"-"+str(tglpinjam)+".txt", "w")
                #     print('''
                #         ************************  PERPUS NASIONAL  ************************
                #         ************ Sistem Peminjaman Buku Perpustakaan Digital ************
                #         ************************ Struk Bukti Pinjam *************************
                #         ''')
                #     print('\t\t\tTanggal : ',tglpinjam)
                #     print("\t\t\tNama Peminjam Buku : ",nama)
                #     print("\t\t\tJudul Buku : ",judul)
                #     print("\t\t\tTanggal Peminjaman : ",tglpinjam)
                #     print("\t\t\tTanggal Kembali : ",tglkembali)
                #     print('''
                #                 ---Terima Kasih Telah Meminjam Buku Ditempat Kami---
                #                 ---Struk Harap Dibawa pada saat pengembalian Buku---
                #         ''')
                #     sys.stdout.close()
                #     sys.stdout = sys.__stdout__
                #     time.sleep(1) #Fungsi Tambahan
                #     os.system("struk-"+nama+"-"+str(tglpinjam)+".txt") #Membuka File Struk