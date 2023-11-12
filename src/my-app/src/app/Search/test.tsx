"use client";
import Image from "next/image";
import { useState, useRef } from "react";
import placeholder from "../../public/images/placeholder.jpg";
import { toast } from "@/components/ui/use-toast";
import { request } from "http";
import Card from "../card";
interface response {
  similarity: number;
  index: number;
}
const Form = () => {
  const [image, setImage] = useState<File | null>(null);
  const [imagedataset, setImagedataset] = useState<File[] | null>(null);
  const [startTime, setStartTime] = useState<number | null>(null);
  const [result, setResult] = useState<response[] | null>(null);
  const [result2, setResult2] = useState<File[] | null>(null);
  const [loading, setLoading] = useState(false);
  const inputRef = useRef<HTMLInputElement>(null);
  const inputRefFolder = useRef<HTMLInputElement>(null);

  const handlePhotoClick = () => {
    if (inputRef.current) {
      inputRef.current.click();
    }
  };

  const handleFolderClick = () => {
    if (inputRefFolder.current) {
      inputRefFolder.current.click();
    }
  };

  const handleImageUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFile = e.target.files && e.target.files[0];

    if (selectedFile) {
      setImage(selectedFile);
    }
  };

  const handleFolderUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFiles = e.target.files;

    if (selectedFiles) {
      setImagedataset(Array.from(selectedFiles));
    }
  };

  const itemsPerPage = 6;
  const [currentPage, setCurrentPage] = useState(1);
  const indexOfLastItem = currentPage * itemsPerPage;
  const indexOfFirstItem = indexOfLastItem - itemsPerPage;
  const currentImages = result?.slice(indexOfFirstItem, indexOfLastItem);

  const totalPages = Math.ceil((imagedataset?.length || 0) / itemsPerPage);
  const calculatePageRange = () => {
    const totalPageCount = Math.min(5, totalPages);
    const startPage = Math.max(1, currentPage - Math.floor(totalPageCount / 2));
    const endPage = Math.min(startPage + totalPageCount - 1, totalPages);
    return Array.from(
      { length: Math.min(totalPageCount, endPage - startPage + 1) },
      (_, index) => startPage + index
    );
  };

  const handleNextPage = () => {
    setCurrentPage(totalPages);
  };

  const handlePrevPage = () => {
    setCurrentPage(1);
  };

  const onSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);
    try {
      const formData = new FormData();
      formData.append("image", image as Blob);
      if (imagedataset) {
        imagedataset.forEach((file) => {
          formData.append("imagedataset", file);
        });
      }

      const res = await fetch("http://localhost:5000/api/process_image", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();
      console.log(data);
      setLoading(false);
      if (res.ok) {
        setResult(data.result);
      } else {
        console.log("Error");
      }
    } catch (error) {
      console.log("Error 2");
      setLoading(false);
    }
  };

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
    <div
      className="py-10 mt-5  rounded-lg w-[85%] justify-center"
      style={{
        background:
          "radial-gradient(circle, #fecccb, #ffd5c8, #ffe0c9, #ffebcc, #fef6d4);",
        paddingLeft: "20px",
        paddingRight: "20px",
      }}
    >
      <form onSubmit={onSubmit} className="formbg">
        <div className="grid grid-cols-2 gap-4 ">
          <div>
            <label className="block mb-4 sm:text-xl md:text-2xl lg:text-4xl">{` ${
              image ? "Uploaded Image : " : "Upload Your Image!"
            }`}</label>
            <div className="relative object-contain w-[160px] md:w-[240px] lg:w-[320px] xl:w-[480px] h-[90px] md:h-[135px] lg:h-[180px] xl:h-[270px] mb-4">
              <Image
                alt="Uploaded Image"
                src={image ? URL.createObjectURL(image) : placeholder}
                layout="fill"
                objectFit="cover"
              />
            </div>
            <input
              type="file"
              className="hidden"
              ref={inputRef}
              onChange={handleImageUpload}
              accept="image/*"
              required
              name="fileupload"
            />
            <button
              onClick={handlePhotoClick}
              className="border-[2px] border-[#757376] bg-[#FEFBD6] p-2 rounded-full text-[#005B4A] transition-colors duration-200 ease-in-out hover:text-gray-600 hover:shadow-lg"
            >
              {image ? "Change Your Photo ?" : "Upload Photo"}
            </button>
          </div>
          <div>
            <label className="block mb-4 sm:text-xl md:text-2xl lg:text-4xl">{`${
              imagedataset
                ? Dataset : ${imagedataset.length} images 
                : "Upload Your Dataset!"
            }`}</label>
            <div className="relative object-contain w-[160px] md:w-[240px] lg:w-[320px] xl:w-[480px] h-[90px] md:h-[135px] lg:h-[180px] xl:h-[270px] mb-4">
              <Image
                alt="Uploaded Image"
                src={
                  imagedataset
                    ? URL.createObjectURL(imagedataset[0])
                    : placeholder
                }
                layout="fill"
                objectFit="cover"
              />
            </div>
            <input
              type="file"
              webkitdirectory="true"
              multiple
              className="hidden"
              ref={inputRefFolder}
              onChange={handleFolderUpload}
              required
              accept="image/*"
              name="folderupload"
            />
            <button
              onClick={handleFolderClick}
              className="border-[2px] border-[#757376] bg-[#FEFBD6] p-2 rounded-full text-[#005B4A] transition-colors duration-200 ease-in-out hover:text-gray-600 hover:shadow-lg"
            >
              {`${imagedataset ? "Change Your Dataset?" : "Upload Folder"}`}
            </button>
          </div>
        </div>

        {loading ? (
          <div className="mt-4 text-center">
            <div className="animate-pulse">Loading Image Similarity...</div>
            <p className="mt-2 text-gray-500">{getElapsedTime()}</p>
          </div>
        ) : (
          result?
            <div>
              <h1 className="text-xl sm:text-2xl md:text-3xl lg:text-4xl py-10">{`Database Amount : ${imagedataset?.length} images`}</h1>
              <div className="flex flex-wrap justify-center gap-10">
                {result.map((response, index) => (
                  <div
                    key={index} // Using index as key, assuming no name property in the File object
                    className={`relative flex items-center justify-center w-[160px] md:w-[240px] xl:w-[320px] h-[160px] md:h-[240px] xl:h-[320px] mb-4 mt-4" // Add margin-top if index is greater than 2
                  }`}
                  >
                    <Card
                      image={imagedataset![response.index]}
                      similarity={response.similarity}
                    />
                  </div>
                ))}
              </div>
              {/*Pagination Codes*/}

              <div className="flex justify-center mt-4">
                <button
                  type="button"
                  onClick={handlePrevPage}
                  disabled={currentPage === 1}
                  className={`disabled:opacity-70 disabled:cursor-not-allowed mx-2 px-4 py-2 rounded-full border-[2px] border-[#757376] bg-[#FEFBD6] text-[#005B4A] transition-all duration-200 ease-in-out hover:text-gray-600 hover:shadow-lg`}
                >
                  Start
                </button>

                <div className="flex">
                  {calculatePageRange().map((pageNumber) => (
                    <button
                      key={pageNumber}
                      type="button"
                      onClick={() => setCurrentPage(pageNumber)}
                      className={`mx-2 px-4 py-2 rounded-full border-[2px] border-[#757376] ${
                        pageNumber === currentPage
                          ? "bg-[#FEFBD6] text-[#005B4A]"
                          : "bg-white text-[#005B4A]"
                      } transition-all duration-200 ease-in-out hover:text-gray-600 hover:shadow-lg`}
                    >
                      {pageNumber}
                    </button>
                  ))}
                </div>

                <button
                  type="button"
                  onClick={handleNextPage}
                  disabled={currentPage === totalPages}
                  className={`disabled:opacity-70 disabled:cursor-not-allowed mx-2 px-4 py-2 rounded-full border-[2px] border-[#757376] bg-[#FEFBD6] text-[#005B4A] transition-all duration-200 ease-in-out hover:text-gray-600 hover:shadow-lg`}
                >
                  End
                </button>
              </div>
            </div>
          )
        )}
        <button
          type="submit"
          className="mt-4 bg-blue-500 text-white px-4 py-2 rounded-full"
        >
          Search!
        </button>
      </form>
    </div>
  );
};

export default Form;