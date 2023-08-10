import Image from "next/image";
import { AiFillStar, AiOutlineStar } from "react-icons/Ai";
type Props = {};

export default function ProductCard({}: Props) {
  const numStar = Array.from({ length: 5 }, (_, index) => index + 1);
  const rating = 4;
  const numRating = 10;

  return (
    <div className="shadow-lg px-2 py-5 rounded-xl flex flex-col items-center ">
      <Image
        src={"/iphone-14.jpg"}
        alt="Product 1"
        width={250}
        height={300}
        className="w-[250px] h-auto"
      />
      <a>
        <h5 className="font-bold mt-2">Apple</h5>
        <h4 className="text-sm">IPhone 14 Pro</h4>
      </a>
      <span className="flex items-center">
        {numStar.map((idx) => {
          return idx <= rating ? (
            <AiFillStar className="text-orange-400" />
          ) : (
            <AiOutlineStar />
          );
        })}
        {numRating}
      </span>
      <div className="relative">
        <p className="absolute top-0 -left-3">$</p>
        <h2 className="relative text-4xl font-semibold">21</h2>
      </div>

      <button className="border border-white rounded-2xl w-full max-w-[250px] bg-orange-300 py-2 my-2 shadow-sm hover:bg-orange-500 active:border active:border-solid active:border-black">
        Add to basket
      </button>
    </div>
  );
}
