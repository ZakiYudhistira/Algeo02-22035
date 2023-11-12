"use client";

import { useState, useRef } from "react";
import Image from "next/image";
import ResultClient from "./result-client";

export default function Home({ imagedataset }: { imagedataset: File[] }) {
  const [startTime, setStartTime] = useState<number | null>(null);

  const getElapsedTime = () => {
    if (startTime) {
      const currentTime = new Date().getTime();
      const elapsedTime = (currentTime - startTime) / 1000; // Convert to seconds
      console.log(elapsedTime);
      return `Time: ${elapsedTime.toFixed(2)} seconds`;
    }
    return "";
  };

  return (
    <main className="px-8 sm:px-10 md:px-14 relative z-10 lg:px-20 xl:px-32 2xl:px-36 bg-custom-blue min-h-screen overflow-hidden">
      <div className="flex flex-row items-center justify-between">
        <h1 className="font-montserrat lg:my-8 z-20 text-[28px] lg:text-4xl text-custom-green-dark font-bold scale-x-105">
          Search Results
        </h1>
        <p className="text-right text-black text-base font-outline">
          {imagedataset?.length} results in {getElapsedTime()} seconds
        </p>
      </div>

      <ResultClient data={imagedataset} />
    </main>
  );
}
