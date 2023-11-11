"use client";

import { useState, useRef } from "react";
import Image from "next/image";
import ResultClient from "./result-client";

export default function Home() {
  const dummyData = [
    {
      imageUrl: "/dummy-black.jpg",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/orang.jpg",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok3.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok4.jpg",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok5.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok6.jpg",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
  ];

  const [imagedataset, setImagedataset] = useState<File[] | null>(null);
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

      <ResultClient data={dummyData} />
    </main>
  );
}
