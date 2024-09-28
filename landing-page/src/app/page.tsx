import Link from "next/link";
import Image from "next/image"; // Import the Image component from Next.js
import { BrainCircuit, MessageSquare, Target, Lightbulb } from "lucide-react";

export default function LandingPage() {
  return (
    <div className="flex min-h-screen flex-col bg-gradient-to-br from-purple-600 via-pink-500 to-red-500 text-white">
      <header className="flex h-20 items-center bg-opacity-90 px-6 shadow-lg backdrop-blur-md lg:px-12">
        <Link className="flex items-center justify-center" href="#">
          <Image
            src="/CAIRO_logo.webp"
            alt="Cairo Logo"
            width={100}
            height={40}
            className="w-30 h-10 transition duration-300 hover:opacity-80"
          />
          {/* <span className="ml-3 text-4xl font-extrabold tracking-wider">
            C<span className="text-black">AI</span>RO
          </span> */}
        </Link>
      </header>
      <main className="flex-1">
        <section className="md:py-18 xl:py-30 w-full py-10 lg:py-24">
          <div className="container mx-auto px-6 md:px-12">
            <div className="flex flex-col items-center space-y-8 text-center">
              <div className="space-y-6">
                <h1 className="text-4xl font-extrabold leading-tight tracking-tight sm:text-5xl md:text-6xl lg:text-7xl">
                  5 Market Hypotheses in a Minute
                </h1>
                <p className="mx-auto max-w-3xl text-xl leading-relaxed text-white text-opacity-90 md:text-2xl">
                  Craft hypothesis, discover ideal leads, and generate content
                  for optimal navigation towards PMF.
                </p>
              </div>
              <div className="w-full max-w-sm space-y-4">
                <Link href="#demo">
                  <button className="w-full rounded-full bg-white px-8 py-4 text-lg font-semibold text-purple-600 shadow-lg transition-all hover:bg-purple-600 hover:text-white hover:shadow-xl">
                    Get Started
                  </button>
                </Link>
              </div>
            </div>
          </div>
        </section>
        <section id="features" className="w-full bg-white py-20 text-gray-900">
          <div className="container mx-auto px-6 md:px-12">
            <h2 className="mb-16 text-center text-3xl font-bold tracking-tight sm:text-4xl">
              How does C<span className="text-pink-600">AI</span>RO work?
            </h2>
            <div className="grid grid-cols-1 gap-12 sm:grid-cols-2 md:grid-cols-3">
              <div className="flex flex-col items-center">
                <MessageSquare className="mb-6 h-16 w-16 text-purple-500 transition duration-300 hover:text-purple-700" />
                <h3 className="text-center text-xl font-semibold">
                  1. Generate Hypothesis
                </h3>
              </div>
              <div className="flex flex-col items-center">
                <Target className="mb-6 h-16 w-16 text-purple-500 transition duration-300 hover:text-purple-700" />
                <h3 className="text-center text-xl font-semibold">
                  2. Targeted Lead Generation
                </h3>
              </div>
              <div className="flex flex-col items-center">
                <Lightbulb className="mb-6 h-16 w-16 text-purple-500 transition duration-300 hover:text-purple-700" />
                <h3 className="text-center text-xl font-semibold">
                  3. AI Content for Validation
                </h3>
              </div>
            </div>
          </div>
        </section>
        <section id="demo" className="w-full bg-gray-100 py-20">
          <div className="container mx-auto px-6 md:px-12">
            <div className="relative h-0 overflow-hidden pb-[56.25%]">
              <iframe
                src="https://sundai-cairo-199983032721.us-central1.run.app/"
                className="absolute left-0 top-0 h-full w-full border-0"
                allowFullScreen
                title="Cairo Demo"
              ></iframe>
            </div>
          </div>
        </section>
      </main>
      <footer className="w-full bg-purple-700 py-10 text-white">
        <div className="container mx-auto px-6 md:px-12">
          <div className="flex flex-col items-center justify-between gap-8 md:flex-row">
            <div className="flex flex-col items-center gap-4 md:flex-row">
              <Image
                src="/CAIRO_logo.webp"
                alt="Cairo Logo"
                width={32}
                height={32}
                className="h-4 w-12 transition duration-300 hover:opacity-80"
              />
            </div>
            <div className="flex gap-8">
              <Link className="text-sm hover:underline" href="#">
                Terms of Service
              </Link>
              <Link className="text-sm hover:underline" href="#">
                Privacy Policy
              </Link>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}
