"use client";
import { useState, useEffect, useRef, useCallback } from "react";
import React, { Component } from "react";
import Image from "next/image";
import axios from "axios";

import ResultClient from "../../components/result-client";
import ResultData from "../../components/result-data";

import { Button } from "@/components/ui/button";
import { Switch } from "@/components/ui/switch";
import UrlForm from "@/components/url-form";

const LoadingDots: React.FC = () => {
  const [dots, setDots] = useState("");

  useEffect(() => {
    const intervalId = setInterval(() => {
      setDots((prevDots) => (prevDots.length >= 5 ? "" : prevDots + "."));
    }, 500);

    return () => clearInterval(intervalId);
  }, []);

  return <span>loading{dots}</span>;
};

const Search = () => {
  const [image, setImage] = useState<File | null>(null);
  const inputRef = useRef<HTMLInputElement>(null);
  const [imagedataset, setImagedataset] = useState<File[]>([]);
  const inputRefFolder = useRef<HTMLInputElement>(null);
  const [isChecked, setChecked] = useState(false);
  const [deltaTime, setDeltaTime] = useState<number | null>(null);
  const [result, setResult] = useState<{ path: string; value: number }[]>([]);
  const [loading, setLoading] = useState(false); // Set initial loading to false
  const [displayedLength, setDisplayedLength] = useState<number>(0);
  console.log("Result: ", result);

  const submitPhoto = useCallback(
    async (e: React.FormEvent<HTMLFormElement>) => {
      e.preventDefault();
      try {
        const formData = new FormData();
        if (image) {
          formData.append("image", image);

          const apiUrl = `http://127.0.0.1:5000/api/upload`;
          const response = await axios.post(apiUrl, formData);

          console.log("Data: ", response.data.result);
          setResult(response.data.result);
        } else {
          console.error("No image selected");
        }
      } catch (error) {
        console.error("Error during backend POST request", error);
      }
    },
    [image]
  );

  const handleImageUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFile = e.target.files && e.target.files[0];

    if (selectedFile) {
      setImage(selectedFile);
    }
  };

  const handlePhotoClick = () => {
    if (inputRef.current) {
      inputRef.current.click();
    }
  };

  const handleFolderUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFiles = e.target.files;

    if (selectedFiles) {
      setImagedataset(Array.from(selectedFiles).map((file) => file));
    }
  };

  const handleFolderClick = async () => {
    if (inputRefFolder.current) {
      inputRefFolder.current.click();
    }
  };

  const submitDataset = useCallback(
    async (e: React.FormEvent<HTMLFormElement>) => {
      e.preventDefault();
      try {
        const formData = new FormData();
        imagedataset.forEach((item) => {
          formData.append("dataset", item);
        });

        const apiUrl = `http://127.0.0.1:5000/api/upload`;
        const response = await axios.post(apiUrl, formData);

        console.log(response.data);

        // Assuming the response contains the cosValues for each file in the dataset
        // setImagedataset( );
      } catch (error) {
        console.error("Error during backend POST request", error);
      }
    },
    [imagedataset]
  );

  // useEffect for image upload
useEffect(() => {
  const submitImageRequest = async () => {
    try {
      const formDataPhoto = new FormData();
      if (image) {
        const apiUrl = `http://127.0.0.1:5000/api/upload`;
        formDataPhoto.append("image", image);
        const responsePhoto = await axios.post(apiUrl, formDataPhoto);
        console.log("Data Photo: ", responsePhoto.data.result);
        setResult(responsePhoto.data.result);
      }
    } catch (error) {
      console.error("Error during backend POST request for image", error);
    }
  };

  submitImageRequest();
}, [image]);

