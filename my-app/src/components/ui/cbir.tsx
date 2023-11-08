import Image from "next/image";
import Link from "next/link";
import React from "react";
import { Button } from "@/components/ui/button";
const Cbir = () => {
return (
  <div className="content-end h-[784px]">
    <div className="flex flex-col justify-left">
      <h1 className="text-left text-custom-black font-outfit lg:leading-[50px] text-[83px] lg:text-6xl font-extrabold tracking-[0.54px]">
        CBIR
      </h1>
      <p className="text-left text-custom-black font-outfit text-[15px] lg:text-s font-regular font-raleway mt-[10px]">
        Kami dari kelompok 4 Keluarga Cemara dari kelas IF 01<br/>
        yang beranggotakan Amel, Zaki, Angie. Project Reverse Image Search ini merupakan<br/>
        tugas besar mata kuliah IF2123 Aljabar Linear dan Geometri.
        </p>
      <div className="flex justify-left">
        <Button
          variant="outline"
          className="text-white bg-custom-pink font-semibold font-raleway mt-5 px-20 rounded-xl"
          >
          Try it now
        </Button>
      </div>
    </div>
  </div>
  
);
};

export default Cbir;