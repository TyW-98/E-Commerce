import BlogCard from "./BlogCard";

export default function Blog() {
  const testBlog = [
    {
      id: 1,
      title: "The Future of Tech: Trends to Watch",
      summary:
        "Discover the exciting trends shaping the tech industry, from artificial intelligence to sustainable innovations.",
      image: "",
      category: "Technology",
    },
    {
      id: 2,
      title: "Unveiling the New Generation Consoles",
      summary:
        "Get a sneak peek into the cutting-edge features and capabilities of the latest gaming consoles hitting the market.",
      image: "",
      category: "Gaming",
    },
  ];

  return (
    <div className="mt-44">
      <div className="text-center">
        <h3 className="text-4xl font-bold">
          Stay Informed with Our Latest News
        </h3>
        <p className="mt-4">
          Get the latest insights and updates from the world of tech and
          e-commerce.
        </p>
      </div>
      <div className="grid grid-cols-2 gap-4 mt-12 px-8">
        {testBlog.map((blog) => {
          return (
            <BlogCard
              key={blog.id}
              title={blog.title}
              summary={blog.summary}
              image={blog.image}
              category={blog.category}
            />
          );
        })}
      </div>
      <div className="flex justify-center">
        <a className="mt-10 border border-black p-3 cursor-pointer active:bg-black active:text-white">
          View All
        </a>
      </div>
    </div>
  );
}
