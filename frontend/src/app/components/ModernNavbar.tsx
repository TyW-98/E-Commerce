"use client";

import React, { useState } from "react";
import DropdownMenu from "./DropdownMenu";
import { AiOutlineSearch } from "react-icons/ai";

export default function ModernNavbar() {
  const [isDropdownOpen, setIsDropdownOpen] = useState(true);
  const [search, setSearch] = useState("");

  function handleSearchInput(event) {
    const { name, value } = event.target;
    setSearch(value);
  }

  return (
    <header>
      <div className="min-w-screen px-10 border-b-black border">
        <nav className="flex align-middle items-center justify-between pt-8 pb-6 ">
          <a
            href=""
            className="text-4xl text-black font-semibold cursor-pointer"
          >
            GoTech
          </a>
          <div className="flex md:justify-evenly w-full px-32 md:max-w-[1000px]">
            <a href="" className="text-base text-slate-700 font-medium">
              Discover More
            </a>
            <a href="" className="text-base text-slate-700 font-medium">
              Explore Now
            </a>
            <a href="" className="text-base text-slate-700 font-medium">
              Shop Online
            </a>
            <p className="text-base text-slate-700 font-medium cursor-pointer">
              Browse Categories{" "}
            </p>
          </div>
          <div className="flex items-center gap-3">
            <div className="flex bg-slate-200 items-center">
              <input
                type="text"
                name="search"
                value={search}
                placeholder="Search"
                className="bg-inherit text-black font-medium p-2 focus:outline-none foucs:border-transparent"
                onChange={handleSearchInput}
              />
              <div>
                <AiOutlineSearch className="text-2xl cursor-pointer font-bold" />
              </div>
            </div>
            <a
              href=""
              className="bg-black text-white py-2 px-5 font-medium border-slate-900 border active:opacity-60"
            >
              Sign Up
            </a>
            <a
              href=""
              className="bg-white text-black py-2 px-5 border-black border font-medium active:opacity-60"
            >
              Login
            </a>
          </div>
        </nav>
      </div>
      {isDropdownOpen ? <DropdownMenu /> : null}
    </header>
  );
}
