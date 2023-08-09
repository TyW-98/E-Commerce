import {
  FaInstagram,
  FaTwitter,
  FaFacebook,
  FaShoppingCart,
} from "react-icons/fa";

import { BsCart3 } from "react-icons/bs";

export default function Navbar() {
  return (
    <div className="min-w-screen bg-slate-600 pb-4 lg:px-96 px-0">
      <nav>
        <div className="flex justify-between py-1">
          <div className="flex flex-row items-center align-middle gap-0.5 text-white text-sm lg:gap-1">
            <a className="cursor-pointer hover:text-orange-400 hover:underline">
              Get App
            </a>
            <a className="before:content-['|'] before:mx-3">Follow Us</a>
            <div className="flex gap-2 text-1xl text-white">
              <FaInstagram className="hover:text-orange-400 hover:underline cursor-pointer" />
              <FaTwitter className="hover:text-orange-400 hover:underline cursor-pointer" />
              <FaFacebook className="hover:text-orange-400 hover:underline cursor-pointer" />
            </div>
          </div>
          <div className="flex flex-row items-center align-middle gap-3 text-white text-sm ">
            <p className="hover:text-orange-400 hover:underline cursor-pointer">
              🔔 Notification
            </p>
            <p className="hover:text-orange-400 hover:underline cursor-pointer">
              🆘 Help
            </p>
            <a className="hover:text-orange-400 hover:underline cursor-pointer after:content-['|'] after:ml-2 after:text-white">
              Register
            </a>
            <a className="hover:text-orange-400 hover:underline cursor-pointer">
              Login
            </a>
          </div>
        </div>
        <div className="flex flex-row gap-5 mt-3 items-center">
          <h1 className="text-4xl text-white font-semibold cursor-pointer">
            <a href="">GoTech</a>
          </h1>
          <input
            type="text"
            className="grow rounded-sm p-2 text-base"
            placeholder="Products"
          />
          <div className="relative cursor-pointer">
            <BsCart3 className="text-4xl text-white mr-5" />
            <span className="absolute z-5 -top-2 right-2 bg-blue-500 text-white text-xs py-0.5 px-3 rounded-xl">
              1
            </span>
          </div>
        </div>
      </nav>
    </div>
  );
}
