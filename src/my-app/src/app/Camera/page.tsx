"use client";
import { useRef, useState, useCallback, useEffect } from "react";
import Webcam from "react-webcam";
import Image from "next/image";
import axios from "axios";

import { Button } from "@/components/ui/button";
import { Switch } from "@/components/ui/switch";

import ResultClient from "../../components/result-client";
import ResultData from "../../components/result-data";
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

const videoConstraints = {
  width: 720,
  height: 360,
  facingMode: "user",
};

const dataURLtoFile = (dataurl, filename) => {
  const arr = dataurl.split(",");
  const mime = arr[0].match(/:(.*?);/)[1];
  const bstr = atob(arr[1]);
  let n = bstr.length;
  const u8arr = new Uint8Array(n);
  while (n--) {
    u8arr[n] = bstr.charCodeAt(n);
  }
  return new File([u8arr], filename, { type: mime });
};

const handleDownload = async () => {
  try {
    const apiUrl = "http://127.0.0.1:5000/api/download";
    const response = await axios.post(apiUrl, {});

    // Create a Blob from the response data
    const blob = new Blob([response.data], { type: "application/pdf" });

    // Create a link element and trigger a download
    const link = document.createElement("a");
    link.href = window.URL.createObjectURL(blob);
    link.download = "results.pdf";
    link.click();
  } catch (error) {
    console.error("Error during download:", error);
  }
};

