import Image from "next/image";
import Hero from "./components/Hero";

export default function Home() {
  return (
    <main className="min-h-screen lg:px-64">
      <section className="">
        <Hero />
      </section>
    </main>
  );
}
