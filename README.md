<div id="top"></div>

<br />
<div align="center">
    <img src="https://github.com/ghebyon/Tucil03-13520079/blob/main/src/icons/GUI-15Puzzle.JPG" width="500" height="">

  <h2 align="center">15-PUZZLE SOLVER</h2>

  <p align="center">
    Program untuk Memecahkan 15-Puzzle dengan Menggunakan Algoritma Branch and Bound
    <br />
    <a href="https://github.com/ghebyon/Tucil03-13520079/tree/main/docs"><strong>Telusuri Dokumen>></strong></a>
    <br />
    <br />

  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#tentang-projek">Tentang Projek</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#penggunaan">Penggunaan</a></li>
    <li><a href="#author">Author</a></li>
  </ol>
</details>

## Tentang Projek
Program ini merupakan program pencarian solusi pada Permainan 15-Puzzle dengan pengaplikasian algoritma Branch and Bound. Aplikasi disediakan dalam bentuk Graphical User Interface dan Command Line Interface. GUI dibuat dengan menggunakan tools Qt Designer dan PyQt5

### Algoritma Branch and Bound
1. Sediakan list notVisited dan list visited.
2. Input suatu Puzzle dan dijadikan sebagai root Puzzle. Masukkan root Puzzle ke dalam list notVisited
3. Untuk setiap Puzzle pada list notVisited, hitung costnya dengan heuristik 

    c(x) = f(x) + g(x)
        
    Keterangan :
    - c(x) = cost untuk simpul x
    - f(x) = cost untuk mencapai simpul x dari akar
    - g(x) = taksiran panjang lintasan terpendek dari P ke simpul solusi
    
    Pilih Puzzle dengan cost terendah sebagai currentPuzzle
4. Periksa apakah puzzle merupakan solusi atau tidak

    - Jika ya, maka pencarian dihentikan
    - Jika tidak, lanjutkan
5. Tentukan pergerakan selanjutnya yang memungkinkan. Syarat pergerakan yang memungkinkan :
    - Slot kosong pada puzzle bergerak ke arah kiri, kanan, atas, atau bawah.
    - Pergerakan tersebut tidak menghasilkan Puzzle yang sudah pernah dikunjungi (tidak terdapat pada list visited)
6. Hapus currentPuzzle dari list notVisited dan 7.masukkan ke dalam listVisited
7. Kembali ke langkah 2


### Built With
* [Qt Designer](https://build-system.fman.io/qt-designer-download)
* [PyQt5](https://pypi.org/project/PyQt5/)

## Penggunaan

### Menggunakan Command Line Interface
1. Buka command line dan arahkan firectory ke folder src
2. Jalankan dengan command

    `python cliTest.py
    `

### Menggunakan Graphical User Interface
1. Buka folder bin dan run file main.exe
2. Masukkan input (dapat dilakukan secara manual maupun dengan mengarahkan directory menggunakan tombol file di kanan bawah)
3. Tekan tombol search yang ada di bawah input puzzle
4. Tunggu sampai kolom solusi menampilkan hasil
5. Kecepatan animasi puzzle dapat diubah dengan menggunakan horizontal slider

## Author
- 13520079 Ghebyon Tohada Nainggolan


<p align="right">(<a href="#top">back to top</a>)</p>