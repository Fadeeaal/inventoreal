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

1. Buka file `models.py` dan isi file tersebut dengan nama `Items` dan atribut-atribut dan tipe data yang ingin digunakan. Dalam program ini, ada 3 atribut wajib (name, amount, description) dan 2 atribut tambahan (category, price).

```py
from django.db import models

class Items(models.Model):
    creator = models.CharField(max_length=255, default='Rakha Fadil Atmojo')
    npm = models.CharField(max_length=255, default='2206082985')
    pbpclass = models.CharField(max_length=255, default='PBP C')
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
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

```py
from django.shortcuts import render
```

3. Buat fungsi `show_main` dengan 1 parameter (anggap namanya `request`) dan di dalam fungsinya, buat sebuah dictionary yang berisi data yang akan dikirimkan ke tampilan yang kemudian di return dengan fungsi `render` dengan 3 argumennya, yaitu `request` (objek permintaan HTTP yang dikirim oleh pengguna), nama file html yang digunakan untuk me-_render_ tampilan, dan `context` (dictionary yang berisi data untuk digunakan dalam penampilan dinamis). Berikut adalah contohnya.

```py
def show_main(request):
    context = {
    'creator' : 'Rakha Fadil Atmojo',
        'npm' : 2206082985,
        'pbpclass' : 'PBP C',
        'items': [
            {
                'name': 'Diamond Sword',
                'category': 'Weapon',
                'price': 1000,
                'amount': 1,
                'description': 'A rare gem-forged blade, renowned for its unmatched sharpness and exquisite artistry, can effortlessly conquer any obstacle.',
            },
            ...
        ]
    }

    return render(request, "main.html", context)
```

4. Buka file `main.html` tadi dan ubah kode yang sebelumnya dibuat secara statis menjadi kode Django yang sesuai untuk menampilkan data. Gunakan sintaksis Django yang menggunakan tanda kurung ganda ganda `({{ }})` untuk memasukkan data dari dictionary data yang dikirimkan oleh fungsi `show_main`

## **Cara membuat sebuah routing pada urls.py aplikasi `main` untuk memetakan fungsi yang telah dibuat pada views.py**

1. Buat file `urls.py` di dalam direktori `main` (jika belum ada) dan import modul path dari `django.urls` dan juga import views yang telah dibuat sebelumnya di `views.py`.

```py
from django.urls import path
from main.views import show_main
```

2. Tambahkan urlpatterns untuk menghubungkan path dengan fungsi yang telah Anda buat di `views.py`, yaitu `show_main`

```py
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

5. Sesuaikan versi Python dengan yang dibutuhkan (cek menggunakan perintah `python --version` pada command prompt).

6. Isi Start Command dengan `python manage.py migrate && gunicorn (nama direktori utama).wsgi`.

7. Tentukan nama aplikasi yang juga akan menjadi nama domain situs web.

8. Centang "HTTP Listener on PORT" dan klik "Deploy App" untuk memulai proses deployment aplikasi.

## **Bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya**

![Alt text](img-properties/bagan-django.jpg)
Dalam web aplikasi Django, ketika client mengirimkan permintaan HTTP, Django menggunakan berkas `urls.py` untuk menentukan view yang sesuai. View dalam berkas `views.py` mengatur logika aplikasi, termasuk interaksi dengan models dalam `models.py` untuk mengakses dan memodifikasi data basis data. Data yang diperlukan untuk merender tampilan dikumpulkan dalam view, dan hasilnya dirender menggunakan berkas HTML. Berkas HTML mengandung kode HTML dan tag-template Django untuk memasukkan data dari view. Setelah selesai dirender, tampilan tersebut dikirim sebagai respon ke client, membentuk aliran pengembangan yang terstruktur dalam Django: `urls.py` mengelola routing, `views.py` mengatur logika, `models.py` mengelola data, dan berkas HTML mengontrol tampilan, menciptakan aplikasi web yang berfungsi dengan baik.

## **Mengapa kita menggunakan virtual environment?**

Virtual environment adalah komponen penting dalam pengembangan perangkat lunak Python, termasuk aplikasi web berbasis Django, karena mengatasi berbagai tantangan yang muncul dalam mengelola proyek dengan spesifikasi yang berbeda-beda. Dengan menggunakan virtual environment, kita menciptakan lingkungan Python yang terisolasi untuk setiap proyek, yang memungkinkan kita mengelola dependensi, versi Python, dan konfigurasi yang sesuai dengan proyek tersebut tanpa khawatir tentang konflik dengan proyek lain atau pengaruh terhadap instalasi Python sistem. File `requirements.txt` membantu merekam daftar dependensi yang diperlukan oleh proyek, memudahkan replikasi lingkungan pengembangan di berbagai mesin. Ini tidak hanya penting dalam pengembangan tim untuk menjaga konsistensi konfigurasi, tetapi juga membantu dalam manajemen dependensi yang efisien. Selain itu, virtual environment membantu menjaga keamanan proyek dengan mengisolasi lingkungan dari pustaka atau komponen lain yang terinstal secara global atau dalam proyek lain, serta mencegah konflik yang mungkin timbul akibat penggunaan yang tidak terduga.

