"use client";

import React, { useState } from "react";

export default function DropdownMenu() {
  const [isOpen, setIsOpen] = useState(false);

  const openDropdown = () => {
    setIsOpen(true);
  };

  const leaveDropdown = () => {
    setIsOpen(false);
  };

  return (
    <div
      className="flex h-12 w-[65px] items-center "
      onMouseEnter={openDropdown}
      onMouseLeave={leaveDropdown}
    >
      <a href="">Browse</a>
      <div
        className={`${
          isOpen ? "inline-block" : "hidden"
        } absolute left-0 bg-orange-300 w-full top-[70px] border-t border-black`}
      >
        <ul>
          <li>1</li>
          <li>1</li>
          <li>1</li>
          <li>1</li>
        </ul>
      </div>
    </div>
  );
}
