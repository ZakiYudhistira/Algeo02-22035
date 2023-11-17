"use client";
import { useState, useEffect, useRef, useCallback } from "react";
import React from "react";
import Image from "next/image";
import axios from "axios";

import ResultClient from "../../components/result-client";
import ResultData from "../../components/result-data";

import { Button } from "@/components/ui/button";
import { Switch } from "@/components/ui/switch";

const Camera = () => {
  const videoRef = useRef(null);

  const handleCameraAction = async (action: string) => {
    try {
      const apiUrl = `http://127.0.0.1:5000/api/camera`;
      await axios.post(apiUrl, { action });
    } catch (error) {
      console.error(`Error during camera ${action}`, error);
    }
  };

  useEffect(() => {
    const video = videoRef.current as HTMLVideoElement | null;

    if (video) {
      const apiUrl = `http://127.0.0.1:5000/video_feed`;
      video.src = apiUrl;

      return () => {
        video.src = "";
      };
    }

    return () => {};
  }, []);

  return (
    <div className="mt-10">
      <h1 className="text-custom-green font-montserrat text-[30px] lg:text-7xl font-bold tracking-[0.54px] text-center mb-12">
        CBIR
        <span className="text-custom-black font-montserrat text-[30px] lg:text-7xl font-bold">
          {" "}
          Camera
        </span>{" "}
      </h1>
      <div className="flex flex-wrap justify-center gap-10">
        {/* Display camera frames */}
        <video
          ref={videoRef}
          width={400}
          height={400}
          autoPlay
          playsInline
          muted
        ></video>

        <div className="flex flex-col">
          <h2 className="text-custom-green-dark font-montserrat text-[22px] font-extrabold">
            Camera Input
          </h2>
          <div className="flex flex-row gap-4 mb-28">
            <Button
              type="button"
              variant="outline"
              className="text-white bg-custom-green-calm font-semibold rounded-xl px-5"
              onClick={() => handleCameraAction("start")}
            >
              Start
            </Button>
            <Button
              type="button"
              variant="outline"
              className="text-white bg-custom-black font-semibold rounded-xl px-5"
              onClick={() => handleCameraAction("stop")}
            >
              Stop
            </Button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Camera;
