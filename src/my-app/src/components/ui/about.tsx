import React from "react";
import Image from "next/image";

const About = () => {
  return (
    <div id="about" className=" flex flex-col md:flex-col gap-5 lg:gap-10 overflow-hidden z-10">
      <h1 className=" text-center text-[#FADE7A] font-montserrat text-[32px] lg:text-5xl font-[700] tracking-[0.54px] leading-[140%]">
        About{" "}
        <span className=" text-center text-white font-montserrat font-[700]">
          Us
        </span>
      </h1>
      <div className="flex flex-col md:flex-row overflow-hidden">
        <div className="w-full overflow-hidden flex flex-col items-center justify-center lg:items-start lg:flex-row lg:justify-start gap-10 lg:gap-10">
          <Image
            src="/gajah.png"
            alt="gajah"
            width={500}
            height={500}
            className="w-[225px] h-[225px] lg:w-[400px] lg:h-[400px] object-center object-contain"
          />
          <Image
            src="/home-gajah.svg"
            alt="background"
            width={750}
            height={700}
            className="lg:w-[500px] lg:h-[500px] w-[300px] h-[500px] absolute -left-[130px] top-[590px] z-[-1] overflow-hidden"
          />
          <div className="flex-1 flex flex-col justify-start px-25">
            <p className=" flex break-normal text-justify text-white font-montserrat text-[16px] lg:text-xl font-[400] tracking-[0.16px] leading-[140%]">
              “Byte” sebagai wadah untuk mengaktualisasi diri yang dapat
              memahami posisi peran dalam berhimpun, serta mengembangkan rasa
              empati dalam mewujudkan ikatan kekeluargaan sebagai satu angkatan.
              <br />
              <br />
              Terdapat komitmen yang kuat untuk memahami dengan mendalam peran
              serta potensi yang dimiliki, baik dalam lingkungan angkatan maupun
              dalam himpunan secara keseluruhan. Kami bersemangat untuk
              mengoptimalkan setiap potensi dan peran yang kami miliki saat kami
              bersatu, dengan harapan dapat mencapai tingkat aktualisasi diri
              yang lebih tinggi dari sebelumnya.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default About;
