"use client";
import { useState, useRef } from "react";
import React, { Component } from "react";
import Image from "next/image";
import Result from "./result";
import axios from "axios";

import { Button } from "@/components/ui/button";
import { Switch } from "@/components/ui/switch";

const Search = () => {
  const [image, setImage] = useState<File | null>(null);
  const [imagedataset, setImagedataset] = useState<File[]>([]);
  // const [startTime, setStartTime] = useState<number | null>(null);
  // const [result, setResult] = useState<response[] | null>(null);
  // const [result2, setResult2] = useState<File[] | null>(null);
  // const [loading, setLoading] = useState(false);
  const inputRef = useRef<HTMLInputElement>(null);
  const inputRefFolder = useRef<HTMLInputElement>(null);
  console.log(imagedataset);

  const handlePhotoClick = async () => {
    if (inputRef.current) {
      inputRef.current.click();

      const selectedFile = inputRef.current.files && inputRef.current.files[0];

      if (selectedFile) {
        try {
          const formData = new FormData();
          formData.append('image', selectedFile);
  
          const apiUrl = `http://127.0.0.1:5000/api/upload?timestamp=${new Date().getTime()}`;
  
          const response = await axios.post(apiUrl, formData);
  
          console.log(response.data);
        } catch (error) {
          console.error('Error during backend POST request', error);
        }
      }
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

  return (
    <div className="mt-10">
      <h1 className="text-custom-green font-montserrat text-[30px] lg:text-7xl font-bold tracking-[0.54px] text-center mb-12">
        Reverse
        <span className="text-custom-black font-montserrat text-[30px] lg:text-7xl font-bold">
          {" "}
          Image Search
        </span>{" "}
      </h1>
      <div className="flex flex-wrap justify-center gap-10">
        <Image
          // receive image from input
          src={image ? URL.createObjectURL(image) : "/dummy.png"}
          alt="Image Input"
          width={500}
          height={500}
          className="w-[500px] lg:w-fit"
        ></Image>

        <div className="flex flex-col">
          <h2 className="text-custom-green-dark font-montserrat text-[22px] font-extrabold">
            Image Input
          </h2>
          <div className="flex flex-row gap-4 mb-28">
            <input
              type="file"
              className="hidden"
              ref={inputRef}
              onChange={handleImageUpload}
              accept="image/*"
              required
              name="fileupload"
            />
            <Button
              variant="outline"
              className="text-white bg-custom-green-calm font-semibold rounded-xl px-5"
              onClick={handlePhotoClick}
            >
              Upload Image  
            </Button>

            <input
              type="file"
              webkitdirectory=""
              multiple
              className="hidden"
              ref={inputRefFolder}
              onChange={handleFolderUpload}
              required
              accept="image/*"
              name="folderupload"
            />
            <Button
              variant="outline"
              className="text-white bg-custom-black font-semibold rounded-xl px-5"
              onClick={handleFolderClick}
            >
              Upload Dataset
            </Button>
          </div>
          <div className="flex flex-col gap-2">
            <div className="flex items-center justify-center gap-4">
              <span className="font-montserrat text-[21px] font-semibold">
                Color
              </span>
              <Switch className="bg-black" />
              <span className="font-montserrat text-[21px] font-semibold">
                Texture
              </span>
            </div>
            <Button
              variant="outline"
              className="text-white bg-gradient-to-r from-[#DF3890] to-[150%] to-[#FF87C6] font-semibold rounded-xl"
            >
              Search
            </Button>
          </div>
        </div>
      </div>
      <Image
        src="/garis-daun.svg"
        alt="garis daun"
        width={750}
        height={700}
        className="lg:w-[1200px] lg:h-[80px] w-[300px] h-[500px] z-[-1] mt-10 mx-auto"
      ></Image>
      <Result imagedataset={imagedataset} />
    </div>
  );
};

export default Search;
