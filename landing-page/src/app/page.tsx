import Link from "next/link";
import { Button } from "./components/button";

import {
  BrainCircuit,
  Rocket,
  BarChart2,
  TrendingUp,
  Clock,
  Brain,
  Zap,
  Search,
} from "lucide-react";

export default function LandingPage() {
  return (
    <div className="flex flex-col min-h-screen bg-gradient-to-br from-purple-500 via-pink-500 to-red-500">
      <header className="px-4 lg:px-6 h-14 flex items-center">
        <Link className="flex items-center justify-center" href="#">
          <BrainCircuit className="h-6 w-6 text-white" />
          <span className="ml-2 text-2xl font-bold text-white">cAIro</span>
        </Link>
      </header>
      <main className="flex-1">
        <section className="w-full py-12 md:py-24 lg:py-32 xl:py-48">
          <div className="container px-4 md:px-6">
            <div className="flex flex-col items-center space-y-4 text-center">
              <div className="space-y-2">
                <h1 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl lg:text-6xl/none text-white">
                  Empower Your Business with cAIro
                </h1>
                <p className="mx-auto max-w-[700px] text-white md:text-xl">
                  Streamline your digital marketing efforts and focus on what
                  you do best.
                </p>
              </div>
              <div className="w-full max-w-sm space-y-2">
                <Link href="#demo">
                  <Button className="w-full bg-white text-purple-600 hover:bg-gray-200">
                    Get Started
                  </Button>
                </Link>
                <p className="text-xs text-gray-200">
                  Start your journey to better marketing today. No commitment
                  required.
                </p>
              </div>
            </div>
          </div>
        </section>

        {/* Key Features Section */}
        <section id="features" className="w-full py-12 bg-white">
          <div className="container px-4 md:px-6">
            <h2 className="text-2xl font-bold tracking-tighter sm:text-3xl text-center mb-8">
              Key Features for Your Success
            </h2>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
              <div className="flex flex-col items-center text-center">
                <Rocket className="h-8 w-8 text-purple-500 mb-2" />
                <h3 className="text-lg font-semibold">Landing Page Setup</h3>
                <p className="mt-2 text-gray-700">
                  Quickly create a professional landing page to attract and
                  convert visitors.
                </p>
              </div>
              <div className="flex flex-col items-center text-center">
                <BarChart2 className="h-8 w-8 text-purple-500 mb-2" />
                <h3 className="text-lg font-semibold">Marketing Materials</h3>
                <p className="mt-2 text-gray-700">
                  Generate and manage high-quality marketing content to engage
                  your audience.
                </p>
              </div>
              <div className="flex flex-col items-center text-center">
                <TrendingUp className="h-8 w-8 text-purple-500 mb-2" />
                <h3 className="text-lg font-semibold">Lead Generation</h3>
                <p className="mt-2 text-gray-700">
                  Automate lead generation to grow your customer base
                  efficiently.
                </p>
              </div>
            </div>
          </div>
        </section>

        {/* Why Choose cAIro Section */}
        <section id="why-choose" className="w-full py-12 bg-gray-50">
          <div className="container px-4 md:px-6">
            <h2 className="text-2xl font-bold tracking-tighter sm:text-3xl text-center mb-8">
              Why Choose cAIro?
            </h2>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
              <div className="flex flex-col items-center text-center">
                <Clock className="h-8 w-8 text-purple-500 mb-2" />
                <h3 className="text-lg font-semibold">Save Time</h3>
                <p className="mt-2 text-gray-700">
                  Spend less time on setup and more time on growing your
                  business.
                </p>
              </div>
              <div className="flex flex-col items-center text-center">
                <Brain className="h-8 w-8 text-purple-500 mb-2" />
                <h3 className="text-lg font-semibold">Expertise</h3>
                <p className="mt-2 text-gray-700">
                  Access professional marketing expertise without the high
                  costs.
                </p>
              </div>
              <div className="flex flex-col items-center text-center">
                <Zap className="h-8 w-8 text-purple-500 mb-2" />
                <h3 className="text-lg font-semibold">Automation</h3>
                <p className="mt-2 text-gray-700">
                  Automate repetitive tasks and streamline your marketing
                  processes.
                </p>
              </div>
              <div className="flex flex-col items-center text-center">
                <Search className="h-8 w-8 text-purple-500 mb-2" />
                <h3 className="text-lg font-semibold">Online Presence</h3>
                <p className="mt-2 text-gray-700">
                  Improve your online presence and reach a wider audience.
                </p>
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
      <footer className="w-full py-6 bg-purple-600 text-white">
        <div className="container px-4 md:px-6">
          <div className="flex flex-col items-center justify-between gap-4 md:flex-row">
            <div className="flex flex-col items-center gap-4 px-8 md:flex-row md:gap-2 md:px-0">
              <BrainCircuit className="h-6 w-6" />
              <p className="text-center text-sm leading-loose md:text-left">
                © 2024 cAIro. All rights reserved.
              </p>
            </div>
            <div className="flex gap-4">
              <Link
                className="text-sm hover:underline underline-offset-4"
                href="#"
              >
                Terms of Service
              </Link>
              <Link
                className="text-sm hover:underline underline-offset-4"
                href="#"
              >
                Privacy Policy
              </Link>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}
