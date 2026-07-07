import React from 'react';

const TeacherProfile = () => {
    return (
        <html className="light" lang="en">
            <head>
                <meta charSet="utf-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>Dr. Arpan Sharma | TutorConnect Nepal</title>
                <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
                <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet" />
                <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet" />
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
                                        "label-md": ["Inter"],
                                        "label-sm": ["Inter"],
                                        "headline-sm": ["Inter"],
                                        "display-lg": ["Inter"],
                                        "headline-md": ["Inter"],
                                        "body-lg": ["Inter"],
                                        "headline-lg": ["Inter"],
                                        "body-md": ["Inter"]
                                    }
                                }
                            }
                        }
                    `}
                </script>
                <style>{`
                    .material-symbols-outlined {
                        font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
                        vertical-align: middle;
                    }
                    .glass-effect {
                        backdrop-filter: blur(12px);
                        -webkit-backdrop-filter: blur(12px);
                    }
                    body {
                        font-family: 'Inter', sans-serif;
                        background-color: #f8f9ff;
                    }
                `}</style>
            </head>
            <body className="text-on-background">
                {/* TopNavBar */}
                <header className="bg-surface/80 backdrop-blur-xl docked full-width top-0 sticky z-50 border-b border-outline-variant shadow-sm">
                    <div className="flex justify-between items-center w-full px-lg md:px-xxl py-md max-w-container-max mx-auto">
                        <div className="flex items-center gap-xl">
                            <span className="font-headline-md text-headline-md font-bold text-primary">TutorConnect Nepal</span>
                            <nav className="hidden md:flex items-center gap-lg">
                                <a className="font-body-md text-body-md text-on-surface-variant hover:text-primary transition-colors" href="#">Find Tutors</a>
                                <a className="font-body-md text-body-md text-on-surface-variant hover:text-primary transition-colors" href="#">How it Works</a>
                                <a className="font-body-md text-body-md text-on-surface-variant hover:text-primary transition-colors" href="#">Categories</a>
                            </nav>
                        </div>
                        <div className="flex items-center gap-md">
                            <button className="hidden md:block font-body-md text-body-md px-md py-sm text-primary hover:bg-surface-container-low transition-all active:scale-95 duration-150">Join as Tutor</button>
                            <button className="font-body-md text-body-md px-lg py-sm bg-primary text-on-primary rounded-lg shadow-sm hover:shadow-md active:scale-95 transition-all">Log In</button>
                        </div>
                    </div>
                </header>
                <main className="max-w-container-max mx-auto px-lg md:px-xxl py-xl">
                    {/* Breadcrumbs */}
                    <nav className="flex items-center gap-xs text-on-surface-variant mb-lg font-label-md text-label-md">
                        <a className="hover:text-primary" href="#">Tutors</a>
                        <span className="material-symbols-outlined text-[18px]">chevron_right</span>
                        <a className="hover:text-primary" href="#">Science & Math</a>
                        <span className="material-symbols-outlined text-[18px]">chevron_right</span>
                        <span className="text-on-surface font-semibold">Dr. Arpan Sharma</span>
                    </nav>
                    <div className="grid grid-cols-1 lg:grid-cols-12 gap-xxl items-start">
                        {/* Left Column: Content */}
                        <div className="lg:col-span-8 space-y-xxl">
                            {/* Hero Section */}
                            <section className="flex flex-col md:flex-row gap-xl items-center md:items-start">
                                <div className="relative">
                                    <img className="w-48 h-48 md:w-56 md:h-56 rounded-xl object-cover shadow-lg border-4 border-white" data-alt="A professional headshot of a South Asian male professor in his late 40s, wearing a crisp white shirt and a navy blazer. He has a warm, confident smile and is photographed against a soft-focus academic background with bookshelves. The lighting is bright and natural, reflecting a clean and trustworthy educational atmosphere consistent with high-end professional platforms." src="https://lh3.googleusercontent.com/aida-public/AB6AXuCT5f5ICZBSlYdnVrF0E9yos25GD6Xhi4xhsVZs0A_5-xZ2ENeLp9fR1vxcNDZVFlemG7-d_0ro8Q4ia_AUnbHn9AIe4ybgZgaCI-LyGMTu67ClTTA2VYJLYSmcK0VYNiccodkE6RtsM79Gwo2QwRDojtMncBHNU1ZEqS5udPrNbP1Uf7LM59cjq5KRRuzpMhDQ6yylk8DRKGOFiQiCbA-l3ZEA-mXdizIkEiqNFQ4K2CD16iuSjL0wYmGzC9jQFoDuaHRqmkEx9dU" />
                                    <div className="absolute -bottom-2 -right-2 bg-primary text-on-primary p-xs rounded-full border-4 border-white">
                                        <span className="material-symbols-outlined" style={{ fontVariationSettings: "'FILL' 1" }}>verified</span>
                                    </div>
                                </div>
                                <div className="flex-1 text-center md:text-left space-y-sm">
                                    <div className="flex flex-wrap justify-center md:justify-start items-center gap-sm">
                                        <h1 className="font-headline-lg text-headline-lg text-on-surface">Dr. Arpan Sharma</h1>
                                        <div className="flex gap-xs">
                                            <span className="px-sm py-xs bg-surface-container-high text-primary font-label-sm text-label-sm rounded-full flex items-center gap-xs">
                                                <span className="material-symbols-outlined text-[16px]" style={{ fontVariationSettings: "'FILL' 1" }}>star</span>
                                                Top Rated
                                            </span>
                                            <span className="px-sm py-xs bg-primary-container/10 text-primary font-label-sm text-label-sm rounded-full flex items-center gap-xs">
                                                <span className="material-symbols-outlined text-[16px]" style={{ fontVariationSettings: "'FILL' 1" }}>verified_user</span>
                                                Verified
                                            </span>
                                        </div>
                                    </div>
                                    <p className="font-body-lg text-body-lg text-on-surface-variant max-w-2xl">PhD in Applied Physics | Specialized in Advanced Calculus and Quantum Mechanics</p>
                                    <div className="flex flex-wrap justify-center md:justify-start gap-md pt-sm">
                                        <div className="flex items-center gap-xs text-on-surface-variant font-label-md text-label-md">
                                            <span className="material-symbols-outlined text-primary">location_on</span>
                                            Kathmandu, Nepal
                                        </div>
                                        <div className="flex items-center gap-xs text-on-surface-variant font-label-md text-label-md">
                                            <span className="material-symbols-outlined text-primary">translate</span>
                                            Nepali, English, Hindi
                                        </div>
                                        <div className="flex items-center gap-xs text-on-surface-variant font-label-md text-label-md">
                                            <span className="material-symbols-outlined text-primary" style={{ fontVariationSettings: "'FILL' 1" }}>work</span>
                                            12+ Years Experience
                                        </div>
                                    </div>
                                </div>
                            </section>
                            {/* Subjects Bento Grid */}
                            <section className="space-y-md">
                                <h2 className="font-headline-sm text-headline-sm text-on-surface">Expertise & Subjects</h2>
                                <div className="grid grid-cols-2 sm:grid-cols-4 gap-md">
                                    <div className="p-md bg-white border border-outline-variant rounded-xl flex flex-col gap-sm hover:shadow-md transition-shadow">
                                        <span className="material-symbols-outlined text-primary text-[32px]">calculate</span>
                                        <span className="font-label-md text-label-md font-bold">Mathematics</span>
                                        <span className="text-xs text-on-surface-variant">Calculus, Linear Algebra</span>
                                    </div>
                                    <div className="p-md bg-white border border-outline-variant rounded-xl flex flex-col gap-sm hover:shadow-md transition-shadow">
                                        <span className="material-symbols-outlined text-primary text-[32px]">science</span>
                                        <span className="font-label-md text-label-md font-bold">Physics</span>
                                        <span className="text-xs text-on-surface-variant">Quantum, Mechanics</span>
                                    </div>
                                    <div className="p-md bg-white border border-outline-variant rounded-xl flex flex-col gap-sm hover:shadow-md transition-shadow">
                                        <span className="material-symbols-outlined text-primary text-[32px]">functions</span>
                                        <span className="font-label-md text-label-md font-bold">Statistics</span>
                                        <span className="text-xs text-on-surface-variant">Data Analysis, R</span>
                                    </div>
                                    <div className="p-md bg-white border border-outline-variant rounded-xl flex flex-col gap-sm hover:shadow-md transition-shadow">
                                        <span className="material-symbols-outlined text-primary text-[32px]">terminal</span>
                                        <span className="font-label-md text-label-md font-bold">Programming</span>
                                        <span className="text-xs text-on-surface-variant">Python, MATLAB</span>
                                    </div>
                                </div>
                            </section>
                            {/* About Me */}
                            <section className="space-y-md">
                                <h2 className="font-headline-sm text-headline-sm text-on-surface">About Arpan</h2>
                                <div className="font-body-md text-body-md text-on-surface-variant space-y-md leading-relaxed">
                                    <p>With over a decade of teaching experience at Nepal's premier institutions, I specialize in bridging the gap between theoretical complex concepts and practical application. My teaching philosophy centers on "Conceptual Clarity"—ensuring students don't just memorize formulas but understand the underlying logic.</p>
                                    <p>I have successfully mentored over 500+ students for competitive exams like JEE, SATs, and local university entrance tests. Whether you're struggling with high school trigonometry or university-level quantum physics, I tailor my sessions to your specific learning pace and style.</p>
                                </div>
                            </section>
                            {/* Education */}
                            <section className="space-y-md">
                                <h2 className="font-headline-sm text-headline-sm text-on-surface">Education & Qualifications</h2>
                                <div className="space-y-base">
                                    <div className="flex gap-md p-md bg-surface-container-low rounded-xl border border-outline-variant/30">
                                        <span className="material-symbols-outlined text-primary">school</span>
                                        <div>
                                            <h4 className="font-label-md text-label-md font-bold">PhD in Applied Physics</h4>
                                            <p className="text-on-surface-variant">Tribhuvan University | 2015 - 2019</p>
                                        </div>
                                    </div>
                                    <div className="flex gap-md p-md bg-surface-container-low rounded-xl border border-outline-variant/30">
                                        <span className="material-symbols-outlined text-primary">history_edu</span>
                                        <div>
                                            <h4 className="font-label-md text-label-md font-bold">MSc in Theoretical Physics</h4>
                                            <p className="text-on-surface-variant">Jawaharlal Nehru University | 2011 - 2013</p>
                                        </div>
                                    </div>
                                </div>
                            </section>
                            {/* Reviews */}
                            <section className="space-y-md pb-xxl">
                                <div className="flex justify-between items-end">
                                    <h2 className="font-headline-sm text-headline-sm text-on-surface">Reviews & Ratings</h2>
                                    <span className="text-primary font-label-md text-label-md cursor-pointer hover:underline">See all 148 reviews</span>
                                </div>
                                <div className="grid grid-cols-1 md:grid-cols-2 gap-lg">
                                    {/* Review 1 */}
                                    <div className="p-lg bg-white border border-outline-variant rounded-xl space-y-sm">
                                        <div className="flex justify-between items-start">
                                            <div className="flex items-center gap-sm">
                                                <div className="w-10 h-10 bg-secondary rounded-full flex items-center justify-center text-white font-bold">RS</div>
                                                <div>
                                                    <p className="font-label-md text-label-md font-bold">Rohan Sapkota</p>
                                                    <p className="text-xs text-on-surface-variant">2 weeks ago</p>
                                                </div>
                                            </div>
                                            <div className="flex text-primary">
                                                <span className="material-symbols-outlined text-[18px]" style={{ fontVariationSettings: "'FILL' 1" }}>star</span>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </section>
                        </div>
                    </div>
                </main>
            </body>
        </html>
    );
};

export default TeacherProfile;