const Camera = () => {
  const [isCaptureEnable, setCaptureEnable] = useState<boolean>(false);
  const [autoCapture, setAutoCapture] = useState<boolean>(false);
  const webcamRef = useRef<Webcam>(null);
  const [url, setUrl] = useState<string | null>(null);

  const [imagedataset, setImagedataset] = useState<File[]>([]);
  const inputRefFolder = useRef<HTMLInputElement>(null);

  const [deltaTime, setDeltaTime] = useState<number | null>(null);
  const [result, setResult] = useState<{ path: string; value: number }[]>([]);
  const [loading, setLoading] = useState(false);

  const [isChecked, setChecked] = useState(false);

  const handleSwitchChange = () => {
    setChecked(!isChecked);
  };

  const handleFolderClick = async () => {
    if (inputRefFolder.current) {
      inputRefFolder.current.click();
    }
  };

  const handleFolderUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFiles = e.target.files;

    if (selectedFiles) {
      setImagedataset(Array.from(selectedFiles).map((file) => file));
    }
  };

  const submitDataset = async (e: React.FormEvent<HTMLFormElement>) => {
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
  };

  const captureAndSend = useCallback(async () => {
    const imageSrc = webcamRef.current?.getScreenshot();
    if (imageSrc) {
      setUrl(imageSrc);

      // Send the captured image to the local folder
      try {
        const formData = new FormData();
        formData.append("image", dataURLtoFile(imageSrc, "captured.jpg"));

        const apiUrl = `http://127.0.0.1:5000/api/upload`; // Update the API endpoint
        const response = await axios.post(apiUrl, formData);

        console.log(response.data);
      } catch (error) {
        console.error("Error during backend POST request", error);
      }
    }
  }, [webcamRef]);

  const handleStop = async () => {
    setCaptureEnable(false);
    setAutoCapture(false);
  };

  useEffect(() => {
    let intervalId: NodeJS.Timeout;

    const captureAndSend = async () => {
      const imageSrc = webcamRef.current?.getScreenshot();
      if (imageSrc) {
        setUrl(imageSrc);

        // Send the captured image to the local folder
        try {
          const formData = new FormData();
          formData.append("image", dataURLtoFile(imageSrc, "captured.jpg"));

          const apiUrl = `http://127.0.0.1:5000/api/upload`; // Update the API endpoint
          const response = await axios.post(apiUrl, formData);

          console.log(response.data);

          // Call CBIR endpoint for automatic processing
          const cbirApiUrl = `http://127.0.0.1:5000/api/cbir`;
          const cbirResponse = await axios.post(cbirApiUrl, {
            option: isChecked ? "texture" : "color",
          });

          // Update the results and delta time
          setResult(cbirResponse.data.result);
          setDeltaTime(cbirResponse.data.delta_time);
        } catch (error) {
          console.error("Error during backend POST request", error);
        }
      }
    };

    if (isCaptureEnable && autoCapture) {
      // Capture and send an image every 10 seconds
      intervalId = setInterval(() => {
        captureAndSend();
      }, 15000);
    }

    if (imagedataset.length > 0) {
      // Assuming you want to submit the dataset when it is uploaded
      const syntheticEventDataset = new Event("submit", {
        bubbles: true,
        cancelable: true,
      });
      submitDataset(syntheticEventDataset);
    }

    // Cleanup function
    return () => {
      clearInterval(intervalId);
    };
  }, [
    isCaptureEnable,
    autoCapture,
    imagedataset.length,
    submitDataset,
    captureAndSend,
    isChecked,
  ]);

  return (
    <div className="min-h-screen px-24 pt-8 pb-24">
      <h1 className="text-custom-green font-montserrat text-[30px] lg:text-7xl font-bold tracking-[0.54px] text-center mb-12">
        CBIR
        <span className="text-custom-black font-montserrat text-[30px] lg:text-7xl font-bold">
          {" "}
          Camera
        </span>{" "}
      </h1>

      {/* Camera input + Dataset input */}
      <div className="flex flex-col items-center justify-between gap-5">
        <div className="flex gap-5">
          <div>
            {isCaptureEnable && (
              <Webcam
                audio={false}
                width={540}
                height={360}
                ref={webcamRef}
                screenshotFormat="image/jpeg"
                videoConstraints={videoConstraints}
              />
            )}
          </div>
          <div>
            {url && (
              <div>
                <img src={url} alt="Screenshot" />
              </div>
            )}
          </div>
        </div>

        <div className="flex flex-row items-center justify-between gap-5">
          {/* Start button */}
          {isCaptureEnable || (
            <Button
              className="text-white text-lg bg-custom-green-calm font-semibold rounded-xl px-10 py-5"
              onClick={() => {
                setCaptureEnable(true);
                setAutoCapture(true);
              }}
            >
              Start
            </Button>
          )}

          {/* Stop button | Replace start button pas diklik*/}
          {isCaptureEnable && (
            <div className="flex gap-5">
              <Button
                className="text-white text-xl bg-custom-green-calm font-semibold rounded-xl px-10 py-5"
                onClick={handleStop}
              >
                Stop
              </Button>
            </div>
          )}

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
              className="text-white text-lg bg-custom-black font-semibold rounded-xl px-10 py-5"
              onClick={handleFolderClick}
            >
              Upload Dataset
            </Button>
          </form>

          {url && (
            <div className="flex gap-5">
              <Button
                className="text-white text-lg bg-custom-green-calm font-semibold rounded-xl px-10 py-5"
                onClick={() => {
                  setUrl(null);
                }}
              >
                Delete
              </Button>
            </div>
          )}
        </div>
      </div>

      {/* Color-Texture Switch*/}
      <div className="flex items-center justify-center py-8 gap-4">
        <span className="font-montserrat text-[21px] font-semibold">Color</span>
        <Switch
          className="bg-black"
          checked={isChecked}
          onCheckedChange={handleSwitchChange}
        />
        <span className="font-montserrat text-[21px] font-semibold">
          Texture
        </span>
      </div>

      <UrlForm />

      {/* Batas suci buat retrieve Dataset terus langsung jebret */}
      <Image
        src="/garis-daun.svg"
        alt="garis daun"
        width={750}
        height={700}
        className="lg:w-[1425px] lg:h-[100px] z-[-1] mt-10 mx-auto"
      ></Image>

      <div className="px-8 sm:px-8 md:px-12 relative z-10 lg:px-12 xl:px-12 2xl:px-12 bg-custom-blue min-h-screen overflow-hidden">
        <div className="flex flex-row items-center justify-between">
          {result && result.length > 0 ? (
            <div className="flex items-center justify-between gap-10">
              <h1 className="font-montserrat lg:my-8 z-20 text-[28px] lg:text-4xl text-custom-green-dark font-bold scale-x-105">
                Search Results
              </h1>
              <Button
                type="submit"
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

export default Camera;
