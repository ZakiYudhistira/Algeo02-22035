import Image from "next/image";
import React from "react";

type ResultCardProps = {
  file: string;
  value?: number;
};

const ResultContain: React.FC<ResultCardProps> = ({ file, value }) => {
  console.log("Ini path: ", file);
  return (
    <div className="cursor-pointer drop-shadow-xl animate-blink rounded-3xl bg-gradient-to-br from-[#DEF6B6] to-[#AADD56] p-1 hover:scale-105 transition duration-300 ease-in-out">
      <div className="h-full rounded-3xl">
        <div
          style={{
            background:
              "linear-gradient(to bottom right, #DEF6B6 0%, #AADD56 100%)",
          }}
          className="w-full h-full p-3 text-white font-montserrat items-center rounded-3xl bg-gradient-to-br from-[#FFFFFF1A] to-[#FFFFFF40] relative"
        >
          <Image
            priority
            width={300}
            height={300}
            src={file}
            alt=""
            className={`rounded-t-3xl w-full h-[250px] object-center object-cover bg-[url('/logo.png')]`}
          />
          {value !== undefined && (
            <div className="w-full pt-3 flex flex-col items-center gap-3 px-2">
              <p className="text-center text-custom-green-dark font-montserrat text-lg font-bold">
                {value.toFixed(2)}%
              </p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default ResultContain;
