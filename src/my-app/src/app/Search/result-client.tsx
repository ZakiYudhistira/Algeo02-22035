"use client";
import ResultCard from "@/app/Search/result-card";
import Pagination from "@/app/Search/pagination";
import React from "react";
import { useState } from "react";

type ResultCardProps = {
  data: {
    file: File[];
  };
};

const ResultClient = ({ data }: { data: File[] }) => {
  console.log(data);
  const listPerPage = 6;
  const [currentPage, setCurrentPage] = useState(1); // Current page
  // Calculate the starting and ending indices of list for the current page
  const indexOfLastCard = currentPage * listPerPage;
  const indexOfFirstCard = indexOfLastCard - listPerPage;
  const currentList = data.slice(indexOfFirstCard, indexOfLastCard);
  const numberPage = Math.ceil(data.length / listPerPage);

  return (
    <div className="flex flex-col gap-10 lg:gap-16">
      <div className="grid h-fit gap-7 pt-7 lg:gap-12 items-stretch grid-cols-1 sm:grid-cols-2 xl:grid-cols-3">
        {currentList &&
          currentList.map((item, index) => (
            <ResultCard key={index} file={item} />
          ))}
      </div>
      
      <div className="flex w-full items-center justify-center pb-10 lg:pb-24">
        {/* Display pagination component */}
        <Pagination
          numberPage={numberPage}
          setCurrentNumberPage={setCurrentPage}
          currentNumberPage={currentPage}
          primaryColor="pink"
          nextButton
          previousButton
        />
      </div>
    </div>
  );
};

export default ResultClient;
