import Image from "next/image";
import Hero from "./components/Hero";
import ProductCategory from "./components/ProductCategory";
import Blog from "./components/Blog";

export default function Home() {
  return (
    <main className="min-h-screen lg:px-64">
      <section id="hero">
        <Hero />
      </section>
      <section id="product-category">
        <ProductCategory />
      </section>
      <section id="blog">
        <Blog />
      </section>
    </main>
  );
}
