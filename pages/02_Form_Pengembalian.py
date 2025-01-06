#Import Libary
import datetime
import streamlit as st
from Array_Peminjam import peminjam
from Array_Peminjam import key_peminjam

#Konfigurasi Halaman Streamlit
st.set_page_config(page_title="Menu Pengembalian Buku", page_icon="📄", layout="centered")

#Inisialisasi Variabel
arynama,aryjudul,arytglpinjam,arytglkembali = [],[],[],[]

#Elemen Halaman Streamlit
st.empty()
st.title("📄 Menu Pengembalian Buku")
st.write("Silahkan Masukkan Data Diri Anda")

#Input Form
form2 = st.form(key="annotation2",clear_on_submit=True)
with form2:
        # nama = form2.text_input("Nama Lengkap :")
        nama = form2.selectbox('Pilih Peminjam',key_peminjam)
        # judul = form2.selectbox('Pilih Judul Buku',('','As A Man Thinketh by James Allen','The Metamorphosis by Franz Kafka','1984 by George Orwell','Manusia Setengan Salmon by Raditya Dika','Ubur Ubur Lembur by Raditya Dika','Sang Pemimpi by Andrea Hirata','The Little Prince by Antonie De Saint-Exupery','The Laws Of Human Nature by Robert Greene','The Art Of Being Alone by Renuka Gavrani','Steal Like An Artist by Austin Kleon'))
        tglkembali = form2.date_input("Tanggal Deadline Pengembalian :")
        submitted = st.form_submit_button(label="Submit")
        #Logika Perhitungan Denda
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

        #Menampilkan Hasil
        if submitted: 
            id = str(nama.split(" - ")[0]) 
            st.write(id)
            st.write(peminjam)
            # my_list = ['Harun al', 'A25325 - asfsafasf']
            peminjamTerbaru = [sublist for sublist in peminjam if not any(id in item for item in sublist)]
            peminjam.clear()
            peminjam.append(peminjamTerbaru)
            
            if(denda == 0):
                st.success("Terimakasih sudah mengembalikan buku tepat pada waktunya!")
                st.balloons()
            else:
                st.success("Anda terlambat mengembalikan buku sebanyak "+ str(totalHari) +" hari, maka harap membayar denda sebesar "+ str(denda) +" rupiah")