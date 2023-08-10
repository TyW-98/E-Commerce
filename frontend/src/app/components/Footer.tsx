"use client";
import { useState, ChangeEvent, MouseEvent } from "react";
import {
  FaFacebook,
  FaInstagram,
  FaTwitter,
  FaYoutube,
  FaLinkedin,
} from "react-icons/fa";

export default function Footer() {
  const [email, setEmail] = useState("");
  const socialIcons = [
    "Facebook",
    "Instagram",
    "Twitter",
    "Youtube",
    "Linkedin",
  ];
  const links = [
    "About Us",
    "Services",
    "Products",
    "Contact",
    "Blog",
    "FAQ",
    "Support",
    "Terms",
    "Privacy",
    "Sitemap",
  ];
  const currentYear = new Date().getFullYear();

  function handleEmailInput(event: ChangeEvent<HTMLInputElement>): void {
    const { name, value } = event.target;
    setEmail(value);
  }

  function handleEmailSubmit(event: MouseEvent<HTMLButtonElement>): void {
    event.preventDefault();
  }

  return (
    <footer className="lg:px-64 mt-44">
      <div className="w-max mx-auto text-center">
        <div className="text-center">
          <h5 className="text-5xl/4 font-bold mb-12">
            Get the latest updates here
          </h5>
          <p className="mb-10 text-lg">
            Subscribe to our newsletter for exclusive offers
          </p>
        </div>
        <div>
          <form className="flex gap-4 mb-4">
            <input
              type="email"
              name="email"
              value={email}
              placeholder="Enter your email"
              className="border-2 border-slate-500 border-solid p-4 lg:w-[550px]"
              onChange={handleEmailInput}
            />
            <button className="py-2 px-4 border-2 border-slate-500 border-solid bg-black text-white active:opacity-80">
              Subscribe
            </button>
          </form>
        </div>
        <p className="">By subscribing, you agree to our Privacy Policy.</p>
      </div>
      <div className="display flex justify-between mt-40 pr-2 items-center">
        <div>
          <h5 className="text-2xl font-bold">GoTech</h5>
          <p className="my-5">
            <span>Address:</span> 123 Main St, New York, NY 1001 |{" "}
            <span>Contact:</span> (555) 123-4567 |<span> Email:</span>{" "}
            info@example.com
          </p>
          <div className="flex gap-2">
            {socialIcons.map((icon, index) => {
              const IconComponent = {
                Facebook: FaFacebook,
                Instagram: FaInstagram,
                Twitter: FaTwitter,
                Youtube: FaYoutube,
                Linkedin: FaLinkedin,
              }[icon];
              return <IconComponent key={icon} className="cursor-pointer" />;
            })}
          </div>
        </div>
        <ul className="grid grid-cols-2 grid-rows-5 gap-x-44 gap-y-4">
          {links.map((lk, index) => {
            return (
              <li key={index}>
                <a href="">{lk}</a>
              </li>
            );
          })}
        </ul>
      </div>
      <div className="flex justify-between border-t-2 border-black mt-10 mb-7 py-8">
        <p>© {currentYear} GoTech, All rights reserved</p>
        <div className="flex gap-4 underline">
          <a>Privacy Policy</a>
          <a>Terms of Use</a>
          <a>Cookie Policy</a>
        </div>
      </div>
    </footer>
  );
}
