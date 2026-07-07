import React from 'react';

const LearningHub = () => {
    return (
        <html className="light" lang="en">
            <head>
                <meta charSet="utf-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>Learning Hub | TutorConnect Nepal</title>
                <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
                <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet" />
                <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet" />
                <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet" />
                <script id="tailwind-config">
                    {`
                        tailwind.config = {
                            darkMode: "class",
                            theme: {
                                extend: {
                                    colors: {
                                        "on-error-container": "#93000a",
                                        "surface-container-high": "#dce9ff",
                                        "on-primary-container": "#f4fffc",
                                        "surface-dim": "#cbdbf5",
                                        "on-tertiary-fixed-variant": "#773215",
                                        "surface-container-low": "#eff4ff",
                                        "secondary": "#4648d4",
                                        "primary-container": "#008378",
                                        "error": "#ba1a1a",
                                        "surface-variant": "#d3e4fe",
                                        "inverse-primary": "#6bd8cb",
                                        "surface-container": "#e5eeff",
                                        "on-primary-fixed-variant": "#005049",
                                        "error-container": "#ffdad6",
                                        "on-tertiary-container": "#fffbff",
                                        "on-background": "#0b1c30",
                                        "on-secondary-fixed-variant": "#2f2ebe",
                                        "on-secondary": "#ffffff",
                                        "surface-tint": "#006a61",
                                        "on-secondary-fixed": "#07006c",
                                        "surface-container-highest": "#d3e4fe",
                                        "surface": "#f8f9ff",
                                        "tertiary-fixed-dim": "#ffb59a",
                                        "on-primary-fixed": "#00201d",
                                        "inverse-on-surface": "#eaf1ff",
                                        "tertiary-fixed": "#ffdbce",
                                        "background": "#f8f9ff",
                                        "surface-container-lowest": "#ffffff",
                                        "primary-fixed": "#89f5e7",
                                        "on-surface": "#0b1c30",
                                        "tertiary-container": "#b05e3d",
                                        "inverse-surface": "#213145",
                                        "on-surface-variant": "#3d4947",
                                        "on-error": "#ffffff",
                                        "outline": "#6d7a77",
                                        "tertiary": "#924628",
                                        "primary": "#00685f",
                                        "on-tertiary": "#ffffff",
                                        "primary-fixed-dim": "#6bd8cb",
                                        "on-tertiary-fixed": "#370e00",
                                        "secondary-container": "#6063ee",
                                        "on-primary": "#ffffff",
                                        "outline-variant": "#bcc9c6",
                                        "surface-bright": "#f8f9ff",
                                        "on-secondary-container": "#fffbff",
                                        "secondary-fixed": "#e1e0ff",
                                        "secondary-fixed-dim": "#c0c1ff"
                                    },
                                    borderRadius: {
                                        DEFAULT: "0.25rem",
                                        lg: "0.5rem",
                                        xl: "0.75rem",
                                        full: "9999px"
                                    },
                                    spacing: {
                                        xs: "4px",
                                        xl: "32px",
                                        "container-max": "1280px",
                                        lg: "24px",
                                        md: "16px",
                                        sm: "8px",
                                        xxl: "48px",
                                        base: "8px",
                                        gutter: "24px"
                                    },
                                    fontFamily: {
                                        "headline-lg-mobile": ["Inter"],
                                        "label-md": ["Inter"],
                                        "label-sm": ["Inter"],
                                        "headline-sm": ["Inter"],
                                        "display-lg": ["Inter"],
                                        "headline-md": ["Inter"],
                                        "body-lg": ["Inter"],
                                        "display-lg-mobile": ["Inter"],
                                        "headline-lg": ["Inter"],
                                        "body-md": ["Inter"]
                                    },
                                    fontSize: {
                                        "headline-lg-mobile": ["24px", { lineHeight: "1.3", fontWeight: "600" }],
                                        "label-md": ["14px", { lineHeight: "1.4", letterSpacing: "0.01em", fontWeight: "500" }],
                                        "label-sm": ["12px", { lineHeight: "1.3", fontWeight: "600" }],
                                        "headline-sm": ["20px", { lineHeight: "1.4", fontWeight: "600" }],
                                        "display-lg": ["48px", { lineHeight: "1.1", letterSpacing: "-0.02em", fontWeight: "700" }],
                                        "headline-md": ["24px", { lineHeight: "1.3", fontWeight: "600" }],
                                        "body-lg": ["18px", { lineHeight: "1.6", fontWeight: "400" }],
                                        "display-lg-mobile": ["36px", { lineHeight: "1.2", letterSpacing: "-0.02em", fontWeight: "700" }],
                                        "headline-lg": ["32px", { lineHeight: "1.25", fontWeight: "600" }],
                                        "body-md": ["16px", { lineHeight: "1.5", fontWeight: "400" }]
                                    }
                                }
                            }
                        }
                    `}
                </script>
                <style>{`
                    body { font-family: 'Inter', sans-serif; -webkit-font-smoothing: antialiased; }
                    .material-symbols-outlined { font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24; }
                    .glass-card { background: rgba(255, 255, 255, 0.7); backdrop-filter: blur(12px); border: 1px solid rgba(226, 232, 240, 0.8); }
                    .hero-gradient { background: radial-gradient(circle at top right, #e1e0ff 0%, #f8f9ff 100%); }
                `}</style>
            </head>
            <body className="bg-background text-on-background min-h-screen">
                {/* TopNavBar */}
                <header className="bg-surface/80 dark:bg-surface-dim/80 backdrop-blur-xl docked full-width top-0 sticky z-50 border-b border-outline-variant dark:border-on-surface-variant/20 shadow-sm">
                    <div className="flex justify-between items-center w-full px-lg md:px-xxl py-md max-w-container-max mx-auto">
                        <div className="flex items-center gap-xl">
                            <a className="font-headline-md text-headline-md font-bold text-primary dark:text-primary-fixed-dim" href="#">TutorConnect Nepal</a>
                            <nav className="hidden md:flex gap-lg">
                                <a className="font-body-md text-body-md text-on-surface-variant dark:text-outline hover:text-primary transition-colors" href="#">Find Tutors</a>
                                <a className="font-body-md text-body-md text-on-surface-variant dark:text-outline hover:text-primary transition-colors" href="#">How it Works</a>
                                <a className="font-body-md text-body-md text-on-surface-variant dark:text-outline hover:text-primary transition-colors" href="#">Categories</a>
                            </nav>
                        </div>
                        <div className="flex items-center gap-md">
                            <button className="hidden md:block font-label-md text-label-md text-primary hover:bg-surface-container-low px-md py-sm rounded-lg transition-all active:scale-95 duration-150">Join as Tutor</button>
                            <button className="bg-primary text-on-primary font-label-md text-label-md px-lg py-sm rounded-xl shadow-sm hover:translate-y-[-2px] transition-all active:scale-95 duration-150">Log In</button>
                        </div>
                    </div>
                </header>
                <main className="max-w-container-max mx-auto px-lg md:px-xxl py-xxl">
                    {/* Hero Section */}
                    <section className="mb-xxl text-center md:text-left">
                        <div className="inline-flex items-center gap-sm bg-primary-fixed text-on-primary-fixed px-md py-xs rounded-full mb-md">
                            <span className="material-symbols-outlined text-[18px]">school</span>
                            <span className="font-label-sm text-label-sm uppercase tracking-wider">Resources & Insights</span>
                        </div>
                        <h1 className="font-display-lg-mobile md:font-display-lg text-display-lg-mobile md:text-display-lg text-on-background mb-sm">Learning Hub</h1>
                        <p className="font-body-lg text-body-lg text-on-surface-variant max-w-2xl">Empowering students and parents with professional educational tips, tutor spotlights, and comprehensive study guides from Nepal's best educators.</p>
                    </section>
                    {/* Category Pills */}
                    <section className="flex flex-wrap gap-md mb-xl overflow-x-auto pb-sm scrollbar-hide">
                        <button className="bg-primary text-on-primary font-label-md text-label-md px-lg py-sm rounded-full transition-all">All Articles</button>
                        <button className="bg-surface-container-high text-on-surface-variant font-label-md text-label-md px-lg py-sm rounded-full hover:bg-primary-fixed transition-all">Study Tips</button>
                        <button className="bg-surface-container-high text-on-surface-variant font-label-md text-label-md px-lg py-sm rounded-full hover:bg-primary-fixed transition-all">Exam Prep</button>
                        <button className="bg-surface-container-high text-on-surface-variant font-label-md text-label-md px-lg py-sm rounded-full hover:bg-primary-fixed transition-all">Parenting</button>
                        <button className="bg-surface-container-high text-on-surface-variant font-label-md text-label-md px-lg py-sm rounded-full hover:bg-primary-fixed transition-all">Tutor Spotlight</button>
                        <button className="bg-surface-container-high text-on-surface-variant font-label-md text-label-md px-lg py-sm rounded-full hover:bg-primary-fixed transition-all">University Guides</button>
                    </section>
                    {/* Featured Post */}
                    <section className="mb-xxl">
                        <div className="group relative bg-surface-container-lowest rounded-[24px] overflow-hidden border border-outline-variant shadow-sm hover:shadow-lg transition-all duration-300 grid grid-cols-1 md:grid-cols-2 min-h-[480px]">
                            <div className="relative h-64 md:h-full overflow-hidden">
                                <img className="absolute inset-0 w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" data-alt="A focused high school student in Kathmandu studying in a modern, bright library with large windows. The lighting is soft and natural, emphasizing a calm, academic atmosphere. The aesthetic is clean and professional with subtle teal and blue accents in the environment, symbolizing clarity and progress." src="https://lh3.googleusercontent.com/aida-public/AB6AXuByqs8TrglSK_kq7cX_hkrpU1xjv9NLd8xuI_EmfCrbSbwmrR6k25AfMJcc6jugijLi35HV1Bzlbjv7Sy3CyI9Jqv8n-fHOdf9OuLCeUtlil82NPwpE6ajU1BHkh5O4jEGigeCk446--OUdSBnG-L3K56IzMzqQcPPMMOXb4IlaEkAIj7M5JUYKZPFnkWXPUfZQ-Sysslyn0Kk-5j4747kufW9tBsRrro1IRueFu5mhE35swJy9Jf_oAcw82As5XKuID8re5CtEUVk" />
                                <div className="absolute top-md left-md bg-secondary text-on-secondary px-md py-xs rounded-lg font-label-sm text-label-sm">FEATURED</div>
                            </div>
                            <div className="p-xl md:p-xxl flex flex-col justify-center">
                                <div className="flex items-center gap-sm text-primary mb-md">
                                    <span className="font-label-md text-label-md">Study Tips</span>
                                    <span className="w-1 h-1 bg-outline-variant rounded-full"></span>
                                    <span className="font-label-md text-label-md text-on-surface-variant">May 15, 2024</span>
                                </div>
                                <h2 className="font-headline-lg text-headline-lg text-on-background mb-md leading-tight group-hover:text-primary transition-colors">How to Master the SEE Exams: A Comprehensive Guide for Nepali Students</h2>
                                <p className="font-body-md text-body-md text-on-surface-variant mb-xl">Exam season can be overwhelming, but with the right strategy, success is within reach. We break down the top 10 study techniques used by toppers across Nepal to help you excel in your Secondary Education Examination.</p>
                                <div className="flex items-center justify-between mt-auto">
                                    <div className="flex items-center gap-sm">
                                        <img className="w-10 h-10 rounded-full border border-outline-variant" data-alt="A professional headshot of a friendly educator, an expert teacher with a warm smile, wearing professional attire. The background is a soft-focus academic setting. The photo is high-quality with professional studio lighting, adhering to the clean, institutional reliability aesthetic." src="https://lh3.googleusercontent.com/aida-public/AB6AXuBuOz69qSzg59eF3dd_wDafL5XkQZmxqWxBgaYKHzZ4He2MJFy40H1DLTmSLnX3v3ORUG98CQfeQiz_Z0PUnl8B_VL86AtUkbEzGfb8X5rvPwtsBCByxK8FoNkhrqpm-OSB5D_m2f2A8vbM0suR2eEiEJnHJ-S6JkPJafSNDf2bTcPOot6CnR8dWsAHxS3qPkv-WTC4pdDMDYvlAayHCYatHM2CeXJXXWcK83KiQGl9mbLbbnc5K3xIgQ3bYcNzdmI27leblYujQCM" />
                                        <div>
                                            <p className="font-label-md text-label-md text-on-surface">By Prof. Ramesh Karki</p>
                                            <p className="font-label-sm text-label-sm text-on-surface-variant">Education Consultant</p>
                                        </div>
                                    </div>
                                    <span className="font-label-sm text-label-sm text-on-surface-variant flex items-center gap-xs">
                                        <span className="material-symbols-outlined text-[16px]">schedule</span>
                                        12 min read
                                    </span>
                                </div>
                            </div>
                        </div>
                    </section>
                    {/* Bento Grid Posts */}
                    <section className="grid grid-cols-1 md:grid-cols-3 gap-xl">
                        {/* Article 1: Tutor Spotlight */}
                        <article className="group bg-surface-container-lowest rounded-xl overflow-hidden border border-outline-variant hover:shadow-md transition-all">
                            <div className="h-48 overflow-hidden">
                                <img className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110" data-alt="An action shot of a passionate mathematics tutor explaining complex calculus on a clean whiteboard. The setting is a brightly lit, modern tutoring center in Lalitpur. High-key lighting and a palette of crisp whites and primary teals create a professional, encouraging mood." src="https://lh3.googleusercontent.com/aida-public/AB6AXuDCl4HbohPWyqHrYL4Qrsb6srYg7EE7JQylLKSW9m04URGx0XnaNB5OHgA8itoWI5aVMMA0B5QRJz8Qhxri_HFyyKKpfw6rRKqBJLgL4ZUzL_qp1zRsUD22DjXkzIPJOzIoyj_7npchbxEUTk-ej5yGupe8KpM4y-35S2atNxE9y9mx08zn-weueGe974XJI3zR62LvXayeFpgwc0Ml2UlD395H7UVbKgCshFz1CZFhA7NFhvA2UmMN6e6SvuaYW51rHHDdUXrIzts" />
                            </div>
                            <div className="p-lg">
                                <div className="flex items-center gap-sm text-secondary mb-sm">
                                    <span className="font-label-sm text-label-sm uppercase font-bold tracking-tight">Tutor Spotlight</span>
                                </div>
                                <h3 className="font-headline-sm text-headline-sm text-on-background mb-sm leading-tight group-hover:text-primary transition-colors">Meet Dr. Arpan Sharma: Revolutionizing Math Education</h3>
                                <p className="font-body-md text-body-md text-on-surface-variant mb-lg line-clamp-2">Discover how one educator is making advanced mathematics accessible to students across remote areas of Nepal.</p>
                                <div className="flex items-center justify-between border-t border-outline-variant pt-md">
                                    <span className="font-label-sm text-label-sm text-on-surface-variant">May 12, 2024</span>
                                    <span className="font-label-sm text-label-sm text-on-surface-variant flex items-center gap-xs">
                                        <span className="material-symbols-outlined text-[14px]">schedule</span>
                                        8 min read
                                    </span>
                                </div>
                            </div>
                        </article>
                        {/* Article 2: Parenting */}
                        <article className="group bg-surface-container-lowest rounded-xl overflow-hidden border border-outline-variant hover:shadow-md transition-all">
                            <div className="h-48 overflow-hidden">
                                <img className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110" data-alt="A heartwarming scene of a Nepali parent and child engaged in shared reading at a cozy home desk. Soft evening lighting through a window creates a warm, supportive atmosphere. The design follows a modern professional look with minimal clutter and organized learning materials." src="https://lh3.googleusercontent.com/aida-public/AB6AXuABSZQtR8AM2xGw7vpWHZNQBD-eXumDmWDcplL0FuFJHazd6NPt5xanwAzGeU4o3sz0phcNMIHoyDcI75CPl_fDiACIxv9GtWspLTcMd-f77vsjZ55wW5RCEY_j5g4L7mZ4OQLaMSzqRq8Vu7sJ0D6LyUkVVL4CZhcc5jc9ZqNS0q5kbHzi2sK7XqPBqet7SYts6eWPofPfP02V3nNwMhGzf5H_O-7595zoWsBtz7IaEiOuUalKTMH2yGsBLdnkDnHt9Usa2r_BmQE" />
                            </div>
                            <div className="p-lg">
                                <div className="flex items-center gap-sm text-primary mb-sm">
                                    <span className="font-label-sm text-label-sm uppercase font-bold tracking-tight">Parenting</span>
                                </div>
                                <h3 className="font-headline-sm text-headline-sm text-on-background mb-sm leading-tight group-hover:text-primary transition-colors">Supporting Your Child's Mental Health During Finals</h3>
                                <p className="font-body-md text-body-md text-on-surface-variant mb-lg line-clamp-2">Practical advice for parents on how to create a stress-free environment during the intense exam periods.</p>
                                <div className="flex items-center justify-between border-t border-outline-variant pt-md">
                                    <span className="font-label-sm text-label-sm text-on-surface-variant">May 10, 2024</span>
                                    <span className="font-label-sm text-label-sm text-on-surface-variant flex items-center gap-xs">
                                        <span className="material-symbols-outlined text-[14px]">schedule</span>
                                        6 min read
                                    </span>
                                </div>
                            </div>
                        </article>
                        {/* Article 3: Exam Prep */}
                        <article className="group bg-surface-container-lowest rounded-xl overflow-hidden border border-outline-variant hover:shadow-md transition-all">
                            <div className="h-48 overflow-hidden">
                                <img className="w-full h-full object-cover transition-transform duration-500 group-hover:scale-110" data-alt="A high-quality top-down shot of a well-organized study desk featuring a laptop, neat handwritten notes in Nepali and English, and a cup of tea. The lighting is bright and even, highlighting professional productivity. The aesthetic is clean, academic, and modern." src="https://lh3.googleusercontent.com/aida-public/AB6AXuCqyB83mIit_zTXHOJ2bcmDhmqLy00lFcXrHQZzQqu9PsHDaaCXFTfg_TSih9POv-mKnNlNtOyUWo_j0Newnt-v_Pzrla5JNw0wXNj3Ce8Fu5S47yvA-ELszbka9psNg--nqmzZ-CLAPTL8PaH01-GLkt5mlBLb0U1yyE-rB2kjdc57XP-BdFmqe3DD7to1fO7aoCpL7U8PyRF8dGX7gVaQxEYs_XHaRC085NUUkqnpTy9FUhhDMVmwJPFWjRm_2xOvZkihfYRKiCU" />
                            </div>
                            <div className="p-lg">
                                <div className="flex items-center gap-sm text-tertiary mb-sm">
                                    <span className="font-label-sm text-label-sm uppercase font-bold tracking-tight">Exam Prep</span>
                                </div>
                                <h3 className="font-headline-sm text-headline-sm text-on-background mb-sm leading-tight group-hover:text-primary transition-colors">IELTS Success: Tips for Achieving a Band 8+</h3>
                                <p className="font-body-md text-body-md text-on-surface-variant mb-lg line-clamp-2">Our expert tutors share their secrets on mastering the listening and speaking modules of the IELTS exam.</p>
                                <div className="flex items-center justify-between border-t border-outline-variant pt-md">
                                    <span className="font-label-sm text-label-sm text-on-surface-variant">May 08, 2024</span>
                                    <span className="font-label-sm text-label-sm text-on-surface-variant flex items-center gap-xs">
                                        <span className="material-symbols-outlined text-[14px]">schedule</span>
                                        15 min read
                                    </span>
                                </div>
                            </div>
                        </article>
                    </section>
                    {/* Newsletter CTA */}
                    <section className="mt-xxl bg-surface-container-high rounded-[32px] p-xl md:p-xxl flex flex-col md:flex-row items-center justify-between gap-xl">
                        <div className="md:max-w-xl text-center md:text-left">
                            <h2 className="font-headline-lg text-headline-lg text-on-surface mb-md">Stay ahead in your learning journey</h2>
                            <p className="font-body-md text-body-md text-on-surface-variant">Subscribe to our weekly newsletter and get the latest educational resources, tips, and tutor updates delivered directly to your inbox.</p>
                        </div>
                        <form className="flex flex-col sm:flex-row gap-md w-full md:w-auto" onSubmit={(e) => e.preventDefault()}>
                            <input className="bg-surface-container-lowest border border-outline-variant rounded-xl px-lg py-md focus:outline-none focus:ring-2 focus:ring-primary/20 min-w-[300px]" placeholder="Enter your email" type="email" />
                            <button className="bg-primary text-on-primary font-label-md text-label-md px-xxl py-md rounded-xl hover:shadow-lg transition-all active:scale-95">Subscribe</button>
                        </form>
                    </section>
                </main>
                {/* Footer */}
                <footer className="bg-surface-container-highest dark:bg-on-surface-variant border-t border-outline-variant dark:border-on-surface-variant/30 mt-xxl">
                    <div className="grid grid-cols-1 md:grid-cols-4 gap-xl px-lg md:px-xxl py-xxl max-w-container-max mx-auto">
                        <div className="flex flex-col gap-md">
                            <span className="font-headline-md text-headline-md font-bold text-primary">TutorConnect Nepal</span>
                            <p className="font-body-md text-body-md text-on-surface-variant dark:text-inverse-on-surface/70">Connecting Nepal's brightest minds through quality education and expert tutoring.</p>
                        </div>
                        <div>
                            <h4 className="font-label-md text-label-md font-bold text-on-surface mb-lg">Platform</h4>
                            <div className="flex flex-col gap-sm">
                                <a className="font-body-md text-body-md text-on-surface-variant dark:text-inverse-on-surface/70 hover:text-primary transition-colors" href="#">Find Tutors</a>
                                <a className="font-body-md text-body-md text-on-surface-variant dark:text-inverse-on-surface/70 hover:text-primary transition-colors" href="#">How it Works</a>
                                <a className="font-body-md text-body-md text-on-surface-variant dark:text-inverse-on-surface/70 hover:text-primary transition-colors" href="#">Safety Guide</a>
                            </div>
                        </div>
                        <div>
                            <h4 className="font-label-md text-label-md font-bold text-on-surface mb-lg">Resources</h4>
                            <div className="flex flex-col gap-sm">
                                <a className="font-body-md text-body-md text-primary font-bold" href="#">Learning Hub</a>
                                <a className="font-body-md text-body-md text-on-surface-variant dark:text-inverse-on-surface/70 hover:text-primary transition-colors" href="#">About Us</a>
                                <a className="font-body-md text-body-md text-on-surface-variant dark:text-inverse-on-surface/70 hover:text-primary transition-colors" href="#">Contact Support</a>
                            </div>
                        </div>
                        <div>
                            <h4 className="font-label-md text-label-md font-bold text-on-surface mb-lg">Legal</h4>
                            <div className="flex flex-col gap-sm">
                                <a className="font-body-md text-body-md text-on-surface-variant dark:text-inverse-on-surface/70 hover:text-primary transition-colors" href="#">Privacy Policy</a>
                                <a className="font-body-md text-body-md text-on-surface-variant dark:text-inverse-on-surface/70 hover:text-primary transition-colors" href="#">Terms of Service</a>
                            </div>
                        </div>
                    </div>
                    <div className="max-w-container-max mx-auto px-lg md:px-xxl py-lg border-t border-outline-variant/30 flex flex-col md:flex-row justify-between items-center gap-md">
                        <p className="font-body-md text-body-md text-on-surface-variant dark:text-inverse-on-surface/50">© 2024 TutorConnect Nepal. All rights reserved.</p>
                        <div className="flex gap-lg">
                            <a className="text-on-surface-variant hover:text-primary transition-colors" href="#"><span className="material-symbols-outlined">face_nod</span></a>
                            <a className="text-on-surface-variant hover:text-primary transition-colors" href="#"><span className="material-symbols-outlined">linked_camera</span></a>
                            <a className="text-on-surface-variant hover:text-primary transition-colors" href="#"><span className="material-symbols-outlined">alternate_email</span></a>
                        </div>
                    </div>
                </footer>
            </body>
        </html>
    );
};

export default LearningHub;