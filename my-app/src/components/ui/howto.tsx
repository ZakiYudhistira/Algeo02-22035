import Image from "next/image";
import Link from "next/link";
import React from "react";
import { Button } from "@/components/ui/button";
const Howto = () => {
return (
  <div className="relative">
    <div className="flex flex-col justify-center">
      <h1 className="text-center text-custom-black font-outfit lg:leading-[50px] text-[83px] lg:text-6xl font-extrabold tracking-[0.54px]">
        How To
        <span className="text-custom-pink font-outfit lg:leading-[50px] text-[83px] lg:text-6xl font-extrabold">
        {" "}
          Use
        </span>{" "}
      </h1>
      
      <div className="flex flex-wrap justify-center mt-10 gap-5">
        <div className="relative">
          <p className="absolute text-center my-8 ml-6 pt-7 text-white font-medium">
            Upload image & <br/>
            upload dataset
          </p>
          <Image
            src="/circleHow.png"
            alt="Image Input"
            width={600}
            height={600}
            className="w-[600px] lg:w-fit -z-[1]"
          ></Image>
        </div>
        <div className="relative">
          <p className="absolute text-center my-9 ml-6 pt-7 text-white font-medium">
            Choose color or<br/>
            texture
          </p>
          <Image
            src="/circleHow.png"
            alt="Image Input"
            width={600}
            height={600}
            className="w-[600px] lg:w-fit -z-[1]"
          ></Image>
        </div>
        <div className="relative">
          <p className="absolute text-center my-8 ml-6 pt-7 text-white font-medium">
            Search and wait <br/>
            for the result
          </p>
          <Image
            src="/circleHow.png"
            alt="Image Input"
            width={600}
            height={600}
            className="w-[600px] lg:w-fit -z-[1]"
          ></Image>
        </div>
      </div>
      
      <div className="flex justify-center mt-7">
        <Button
          variant="outline"
          className="text-white bg-custom-green font-semibold font-raleway mt-5 rounded-xl px-7"
          >
          Use it now
        </Button>
      </div>
    </div>
  </div>
  
);
};

export default Howto;
