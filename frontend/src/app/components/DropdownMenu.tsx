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

  const menuItems = [
    {
      title: "Featured",
      links: [
        "Best Sellers",
        "New Arrivals",
        "Top Rated",
        "Deals of the Day",
        "Clearance",
      ],
    },
    {
      title: "Categories",
      links: ["Laptops", "Smartphones", "Tablets", "Accessories", "Gaming"],
    },
    {
      title: "Brands",
      links: ["Apple", "Samsung", "HP", "Microsoft", "Sony"],
    },
    {
      title: "Product Types",
      links: ["Monitors", "Keyboards", "Headphones", "Cameras", "Printers"],
    },
  ];

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
        } absolute left-0 bg-white w-full top-[70px] border-t border-black z-10`}
      >
        <ul className="grid grid-cols-4 text-center">
          {menuItems.map((cat) => {
            return (
              <li key={cat.title}>
                <ul className="flex flex-col gap-3 my-3">
                  <li className="text-xl font-bold underline">{cat.title}</li>
                  {cat.links.map((item, index) => {
                    return (
                      <li
                        key={index}
                        className="cursor-pointer hover:underline active:underline active:to-blue-600"
                      >
                        <a>{item}</a>
                      </li>
                    );
                  })}
                </ul>
              </li>
            );
          })}
        </ul>
      </div>
    </div>
  );
}
