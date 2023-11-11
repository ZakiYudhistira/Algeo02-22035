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
      <div className="flex flex-wrap justify-center mt-5 gap-5">
        <div className="relative w-[600px] lg:w-fit">
          <Image
            src="/how-to.svg"
            alt="Image Input"
            width={600}
            height={600}
            className="w-[600px] lg:w-fit -z-[1]"
          ></Image>
          <div className="absolute top-[47%] left-[14%] transform -translate-x-1/2 -translate-y-1/2 text-center text-white">
            <p className="text-2xl font-outfit font-semibold">
              Upload image & <br />
              upload dataset
            </p>
          </div>
          <div className="absolute top-[47%] left-[48%] transform -translate-x-1/2 -translate-y-1/2 text-center text-white">
            <p className="text-2xl font-outfit font-semibold">
              Choose color
              <br />
              or texture
            </p>
          </div>
          <div className="absolute top-[47%] right-[4%] transform -translate-x-1/2 -translate-y-1/2 text-center text-white">
            <p className="text-2xl font-outfit font-semibold">
              Search and wait <br />
              for the result
            </p>
          </div>
        </div>
      </div>
      <div className="relative">
        <Button
          variant="outline"
          className="absolute left-[42%] text-xl text-white bg-custom-pink font-semibold font-raleway rounded-xl px-8 py-7"
        >
          <Link href="/Search">Use it now</Link>
        </Button>
      </div>
    </div>
  );
};

export default Howto;
