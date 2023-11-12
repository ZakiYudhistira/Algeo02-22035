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

interface ResultClientProps {
  data: File[];
  numberPage: number;
  currentNumberPage: number;
  setCurrentNumberPage: (pageNumber: number) => void;
  previousButton: boolean;
  nextButton: boolean;
  primaryColor: string;
}

const ResultClient: React.FC<ResultClientProps> = ({
  data,
  currentNumberPage,
  setCurrentNumberPage,
  previousButton,
  nextButton,
  primaryColor,
}) => {
  console.log(data);
  const listPerPage = 6;
  const [currentPage, setCurrentPage] = useState(1); // Current page
  // Calculate the starting and ending indices of list for the current page
  const indexOfLastCard = currentPage * listPerPage;
  const indexOfFirstCard = indexOfLastCard - listPerPage;
  const currentList = data.slice(indexOfFirstCard, indexOfLastCard);
  const numberPage = Math.ceil(data.length / listPerPage);

   // Define color effects based on the primary color provided
   const colorEffect = {
    pink: { selected: "fill-[#DF3890]", unselected: "fill-[#7A2F8B]" },
  };

  // Create an array of numbers representing the page numbers
  const numbers = Array.from({ length: numberPage }, (_, index) => index + 1);

  // Handle previous page button click
  const handlePreviousClick = () => {
    const newPage = ((currentNumberPage - 2 + numberPage) % numberPage) + 1;
    setCurrentNumberPage(newPage);
  };

  // Handle next page button click
  const handleNextClick = () => {
    const newPage = (currentNumberPage % numberPage) + 1;
    setCurrentNumberPage(newPage);
  };

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
