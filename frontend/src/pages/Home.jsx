import React, { useRef } from "react";
import { Link } from "react-router-dom";
import { motion } from "framer-motion";

export default function Home() {
  const featuresRef = useRef(null);

  const handleScrollDown = () => {
    if (featuresRef.current) {
      featuresRef.current.scrollIntoView({ behavior: "smooth" });
    }
  };

  return (
    <main className="overflow-x-hidden font-sans bg-white text-gray-800 scroll-smooth">
      {/* HERO SECTION */}
      <section className="relative min-h-screen flex flex-col justify-center items-center text-center px-4 bg-gradient-to-br from-blue-800 via-indigo-900 to-black">
        <div className="absolute inset-0 bg-opacity-30 backdrop-blur-lg z-0" />
        <motion.div
          initial={{ opacity: 0, y: 60 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          className="z-10 relative max-w-5xl mx-auto text-white"
        >
          <h1 className="text-5xl md:text-6xl font-extrabold tracking-tight drop-shadow-2xl">
            Smart Scheduling Starts Here.
          </h1>
          <p className="mt-6 text-lg md:text-xl font-light max-w-2xl mx-auto text-gray-200">
            UniScheduL is an intelligent, conflict-free scheduling platform designed to streamline university timetables and business operations alike.
          </p>

          <div className="mt-10 flex flex-col sm:flex-row gap-4 justify-center">
            <Link to="/login" className="bg-white text-blue-700 font-semibold px-8 py-3 rounded-full hover:scale-105 hover:bg-blue-100 transition-transform duration-300">
              Get Started
            </Link>
            <button onClick={handleScrollDown} className="border border-white text-white px-8 py-3 rounded-full hover:bg-white hover:text-blue-700 transition-transform duration-300 hover:scale-105">
              See How It Works
            </button>
          </div>

          <motion.div
            onClick={handleScrollDown}
            className="mt-16 flex justify-center animate-bounce cursor-pointer"
            whileHover={{ scale: 1.2 }}
          >
            <div className="w-12 h-12 flex items-center justify-center rounded-full border-2 border-white">
              <svg className="w-6 h-6 text-white" fill="none" stroke="currentColor" strokeWidth="2" viewBox="0 0 24 24">
                <path d="M12 5v14m0 0l-5-5m5 5l5-5" />
              </svg>
            </div>
          </motion.div>
        </motion.div>
      </section>

      {/* WHY UNISCHEDUL */}
      <section ref={featuresRef} id="learn-more" className="py-20 bg-white text-center px-6">
        <motion.div initial={{ opacity: 0 }} whileInView={{ opacity: 1 }} transition={{ duration: 1 }}>
          <h2 className="text-4xl font-bold mb-4">Why UniScheduL?</h2>
          <p className="max-w-2xl mx-auto text-gray-600 mb-12">
            Built with precision and purpose to automate every scheduling scenario imaginable.
          </p>

          <div className="grid md:grid-cols-3 gap-8 max-w-6xl mx-auto">
            {[
              {
                title: "Automated Timetabling",
                desc: "Generate conflict-free schedules with AI-assisted logic and zero manual adjustments.",
                icon: "M3 7h18M3 12h18M3 17h18",
              },
              {
                title: "Real-Time Conflict Detection",
                desc: "Get instant alerts and resolve schedule clashes with one-click optimization.",
                icon: "M5 13l4 4L19 7",
              },
              {
                title: "Flexible Use Cases",
                desc: "From lecture halls to coworking spaces, UniScheduL adapts to your ecosystem.",
                icon: "M8 12l6-6m0 0l6 6m-6-6v12",
              },
            ].map(({ title, desc, icon }, i) => (
              <motion.div
                key={i}
                className="p-6 bg-white border rounded-xl shadow-md hover:shadow-2xl transition-all duration-300"
                whileHover={{ scale: 1.03 }}
              >
                <div className="text-blue-600 mb-4">
                  <svg className="w-10 h-10 mx-auto" fill="none" stroke="currentColor" strokeWidth="2" viewBox="0 0 24 24">
                    <path d={icon} />
                  </svg>
                </div>
                <h3 className="text-xl font-semibold mb-2">{title}</h3>
                <p className="text-sm text-gray-600">{desc}</p>
              </motion.div>
            ))}
          </div>
        </motion.div>
      </section>

      {/* BEYOND ACADEMIA */}
      <section className="bg-gradient-to-t from-gray-100 to-white py-20 text-center">
        <motion.div initial={{ opacity: 0 }} whileInView={{ opacity: 1 }} transition={{ duration: 0.8 }}>
          <h2 className="text-3xl font-bold mb-4">Beyond Academia</h2>
          <p className="text-gray-600 max-w-xl mx-auto mb-10">
            UniScheduL powers more than campuses — it’s built for business, logistics, and global workflows.
          </p>
          <div className="flex flex-wrap justify-center gap-6 text-sm font-medium text-gray-700">
            {["📅 Event Scheduling", "🏢 Workspace Management", "🚚 Logistics Planning"].map((tag, i) => (
              <motion.div
                key={i}
                className="bg-white px-6 py-4 rounded-full shadow hover:shadow-lg transition duration-300"
                whileHover={{ scale: 1.05 }}
              >
                {tag}
              </motion.div>
            ))}
          </div>
        </motion.div>
      </section>

      {/* IMPACT METRICS */}
      <section className="bg-white py-20 text-center px-6">
        <motion.div initial={{ opacity: 0 }} whileInView={{ opacity: 1 }} transition={{ duration: 0.8 }}>
          <h2 className="text-3xl font-bold text-blue-700 mb-6">A Measurable Difference</h2>
          <p className="text-gray-700 mb-8 max-w-xl mx-auto">
            Hundreds of hours saved. Resources optimized. Chaos replaced with clarity.
          </p>
          <div className="grid md:grid-cols-3 gap-8 max-w-4xl mx-auto">
            {[
              { value: "500+", label: "Hours Saved Per Semester" },
              { value: "99.9%", label: "Conflict Resolution Accuracy" },
              { value: "100%", label: "User Satisfaction in Pilot Campuses" },
            ].map(({ value, label }, i) => (
              <motion.div key={i} whileHover={{ scale: 1.05 }}>
                <div className="text-4xl font-bold text-blue-600">{value}</div>
                <p className="text-sm mt-1 text-gray-500">{label}</p>
              </motion.div>
            ))}
          </div>
        </motion.div>
      </section>

      {/* CTA SECTION */}
      <section className="bg-blue-700 text-white py-20 text-center px-6">
        <motion.div initial={{ opacity: 0, y: 40 }} whileInView={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }}>
          <h2 className="text-4xl font-bold mb-4">Join the Future of Scheduling — Anywhere It’s Needed</h2>
          <p className="mb-6 max-w-xl mx-auto text-blue-100">
            From academic halls to global logistics, UniScheduL is redefining what’s possible in planning.
          </p>
          <Link to="/login" className="bg-white text-blue-700 px-8 py-3 rounded-full font-semibold hover:bg-blue-100 hover:scale-105 transition-transform duration-300">
            Get Started
          </Link>
        </motion.div>
      </section>

      {/* FOOTER */}
      <footer className="bg-gray-900 text-gray-400 text-sm py-6">
        <div className="max-w-6xl mx-auto px-6 flex flex-col md:flex-row justify-between items-center">
          <div className="mb-4 md:mb-0">
            <h4 className="text-white font-bold text-lg">UniScheduL</h4>
            <p>© {new Date().getFullYear()} All rights reserved.</p>
          </div>
          <div className="flex gap-6">
            <a href="#learn-more" className="hover:text-white transition">Features</a>
            <a href="https://github.com/edeniyanda" target="_blank" rel="noreferrer" className="hover:text-white transition">GitHub</a>
            <a href="/docs" className="hover:text-white transition">Docs</a>
          </div>
        </div>
      </footer>
    </main>
  );
}
