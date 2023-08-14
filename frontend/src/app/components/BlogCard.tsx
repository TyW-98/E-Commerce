import React from "react";
import Image from "next/image";

type Props = {
  title: string;
  summary: string;
  image: string;
  category: string;
};

export default function BlogCard({ title, summary, image, category }: Props) {
  return (
    <div className="w-10/12 mx-auto">
      <div className="bg-gray-400 h-[300px]"></div>
      <p className="bg-gray-200 inline-block py-1 px-2 mt-5">{category}</p>
      <div className="mt-4 cursor-pointer active:text-blue-500">
        <h5 className="text-xl font-bold mt-4">{title}</h5>
        <p className="text-sm mt-2">{summary}</p>
        <a className="text-sm mt-3 flex justify-end ">Read more &gt;</a>
      </div>
    </div>
  );
}
