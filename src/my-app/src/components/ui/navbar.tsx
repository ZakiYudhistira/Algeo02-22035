"use client";
import Image from "next/image";
import Link from "next/link";
import React, { useState } from "react";
import { usePathname } from "next/navigation";
import { useRef, useEffect } from "react";

const Navbar = ({ expandNavbar, setExpandNavbar }) => {
  const pathname = usePathname();
  const [isHovered, setIsHovered] = useState(false);
  const blackBgRef = useRef(null);

  // Define the path data as an array of objects
  const path = [
    {
      name: "Home",
      url: "/",
    },
    {
      name: "Search",
      url: "/Search",
    },
    {
      name: "Explore",
      url: "/Explore",
    },
  ];

  // Close Navbar when user clicks on black background stuffs
  useEffect(() => {
    function handleClickOutside(event) {
      // If Userclick is in the black background stuff
      if (blackBgRef.current && blackBgRef.current.contains(event.target)) {
        setExpandNavbar(false);
      }
    }
    // Bind the event listener
    document.addEventListener("mousedown", handleClickOutside);
    return () => {
      // Unbind the event listener on clean up
      document.removeEventListener("mousedown", handleClickOutside);
    };
  }, [setExpandNavbar]);

  return (
    <nav className="sticky left-0 right-0 top-0 flex justify-between  z-20  w-full bg-white py-3 px-7 lg:px-10 xl:px-16 2xl:px-24 lg:py-3">
      {/* Logo */}
      <Image
        src="/logo.png"
        alt="Logo Keluarga Cemara"
        width={220}
        height={40}
        className="w-[50px] lg:w-[220px] lg-h-[40px] rounded"
      />

      {/* Container for mapping links */}
      <ul
        className={`fixed right-0 top-0 z-10 flex h-full w-7/12 flex-col gap-5 lg:gap-16 xl:gap-20 2xl:gap-28 bg-custom-blue px-10 sm:px-20 md:px-24 max-lg:py-10 font-montserrat text-base font-semibold duration-300 ease-in-out lg:static lg:h-auto lg:flex-1 lg:justify-center lg:translate-x-0 lg:flex-row lg:items-center lg:border-none lg:bg-transparent xl:text-xl ${
          expandNavbar ? "translate-x-0" : "translate-x-full"
        }`}
      >
        {path.map((item) => {
          return (
            // If the path has no subtitle
            <Link key={item.name} href={item.url}>
              <li
                className={`${
                  pathname.toLowerCase() === item.url.toLowerCase()
                    ? "text-custom-green"
                    : "text-custom-black"
                } hover:text-custom-green`}
              >
                {item.name}
              </li>
            </Link>
          );
        })}
      </ul>
      {/* Black background on mobile behind click detail navbar */}
      {expandNavbar && (
        <div
          ref={blackBgRef}
          className="fixed inset-0 z-0 h-full w-full bg-opacity-40 bg-black lg:hidden"
        />
      )}
    </nav>
  );
};

export default Navbar;
