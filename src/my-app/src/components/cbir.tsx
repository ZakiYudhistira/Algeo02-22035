import Image from "next/image";
import Link from "next/link";
import React from "react";
import { Button } from "@/components/ui/button";

const Cbir = () => {
  return (
    <div className="h-screen">
      <Image
        src="/home-2.svg"
        alt="Image Input"
        width={500}
        height={500}
        className="absolute left-0 lg:w-full -z-[2]"
      ></Image>
      <div className="flex flex-col justify-start mt-[35vh]">
        <h1 className="text-custom-black font-outfit lg:text-7xl font-extrabold">
          CBIR
        </h1>
        <p className="text-custom-black font-outfit lg:text-xl font-regular mt-[10px]">
          Kami dari kelompok 4 Keluarga Cemara dari kelas IF 01
          <br />
          yang beranggotakan Amel, Zaki, Angie. Project Reverse Image Search ini
          merupakan
          <br />
          tugas besar mata kuliah IF2123 Aljabar Linear dan Geometri.
        </p>
        <div>
          <Link href="/Search">
            <Button
              variant="outline"
              className="text-white text-xl bg-custom-pink font-semibold font-raleway mt-5 px-14 py-6 rounded-xl"
            >
              Try it now
            </Button>
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Cbir;
