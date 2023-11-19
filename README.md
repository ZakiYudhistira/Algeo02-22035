> APLIKASI ALJABAR VEKTOR DALAM SISTEM TEMU BALIK GAMBAR

Tugas besar Aljabar Linier dan Geomteri, dibuat oleh :
Zaki Yudhistira Candra/13522031
Amalia Putri/13522042
Angelica Kierra/13522048

# Content Based Image Retrieval

> Terdapat dua fitur CBIR yang dapat digunakan yaitu, CBIR dengan parameter Warna dan Teksur
> Video Explanation [_here_](https://www.example.com).

## Table of Contents

- [General Info](#general-information)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Screenshots](#screenshots)
- [Setup](#setup)
- [Usage](#usage)

## General Information

- Provide general information about your project here.
- What problem does it (intend to) solve?
- What is the purpose of your project?
- Why did you undertake it?
<!-- You don't have to answer all the questions - just the ones relevant to your project. -->

## Technologies Used

- Python - version 3.10.5
- NextJs - next@14.0.1
- Flask - version 3.0.0

## Features

- Content Based Image Retrieval dengan Parameter Texture (UTAMA)
- Content Based Image Retrieval dengan Parameter Warna (UTAMA)
- CBIR dengan menggunakan Kamera
- Image Scraping
- Caching
- Download as PDF

## Screenshots

![Example screenshot](./img/screenshot.png)

## Setup

1. Start program website

- cd src/my-app
- npm install
- npm run dev

2. Start program API

- cd src
- python app.py

## Usage

### CBIR-WARNA

1. Upload gambar query atau menggunakan kamera
2. Upload dataset gambar atau masukan link URL sebagai dataset
3. Pilih seleksi warna
4. Tekan tombol 'Search'
5. Tunggu hasil pencarian
6. Mengunduh hasil pencarian (opsional)

### CBIR-TEKSTUR

1. Upload gambar query atau menggunakan kamera
2. Upload dataset gambar atau masukan link URL sebagai dataset
3. Pilih seleksi teksur
4. Tekan tombol 'Search'
5. Tunggu hasil pencarian
6. Mengunduh hasil pencarian (opsional)

- Mencari cosine similarity berdasarkan konsep CBIR warna atau CBIR tekstur dari input gambar/frame camera dan dataset/image scraping
- Mengurutkan nilai cosine similarity dari yang terbesar hingga terkecil dengan kemiripan > 60% saja yang ditampilkan
- Mengunduh hasil pencarian berupa gambar yang ditampilkan dalam format PDF

## Project Status

Project is: _complete_.

## Room for Improvement

Ruang perbaikan:

- Penampilan website yang dapat dibuat secara responsif mengikuti media yang digunakan oleh pengguna, seperti handphone, tablet, dan laptop.

Yang akan dilakukan kedepannya:

- Mengatur tampilan website dengan width dan height yang lebih baik sehingga dapat menyesuaikan dengan media yang digunakan oleh pengguna.

## Acknowledgements

Kami mengucapkan terima kasih kepada:

- Tuhan Yang Maha Esa
- Kak Fahziar Wutono, alumni IF ITB 2012 (kakak mentornya amel)
- Apartemen GCA 2 sebagai markas nubes
- Kak Alex Sander, asisten pembimbing
- Mie gacoan level 0 dan level 1, udang keju, dan es milo

## Github Profile

Created by
[@ZakiYudhistira](https://github.com/ZakiYudhistira)
[@amaliap21](https://github.com/amaliap21)
[@angiekierra](https://github.com/angiekierra)
