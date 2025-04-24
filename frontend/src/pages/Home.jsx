// Home.jsx
import React, { useRef, useEffect } from "react";
import { Link } from "react-router-dom";
import AOS from "aos";
import "aos/dist/aos.css";

export default function Home() {
  const featuresRef = useRef(null);

  useEffect(() => {
    AOS.init({ duration: 1000 });
  }, []);

  const handleScrollDown = () => {
    if (featuresRef.current) {
      featuresRef.current.scrollIntoView({ behavior: "smooth" });
    }
  };

  return (
    <main className="overflow-x-hidden font-sans bg-gray-900 text-white">
      {/* Hero Section */}
      <section className="relative min-h-screen flex flex-col justify-center items-center text-center px-4 bg-gradient-to-br from-blue-800 via-purple-800 to-indigo-900">
        <div className="absolute inset-0 z-0">
          <div className="absolute top-[-15%] left-[-25%] w-[40rem] h-[40rem] rounded-full bg-blue-700 opacity-20 blur-3xl animate-pulse" />
          <div className="absolute bottom-[-15%] right-[-10%] w-[60rem] h-[60rem] rounded-full bg-purple-700 opacity-20 blur-2xl animate-pulse" />
        </div>

        <div className="relative z-10 max-w-4xl mx-auto">
          <h1 className="text-5xl md:text-6xl font-extrabold tracking-tight mb-6 drop-shadow-lg">
            UniScheduL
          </h1>
          <p className="text-xl md:text-2xl text-gray-300 font-light mb-8">
            A futuristic platform for academic scheduling & research synergy.
          </p>

          <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
            <Link
              to="/login"
              className="px-6 py-3 bg-gradient-to-r from-blue-600 to-indigo-600 text-white rounded-full shadow-xl hover:from-blue-700 hover:to-indigo-700 transition-all"
            >
              Get Started
            </Link>
            <button
              onClick={handleScrollDown}
              className="px-6 py-3 border border-white text-white rounded-full hover:bg-white hover:text-indigo-700 transition-all"
            >
              Learn More
            </button>
          </div>
        </div>

        <div
          onClick={handleScrollDown}
          className="absolute bottom-8 left-1/2 transform -translate-x-1/2 cursor-pointer group"
        >
          <div className="w-10 h-10 flex items-center justify-center border-2 border-white rounded-full text-white hover:bg-white hover:text-blue-800 transition">
            <svg
              className="w-5 h-5 animate-bounce group-hover:animate-none"
              fill="none"
              stroke="currentColor"
              strokeWidth="2"
              viewBox="0 0 24 24"
            >
              <path d="M12 5v14m0 0l-5-5m5 5l5-5" />
            </svg>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section
        id="learn-more"
        ref={featuresRef}
        className="bg-gray-100 text-gray-800 py-20 px-6"
      >
        <div className="text-center mb-16" data-aos="fade-up">
          <h2 className="text-4xl font-bold mb-4">Why UniScheduL?</h2>
          <p className="max-w-2xl mx-auto text-lg text-gray-600">
            A powerful academic infrastructure—designed for students, professors,
            and institutions.
          </p>
        </div>

        <div className="grid md:grid-cols-3 gap-10 max-w-6xl mx-auto">
          {[
            {
              title: "Sleek Timetabling",
              icon: (
                <path d="M3 7h18M3 12h18M3 17h18" />
              ),
              desc: "Drag-and-drop interface with real-time conflict checks.",
            },
            {
              title: "Smart Conflict Resolution",
              icon: (
                <path d="M5 13l4 4L19 7" />
              ),
              desc: "Detects and resolves schedule overlaps instantly.",
            },
            {
              title: "Collaborative Research",
              icon: (
                <path d="M8 12l6-6m0 0l6 6m-6-6v12" />
              ),
              desc: "Project dashboards and research-sharing workflows.",
            },
          ].map((item, idx) => (
            <div
              key={idx}
              className="bg-white rounded-xl shadow-lg p-6 hover:shadow-2xl transition-all duration-300"
              data-aos="zoom-in"
              data-aos-delay={idx * 200}
            >
              <div className="mb-4 text-indigo-600 flex justify-center">
                <svg
                  className="w-12 h-12"
                  fill="none"
                  stroke="currentColor"
                  strokeWidth="2"
                  viewBox="0 0 24 24"
                >
                  {item.icon}
                </svg>
              </div>
              <h3 className="text-xl font-semibold mb-2">{item.title}</h3>
              <p className="text-gray-600 text-sm">{item.desc}</p>
            </div>
          ))}
        </div>
      </section>

      {/* Call to Action */}
      <section className="bg-gradient-to-r from-indigo-800 to-purple-800 py-16 text-center text-white px-4">
        <h2 className="text-3xl font-bold mb-4">Ready to Transform Your Campus?</h2>
        <p className="max-w-xl mx-auto mb-8 text-gray-300">
          Sign up and bring futuristic efficiency to your scheduling and collaboration.
        </p>
        <Link
          to="/login"
          className="px-6 py-3 bg-white text-indigo-800 font-semibold rounded-full hover:bg-gray-100 transition"
        >
          Join Now
        </Link>
      </section>

      {/* Footer */}
      <footer className="bg-gray-950 text-gray-400 py-8 px-6">
        <div className="max-w-6xl mx-auto flex flex-col md:flex-row justify-between items-center">
          <div>
            <h4 className="text-white text-xl font-bold">UniScheduL</h4>
            <p className="text-sm">© {new Date().getFullYear()} All rights reserved.</p>
          </div>
          <div className="flex gap-4 text-sm mt-4 md:mt-0">
            <a href="#learn-more" className="hover:text-white">Features</a>
            <a
              href="https://github.com/edeniyanda"
              target="_blank"
              rel="noreferrer"
              className="hover:text-white"
            >
              GitHub
            </a>
          </div>
        </div>
      </footer>
    </main>
  );
}
