import ModernNavbar from "../components/ModernNavbar";

export default function LoginLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <div className="min-h-screen flex flex-col">
      <ModernNavbar />
      <main className="flex flex-grow items-center justify-center">
        {children}
      </main>
    </div>
  );
}
