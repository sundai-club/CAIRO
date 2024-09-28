'use client'

import Link from "next/link"
import { Button } from "l/components/ui/button"
import { BrainCircuit, MessageSquare, Target, Lightbulb } from "lucide-react"

export function CairoLanding() {
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
                  Your Message, Their Attention
                </h1>
                <p className="mx-auto max-w-[700px] text-white md:text-xl">
                  We specialize in crafting compelling marketing messages and providing targeted customer leads to fuel
                  your business growth. Let us help you connect with your ideal audience and optimize your outreach
                  efforts.
                </p>
              </div>
              <div className="w-full max-w-sm space-y-2">
                <Link href="/get-started">
                  <Button className="w-full bg-white text-purple-600 hover:bg-gray-200">
                    Get Started
                  </Button>
                </Link>
                <p className="text-xs text-gray-200">
                  Start your journey to better marketing today. No commitment required.
                </p>
              </div>
            </div>
          </div>
        </section>
        <section id="features" className="w-full py-12 bg-white">
          <div className="container px-4 md:px-6">
            <h2 className="text-2xl font-bold tracking-tighter sm:text-3xl text-center mb-8">Why Choose cAIro?</h2>
            <div className="flex justify-center space-x-8 md:space-x-16">
              <div className="flex flex-col items-center">
                <MessageSquare className="h-8 w-8 text-purple-500 mb-2" />
                <h3 className="text-lg font-semibold">AI-Powered Messaging</h3>
              </div>
              <div className="flex flex-col items-center">
                <Target className="h-8 w-8 text-purple-500 mb-2" />
                <h3 className="text-lg font-semibold">Targeted Lead Generation</h3>
              </div>
              <div className="flex flex-col items-center">
                <Lightbulb className="h-8 w-8 text-purple-500 mb-2" />
                <h3 className="text-lg font-semibold">AI-powered Discovery</h3>
              </div>
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
              <Link className="text-sm hover:underline underline-offset-4" href="#">
                Terms of Service
              </Link>
              <Link className="text-sm hover:underline underline-offset-4" href="#">
                Privacy Policy
              </Link>
            </div>
          </div>
        </div>
      </footer>
    </div>
  )
}