import Pagination from "@/app/Search/pagination";
import React from "react";
import { useState } from "react";
import ResultContain from "@/app/Search/result-contain";

type ResultDataProps = {
  data: { path: string; value: number }[];
};

const ResultData: React.FC<ResultDataProps> = ({ data }) => {
  console.log("Ini data: ", data);
  const listPerPage = 6;
  const [currentPage, setCurrentPage] = useState(1);
  const indexOfLastCard = currentPage * listPerPage;
  const indexOfFirstCard = indexOfLastCard - listPerPage;
  const currentList = data.slice(indexOfFirstCard, indexOfLastCard);
  const numberPage = Math.ceil(data.length / listPerPage);

  return (
    <div className="flex flex-col gap-10 lg:gap-16">
      <div className="grid h-fit gap-7 pt-7 lg:gap-12 items-stretch grid-cols-1 sm:grid-cols-2 xl:grid-cols-3">
        {currentList.map((item, index) => (
          <ResultContain
            key={index}
            file={item.path}
            value={item.value}
          />
        ))}
      </div>

      <div className="flex w-full items-center justify-center pb-10 lg:pb-24">
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

export default ResultData;
