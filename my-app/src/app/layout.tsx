"use client";
import "./globals.css";
import { Inter, Montserrat } from "next/font/google";
import Navbar from "@/components/ui/navbar";
import Footer from "@/components/ui/footer";

import { useState, useEffect } from "react";
import { usePathname } from "next/navigation";

const inter = Inter({
  subsets: ["latin"],
  display: "swap",
  variable: "--font-inter",
});
const montserrat = Montserrat({
  subsets: ["latin"],
  display: "swap",
  variable: "--font-montserrat",
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
      <body className={inter.className}>
        <Navbar expandNavbar={expandNavbar} setExpandNavbar={setExpandNavbar} />
        {children}
        <Footer />
      </body>
    </html>
  );
}
