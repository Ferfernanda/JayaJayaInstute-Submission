# JayaJayaInstitute-Submission
 
# Submission Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding

Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.
### Permasalahan Bisnis

1. **Tingkat Drop-out Tinggi:**
- Institut menghadapi masalah dengan tingkat drop-out yang signifikan di antara student mereka.
- Analisis data untuk menemukan pola dan tren yang berkaitan dengan student yang drop-out.

2. **Kurangnya Prediksi Awal:**
- Tidak adanya sistem untuk mendeteksi potensi drop-out secara dini sehingga intervensi dapat dilakukan lebih efektif.
- Pembuatan dashboard bisnis untuk membantu dalam pengambilan keputusan variabel.

### Cakupan Proyek
Membangun sistem prediksi menggunakan machine learning untuk mengidentifikasi siswa yang berpotensi drop-out, serta menyediakan dashboard untuk memantau kinerja siswa.
1. Data Understanding hingga Preparation Data student.
2. Mengidentifikasi variabel-variabel yang berhubungan dengan Status dengan correlation matrix dll.
3. Membangun model machine learning untuk memprediksi kemungkinan karyawan akan keluar menggunakan model Logistic Regression.
4. Membuat dashboard bisnis yang memberikan wawasan visual mengenai faktor-faktor yang mempengaruhi status dan membantu manajemen dalam mengambil keputusan.
5. Merekomendasikan Action Items berdasarkan hasil analisis.

### Persiapan

Sumber data: [Employee Data](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance)

Setup environment:
Apabila menginstal Python melalui Anaconda ataupun Miniconda, Anda dapat menggunakan conda sebagai package manager dan environment management system

1. Buka Terminal ataupun PowerShell

2. Jalankan perintah berikut untuk membuat virtual environment baru dengan Python 3.9:

```
conda create --name main-jjm python=3.9
conda activate main-jjm
pip install -r requirements.txt
```
3. Untuk Melakukan prediksi, run the app

   ```
   $ streamlit run app.py
   ```

4. Isi variable pada streamlit tersebut dengan ketentuan yang sudah ditentukan

5. Tekan tombol run dan hasil prediksi akan keluar

Selain itu, anda bisa langsung mengakses streamlit pada link berikut!

**Link Prototype:** [Jaya Jaya Institute: Student's Status Predictions](https://ferfernanda-jayajayainstitute-prediction.streamlit.app/)

## Business Dashboard

Business dashboard yang dibuat menggunakan Metabase akan mencakup visualisasi berikut:

1. **Overview Dashboard:** Menampilkan metrik-metrik utama seperti jumlah total student enrolled, distribusi student berdasarkan course, dan lainnya.

2. **Student's Status Dashboard:** Menampilkan analisis mendalam mengenai faktor-faktor yang mempengaruhi status seperti Scholarship Holder, Displace, dan lainnya.

## Conclusion

Dari proyek ini, kita mendapatkan beberapa wawasan penting mengenai faktor-faktor yang mempengaruhi status student di Jaya Jaya Institute. Model machine learning logistic regression yang telah dibangun dapat memprediksi dengan baik kemungkinan student berpotensi drop-out berdasarkan data historis. Business dashboard yang dibuat dapat membantu manajemen dalam memonitor dan mengambil tindakan yang diperlukan untuk melakukan tindakan terlebih dahulu kepada student.
Proyek ini berhasil mengembangkan solusi untuk mendeteksi dini potensi drop-out siswa menggunakan teknik machine learning. Dashboard bisnis memberikan visibilitas yang diperlukan untuk memantau dan mengambil tindakan yang sesuai.

### Rekomendasi Action Items 

1. **Implementasi Sistem Monitoring Real-Time:** Mengidentifikasi agar dapat mendeteksi perubahan perilaku siswa yang dapat mengindikasikan potensi drop-out.

2. **Komunikasi dengan Konselor:** Dengan adanya fitur deteksi dini potensi status student, maka konselor dapat melakukan perlakuan khusus lebih dini untuk menghindari student yang berpotensi drop-out

Dengan mengimplementasikan rekomendasi ini, diharapkan JayaJaya Institut dapat memperbaiki tingkat kelulusan siswa dan mengurangi tingkat drop-out secara signifikan.

### Login Metabase
**Email:** root@mail.com
**Password:** root123
