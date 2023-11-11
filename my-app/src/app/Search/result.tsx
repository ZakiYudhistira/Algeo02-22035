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
    {
      imageUrl: "/kelompok7.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok8.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok9.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok10.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok11.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok12.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok13.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },

    {
      imageUrl: "/kelompok14.jpg",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok15.jpg",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok16.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok17.jpg",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok18.jpg",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok19.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok20.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok21.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok22.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok23.jpg",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok23.jpg",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok19.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok20.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok21.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok22.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok23.jpg",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok23.jpg",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok19.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok20.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok21.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok22.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok23.jpg",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok23.jpg",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok19.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok20.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok21.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok22.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok23.jpg",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok23.jpg",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok19.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok20.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok21.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok22.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok23.jpg",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok23.jpg",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok19.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok20.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok21.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok22.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok23.jpg",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok23.jpg",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok19.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok20.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok21.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok22.png",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok23.jpg",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
    {
      imageUrl: "/kelompok23.jpg",
      width: 1080,
      height: 1920,
      cosValue: "0.5",
    },
  ];
  return (
    <main className="px-8 sm:px-10 md:px-14 relative z-10 lg:px-20 xl:px-32 2xl:px-36 bg-custom-blue min-h-screen overflow-hidden">
      <div className="flex flex-row items-center justify-between">
        <h1 className="font-montserrat lg:my-8 z-20 text-[28px] lg:text-4xl text-custom-green-dark font-bold scale-x-105">
          Search Results
        </h1>
        <p className="text-right text-black text-base font-outline">
          54 results in 0.7 seconds
        </p>
      </div>

      <ResultClient data={dummyData} />
    </main>
  );
}
