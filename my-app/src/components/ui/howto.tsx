import Image from "next/image";
import Link from "next/link";
import React from "react";
import { Button } from "@/components/ui/button";
const Howto = () => {
  return (
    <div className="h-screen mt-[30vh]">
      <h1 className="text-center text-custom-black font-outfit lg:leading-[50px] text-[83px] lg:text-6xl font-extrabold tracking-[0.54px]">
        How To
        <span className="text-custom-pink font-outfit lg:leading-[50px] text-[83px] lg:text-6xl font-extrabold">
          {" "}
          Use
        </span>{" "}
      </h1>
      <div className="flex flex-wrap justify-center mt-16 gap-5">
        <div className="relative w-[600px] lg:w-fit">
          <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 text-center text-white">
            <p className="font-medium">
              Upload image & <br />
              upload dataset
            </p>
          </div>
          <Image
            src="/circle-1.svg"
            alt="Image Input"
            width={600}
            height={600}
            className="w-[600px] lg:w-fit -z-[1]"
          ></Image>
        </div>

        <div className="relative">
          <p className="absolute text-center my-9 ml-6 pt-7 text-white font-medium">
            Choose color or
            <br />
            texture
          </p>
          <Image
            src="/circle-1.svg"
            alt="Image Input"
            width={600}
            height={600}
            className="w-[600px] lg:w-fit -z-[1]"
          ></Image>
        </div>
        <div className="relative">
          <p className="absolute text-center my-8 ml-6 pt-7 text-white font-medium">
            Search and wait <br />
            for the result
          </p>
          <Image
            src="/circle-1.svg"
            alt="Image Input"
            width={600}
            height={600}
            className="w-[600px] lg:w-fit -z-[1]"
          ></Image>
        </div>

        <Button
          variant="outline"
          className="text-white bg-custom-green font-semibold font-raleway mt-5 rounded-xl px-7"
        >
          Use it now
        </Button>
      </div>
    </div>
  );
};

export default Howto;
