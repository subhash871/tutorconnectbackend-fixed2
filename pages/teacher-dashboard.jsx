import React from 'react';

const TeacherDashboard = () => {
    return (
        <html className="light" lang="en">
            <head>
                <meta charSet="utf-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>Teacher Dashboard - TutorConnect Nepal</title>
                <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
                <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet" />
                <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet" />
                <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet" />
                <style>{`
                    .material-symbols-outlined {
                        font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
                    }
                    body {
                        font-family: 'Inter', sans-serif;
                    }
                    .glass-card {
                        background: rgba(255, 255, 255, 0.8);
                        backdrop-filter: blur(8px);
                        border: 1px solid #E2E8F0;
                    }
                    .sidebar-active-indicator {
                        width: 4px;
                        height: 24px;
                        background-color: #00685f;
                        border-radius: 0 4px 4px 0;
                        position: absolute;
                        left: 0;
                    }
                    /* Custom Scrollbar */
                    ::-webkit-scrollbar {
                        width: 6px;
                    }
                    ::-webkit-scrollbar-track {
                        background: #f1f1f1;
                    }
                    ::-webkit-scrollbar-thumb {
                        background: #bcc9c6;
                        border-radius: 10px;
                    }
                    ::-webkit-scrollbar-thumb:hover {
                        background: #00685f;
                    }
                `}</style>
                <script id="tailwind-config">
                    {`
                        tailwind.config = {
                            darkMode: "class",
                            theme: {
                                extend: {
                                    colors: {
                                        "on-surface-variant": "#3d4947",
                                        "on-tertiary": "#ffffff",
                                        "tertiary": "#924628",
                                        "inverse-surface": "#213145",
                                        "primary-fixed-dim": "#6bd8cb",
                                        "background": "#f8f9ff",
                                        "on-secondary-fixed-variant": "#2f2ebe",
                                        "on-primary-fixed-variant": "#005049",
                                        "on-tertiary-container": "#fffbff",
                                        "secondary-fixed-dim": "#c0c1ff",
                                        "on-primary-fixed": "#00201d",
                                        "surface-tint": "#006a61",
                                        "on-primary-container": "#f4fffc",
                                        "tertiary-container": "#b05e3d",
                                        "surface": "#f8f9ff",
                                        "surface-container-high": "#dce9ff",
                                        "outline-variant": "#bcc9c6",
                                        "surface-container": "#e5eeff",
                                        "primary-container": "#008378",
                                        "tertiary-fixed-dim": "#ffb59a",
                                        "primary-fixed": "#89f5e7",
                                        "surface-bright": "#f8f9ff",
                                        "on-secondary-container": "#fffbff",
                                        "on-surface": "#0b1c30",
                                        "error-container": "#ffdad6",
                                        "error": "#ba1a1a",
                                        "tertiary-fixed": "#ffdbce",
                                        "inverse-primary": "#6bd8cb",
                                        "on-tertiary-fixed": "#370e00",
                                        "on-secondary": "#ffffff",
                                        "on-primary": "#ffffff",
                                        "inverse-on-surface": "#eaf1ff",
                                        "on-error": "#ffffff",
                                        "secondary-fixed": "#e1e0ff",
                                        "outline": "#6d7a77",
                                        "on-secondary-fixed": "#07006c",
                                        "secondary-container": "#6063ee",
                                        "surface-container-highest": "#d3e4fe",
                                        "surface-variant": "#d3e4fe",
                                        "surface-container-lowest": "#ffffff",
                                        "secondary": "#4648d4",
                                        "surface-container-low": "#eff4ff",
                                        "on-background": "#0b1c30",
                                        "on-error-container": "#93000a",
                                        "primary": "#00685f",
                                        "surface-dim": "#cbdbf5",
                                        "on-tertiary-fixed-variant": "#773215"
                                    },
                                    borderRadius: {
                                        DEFAULT: "0.25rem",
                                        lg: "0.5rem",
                                        xl: "0.75rem",
                                        full: "9999px"
                                    },
                                    spacing: {
                                        "container-max": "1280px",
                                        "gutter": "24px",
                                        xs: "4px",
                                        xl: "32px",
                                        sm: "8px",
                                        md: "16px",
                                        xxl: "48px",
                                        base: "8px",
                                        lg: "24px"
                                    },
                                    fontFamily: {
                                        "body-md": ["Inter"],
                                        "headline-md": ["Inter"],
                                        "display-lg": ["Inter"],
                                        "headline-sm": ["Inter"],
                                        "label-md": ["Inter"]
                                    },
                                    fontSize: {
                                        "body-md": ["16px", { lineHeight: "1.5", fontWeight: "400" }],
                                        "headline-md": ["24px", { lineHeight: "1.3", fontWeight: "600" }],
                                        "display-lg": ["48px", { lineHeight: "1.1", letterSpacing: "-0.02em", fontWeight: "700" }],
                                        "headline-sm": ["20px", { lineHeight: "1.4", fontWeight: "600" }],
                                        "label-md": ["14px", { lineHeight: "1.4", letterSpacing: "0.01em", fontWeight: "500" }]
                                    }
                                }
                            }
                        }
                    `}
                </script>
            </head>
            <body className="bg-background text-on-surface">
                {/* Sidebar Navigation Shell */}
                <aside className="h-screen w-64 fixed left-0 top-0 bg-surface-container-low border-r border-outline-variant flex flex-col py-xl px-md gap-base z-50">
                    <div className="mb-xxl px-md">
                        <h1 className="font-headline-sm text-headline-sm font-black text-primary">TutorConnect</h1>
                        <p className="text-[10px] uppercase tracking-widest text-outline">Nepal Edition</p>
                    </div>
                    <div className="flex items-center gap-md px-md mb-xl">
                        <div className="w-10 h-10 rounded-full overflow-hidden border-2 border-primary-fixed">
                            <img className="w-full h-full object-cover" data-alt="A professional headshot of a friendly South Asian male tutor in his late 30s, wearing a smart casual blazer. He is positioned against a soft-focus academic background with books. The lighting is warm and professional, emphasizing expertise and approachable character in a high-fidelity light-mode UI style." src="https://lh3.googleusercontent.com/aida-public/AB6AXuAoyHz6po6IaB4G-CjBbrP5x08DDn8nMSYts_pFEZcF0wfl6a_XJJV5aje3haNlUrov4e8JqIleN7JCYjhP0d6_sS8P8bGqRi9j3gdB67V0TpRJwTuZ1pKH6k1Z-hH6ccOnzoq5cKAI9s1mUJ8M3vxkkCiFwLHwvyfs75TG004LZra8cpkFt2XWdq27bDKQ08-hKjTD0Km1uja-eqcYefLpfZc_vkrWmFAiTD5RKzjbdWhYDH005PMFSoleGb411RJBMBkSBzppu6s" />
                        </div>
                        <div>
                            <p className="font-label-md text-label-md text-on-surface-variant">Welcome back,</p>
                            <p className="font-bold text-on-surface">Dr. Arpan Sharma</p>
                        </div>
                    </div>
                    <nav className="flex-grow space-y-sm">
                        {/* Active State Logic: Dashboard is current page */}
                        <a className="flex items-center gap-md bg-primary-container text-on-primary-container rounded-lg px-md py-sm border-l-4 border-primary transition-all duration-200" href="#">
                            <span className="material-symbols-outlined" data-icon="dashboard">dashboard</span>
                            <span className="font-label-md text-label-md">Dashboard</span>
                        </a>
                        <a className="flex items-center gap-md text-on-surface-variant px-md py-sm hover:bg-surface-container-high hover:translate-x-1 transition-all" href="#">
                            <span className="material-symbols-outlined" data-icon="event_available">event_available</span>
                            <span className="font-label-md text-label-md">Availability</span>
                        </a>
                        <a className="flex items-center gap-md text-on-surface-variant px-md py-sm hover:bg-surface-container-high hover:translate-x-1 transition-all" href="#">
                            <span className="material-symbols-outlined" data-icon="calendar_month">calendar_month</span>
                            <span className="font-label-md text-label-md">Bookings</span>
                        </a>
                        <a className="flex items-center gap-md text-on-surface-variant px-md py-sm hover:bg-surface-container-high hover:translate-x-1 transition-all" href="#">
                            <span className="material-symbols-outlined" data-icon="payments">payments</span>
                            <span className="font-label-md text-label-md">Earnings</span>
                        </a>
                        <a className="flex items-center gap-md text-on-surface-variant px-md py-sm hover:bg-surface-container-high hover:translate-x-1 transition-all" href="#">
                            <span className="material-symbols-outlined" data-icon="star">star</span>
                            <span className="font-label-md text-label-md">Reviews</span>
                        </a>
                        <a className="flex items-center gap-md text-on-surface-variant px-md py-sm hover:bg-surface-container-high hover:translate-x-1 transition-all" href="#">
                            <span className="material-symbols-outlined" data-icon="settings">settings</span>
                            <span className="font-label-md text-label-md">Settings</span>
                        </a>
                    </nav>
                    <div className="mt-auto space-y-sm pt-xl border-t border-outline-variant/30">
                        <a className="flex items-center gap-md text-on-surface-variant px-md py-sm hover:bg-surface-container-high transition-all" href="#">
                            <span className="material-symbols-outlined" data-icon="help">help</span>
                            <span className="font-label-md text-label-md">Help Center</span>
                        </a>
                        <a className="flex items-center gap-md text-error px-md py-sm hover:bg-error-container transition-all rounded-lg" href="#">
                            <span className="material-symbols-outlined" data-icon="logout">logout</span>
                            <span className="font-label-md text-label-md">Logout</span>
                        </a>
                    </div>
                </aside>
                {/* Main Content Canvas */}
                <main className="ml-64 min-h-screen p-xxl">
                    <header className="mb-xxl flex justify-between items-end">
                        <div>
                            <h2 className="font-display-lg text-display-lg text-primary">Instructor Dashboard</h2>
                            <p className="font-body-lg text-body-lg text-on-surface-variant">Here's what's happening with your classes today.</p>
                        </div>
                        <button className="bg-primary text-on-primary px-lg py-md rounded-xl font-label-md text-label-md flex items-center gap-sm shadow-sm hover:shadow-md active:scale-95 transition-all">
                            <span className="material-symbols-outlined text-[20px]" data-icon="add">add</span>
                            Create New Session
                        </button>
                    </header>
                    {/* Top Stats Row (Bento Style) */}
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-lg mb-xxl">
                        <div className="glass-card p-xl rounded-xl shadow-sm border border-outline-variant flex items-center gap-xl">
                            <div className="w-12 h-12 rounded-full bg-primary-container/20 flex items-center justify-center text-primary">
                                <span className="material-symbols-outlined text-[28px]" data-icon="star" data-weight="fill" style={{ fontVariationSettings: "'FILL' 1" }}>star</span>
                            </div>
                            <div>
                                <p className="font-label-md text-label-md text-on-surface-variant">Avg. Rating</p>
                                <p className="font-headline-md text-headline-md">4.92 <span className="text-label-sm text-outline">/ 5.0</span></p>
                            </div>
                        </div>
                        <div className="glass-card p-xl rounded-xl shadow-sm border border-outline-variant flex items-center gap-xl">
                            <div className="w-12 h-12 rounded-full bg-secondary-container/10 flex items-center justify-center text-secondary">
                                <span className="material-symbols-outlined text-[28px]" data-icon="visibility">visibility</span>
                            </div>
                            <div>
                                <p className="font-label-md text-label-md text-on-surface-variant">Profile Views</p>
                                <p className="font-headline-md text-headline-md">1,284 <span className="text-label-sm text-primary font-bold text-[12px]">+12%</span></p>
                            </div>
                        </div>
                        <div className="glass-card p-xl rounded-xl shadow-sm border border-outline-variant flex items-center gap-xl">
                            <div className="w-12 h-12 rounded-full bg-tertiary-container/10 flex items-center justify-center text-tertiary">
                                <span className="material-symbols-outlined text-[28px]" data-icon="schedule">schedule</span>
                            </div>
                            <div>
                                <p className="font-label-md text-label-md text-on-surface-variant">Response Time</p>
                                <p className="font-headline-md text-headline-md">14 <span className="text-label-sm text-outline">mins</span></p>
                            </div>
                        </div>
                    </div>
                    {/* Main Dashboard Grid */}
                    <div className="grid grid-cols-1 lg:grid-cols-3 gap-xxl">
                        {/* Column 1 & 2: Earnings & Bookings */}
                        <div className="lg:col-span-2 space-y-xxl">
                            {/* Earnings Widget */}
                            <section className="glass-card p-xl rounded-xl shadow-sm border border-outline-variant overflow-hidden">
                                <div className="flex justify-between items-center mb-xl">
                                    <h3 className="font-headline-sm text-headline-sm">Earnings Overview</h3>
                                    <select className="bg-surface-container-low border-none rounded-lg font-label-md text-label-md px-md">
                                        <option>Last 30 Days</option>
                                        <option>Last 90 Days</option>
                                    </select>
                                </div>
                                <div className="grid grid-cols-1 md:grid-cols-2 gap-xxl items-end">
                                    <div className="space-y-xl">
                                        <div>
                                            <p className="font-label-md text-label-md text-on-surface-variant">Total Earned</p>
                                            <p className="text-[40px] font-black text-primary leading-none">Rs. 42,500</p>
                                        </div>
                                        <div className="p-md rounded-lg bg-surface-container-high/50 border border-outline-variant/30">
                                            <p className="font-label-sm text-label-sm text-outline">Pending Payments</p>
                                            <p className="font-headline-sm text-headline-sm text-tertiary">Rs. 8,200</p>
                                        </div>
                                    </div>
                                    {/* Simple Line Chart Mockup */}
                                    <div className="h-40 relative">
                                        <svg className="w-full h-full" viewBox="0 0 400 150">
                                            <defs>
                                                <linearGradient id="chartGradient" x1="0" x2="0" y1="0" y2="1">
                                                    <stop offset="0%" stopColor="#00685f" stopOpacity="0.2"></stop>
                                                    <stop offset="100%" stopColor="#00685f" stopOpacity="0"></stop>
                                                </linearGradient>
                                            </defs>
                                            <path d="M0,130 Q50,110 80,120 T150,80 T220,100 T300,50 T400,30 L400,150 L0,150 Z" fill="url(#chartGradient)"></path>
                                            <path d="M0,130 Q50,110 80,120 T150,80 T220,100 T300,50 T400,30" fill="none" stroke="#00685f" strokeLinecap="round" strokeWidth="3"></path>
                                            <circle cx="400" cy="30" fill="#00685f" r="4"></circle>
                                        </svg>
                                        <div className="flex justify-between mt-sm font-label-sm text-label-sm text-outline uppercase tracking-tighter">
                                            <span>Week 1</span>
                                            <span>Week 2</span>
                                            <span>Week 3</span>
                                            <span>Week 4</span>
                                        </div>
                                    </div>
                                </div>
                            </section>
                            {/* Booking Requests */}
                            <section>
                                <div className="flex justify-between items-center mb-lg">
                                    <h3 className="font-headline-sm text-headline-sm">New Booking Requests</h3>
                                    <a className="text-primary font-label-md text-label-md hover:underline" href="#">View all</a>
                                </div>
                                <div className="space-y-md">
                                    {/* Request Card 1 */}
                                    <div className="glass-card p-lg rounded-xl flex items-center justify-between hover:border-primary/40 transition-colors">
                                        <div className="flex items-center gap-lg">
                                            <div className="w-14 h-14 rounded-lg bg-surface-container-highest overflow-hidden">
                                                <img className="w-full h-full object-cover" data-alt="Close-up portrait of a studious teenage boy with glasses, smiling politely. He is holding a notebook, suggesting a student persona. Bright, clean high-key lighting for a professional educational portal appearance. Soft teal background elements consistent with the brand's primary color." src="https://lh3.googleusercontent.com/aida-public/AB6AXuBJkzrzj31FqKgqWXVnAANDji1YaMJwh57WPnUJkzCZrmt7cLZZNsROYffzQ8pHyRhqGDv1UiTLc7z2RH9lbpz8JJ3rW0FbNKqK3eho52OruCZqiGObjTe8y88Thfflu-tbuvcnmG_myi1MyH03J7vlLTzq56Cgmp68xqr-lBxCfLq2gCV7JgcB9pDiw0p1sur-k32W_gtsNSa5d3i_dk9TBoDxYCOU4UjTjchlctIHcxJ7vmYraXAW1IcT430NUEaL7nJ17CPd39w" />
                                            </div>
                                            <div>
                                                <h4 className="font-bold text-on-surface">Bibek Koirala</h4>
                                                <p className="text-label-sm text-outline">Physics • Grade 12 • 2 Hours</p>
                                                <p className="text-[12px] text-primary flex items-center gap-xs mt-1">
                                                    <span className="material-symbols-outlined text-[14px]" data-icon="event">event</span>
                                                    Tomorrow, 4:00 PM - 6:00 PM
                                                </p>
                                            </div>
                                        </div>
                                        <div className="flex gap-sm">
                                            <button className="px-md py-sm rounded-lg border border-outline-variant text-on-surface-variant font-label-md text-label-md hover:bg-surface-container-high transition-colors">Decline</button>
                                            <button className="px-md py-sm rounded-lg bg-primary text-on-primary font-label-md text-label-md hover:opacity-90 active:scale-95 transition-all">Accept</button>
                                        </div>
                                    </div>
                                    {/* Request Card 2 */}
                                    <div className="glass-card p-lg rounded-xl flex items-center justify-between hover:border-primary/40 transition-colors">
                                        <div className="flex items-center gap-lg">
                                            <div className="w-14 h-14 rounded-lg bg-surface-container-highest overflow-hidden">
                                                <img className="w-full h-full object-cover" data-alt="Portrait of a young female student with an eager and attentive expression. She has dark hair and is wearing a school uniform-style sweater. The background is a crisp, minimalist indoor setting with natural light, perfect for a high-end educational user interface." src="https://lh3.googleusercontent.com/aida-public/AB6AXuAdLvcRHH7En9PTH0B1kX_sCaHlmahRDA3F5YbCVgH5PlQETGFHNvwulUVCrgHhAid3dcHsPr4Mggh90szR0MQByIZvB6QcR3wEMbUgq6DOVU2Y7pW5-IlvpEKuempDRt9HSwupM95pNSidRSdYFQE6yvGmt-LxpxwLhgoLqQWtOy2Ozls3mZtzZTRdHGhi6M0TVmcJ-Zf9DIIFPZG8rWcACEB9qq9LtfHCb8_ILia5NtOlkbT1ywE7vpAzd2ZdVczDJaxTgfJrIgQ" />
                                            </div>
                                            <div>
                                                <h4 className="font-bold text-on-surface">Sneha Thapa</h4>
                                                <p className="text-label-sm text-outline">Mathematics • Grade 10 • 1.5 Hours</p>
                                                <p className="text-[12px] text-primary flex items-center gap-xs mt-1">
                                                    <span className="material-symbols-outlined text-[14px]" data-icon="event">event</span>
                                                    Friday, 10:00 AM - 11:30 AM
                                                </p>
                                            </div>
                                        </div>
                                        <div className="flex gap-sm">
                                            <button className="px-md py-sm rounded-lg border border-outline-variant text-on-surface-variant font-label-md text-label-md hover:bg-surface-container-high transition-colors">Decline</button>
                                            <button className="px-md py-sm rounded-lg bg-primary text-on-primary font-label-md text-label-md hover:opacity-90 active:scale-95 transition-all">Accept</button>
                                        </div>
                                    </div>
                                </div>
                            </section>
                        </div>
                        {/* Column 3: Availability & Profile Summary */}
                        <div className="space-y-xxl">
                            {/* Today's Schedule */}
                            <section className="bg-primary text-on-primary p-xl rounded-xl shadow-lg relative overflow-hidden">
                                {/* Subtle background pattern */}
                                <div className="absolute top-0 right-0 opacity-10 pointer-events-none">
                                    <span className="material-symbols-outlined text-[120px]" data-icon="calendar_today">calendar_today</span>
                                </div>
                                <h3 className="font-headline-sm text-headline-sm mb-xl relative z-10">Today's Schedule</h3>
                                <div className="space-y-xl relative z-10">
                                    <div className="flex gap-lg">
                                        <div className="flex flex-col items-center">
                                            <span className="font-bold">14:00</span>
                                            <div className="w-[2px] h-full bg-on-primary/30 my-xs"></div>
                                        </div>
                                        <div className="pb-md">
                                            <p className="font-bold">Introduction to Calculus</p>
                                            <p className="text-sm opacity-80">Rohan Adhikari • Online</p>
                                            <button className="mt-md text-[12px] font-bold bg-on-primary text-primary px-md py-xs rounded-full">Join Room</button>
                                        </div>
                                    </div>
                                    <div className="flex gap-lg">
                                        <div className="flex flex-col items-center">
                                            <span className="font-bold">17:30</span>
                                            <div className="w-[2px] h-10 bg-on-primary/30 my-xs"></div>
                                        </div>
                                        <div>
                                            <p className="font-bold">Thermodynamics Review</p>
                                            <p className="text-sm opacity-80">Sunita Mahat • Home Visit</p>
                                        </div>
                                    </div>
                                </div>
                                <button className="w-full mt-xl py-sm rounded-lg bg-white/10 hover:bg-white/20 transition-colors text-label-md font-bold">
                                    Manage Availability
                                </button>
                            </section>
                            {/* Profile Strength Widget */}
                            <section className="glass-card p-xl rounded-xl border border-outline-variant">
                                <h3 className="font-headline-sm text-headline-sm mb-md">Profile Performance</h3>
                                <div className="space-y-lg">
                                    <div>
                                        <div className="flex justify-between mb-xs">
                                            <span className="font-label-md text-label-md">Profile Completion</span>
                                            <span className="font-bold text-primary">85%</span>
                                        </div>
                                        <div className="w-full h-2 bg-surface-container-highest rounded-full overflow-hidden">
                                            <div className="h-full bg-primary" style={{ width: '85%' }}></div>
                                        </div>
                                    </div>
                                    <div className="p-md bg-tertiary-fixed rounded-lg">
                                        <p className="font-label-md text-on-tertiary-fixed flex items-center gap-xs">
                                            <span className="material-symbols-outlined text-[18px]" data-icon="lightbulb">lightbulb</span>
                                            Tip for today
                                        </p>
                                        <p className="text-sm text-on-tertiary-fixed-variant mt-sm">Add a short introductory video to increase booking rates by up to 40%.</p>
                                    </div>
                                    <div className="flex items-center justify-between pt-md border-t border-outline-variant/30">
                                        <div>
                                            <p className="text-outline text-label-sm">Active Students</p>
                                            <p className="font-bold text-lg">12</p>
                                        </div>
                                        <div className="text-right">
                                            <p className="text-outline text-label-sm">Hours Taught</p>
                                            <p className="font-bold text-lg">148h</p>
                                        </div>
                                    </div>
                                </div>
                            </section>
                        </div>
                    </div>
                </main>
                {/* Footer Component (Minimal for Dashboard) */}
                <footer className="ml-64 border-t border-outline-variant/30 py-xl px-xxl bg-surface-container-low">
                    <div className="max-w-container-max mx-auto flex flex-col md:flex-row justify-between items-center gap-md">
                        <p className="text-on-surface-variant text-label-md">© 2024 TutorConnect Nepal. All rights reserved.</p>
                        <div className="flex gap-xl">
                            <a className="text-on-surface-variant text-label-md hover:text-primary transition-colors" href="#">About Us</a>
                            <a className="text-on-surface-variant text-label-md hover:text-primary transition-colors" href="#">Privacy Policy</a>
                            <a className="text-on-surface-variant text-label-md hover:text-primary transition-colors" href="#">Contact Support</a>
                        </div>
                    </div>
                </footer>
                <script>{`
                    // Simple Micro-interaction for hover effects
                    document.querySelectorAll('.glass-card').forEach(card => {
                        card.addEventListener('mouseenter', () => {
                            card.style.transform = 'translateY(-4px)';
                            card.style.transition = 'transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1)';
                        });
                        card.addEventListener('mouseleave', () => {
                            card.style.transform = 'translateY(0)';
                        });
                    });

                    // Search Bar functionality (Conceptual)
                    const observer = new IntersectionObserver((entries) => {
                        entries.forEach(entry => {
                            if (entry.isIntersecting) {
                                entry.target.classList.add('opacity-100', 'translate-y-0');
                                entry.target.classList.remove('opacity-0', 'translate-y-4');
                            }
                        });
                    }, { threshold: 0.1 });

                    document.querySelectorAll('section').forEach(section => {
                        section.classList.add('transition-all', 'duration-700', 'opacity-0', 'translate-y-4');
                        observer.observe(section);
                    });
                `}</script>
            </body>
        </html>
    );
};

export default TeacherDashboard;