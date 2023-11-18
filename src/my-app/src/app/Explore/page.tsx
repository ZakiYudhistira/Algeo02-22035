import React, { Component } from "react";
import Image from "next/image";

const Explore = () => {
  return (
    <div className="flex min-h-screen flex-col px-24 pt-8 pb-24 relative ">
      <Image
        src="/about-1.svg"
        alt="about-1"
        width={1645}
        height={1271}
        className="absolute left-0 -z-[5] lg:w-[100%]"
      ></Image>
      <h1 className="text-custom-pink font-montserrat lg:text-7xl font-bold tracking-[0.54px] mt-10">
        About Us
      </h1>
      <div className="box-content w-[53.25rem]">
        <p className="text-custom-black font-outfit lg:text-xl font-normal text-justify mb-[6rem] mt-10">
          Kami dari kelompok 04, bernama {"Keluarga Cemara"}. Kami terdiri dari
          3 orang yang semuanya dari kelas K01. Jujur banget, ini pertama kali
          kami nguli website, tapi gapapa. Jadinya, kami banyak explore hal
          baru. So... maap ya kalo website-nya jelek, kami masih belajar hehe😋
        </p>
      </div>
      <h1 className="text-custom-green-dark font-outfit lg:text-3xl font-bold tracking-[0.54px]">
        Meet the team
      </h1>
      <div className="flex flex-row mt-5 mb-[6.75rem]">
        <div className="box-content h-[28.25rem] w-[17rem] mr-[1rem] rounded-[1rem] bg-white shadow-xl">
          <Image
            src="/mas_jaki.jpg"
            alt="Image Input"
            width={272}
            height={308}
            className="w[17rem] rounded-[1rem]"
          ></Image>
          <h1 className="text-custom-green font-Outfit lg:text-2xl font-bold tracking-[0.54px]  mt-[1rem] ml-[1.25rem]">
            Zaki Yudhistira
          </h1>
          <p className="ml-[1.25rem]">13522031</p>
        </div>
        <div className="box-content h-[28.25rem] w-[17rem] mr-[1rem] rounded-[1rem] bg-white shadow-xl">
          <Image
            src="/melmel.jpg"
            alt="Image Input"
            width={272}
            height={308}
            className="w[17rem] rounded-[1rem]"
          ></Image>
          <h1 className="text-custom-green font-Outfit lg:text-2xl font-bold tracking-[0.54px] mt-[1rem] ml-[1.25rem]">
            Amalia Putri
          </h1>
          <p className="ml-[1.25rem]">13522042</p>
        </div>
        <div className="box-content h-[28.25rem] w-[17rem] mr-[1rem] rounded-[1rem] bg-white shadow-xl">
          <Image
            src="/dede_enji.jpg"
            alt="Image Input"
            width={272}
            height={308}
            className="w[17rem] rounded-[1rem]"
          ></Image>
          <h1 className="text-custom-green font-Outfit lg:text-2xl font-bold tracking-[0.54px] mt-[1rem] ml-[1.25rem]">
            Angelica Kierra
          </h1>
          <p className="ml-[1.25rem]">13522048</p>
        </div>
      </div>
      <h1 className="text-custom-pink font-montserrat lg:text-7xl font-bold tracking-[0.54px] mt-5">
        Explore
      </h1>
      <div className="box-content  w-[53.25rem]">
        <p className="text-custom-black font-outfit lg:text-xl font-normal text-justify mb-[6rem] mt-5">
          Ini adalah tugas besar ke-2 mata kuliah Aljabar Linier dan Geometri
          IF2123. Di website ini, pengguna dapat menjelajahi informasi visual
          yang tersimpan di berbagai platform, baik itu dalam bentuk pencarian
          gambar pribadi, analisis gambar medis untuk diagnosis, pencarian
          ilustrasi ilmiah hingga pencarian produk berdasarkan gambar komersial.
        </p>
      </div>
      <h1 className="text-custom-green-dark font-outfit lg:text-3xl font-bold tracking-[0.54px]">
        CBIR overview
      </h1>
      <div className="box-content  w-[53.25rem]">
        <p className="text-custom-black font-outfit lg:text-xl font-normal text-justify mb-[6rem] mt-5">
          Content-Based Image Retrieval (CBIR) adalah metode pencarian gambar
          berdasarkan fitur-fitur visualnya. Proses ini melibatkan ekstraksi
          fitur seperti warna, tekstur, dan bentuk dari gambar, diwakili sebagai
          vektor numerik. Melalui algoritma pencocokan, CBIR membandingkan
          vektor-fitur gambar yang dicari dengan dataset, menghasilkan urutan
          gambar yang paling mirip secara visual. CBIR memungkinkan pengguna
          mengeksplorasi koleksi gambar secara efisien yang fokus pada kemiripan
          citra visual.
        </p>
      </div>
      <div className="relative h-[1150px] ">
        <h1 className="text-custom-green-dark font-outfit lg:text-3xl font-bold tracking-[0.54px]">
          How our system works
        </h1>
        <p className="text-custom-black font-outfit lg:text-xl font-normal text-justify mb-[6rem] p-48">
          <h2 className="text-custom-green-dark font-outfit text-2xl font-semibold">
            Parameter Warna
          </h2>
          CBIR dengan parameter warna adalah teknik Content-Based Image
          Retrieval yang memanfaatkan spektrum warna dalam suatu gambar. Proses
          ini melibatkan ekstraksi dan perbandingan fitur-fitur visual untuk
          menemukan gambar serupa. CBIR menggunakan karakteristik warna pada
          setiap pixel, diekspresikan melalui histogram warna, untuk menilai
          kemiripan antara gambar. Dengan fokus pada representasi warna, CBIR
          memungkinkan pencarian gambar berdasarkan kesamaan visual, memberikan
          hasil yang relevan dan efisien dalam mengidentifikasi gambar dengan
          warna serupa dalam dataset.
          <br />
          <br />
          <h2 className="text-custom-green-dark font-outfit text-2xl font-semibold">
            Parameter Tekstur
          </h2>
          CBIR dengan parameter tekstur adalah metode Content-Based Image
          Retrieval yang memanfaatkan karakteristik tekstur dalam suatu gambar.
          Ini melibatkan ekstraksi pola tekstur yang membedakan objek atau area
          dalam gambar. Proses CBIR dengan parameter tekstur melibatkan analisis
          pola spesifik pada struktur permukaan gambar. Gambar diubah menjadi
          matriks dan diperlakukan sebagai citra Grayscale untuk memfasilitasi
          pemrosesan. Dengan fokus pada tekstur, CBIR ini memungkinkan pencarian
          gambar berdasarkan kemiripan pola tekstur, memberikan hasil yang
          relevan dan efisien dalam menemukan gambar dengan karakteristik
          tekstur serupa dalam dataset.
          <br />
          <br />
          <h2 className="text-custom-green-dark font-outfit text-2xl font-semibold">
            Front-End Website
          </h2>
          Untuk pembuatan front-end website, sistem ini memanfaatkan Next.js,
          sebuah framework React, untuk mempermudah pengembangan web. Dirancang
          oleh tim Vercel, Next.js menyediakan fitur-fitur seperti Server-Side
          Rendering (SSR), Static Site Generation (SSG), dan routing berbasis
          file system. Framework ini memungkinkan pengembang membuat aplikasi
          web responsif, efisien, dan mudah diatur. Dengan fokus pada kemudahan
          pengembangan, Next.js memfasilitasi pembuatan aplikasi web yang lebih
          baik dalam hal kinerja dan responsivitas.
          <br />
          <br />
          <h2 className="text-custom-green-dark font-outfit text-2xl font-semibold">
            Back-End Website
          </h2>
          Untuk pembuatan back-end website, sistem ini framework yang digunakan
          adalah Flask yang merupakan berbasis python. Flask dipilih karena
          kalkulasi CBIR menggunakan bahasa python. Flask dirancang untuk
          menjadi sederhana, fleksibel, dan mudah dipahami, memungkinkan
          pengembang untuk membuat aplikasi web dengan cepat tanpa kompleksitas
          yang berlebihan.
        </p>
      </div>
      <div className="flex justify-center mt-20">
        <Image
          src="/system.png"
          alt="Image Input"
          width={1250}
          height={1000}
          className="absolute bottom-14 w[1250px] rounded-[1rem] -z-[1]"
        ></Image>
      </div>
    </div>
  );
};

export default Explore;
