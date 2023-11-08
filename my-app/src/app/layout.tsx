"use client";
import "./globals.css";
import { Outfit, Raleway } from "next/font/google";
import Navbar from "@/components/ui/navbar";
import Footer from "@/components/ui/footer";

import { useState, useEffect } from "react";
import { usePathname } from "next/navigation";

const outfit = Outfit({
  subsets: ["latin"],
  display: "swap",
  variable: "--font-outfit",
});
const raleway = Raleway({
  subsets: ["latin"],
  display: "swap",
  variable: "--font-raleway",
});

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const [expandNavbar, setExpandNavbar] = useState(false);

  // Reset navbar everytime path changes
  const pathname = usePathname();
  useEffect(() => {
    setExpandNavbar(false);
  }, [pathname]);

  return (
    <html lang="en">
      <body className={raleway.className}>
        <Navbar expandNavbar={expandNavbar} setExpandNavbar={setExpandNavbar} />
        {children}
        <Footer />
      </body>
    </html>
  );
}
