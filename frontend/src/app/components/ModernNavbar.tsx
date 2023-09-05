"use client";

import React, { ChangeEvent, useState } from "react";
import DropdownMenu from "./DropdownMenu";
import { AiOutlineSearch } from "react-icons/ai";

export default function ModernNavbar() {
  const [isDropdownOpen, setIsDropdownOpen] = useState(true);
  const [search, setSearch] = useState("");

  function handleSearchInput(event: ChangeEvent<HTMLInputElement>) {
    const { name, value } = event.target;
    setSearch(value);
  }

  return (
    <header>
      <div className="min-w-screen px-10 border-b-black border pt-4">
        <nav className="flex align-middle items-center justify-between">
          <a
            href="/"
            className="text-4xl text-black font-semibold cursor-pointer"
          >
            GoTech
          </a>
          <div className="flex md:justify-evenly w-full px-32 md:max-w-[1000px]">
            <DropdownMenu />
            <div className="h-12 flex items-center">
              <a href="" className="text-base text-slate-700 font-medium">
                Discover More
              </a>
            </div>
            <div className="h-12 flex items-center">
              <a href="" className="text-base text-slate-700 font-medium">
                Explore now
              </a>
            </div>
            <div className="h-12 flex items-center">
              <a href="" className="text-base text-slate-700 font-medium">
                Blog
              </a>
            </div>
          </div>
          <div className="flex items-center gap-3 mb-4">
            {/* <div className="flex bg-slate-200 items-center">
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
            </div> */}
            <a
              href=""
              className="bg-black text-white py-2 px-5 font-medium border-slate-900 border active:opacity-60"
            >
              Sign Up
            </a>
            <a
              href="login/"
              className="bg-white text-black py-2 px-5 border-black border font-medium active:opacity-60"
            >
              Login
            </a>
          </div>
        </nav>
      </div>
    </header>
  );
}
