import time
import sys
import os
import streamlit as st
# from Array_Buku import buku
# from Array_Peminjam import peminjam
# from Array_Peminjam import key_peminjam
import datetime
# import qrcode
import Array_Peminjam
import Array_Buku
import importlib
from PIL import Image


#Konfigurasi Halaman Streamlit
st.set_page_config(page_title="Menu Peminjaman Buku", page_icon="📖", layout="centered")

#Inisialisasi Variabel
arynama,aryjudul,arytglpinjam,arytglkembali = [],[],[],[]

#Elemen Halaman Streamlit
st.empty()
st.title("📖 Menu Peminjaman Buku")
st.write("Silahkan Masukkan Data Diri Anda")

# if st.button("pinjem Buku" ):
#     buku[0][1] = buku[0][1] - 1

# list_buku = []
# for item, index in enumerate(buku):
#     list_buku.append(str(item[3]))

#Input Form
form3 = st.form(key="annotation1",clear_on_submit=False)
with form3:
        nama = form3.text_input("Scan QR Code :")
        # judul = form3.selectbox('Pilih Judul Buku',('','0 - As A Man Thinketh by James Allen','1 - The Metamorphosis by Franz Kafka','2 - 1984 by George Orwell','3 - Manusia Setengan Salmon by Raditya Dika','4 - Ubur Ubur Lembur by Raditya Dika','5 - Sang Pemimpi by Andrea Hirata','6 - The Little Prince by Antonie De Saint-Exupery','7 - The Laws Of Human Nature by Robert Greene','8 - The Art Of Being Alone by Renuka Gavrani','9 - Steal Like An Artist by Austin Kleon'))
        # tglpinjam = value=datetime.date.today()
        # tglkembali = form3.date_input("Tanggal Kembali :")
        submitted = st.form_submit_button(label="Submit")
        
                
        #Pengiriman Data
        if submitted:
            index = int(judul.split(" - ")[0]) 
            judul = str(judul.split(" - ")[1]) 
            if buku[index][1] == 0:
                st.error("Maaf, Buku yang Anda Pilih Sedang Tidak Tersedia")
            else:
                
                #buku[index][1] = buku[index][1] - 1
                st.success("Terimakasih sudah meminjam buku di perpustakaan Nasional!")
                # st.balloons()
                
                id = time.strftime("%d%m%y%H%M%S")
                
                peminjam.append(
                    [
                        id,
                        nama,
                        judul,
                        tglpinjam.strftime("%Y-%m-%d"),
                        tglkembali.strftime("%Y-%m-%d")
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


                st.success("Terimakasih sudah meminjam buku di perpustakaan Nasional!")    
                            
