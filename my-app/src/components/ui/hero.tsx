import Image from "next/image";
import Link from "next/link";
import React from "react";
import { Button } from "@/components/ui/button";

const Hero = () => {
  return (
    <div className="h-screen">
      <Image
        src="/home-1.svg"
        alt="Image Input"
        width={500}
        height={500}
        className="absolute left-0 top-0 lg:w-[100%] -z-[1]"
      ></Image>
      <div className="flex flex-col justify-center gap-10 pt-20">
        <h1 className="text-center text-custom-green font-outfit text-8xl font-extrabold tracking-[0.54px]">
          Reverse
          <br />
          <span className="text-center text-custom-black font-outfit text-8xl font-extrabold">
            Image Search
          </span>
        </h1>
        <p className="text-center text-custom-black font-outfit text-xl font-regular mt-[10px]">
          Kami dari kelompok 4 Keluarga Cemara dari kelas IF 01
          <br />
          yang beranggotakan Amel, Zaki, Angie. Project Reverse Image Search ini
          merupakan
          <br />
          tugas besar mata kuliah IF2123 Aljabar Linear dan Geometri.
        </p>
        <div className="flex justify-center">
          <Button
            variant="outline"
            className="text-white text-lg bg-custom-green-dark font-semibold font-raleway py-6 px-8 rounded-xl"
          >
            <Link href="/Explore">Explore More</Link>
          </Button>
        </div>
      </div>
    </div>
  );
};

export default Hero;
