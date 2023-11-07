import Image from "next/image";
import Link from "next/link";
import React from "react";

const Hero = () => {
  return (
    <div className="flex flex-col gap-5">
      <div className="">
        <h1 className="text-center text-custom-green font-montserrat lg:leading-[70px] text-[30px] lg:text-5xl font-bold tracking-[0.54px]">
          Reverse
          <span className="text-center text-custom-black font-montserrat text-[30px] lg:text-5xl font-bold">
            Image Search
          </span>
        </h1>
      </div>
    </div>
  );
};

export default Hero;
