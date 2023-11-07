import Image from "next/image";
import Link from "next/link";
import React from "react";
import { Button } from "@/components/ui/button";
const Hero = () => {
  return (
    <div className="bg-scroll"
        style={{
          backgroundImage: `url('/foreword.png')`,
          height: "972px",
     }}>
      <div className="flex flex-col justify-center">
        <h1 className="text-center text-custom-green font-outfit lg:leading-[50px] text-[83px] lg:text-6xl font-extrabold tracking-[0.54px]">
          Reverse
        </h1>
        <h1 className="text-center text-custom-black font-outfit text-[83px] lg:text-6xl font-extrabold">
          Image Search
        </h1>
        <p className="text-center text-custom-black font-outfit text-[15px] lg:text-s font-regular font-raleway mt-[10px]">
          Kami dari kelompok 4 Keluarga Cemara dari kelas IF 01<br/>
          yang beranggotakan Amel, Zaki, Angie. Project Reverse Image Search ini merupakan<br/>
          tugas besar mata kuliah IF2123 Aljabar Linear dan Geometri.
          </p>
        <div className="flex justify-center">
          <Button
            variant="outline"
            className="text-white bg-custom-green-dark font-semibold font-raleway mt-5"
            >
            Explore More
          </Button>
        </div>
      </div>
    </div>
    
  );
};

export default Hero;
