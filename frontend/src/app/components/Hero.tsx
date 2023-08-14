import Image from "next/image";

export default function Hero() {
  return (
    <div className="grid grid-cols-2 w-full items-center">
      <div>
        <h1 className="text-6xl font-bold">Welcome to Tech Universe</h1>
        <p className="mt-4">Discover the latest tech gadgets and accessories</p>
        <div className="flex gap-4 mt-4">
          <a className="bg-black text-white px-4 py-2 active:opacity-70 cursor-pointer">
            Shop
          </a>
          <a className="bg-white text-black px-4 py-2 active:bg-black active:text-white cursor-pointer border border-black ">
            Learn More
          </a>
        </div>
      </div>
      <div className="grid grid-cols-2 gap-4">
        <div className="col-span-1">
          <div className="h-44 bg-gray-400"></div>
          <div className="h-96 bg-gray-400 mt-4"></div>
          <div className="h-64 bg-gray-400 mt-4"></div>
        </div>
        <div>
          <div className="h-64 bg-gray-400"></div>
          <div className="h-96 bg-gray-400 mt-4"></div>
          <div className="h-44 bg-gray-400 mt-4"></div>
        </div>
      </div>
    </div>
  );
}
