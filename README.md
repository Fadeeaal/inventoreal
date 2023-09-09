# Inventoreal
Tautan menuju aplikasi adaptable Inventoreal bisa diakses melalui [tautan ini](https://inventoreal.adaptable.app/).

## *Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya*
MVC (Model-View-Controller), MVT (Model-View-Template) dan MVVM (Model-View-ViewModel) adalah pola arsitektur perangkat lunak yang digunakan dalam pengembangan aplikasi untuk memisahkan komponen aplikasi dari aplikasi yang berbeda agar lebih terstruktur dan sederhana. untuk mengelola. Meskipun  memiliki kesamaan dalam pembagian tugas, namun digunakan dalam konteks yang berbeda dan terdapat perbedaan dalam cara pengorganisasian komponen-komponen tersebut.

### MVC (Model - View - Controller)
#### Model
Model dalam MVC adalah representasi data dan aturan bisnis dari aplikasi. Ini adalah bagian yang bertanggung jawab untuk **mengakses dan memanipulasi data**, baik dari database atau sumber lainnya. Model juga menentukan logika bisnis, seperti validasi data dan perhitungan. Misalnya, jika kita ingin mengembangkan aplikasi e-commerce, model akan mengatur cara data produk, pelanggan, dan pesanan disimpan dan diakses.

#### View
View adalah bagian yang **menangani tampilan kepada pengguna**. Ini adalah apa yang dilihat pengguna saat berinteraksi dengan aplikasi yang kita buat. View bertugas hanya untuk mengambil data dari model dan menuangkannya ke layar. Contohnya dalam aplikasi e-commerce, view akan memperlihatkan daftar produk dan detail pesanan kepada pengguna.

#### Controller
Controller merupakan bagian yang bertindak sebagai **perantara antara model dan view**. Ini mengelola alur informasi dalam aplikasi. Controller menangani permintaan pengguna, memprosesnya, dan mengirimkannya ke Model untuk memperbarui data atau mengambil data yang diperlukan. Misalnya pada aplikasi e-commerce. Jika pengguna menambahkan produk ke keranjang belanja, controller akan mengatur supaya model menyimpan data tersebut dan kemudian memberi tahu view untuk memperbarui tampilan. 

### MVT (Model - View - Template)
#### Model
Sama seperti MVC, model adalah komponen konsep MVT yang bertanggung jawab untuk **mengatur dan mengelola data aplikasi**. Model mewakili struktur data dan logika aplikasi  di balik tampilan. Model menghubungkan aplikasi ke database dan mengelola interaksi dengan data tersebut.

#### View
View merupakan komponen yang mengatur logika presentasi dalam konsep MVT. View ini mengontrol cara data yang dikelola model ditampilkan kepada pengguna. Dalam konteks MVT, tampilan bertindak sebagai **pengatur yang menampilkan dan mengambil data dari model** untuk dipresentasikan kepada pengguna.

#### Template
Template dalam MVT adalah bagian yang bertanggung jawab untuk **mengatur tampilan pengguna**, contohnya seperti halaman web. Dalam kerangka kerja seperti Django, Template digunakan untuk merancang tampilan halaman web dan menggabungkan data dari Model sehingga pengguna dapat melihat informasi yang dihasilkan melalui view.

### MVVM (Model - View - ViewModel)
#### Model
Model dalam MVVM adalah komponen yang **mengelola data dan logika aplikasi**, serupa dengan Model dalam MVC dan MVT. Model dan ViewModel pada MVVM ini nantinya akan bekerja sama untuk mengambil dan menyimpan data.

#### View
View dalam MVVM adalah komponen yang bertanggung jawab untuk **menampilkan tampilan dan memberi tahu ViewModel tentang tindakan pengguna**. Namun, dalam MVVM, View berfungsi sebagai penampil pasif yang hanya menampilkan data dan tidak mengandung logika aplikasi apapun.

#### ViewModel
ViewModel adalah salah satu komponen utama dalam MVVM yang bertindak sebagai jembatan antara Model dan View. ViewModel **mengubah data dari Model menjadi format yang dapat ditampilkan oleh View dan mengelola logika tampilan**. Misalnya, jika kita memiliki aplikasi cuaca, ViewModel akan mengambil data cuaca dari Model dan merubahnya menjadi format yang dapat ditampilkan oleh View, seperti ikon cuaca, suhu, dan deskripsi.

### Perbedaan MVC, MVT, dan MVVM
#### MVC
MVC adalah pola desain yang telah digunakan dalam berbagai jenis aplikasi, termasuk aplikasi desktop, web, dan mobile. Ini adalah konsep yang serbaguna dan diterapkan secara luas. Dalam MVC, Controller memiliki peran yang cukup aktif dalam mengatur aliran informasi antara Model dan View. Model dan View juga dapat berinteraksi secara langsung dalam beberapa kasus. Dalam kata lain, MVC terfokus pada pemisahan tugas dengan Model yang mengelola data dan logika bisnis, View yang menampilkan data, dan Controller yang mengatur aliran informasi dan dalam MVC, developer harus sering mengelola secara manual pembaruan tampilan setiap kali data berubah. Ini dapat memerlukan kode tambahan untuk menghubungkan Model dan View.

#### MVT
MVT adalah konsep yang utamanya digunakan dalam pengembangan web dengan menggunakan kerangka kerja Django yang berbasis Python. Salah satu komponen istimewanya, yaitu Template (dalam MVT (Django)), dikhususkan mengatur tampilan halaman web, sedangkan Model dan View berperan seperti dalam MVC. Template adalah komponen tambahan yang tidak ada dalam MVC tradisional dan _framework_ ini memiliki alat bawaan untuk mengurus pembaruan tampilan secara otomatis ketika data berubah.

#### MVVM
MVVM sering digunakan dalam pengembangan aplikasi berbasis antarmuka pengguna (UI), seperti aplikasi mobile atau desktop. Ini memiliki fokus untuk memisahkan tugas tampilan dan logika dalam UI. Adanya ViewModel yang bertindak sebagai perantara antara Model dan View memungkinkan keduanya untuk tetap terpisah dan mengurangi ketergantungan antara keduanya. MVVM ini mengandalkan sistem pengikatan data (_data binding_) untuk secara otomatis memperbarui tampilan ketika data berubah di ViewModel. Ini mengurangi kode boilerplate yang diperlukan untuk pembaruan tampilan, tetapi jika _data binding_ tersebut sangat kompleks, akan sedikit lebih sulit untuk melakukan _debugging_ aplikasinya