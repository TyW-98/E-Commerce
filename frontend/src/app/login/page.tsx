"use client";
import { useState, ChangeEvent, FormEvent } from "react";
import { FaUser, FaLock } from "react-icons/fa";
import { useRouter } from "next/navigation";
import Cookie from "js-cookie";

type Props = {};

export default function LoginPage({}: Props) {
  const router = useRouter();
  const [isLoading, setIsLoading] = useState(false);
  const [loginDetails, setLoginDetails] = useState({
    username: "",
    password: "",
  });

  const handleLoginInput = (event: ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target;
    setLoginDetails((prevLoginDetails) => {
      return {
        ...prevLoginDetails,
        [name]: value,
      };
    });
  };

  async function handleLogin(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();

    setIsLoading(true);

    try {
      const loginResponse = await fetch(
        `http://127.0.0.1:8000/api/user/token/`,
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(loginDetails),
        }
      );

      if (loginResponse.status === 200) {
        const authData = await loginResponse.json();
        const authToken = authData.token;
        Cookie.set("authToken", authToken, {
          expires: 1,
          path: "/",
          secure: true,
        });
        console.log("Login Successfully");
        router.push("/dashboard");
      } else if (!loginResponse.ok) {
        console.error("Login Error", loginResponse.statusText);
      }
    } catch (error) {
      console.log("Login Error", error);
    } finally {
      setIsLoading(false);
    }
  }

  return (
    <section>
      <div>
        <form
          onSubmit={handleLogin}
          className="lg:w-[400px] lg:h-[500px] bg-orange-50 border border-solid border-black rounded-xl p-12 flex flex-col gap-4 mx-auto items-center"
        >
          <h1 className="text-4xl font-bold lg:mb-8">Login</h1>
          <div className="border-b-2 border-b-slate-700">
            <FaUser className="inline-block" />
            <input
              type="text"
              name="username"
              value={loginDetails.username}
              placeholder="Username"
              onChange={handleLoginInput}
              className="bg-transparent p-3 outline-none"
            />
          </div>
          <div className="border-b-2 border-b-slate-700">
            <FaLock className="inline-block" />
            <input
              type="password"
              name="password"
              value={loginDetails.password}
              placeholder="Password"
              onChange={handleLoginInput}
              className="bg-transparent p-3 outline-none"
            />
          </div>
          <div>
            <a className="text-sm text-gray-500 cursor-pointer active:underline">
              Forgot Password?
            </a>
          </div>
          <button
            type="submit"
            className="bg-orange-400 w-[100px] px-4 py-1 rounded-md active:opacity-80 text-lg my-auto"
          >
            Login
          </button>
          <div className="mt-auto">
            <a className="text-sm active:underline cursor-pointer">
              Create Your Account
            </a>
          </div>
        </form>
      </div>
    </section>
  );
}

// TODO: Link to login API and set auth token using cookies.js
