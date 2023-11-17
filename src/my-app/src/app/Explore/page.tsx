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
      <div className="box-content w-[42.5rem]">
        <p className="text-custom-black font-outfit lg:text-xl font-normal text-justify mb-[6rem] mt-10">
          Selamat malam teman-teman ITB, di sini saya ingin menjelaskan sedikit
          tentang bagaimana cara mendapatkan seorang kekasih di ITB, terutama di
          tengah gempuran tubes dan ketidakpastian dari kondisi pasar kencan.
          Cara mudahnya adalah, Anda harus menjadi good looking dan berduit
          banyak, tetapi saya yakin, banyak wanita/pria berkualitas baik yang
          lebih mengutamakan atitud ketimbang material lainnya.
        </p>
      </div>
      <h1 className="text-custom-green-dark font-outfit lg:text-3xl font-bold tracking-[0.54px]">
        Meet the team
      </h1>
      <div className="flex flex-row mt-5 mb-[6.75rem]">
        <div className="box-content h-[25.25rem] w-[17rem] mr-[1rem] rounded-[1rem] bg-white shadow-xl">
          <Image
            src="/sukuna.jpg"
            alt="Image Input"
            width={272}
            height={308}
            className="w[17rem] rounded-[1rem]"
          ></Image>
          <h1 className="text-custom-green font-Outfit lg:text-2xl font-bold tracking-[0.54px] mt-[1.75rem] ml-[1.25rem]">
            Zaki Yudhistira
          </h1>
          <p className="ml-[1.25rem]">13522031</p>
        </div>
        <div className="box-content h-[25.25rem] w-[17rem] mr-[1rem] rounded-[1rem] bg-white shadow-xl">
          <Image
            src="/sukuna.jpg"
            alt="Image Input"
            width={272}
            height={308}
            className="w[17rem] rounded-[1rem]"
          ></Image>
          <h1 className="text-custom-green font-Outfit lg:text-2xl font-bold tracking-[0.54px] mt-[1.75rem] ml-[1.25rem]">
            Amalia Putri
          </h1>
          <p className="ml-[1.25rem]">13522042</p>
        </div>
        <div className="box-content h-[25.25rem] w-[17rem] rounded-[1rem] bg-white shadow-xl">
          <Image
            src="/sukuna.jpg"
            alt="Image Input"
            width={272}
            height={308}
            className="w[17rem] rounded-[1rem]"
          ></Image>
          <h1 className="text-custom-green font-Outfit lg:text-2xl font-bold tracking-[0.54px] mt-[1.75rem] ml-[1.25rem]">
            Angelica Kierra
          </h1>
          <p className="ml-[1.25rem]">13522048</p>
        </div>
      </div>
      <h1 className="text-custom-pink font-montserrat lg:text-7xl font-bold tracking-[0.54px] mt-5">
        Explore
      </h1>
      <div className="box-content w-[42.5rem]">
        <p className="text-custom-black font-outfit lg:text-xl font-normal text-justify mb-[6rem] mt-5">
          Selamat malam teman-teman ITB, di sini saya ingin menjelaskan sedikit
          tentang bagaimana cara mendapatkan seorang kekasih di ITB, terutama di
          tengah gempuran tubes dan ketidakpastian dari kondisi pasar kencan.
          Cara mudahnya adalah, Anda harus menjadi good looking dan berduit
          banyak, tetapi saya yakin, banyak wanita/pria berkualitas baik yang
          lebih mengutamakan atitud ketimbang material lainnya.
        </p>
      </div>
      <h1 className="text-custom-green-dark font-outfit lg:text-3xl font-bold tracking-[0.54px]">
        CBIR overview
      </h1>
      <div className="box-content w-[42.5rem]">
        <p className="text-custom-black font-outfit lg:text-xl font-normal text-justify mb-[6rem] mt-5">
          Selamat malam teman-teman ITB, di sini saya ingin menjelaskan sedikit
          tentang bagaimana cara mendapatkan seorang kekasih di ITB, terutama di
          tengah gempuran tubes dan ketidakpastian dari kondisi pasar kencan.
          Cara mudahnya adalah, Anda harus menjadi good looking dan berduit
          banyak, tetapi saya yakin, banyak wanita/pria berkualitas baik yang
          lebih mengutamakan atitud ketimbang material lainnya.
        </p>
      </div>
      <h1 className="text-custom-green-dark font-outfit lg:text-3xl font-bold tracking-[0.54px]">
        How our system works
      </h1>
    </div>
  );
};

export default Explore;
