// "use client";

import Cbir from "@/components/cbir";
// import DataFetcher from "@/components/ui/data-fetcher";
import Hero from "@/components/hero";
import Howto from "@/components/howto";
import React from "react";
// DataFetcher;

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col justify-between px-24 pt-8 pb-24">
      <Hero />
      <Hero />
      <Cbir />
      <Howto />
    </main>
  );
}
