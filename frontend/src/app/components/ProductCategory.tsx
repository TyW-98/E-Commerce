import Image from "next/image";

export default function ProductCategory() {
  return (
    <div className="grid grid-cols-3 mt-44 gap-16">
      <a>
        <div className="relative h-[450px] cursor-pointer">
          <Image
            src={"/console.avif"}
            layout="fill"
            objectFit="cover"
            objectPosition="center"
            alt="console card"
          />
        </div>
      </a>
      <a>
        <div className="bg-gray-400 h-[450px]"></div>
      </a>
      <a>
        <div className="bg-gray-400 h-[450px]"></div>
      </a>
    </div>
  );
}
