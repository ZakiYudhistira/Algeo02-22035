import Image from "next/image";
import React from "react";

type ResultCardProps = {
  file: File;
  // imageAlt?: string;
  // width?: number;
  // height?: number;
  // cosValue: number;
};

const ResultCard: React.FC<ResultCardProps> = ({
  file,
  // imageAlt = "Test",
  // width = 300,
  // height = 300,
  // cosValue,
}) => {
  return (
    <div className="cursor-pointer drop-shadow-xl animate-blink rounded-3xl bg-gradient-to-br from-[#cbcbcb] to-[#979797] p-1 hover:scale-105 transition duration-300 ease-in-out">
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
            src={URL.createObjectURL(file)}
            alt={""}
            className={`rounded-t-3xl w-full h-[250px] object-center object-cover bg-[url('/logo.png')]`}
          ></Image>

          <div className="w-full py-5 flex flex-col items-center gap-3 px-2">
            <div className="px-8 py-3 bg-white rounded-lg text-custom-black text-center font-semibold">
              <p className="text-center font-montserrat text-sm lg:text-lg">
                {/* {cosValue} */}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ResultCard;
