import Image from "next/image";

export default function ProductCategory() {
  return (
    <div className="grid grid-cols-3 mt-44 gap-16">
      <a>
        <div className="relative h-[450px] cursor-pointer">
          <Image
            src={"/laptop.png"}
            layout="fill"
            objectFit="cover"
            objectPosition="center"
            alt="console card"
          />
        </div>
        <h5 className="text-xl font-bold mt-2">Computer & Laptop</h5>
      </a>
      <a>
        <div className="relative h-[450px] cursor-pointer">
          <Image
            src={"/phone.png"}
            layout="fill"
            objectFit="cover"
            objectPosition="center"
            alt="console card"
          />
        </div>
        <h5 className="text-xl font-bold mt-2">Phone</h5>
      </a>
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
        <h5 className="text-xl font-bold mt-2">Console</h5>
      </a>
    </div>
  );
}
