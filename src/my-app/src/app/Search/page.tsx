"use client";
import React, { Component,useState, useRef } from "react";
import Image from "next/image";
import Result from "./result";
import axios from "axios";

import { Button } from "@/components/ui/button";
import { Switch } from "@/components/ui/switch";

const Search = () => {
  const [image, setImage] = useState<File | null>(null);
  const inputRefImage = useRef<HTMLInputElement>(null);

  // ini nanti taro di input file
  const handleImageChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFile = e.target.files?.[0];
    if (selectedFile) {
      setImage(selectedFile);
    }
  };

  // buat nge click input element karena input elemennya hidden
  const handleImageClick = async () => {
    if (inputRefImage.current) {
      inputRefImage.current.click();
    }

    try {
      const formData = new FormData();
      formData.append('image', image as Blob);

      const response = await axios.post('http://localhost:5000/api/upload', formData);

      console.log('File uploaded successfully');
      console.log('Server response:', response.data);
    } catch (error) {
      console.error('Error uploading file:', error);
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
          src="/dummy.png"
          alt="Image Input"
          width={500}
          height={500}
          className="w-[500px] lg:w-fit -z-[1]"
        ></Image>
        <div className="flex flex-col">
          <h2 className="text-custom-green-dark font-montserrat text-[22px] font-extrabold">
            Image Input
          </h2>
          <div className="flex flex-row gap-4 mb-28">
            <input
              type="file"
              ref = {inputRefImage}
              className="hidden"
              required
              onChange={handleImageChange}
              accept="image/*"
              name="imageupload"
            />
            <Button
              variant="outline"
              className="text-white bg-custom-green-calm font-semibold rounded-xl px-5"
              onClick={handleImageClick}
            >
              Upload Image  
            </Button>
            <Button
              variant="outline"
              className="text-white bg-custom-black font-semibold rounded-xl px-5"
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
      <Result />
    </div>
  );
};

export default Search;
