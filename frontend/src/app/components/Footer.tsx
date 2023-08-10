"use client";
import { useState } from "react";
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

  return (
    <footer className="lg:px-64 mt-44">
      <div className="flex justify-between align-middle items-center">
        <div>
          <h5>Get Exclusive Offers</h5>
          <p>Sign up for our newsletter to receive updates and promotions</p>
        </div>
        <div>
          <div className="flex gap-6">
            <input
              type="text"
              name="email"
              value={email}
              placeholder="Enter your email"
              className="border-2 border-slate-500 border-solid p-4"
            />
            <button className="py-2 px-4 border-2 border-slate-500 border-solid">
              Subscribe
            </button>
          </div>
        </div>
      </div>
      <p className="text-right pr-20 text-sm text-slate-500 ">
        By subscribing, you agree to our Privacy Policy.
      </p>
      <div className="display flex justify-between mt-28 pr-2 items-center">
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