## **Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?**

Meskipun teknisnya memungkinkan kita untuk membuat aplikasi web berbasis Django tanpa menggunakan virtual environment, namun hal itu sangat tidak dianjurkan. Penggunaan virtual environment dalam pengembangan Django adalah standar yang sangat penting. Tanpa virtual environment, proyek akan bergantung pada instalasi Python sistem yang ada di komputer Anda, yang dapat menyebabkan masalah rumit. Salah satunya adalah konflik dependensi, di mana proyek-proyek yang berbeda memerlukan versi pustaka yang berbeda. Selain itu, jika tanpa menggunakan virtual environment, akan menghadapi tantangan dalam manajemen dependensi, ketergantungan global pada lingkungan Python sistem, dan potensi masalah keamanan. Dengan menggunakan virtual environment, kita menciptakan lingkungan Python yang terisolasi untuk setiap proyek, memungkinkan untuk mengelola dependensi, versi Python, dan keamanan proyek secara independen. Ini juga memudahkan manajemen dependensi dan mencegah konflik antara proyek-proyek kita, menjaga kebersihan, stabilitas, dan keamanan dalam pengembangan proyek selanjutnya.

## **Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya**

MVC (Model-View-Controller), MVT (Model-View-Template) dan MVVM (Model-View-ViewModel) adalah pola arsitektur perangkat lunak yang digunakan dalam pengembangan aplikasi untuk memisahkan komponen aplikasi dari aplikasi yang berbeda agar lebih terstruktur dan sederhana. untuk mengelola. Meskipun memiliki kesamaan dalam pembagian tugas, namun digunakan dalam konteks yang berbeda dan terdapat perbedaan dalam cara pengorganisasian komponen-komponen tersebut.

### MVC (Model - View - Controller)
| **Model** | **View** | **Controller** |
| --- | --- | --- |
| Representasi data dan aturan bisnis dari aplikasi. Ini adalah bagian yang bertanggung jawab untuk mengakses dan memanipulasi data, baik dari database atau sumber lainnya. Model juga menentukan logika bisnis, seperti validasi data dan perhitungan. Misalnya, jika kita ingin mengembangkan aplikasi e-commerce, model akan mengatur cara data produk, pelanggan, dan pesanan disimpan dan diakses | Bagian yang menangani tampilan kepada pengguna. Ini adalah apa yang dilihat pengguna saat berinteraksi dengan aplikasi yang kita buat. View bertugas hanya untuk mengambil data dari model dan menuangkannya ke layar. Contohnya dalam aplikasi e-commerce, view akan memperlihatkan daftar produk dan detail pesanan kepada pengguna | Bagian yang bertindak sebagai perantara antara model dan view. Ini mengelola alur informasi dalam aplikasi. Controller menangani permintaan pengguna, memprosesnya, dan mengirimkannya ke Model untuk memperbarui data atau mengambil data yang diperlukan. Misalnya pada aplikasi e-commerce. Jika pengguna menambahkan produk ke keranjang belanja, controller akan mengatur supaya model menyimpan data tersebut dan kemudian memberi tahu view untuk memperbarui tampilan |

### MVT (Model - View - Template)
| **Model** | **View** | **Template** |
| --- | --- | --- |
| Sama seperti MVC, model adalah komponen konsep MVT yang bertanggung jawab untuk mengatur dan mengelola data aplikasi. Model mewakili struktur data dan logika aplikasi di balik tampilan. Model menghubungkan aplikasi ke database dan mengelola interaksi dengan data tersebut | Komponen yang mengatur logika presentasi dalam konsep MVT. View ini mengontrol cara data yang dikelola model ditampilkan kepada pengguna. Dalam konteks MVT, tampilan bertindak sebagai pengatur yang menampilkan dan mengambil data dari model untuk dipresentasikan kepada pengguna | Bagian yang bertanggung jawab untuk mengatur tampilan pengguna, contohnya seperti halaman web. Dalam kerangka kerja seperti Django, Template digunakan untuk merancang tampilan halaman web dan menggabungkan data dari Model sehingga pengguna dapat melihat informasi yang dihasilkan melalui view |

