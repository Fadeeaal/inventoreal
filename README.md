# Inventoreal
Tautan menuju aplikasi adaptable Inventoreal bisa diakses melalui [tautan ini](https://inventoreal.adaptable.app/).

## **Cara membuat proyek Django baru**
1. Buat direktori baru dengan nama yang Anda inginkan, misalnya `inventoreal` dan buka command prompt (untuk Windows) atau terminal shell di dalam direktori tersebut.

2. Buat virtual environment dengan perintah `python -m venv env` untuk mengisolasi proyek Python kita dan aktifkan virtual environment dengan perintah `env\Scripts\activate.bat` (Windows) atau `source env/bin/activate` (Linux/Mac).

3. Buat file `requirements.txt` di dalam direktori proyek dan isi dengan daftar dependencies yang dibutuhkan untuk proyek Anda.

4. Install dependencies dengan perintah `pip install -r requirements.txt`, kemudian buat proyek Django dengan menjalankan perintah `django-admin startproject (nama_app) .`. Nama_app disesuaikan dengan keinginan, dan ini akan membuat folder baru dengan nama tersebut.

5. Buka file `settings.py` yang ada di dalam folder proyek, cari variabel `ALLOWED_HOSTS` dan ubah nilainya menjadi `["*"]` untuk mengizinkan akses dari semua host.

6. Kembali ke command prompt atau terminal dan jalankan server dengan perintah `python manage.py runserver` di dalam direktori proyek (pastikan ada file `manage.py` di sana).

7. Kita dapat membuka proyek Django baru di browser dengan mengakses http://localhost:8000. Jika melihat animasi roket, maka proyek Django sudah berhasil.

8. Untuk menghentikan server, cukup tekan `Ctrl+C` di command prompt atau terminal. Jangan lupa untuk nonaktifkan virtual environment dengan perintah `deactivate`.

> [!NOTE]
> Jika ingin mengunggah proyek ke github, disarankan membuat file `.gitignore` untuk menentukan berkas dan direktori yang harus diabaikan oleh Git.


## **Cara membuat aplikasi dengan nama `main` pada proyek**
1. Buka command prompt pada direktori utama dan aktifkan virtual environment dengan perintah `env\Scripts\activate.bat`.

2. Jalankan perintah `python manage.py startapp main` untuk membuat folder baru bernama `main`.

3. Mendaftarkan aplikasi `main` ke proyek dengan membuka file `settings.py` dalam direktori proyek dan menambahkan `'main'` pada variabel `INSTALLED_APPS`.


## **Cara membuat model pada aplikasi `main`**
1. Buka file `models.py` dan isi file tersebut dengan nama `Item` dan atribut-atribut dan tipe data yang ingin digunakan. Dalam program ini, ada 3 atribut wajib (name, amount, description) dan 2 atribut tambahan (category, price).
``` python
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.IntegerField()
    amount = models.IntegerField()
    description = models.TextField()
```

2. Jalankan perintah `python manage.py makemigrations` untuk mempersiapkan migrasi skema model ke dalam database Django lokal.

3. Jalankan perintah `python manage.py migrate` untuk menerapkan skema model yang telah dibuat ke dalam database Django lokal.

> [!IMPORTANT]
> Setiap kali ada perubahan pada model (menambahkan / mengurangi / mengganti atribut), wajib untuk melakukan migrasi untuk merefleksikan perubahan itu


## **Cara membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML**
1. Buat direktori baru bernama `templates` di dalam direktori aplikasi `main` dan buat file `main.html` di dalamnya

2. Buka file `views.py` dalam direktori `main` dan tambahkan `from django.shortcuts import render` untuk mengimpor fungsi render dari modul django.shortcuts untuk me-render tampilan HTML dengan menggunakan data yang diberikan.
```
from django.shortcuts import render
```

3. Buat fungsi `show_main` dengan 1 parameter (anggap namanya `request`) dan di dalam fungsinya, buat sebuah dictionary yang berisi data yang akan dikirimkan ke tampilan yang kemudian di return dengan fungsi `render` dengan 3 argumennya, yaitu `request` (objek permintaan HTTP yang dikirim oleh pengguna), nama file html yang digunakan untuk me-_render_ tampilan, dan `context` (dictionary yang berisi data untuk digunakan dalam penampilan dinamis)
```python
def show_main(request):
    context = {
        'name': 'Rakha Fadil Atmojo',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)
```

4. Buka file `main.html` tadi dan ubah kode yang sebelumnya dibuat secara statis menjadi kode Django yang sesuai untuk menampilkan data. Gunakan sintaksis Django yang menggunakan tanda kurung ganda ganda `({{ }})` untuk memasukkan data dari dictionary data yang dikirimkan oleh fungsi `show_main`


## **Cara membuat sebuah routing pada urls.py aplikasi `main` untuk memetakan fungsi yang telah dibuat pada views.py**
1. Buat file `urls.py` di dalam direktori `main` (jika belum ada) dan import modul path dari `django.urls` dan juga import views yang telah dibuat sebelumnya di `views.py`.
```python
from django.urls import path
from main.views import show_main
```

2. Tambahkan urlpatterns untuk menghubungkan path dengan fungsi yang telah Anda buat di `views.py`, yaitu `show_main`
```python
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```


## **Cara melakukan routing pada proyek agar dapat menjalankan aplikasi `main`**
1. Buka berkas `urls.py` di dalam direktori proyek `inventoreal` dan import modul `include` dari `django.urls` (`from django.urls import path, include`) untuk melakukan konfigurasi routing tampilan `main`

2. Di dalam variabel urlpatterns, tambahkan path yang akan mengarahkan ke aplikasi 'main', bisa menggunakan `include()` untuk menghubungkan ke file `urls.py` di aplikasi 'main'.
```python
urlpatterns = [
    path('main/', include('main.urls')), 
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
```


## **Cara _deployment_ aplikasi ke Adaptable**
1. Setelah login, pilih "New App" dan "Connect an Existing Repository".

2. Hubungkan Adaptable.io dengan GitHub, pilih "All Repositories" (jika baru pertama kali menghubungkan).

3. Pilih repositori proyek aplikasi yang telah diunggah ke github dan branch untuk _deployment_.

4. Pilih template deployment "Python App Template" dan pilih PostgreSQL sebagai tipe basis data.

6. Sesuaikan versi Python dengan yang dibutuhkan (cek menggunakan perintah `python --version` pada command prompt).

7. Isi Start Command dengan `python manage.py migrate && gunicorn (nama direktori utama).wsgi`.

8. Tentukan nama aplikasi yang juga akan menjadi nama domain situs web.

9. Centang "HTTP Listener on PORT" dan klik "Deploy App" untuk memulai proses deployment aplikasi.


## **Bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya**
![Alt text](<img-properties/bagan-django.jpg>)
Dalam web aplikasi Django, ketika client mengirimkan permintaan HTTP, Django menggunakan berkas `urls.py` untuk menentukan view yang sesuai. View dalam berkas `views.py` mengatur logika aplikasi, termasuk interaksi dengan models dalam `models.py` untuk mengakses dan memodifikasi data basis data. Data yang diperlukan untuk merender tampilan dikumpulkan dalam view, dan hasilnya dirender menggunakan berkas HTML. Berkas HTML mengandung kode HTML dan tag-template Django untuk memasukkan data dari view. Setelah selesai dirender, tampilan tersebut dikirim sebagai respon ke client, membentuk aliran pengembangan yang terstruktur dalam Django: `urls.py` mengelola routing, `views.py` mengatur logika, `models.py` mengelola data, dan berkas HTML mengontrol tampilan, menciptakan aplikasi web yang berfungsi dengan baik.


## **Mengapa kita menggunakan virtual environment?**
Virtual environment adalah komponen penting dalam pengembangan perangkat lunak Python, termasuk aplikasi web berbasis Django, karena mengatasi berbagai tantangan yang muncul dalam mengelola proyek dengan spesifikasi yang berbeda-beda. Dengan menggunakan virtual environment, kita menciptakan lingkungan Python yang terisolasi untuk setiap proyek, yang memungkinkan kita mengelola dependensi, versi Python, dan konfigurasi yang sesuai dengan proyek tersebut tanpa khawatir tentang konflik dengan proyek lain atau pengaruh terhadap instalasi Python sistem. File `requirements.txt` membantu merekam daftar dependensi yang diperlukan oleh proyek, memudahkan replikasi lingkungan pengembangan di berbagai mesin. Ini tidak hanya penting dalam pengembangan tim untuk menjaga konsistensi konfigurasi, tetapi juga membantu dalam manajemen dependensi yang efisien. Selain itu, virtual environment membantu menjaga keamanan proyek dengan mengisolasi lingkungan dari pustaka atau komponen lain yang terinstal secara global atau dalam proyek lain, serta mencegah konflik yang mungkin timbul akibat penggunaan yang tidak terduga.


## **Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**
Meskipun teknisnya memungkinkan kita untuk membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, namun hal itu sangat tidak dianjurkan. Penggunaan virtual environment dalam pengembangan Django adalah standar yang sangat penting. Tanpa virtual environment, proyek akan bergantung pada instalasi Python sistem yang ada di komputer Anda, yang dapat menyebabkan masalah rumit. Salah satunya adalah konflik dependensi, di mana proyek-proyek yang berbeda memerlukan versi pustaka yang berbeda. Selain itu, jika tanpa menggunakan virtual environment, akan menghadapi tantangan dalam manajemen dependensi, ketergantungan global pada lingkungan Python sistem, dan potensi masalah keamanan. Dengan menggunakan virtual environment, kita menciptakan lingkungan Python yang terisolasi untuk setiap proyek, memungkinkan untuk mengelola dependensi, versi Python, dan keamanan proyek secara independen. Ini juga memudahkan manajemen dependensi dan mencegah konflik antara proyek-proyek kita, menjaga kebersihan, stabilitas, dan keamanan dalam pengembangan proyek selanjutnya.


## **Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya**
MVC (Model-View-Controller), MVT (Model-View-Template) dan MVVM (Model-View-ViewModel) adalah pola arsitektur perangkat lunak yang digunakan dalam pengembangan aplikasi untuk memisahkan komponen aplikasi dari aplikasi yang berbeda agar lebih terstruktur dan sederhana. untuk mengelola. Meskipun  memiliki kesamaan dalam pembagian tugas, namun digunakan dalam konteks yang berbeda dan terdapat perbedaan dalam cara pengorganisasian komponen-komponen tersebut.

### MVC (Model - View - Controller)
| **Model** | **View** | **Controller** |
| --- | --- | --- |
| Representasi data dan aturan bisnis dari aplikasi. Ini adalah bagian yang bertanggung jawab untuk **mengakses dan memanipulasi data**, baik dari database atau sumber lainnya. Model juga menentukan logika bisnis, seperti validasi data dan perhitungan. Misalnya, jika kita ingin mengembangkan aplikasi e-commerce, model akan mengatur cara data produk, pelanggan, dan pesanan disimpan dan diakses | Bagian yang **menangani tampilan kepada pengguna**. Ini adalah apa yang dilihat pengguna saat berinteraksi dengan aplikasi yang kita buat. View bertugas hanya untuk mengambil data dari model dan menuangkannya ke layar. Contohnya dalam aplikasi e-commerce, view akan memperlihatkan daftar produk dan detail pesanan kepada pengguna | Bagian yang bertindak sebagai **perantara antara model dan view**. Ini mengelola alur informasi dalam aplikasi. Controller menangani permintaan pengguna, memprosesnya, dan mengirimkannya ke Model untuk memperbarui data atau mengambil data yang diperlukan. Misalnya pada aplikasi e-commerce. Jika pengguna menambahkan produk ke keranjang belanja, controller akan mengatur supaya model menyimpan data tersebut dan kemudian memberi tahu view untuk memperbarui tampilan |

### MVT (Model - View - Template)
| **Model** | **View** | **Template** |
| --- | --- | --- |
| Sama seperti MVC, model adalah komponen konsep MVT yang bertanggung jawab untuk **mengatur dan mengelola data aplikasi**. Model mewakili struktur data dan logika aplikasi  di balik tampilan. Model menghubungkan aplikasi ke database dan mengelola interaksi dengan data tersebut | Komponen yang mengatur logika presentasi dalam konsep MVT. View ini mengontrol cara data yang dikelola model ditampilkan kepada pengguna. Dalam konteks MVT, tampilan bertindak sebagai **pengatur yang menampilkan dan mengambil data dari model** untuk dipresentasikan kepada pengguna | Bagian yang bertanggung jawab untuk **mengatur tampilan pengguna**, contohnya seperti halaman web. Dalam kerangka kerja seperti Django, Template digunakan untuk merancang tampilan halaman web dan menggabungkan data dari Model sehingga pengguna dapat melihat informasi yang dihasilkan melalui view |

### MVVM (Model - View - ViewModel)
| **Model** | **View** | **ViewModel** |
| --- | --- | --- |
| Komponen yang **mengelola data dan logika aplikasi**, serupa dengan Model dalam MVC dan MVT. Model dan ViewModel pada MVVM ini nantinya akan bekerja sama untuk mengambil dan menyimpan data | Komponen yang bertanggung jawab untuk **menampilkan tampilan dan memberi tahu ViewModel tentang tindakan pengguna**. Namun, dalam MVVM, View berfungsi sebagai penampil pasif yang hanya menampilkan data dan tidak mengandung logika aplikasi apapun | Salah satu komponen utama dalam MVVM yang bertindak sebagai jembatan antara Model dan View. ViewModel **mengubah data dari Model menjadi format yang dapat ditampilkan oleh View dan mengelola logika tampilan**. Misalnya, jika kita memiliki aplikasi cuaca, ViewModel akan mengambil data cuaca dari Model dan merubahnya menjadi format yang dapat ditampilkan oleh View, seperti ikon cuaca, suhu, dan deskripsi |

### Perbedaan MVC, MVT, dan MVVM
#### MVC
MVC adalah pola desain yang telah digunakan dalam berbagai jenis aplikasi, termasuk aplikasi desktop, web, dan mobile. Ini adalah konsep yang serbaguna dan diterapkan secara luas. Dalam MVC, Controller memiliki peran yang cukup aktif dalam mengatur aliran informasi antara Model dan View. Model dan View juga dapat berinteraksi secara langsung dalam beberapa kasus. Dalam kata lain, MVC terfokus pada pemisahan tugas dengan Model yang mengelola data dan logika bisnis, View yang menampilkan data, dan Controller yang mengatur aliran informasi dan dalam MVC, developer harus sering mengelola secara manual pembaruan tampilan setiap kali data berubah. Ini dapat memerlukan kode tambahan untuk menghubungkan Model dan View.

#### MVT
MVT adalah konsep yang utamanya digunakan dalam pengembangan web dengan menggunakan kerangka kerja Django yang berbasis Python. Salah satu komponen istimewanya, yaitu Template (dalam MVT (Django)), dikhususkan mengatur tampilan halaman web, sedangkan Model dan View berperan seperti dalam MVC. Template adalah komponen tambahan yang tidak ada dalam MVC tradisional dan _framework_ ini memiliki alat bawaan untuk mengurus pembaruan tampilan secara otomatis ketika data berubah.

#### MVVM
MVVM sering digunakan dalam pengembangan aplikasi berbasis antarmuka pengguna (UI), seperti aplikasi mobile atau desktop. Ini memiliki fokus untuk memisahkan tugas tampilan dan logika dalam UI. Adanya ViewModel yang bertindak sebagai perantara antara Model dan View memungkinkan keduanya untuk tetap terpisah dan mengurangi ketergantungan antara keduanya. MVVM ini mengandalkan sistem pengikatan data (_data binding_) untuk secara otomatis memperbarui tampilan ketika data berubah di ViewModel. Ini mengurangi kode boilerplate yang diperlukan untuk pembaruan tampilan, tetapi jika _data binding_ tersebut sangat kompleks, akan sedikit lebih sulit untuk melakukan _debugging_ aplikasinya