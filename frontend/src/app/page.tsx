import Image from "next/image";
import ProductCard from "./components/ProductCard";

export default function Home() {
  return (
    <main className="min-h-screen lg:px-64 pt-5">
      <section className="grid sm:grid-cols-3 md:grid-cols-4 px-10 gap-2">
        <ProductCard />
        <ProductCard />
        <ProductCard />
        <ProductCard />
        <ProductCard />
      </section>
    </main>
  );
}