### MVVM (Model - View - ViewModel)
| **Model** | **View** | **ViewModel** |
| --- | --- | --- |
| Komponen yang mengelola data dan logika aplikasi, serupa dengan Model dalam MVC dan MVT. Model dan ViewModel pada MVVM ini nantinya akan bekerja sama untuk mengambil dan menyimpan data | Komponen yang bertanggung jawab untuk menampilkan tampilan dan memberi tahu ViewModel tentang tindakan pengguna. Namun, dalam MVVM, View berfungsi sebagai penampil pasif yang hanya menampilkan data dan tidak mengandung logika aplikasi apapun | Salah satu komponen utama dalam MVVM yang bertindak sebagai jembatan antara Model dan View. ViewModel mengubah data dari Model menjadi format yang dapat ditampilkan oleh View dan mengelola logika tampilan. Misalnya, jika kita memiliki aplikasi cuaca, ViewModel akan mengambil data cuaca dari Model dan merubahnya menjadi format yang dapat ditampilkan oleh View, seperti ikon cuaca, suhu, dan deskripsi |

### Perbedaan MVC, MVT, dan MVVM

#### MVC

MVC adalah pola desain yang telah digunakan dalam berbagai jenis aplikasi, termasuk aplikasi desktop, web, dan mobile. Ini adalah konsep yang serbaguna dan diterapkan secara luas. Dalam MVC, Controller memiliki peran yang cukup aktif dalam mengatur aliran informasi antara Model dan View. Model dan View juga dapat berinteraksi secara langsung dalam beberapa kasus. Dalam kata lain, MVC terfokus pada pemisahan tugas dengan Model yang mengelola data dan logika bisnis, View yang menampilkan data, dan Controller yang mengatur aliran informasi dan dalam MVC, developer harus sering mengelola secara manual pembaruan tampilan setiap kali data berubah. Ini dapat memerlukan kode tambahan untuk menghubungkan Model dan View.

#### MVT

MVT adalah konsep yang utamanya digunakan dalam pengembangan web dengan menggunakan kerangka kerja Django yang berbasis Python. Salah satu komponen istimewanya, yaitu Template (dalam MVT (Django)), dikhususkan mengatur tampilan halaman web, sedangkan Model dan View berperan seperti dalam MVC. Template adalah komponen tambahan yang tidak ada dalam MVC tradisional dan _framework_ ini memiliki alat bawaan untuk mengurus pembaruan tampilan secara otomatis ketika data berubah.

#### MVVM

MVVM sering digunakan dalam pengembangan aplikasi berbasis antarmuka pengguna (UI), seperti aplikasi mobile atau desktop. Ini memiliki fokus untuk memisahkan tugas tampilan dan logika dalam UI. Adanya ViewModel yang bertindak sebagai perantara antara Model dan View memungkinkan keduanya untuk tetap terpisah dan mengurangi ketergantungan antara keduanya. MVVM ini mengandalkan sistem pengikatan data (_data binding_) untuk secara otomatis memperbarui tampilan ketika data berubah di ViewModel. Ini mengurangi kode boilerplate yang diperlukan untuk pembaruan tampilan, tetapi jika _data binding_ tersebut sangat kompleks, akan sedikit lebih sulit untuk melakukan _debugging_ aplikasinya

## **Cara mengimplementasikan _Skeleton_ sebagai Kerangka Views**
1. Buat folder bernama `templates` di dalam root folder dan buatlah file bernama `base.html`. Isi file tersebut dengan kode di bawah ini.
```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta
            name="viewport"
            content="width=device-width, initial-scale=1.0"
        />
        {% block meta %}
        {% endblock meta %}
    </head>

    <body>
        {% block content %}
        {% endblock content %}
    </body>
</html>
```
2. Buka `settings.py` pada subdirektori `inventoreal` dan cari variabel `TEMPLATES` yang bertipe data list of dictionaries, kemudian sesuaikan value dari key `DIRS` untuk mengarahkan ke folder `templates` yang telah dibuat sebelumnya.
```py
TEMPLATES = [
    {
        ...
        'DIRS': [BASE_DIR / 'templates'],
        ...
    }
]
```
3. Pada `main/templates/main.html`, tambahkan kode di bawah ini untuk meng-_extend_ dari `base.html` yang baru saja dibuat.
```html
{% extends 'base.html' %}
{% block content %}
    ...
    //kode html yang telah dibuat sebelumnya
    ...
{% endblock content %}
```

## **Cara membuat input form untuk menambahkan objek model pada aplikasi**
1. Jalankan virtual environment terlebih dahulu. Untuk windows, menggunakan command `env\Scripts\activate.bat` dan untuk unix menggunakan command `source env/bin/activate`