// useEffect for dataset upload
useEffect(() => {
  const submitDatasetRequest = async () => {
    try {
      const formDataDataset = new FormData();
      imagedataset.forEach((item) => {
        formDataDataset.append("dataset", item);
      });
      const apiUrl = `http://127.0.0.1:5000/api/upload`;
      const responseDataset = await axios.post(apiUrl, formDataDataset);
      console.log("Data Dataset: ", responseDataset.data);

      // Assuming the response contains the cosValues for each file in the dataset
      // setImagedataset( );
    } catch (error) {
      console.error("Error during backend POST request for dataset", error);
    }
  };

  if (imagedataset.length > 0) {
    submitDatasetRequest();
  }
}, [imagedataset]);

  

  const handleSwitchChange = () => {
    setChecked(!isChecked);
  };

  const handleSearch = async () => {
    setLoading(true); // Set loading to true when search starts
    const valueToSend = isChecked ? "texture" : "color";
    try {
      const apiUrl = `http://127.0.0.1:5000/api/cbir`;
      const response = await axios.post(apiUrl, { option: valueToSend });
      console.log(response.data);
      setResult(response.data.result);

      // Update delta time based on the response
      setDeltaTime(response.data.delta_time);

      // Update displayed length
      setDisplayedLength(response.data.result.length);
    } catch (error) {
      console.error("Error fetching data:", error);
    } finally {
      setLoading(false); // Set loading to false when search is complete
    }
  };

  const handleDownload = async () => {
    try {
        const apiUrl = 'http://127.0.0.1:5000/api/download';
        const response = await axios.post(apiUrl, {});

        // Create a Blob from the response data
        const blob = new Blob([response.data], { type: 'application/pdf' });

        // Create a link element and trigger a download
        const link = document.createElement('a');
        link.href = window.URL.createObjectURL(blob);
        link.download = 'results.pdf';
        link.click();
    } catch (error) {
        console.error('Error during download:', error);
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
          width={700}
          height={350}
          className="w-[500px]"
        ></Image>

        <div className="flex flex-col justify-between">
          <h2 className="text-custom-green-dark font-montserrat text-[22px] font-extrabold">
            Image Input
          </h2>
          <div className="flex flex-row gap-4 mb-10">
            {/* Form to post an uploaded image */}
            <form onSubmit={submitPhoto}>
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
                type="submit"
                variant="outline"
                className="text-white bg-custom-green-calm font-semibold rounded-xl px-5"
                onClick={handlePhotoClick}
              >
                Upload Image
              </Button>
            </form>
            <form onSubmit={submitDataset}>
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
                type="submit"
                variant="outline"
                className="text-white bg-custom-black font-semibold rounded-xl px-5"
                onClick={handleFolderClick}
              >
                Upload Dataset
              </Button>
            </form>
          </div>

          {/* INPUT FORM */}
          <UrlForm />

          {/* SWITCH COLOR-TEXTURE */}
          <div className="flex flex-col gap-2 mt-10">
            <div className="flex items-center justify-center gap-4">
              <span className="font-montserrat text-[21px] font-semibold">
                Color
              </span>
              <Switch
                className="bg-black"
                checked={isChecked}
                onCheckedChange={handleSwitchChange}
              />
              <span className="font-montserrat text-[21px] font-semibold">
                Texture
              </span>
            </div>

            <Button
              type="submit"
              variant="outline"
              className="text-white bg-gradient-to-r from-[#DF3890] to-[150%] to-[#FF87C6] font-semibold rounded-xl"
              onClick={handleSearch}
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
        className="lg:w-[1425px] lg:h-[100px] z-[-1] mt-10 mx-auto"
      ></Image>

      <div className="px-8 sm:px-10 md:px-14 relative z-10 lg:px-20 xl:px-32 2xl:px-36 bg-custom-blue min-h-screen overflow-hidden">
        <div className="flex flex-row items-center justify-between">
          {result && result.length > 0 ? (
            <div className="flex items-center justify-between gap-10">
              <h1 className="font-montserrat lg:my-8 z-20 text-[28px] lg:text-4xl text-custom-green-dark font-bold scale-x-105">
                Search Results
              </h1>
              <Button
                type="button"
                variant="outline"
                className="text-white bg-custom-green-calm font-semibold rounded-xl px-5"
                onClick={handleDownload}
              >
                Download Results
              </Button>
            </div>
          ) : (
            <h1 className="font-montserrat lg:my-8 z-20 text-[28px] lg:text-4xl text-custom-green-dark font-bold scale-x-105">
              Search Results
            </h1>
          )}

          <p className="text-right text-black text-base font-outline">
            {result?.length} results in{" "}
            {loading ? (
              <LoadingDots />
            ) : deltaTime !== null ? (
              `${deltaTime.toFixed(2)} seconds`
            ) : (
              "loading....."
            )}
          </p>
        </div>
        {result && result.length > 0 ? (
          <ResultData data={result} />
        ) : (
          <ResultClient data={imagedataset} />
        )}
      </div>
    </div>
  );
};

export default Search;