2. Kita implementasikan dahulu sebuah skeleton sebagai kerangka viewsnya. Untuk tata caranya, silahkan mengikuti [link ini](#cara-mengimplementasikan-skeleton-sebagai-kerangka-views)

3. Buat file terbaru, yaitu `forms.py` pada folder `main` yang bertujuan untuk membuat struktur form yang dapat menerima data produk baru saat diinput, dan tambahkan kode di bawah ini
```py
from django.forms import ModelForm
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "category", "price", "amount", "description"]
```
> [!NOTE]
> isi variabel `fields` disesuaikan dengan informasi / variabel apa saja yang ingin diminta dari user

4. Buka file `main/views.py` dan tambahkan beberapa import serta function `create_item` untuk menghasilkan form yang dapat menambahkan data produk secara otomatis ketika data di-_submit_ dari form
```py
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
...
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)
```

## **Cara menambahkan fungsi views untuk melihat objek yang sudah ditambahkan (HTML, XML, JSON, XML by ID, dan JSON by ID)**
### **HTML**
1. Pada file `main/views.py`, ubah function `show_main` untuk mengambil seluruh object Item yang tersimpan pada database
```py
def show_main(request):
    items = Item.objects.all()
    context = {
        'creator' : 'Rakha Fadil Atmojo',
        'npm' : 2206082985,
        'pbpclass' : 'PBP C',
        'item' : items,
    }
    return render(request, "main.html", context)
```

2. Buka `main/urls.py`, lalu import function `create_item` yang sudah dibuat tadi dan tambahkan path url ke dalam url patterns untuk mengakses function tadi.
```py
from main.views import show_main, create_item
...
urlpatterns = [
    ...
    path('create-item', create_item, name='create_item'),
]
```

3. Buat file `create_item.html` di dalam folder `main/templates` yang berfungsi sebagai tampilan form untuk meminta input data. Berikut adalah isi dari filenya.
```py
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Product</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Item"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```

4. Buka `main.html` dalam folder `main/templates` dan tambahkan kode di dalam `{% block content %}` untuk menampilkan barang yang di-_input_ melalui `create_item.html` dalam bentuk tabel.
```html
...
<table>
<tr>
    <th>Name</th>
    <th>Category</th>
    <th>Description</th>
    <th>Price</th>
    <th>Amount</th>
</tr>
{% for x in item %}
    <tr>
        <td>{{ x.name }}</td>
        <td>{{ x.category }}</td>
        <td>{{ x.description }}</td>
        <td>{{ x.price }}</td>
        <td>{{ x.amount }}</td>
    </tr>
{% endfor %}
</table>
...
```
### **XML**
1. Buka file `main/views.py`, kemudian import `HttpResponse` dan `Serializer` dan tambahkan function `show_xml`
```py
from django.http import HttpResponse
from django.core import serializers
...
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
```
> [!NOTE]
> serializers digunakan untuk translate objek model menjadi format lain.

2. Buka `main/urls.py` untuk import function `show_xml` dan tambahkan routing url ke url patterns sebagai akses menuju fungsi tersebut
```py
from main.views import show_main, create_item, show_xml
...
urlpatterns = [
    ...
    path('xml/', show_xml, name='show_xml'),
    ...
]
```

### **JSON**
1. Buka file `views.py` pada folder `main` dan buat fungsi `show_json` yang menerima parameter `request`
```py
def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

2. Buka `urls.py` yang ada pada folder `main` dan import fungsi yang sudah dibuat tadi `(show_json)` dan tambahkan path url ke dalam urlpatterns untuk mengakses fungsi yang diimpor tadi
```py
from main.views import show_main, create_item, show_xml, show_json
...
urlpatterns = [
    ...
    path('json/', show_json, name='show_json'),
    ...
]
```

### **XML dan JSON by ID**
1. Buka kembali folder `main` dan akses file `urls.py`, kemudian buat function baru, `show_xml_by_id` dan `show_json_by_id` dengan mengembalikan function berupa `HttpResponse` yang berisi parameter data hasil query yang sudah diserialisasi menjadi JSON atau XML dan parameter `content_type`
```py
...
def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
...
```

2. Buka `urls.py` yang ada pada folder `main` dan import fungsi yang sudah dibuat tadi, yaitu `show_xml_by_id` dan `show_json_by_id`, kemudian perbarui path url yang di dalam urlpatterns untuk mengakses kedua fungsi tersebut, sehingga tampilan akhirnya pada file `main/urls.py` akan menjadi seperti [ini](main/urls.py)
```py
from django.urls import path
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id 

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
]
```

