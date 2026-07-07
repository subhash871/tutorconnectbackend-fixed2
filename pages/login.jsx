import React from 'react';

const Login = () => {
    return (
        <html className="light" lang="en">
            <head>
                <meta charSet="utf-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>Login - TutorConnect Nepal</title>
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
                                        "on-secondary-fixed": "#07006c",
                                        "secondary-container": "#6063ee",
                                        "on-secondary-fixed-variant": "#2f2ebe",
                                        "on-error": "#ffffff",
                                        "surface-variant": "#d3e4fe",
                                        "inverse-surface": "#213145",
                                        "background": "#f8f9ff",
                                        "tertiary-fixed": "#ffdbce",
                                        "outline-variant": "#bcc9c6",
                                        "primary-fixed-dim": "#6bd8cb",
                                        "on-error-container": "#93000a",
                                        "surface-container-lowest": "#ffffff",
                                        "tertiary-fixed-dim": "#ffb59a",
                                        "surface-container-highest": "#d3e4fe",
                                        "error-container": "#ffdad6",
                                        "on-primary-fixed-variant": "#005049",
                                        "surface-container-high": "#dce9ff",
                                        "inverse-on-surface": "#eaf1ff",
                                        "error": "#ba1a1a",
                                        "primary-container": "#008378",
                                        "surface": "#f8f9ff",
                                        "on-primary-container": "#f4fffc",
                                        "surface-container-low": "#eff4ff",
                                        "on-tertiary": "#ffffff",
                                        "tertiary": "#924628",
                                        "inverse-primary": "#6bd8cb",
                                        "on-secondary": "#ffffff",
                                        "on-tertiary-fixed": "#370e00",
                                        "secondary": "#4648d4",
                                        "outline": "#6d7a77",
                                        "surface-bright": "#f8f9ff",
                                        "secondary-fixed": "#e1e0ff",
                                        "primary-fixed": "#89f5e7",
                                        "on-primary": "#ffffff",
                                        "tertiary-container": "#b05e3d",
                                        "on-surface-variant": "#3d4947",
                                        "surface-dim": "#cbdbf5",
                                        "on-primary-fixed": "#00201d",
                                        "primary": "#00685f",
                                        "on-tertiary-fixed-variant": "#773215",
                                        "on-background": "#0b1c30",
                                        "on-tertiary-container": "#fffbff",
                                        "on-surface": "#0b1c30",
                                        "surface-tint": "#006a61",
                                        "secondary-fixed-dim": "#c0c1ff",
                                        "surface-container": "#e5eeff",
                                        "on-secondary-container": "#fffbff"
                                    },
                                    borderRadius: {
                                        DEFAULT: "0.25rem",
                                        lg: "0.5rem",
                                        xl: "0.75rem",
                                        full: "9999px"
                                    },
                                    spacing: {
                                        sm: "8px",
                                        base: "8px",
                                        xl: "32px",
                                        lg: "24px",
                                        xs: "4px",
                                        md: "16px",
                                        gutter: "24px",
                                        xxl: "48px",
                                        "container-max": "1280px"
                                    },
                                    fontFamily: {
                                        "display-lg": ["Inter"],
                                        "headline-md": ["Inter"],
                                        "display-lg-mobile": ["Inter"],
                                        "headline-lg-mobile": ["Inter"],
                                        "headline-lg": ["Inter"],
                                        "body-md": ["Inter"],
                                        "body-lg": ["Inter"],
                                        "label-sm": ["Inter"],
                                        "headline-sm": ["Inter"],
                                        "label-md": ["Inter"]
                                    },
                                    fontSize: {
                                        "display-lg": ["48px", { lineHeight: "1.1", letterSpacing: "-0.02em", fontWeight: "700" }],
                                        "headline-md": ["24px", { lineHeight: "1.3", fontWeight: "600" }],
                                        "display-lg-mobile": ["36px", { lineHeight: "1.2", letterSpacing: "-0.02em", fontWeight: "700" }],
                                        "headline-lg-mobile": ["24px", { lineHeight: "1.3", fontWeight: "600" }],
                                        "headline-lg": ["32px", { lineHeight: "1.25", fontWeight: "600" }],
                                        "body-md": ["16px", { lineHeight: "1.5", fontWeight: "400" }],
                                        "body-lg": ["18px", { lineHeight: "1.6", fontWeight: "400" }],
                                        "label-sm": ["12px", { lineHeight: "1.3", fontWeight: "600" }],
                                        "headline-sm": ["20px", { lineHeight: "1.4", fontWeight: "600" }],
                                        "label-md": ["14px", { lineHeight: "1.4", letterSpacing: "0.01em", fontWeight: "500" }]
                                    }
                                }
                            }
                        }
                    `}
                </script>
                <style>{`
                    .glass-card {
                        background: rgba(255, 255, 255, 0.8);
                        backdrop-filter: blur(12px);
                        border: 1px solid rgba(226, 232, 240, 1);
                    }
                    .material-symbols-outlined {
                        font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
                    }
                `}</style>
            </head>
            <body className="bg-background text-on-background font-body-md min-h-screen flex flex-col">
                {/* TopNavBar Suppression: Auth page is task-focused, suppress per instructions */}
                <main className="flex-grow flex items-center justify-center px-md py-xxl relative overflow-hidden">
                    {/* Atmospheric Background Elements */}
                    <div className="absolute top-0 left-0 w-full h-full -z-10 opacity-30">
                        <div className="absolute top-[-10%] left-[-5%] w-[400px] h-[400px] bg-primary-fixed rounded-full blur-[100px]"></div>
                        <div className="absolute bottom-[-10%] right-[-5%] w-[400px] h-[400px] bg-secondary-fixed rounded-full blur-[100px]"></div>
                    </div>
                    {/* Login Card */}
                    <div className="w-full max-w-[480px] glass-card rounded-xl shadow-lg p-xl md:p-xxl animate-in fade-in slide-in-from-bottom-4 duration-700">
                        {/* Brand Identity */}
                        <div className="text-center mb-xl">
                            <h1 className="font-headline-lg text-headline-lg text-primary tracking-tight mb-xs">TutorConnect Nepal</h1>
                            <p className="font-body-md text-on-surface-variant">Sign in to your educational journey</p>
                        </div>
                        {/* Role Selection Tabs */}
                        <div className="flex p-xs bg-surface-container-low rounded-lg mb-xl">
                            <button className="flex-1 py-sm px-md rounded-md font-label-md transition-all duration-200 bg-primary text-on-primary shadow-sm" id="student-tab" onClick={() => switchTab('student')}>
                                Student
                            </button>
                            <button className="flex-1 py-sm px-md rounded-md font-label-md transition-all duration-200 text-on-surface-variant hover:bg-surface-container-high" id="teacher-tab" onClick={() => switchTab('teacher')}>
                                Teacher
                            </button>
                        </div>
                        {/* Login Form */}
                        <form className="space-y-lg" onSubmit={(e) => e.preventDefault()}>
                            <div className="space-y-xs">
                                <label className="font-label-md text-on-surface-variant ml-xs" htmlFor="email">Email or Phone Number</label>
                                <div className="relative">
                                    <span className="material-symbols-outlined absolute left-md top-1/2 -translate-y-1/2 text-outline">mail</span>
                                    <input className="w-full pl-[48px] pr-md py-md bg-white border border-outline-variant rounded-xl focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition-all placeholder:text-outline-variant font-body-md" id="email" placeholder="e.g. arpan@example.com" type="text" />
                                </div>
                            </div>
                            <div className="space-y-xs">
                                <div className="flex justify-between items-center ml-xs">
                                    <label className="font-label-md text-on-surface-variant" htmlFor="password">Password</label>
                                    <a className="font-label-md text-primary hover:underline transition-all" href="#">Forgot password?</a>
                                </div>
                                <div className="relative">
                                    <span className="material-symbols-outlined absolute left-md top-1/2 -translate-y-1/2 text-outline">lock</span>
                                    <input className="w-full pl-[48px] pr-md py-md bg-white border border-outline-variant rounded-xl focus:ring-2 focus:ring-primary/20 focus:border-primary outline-none transition-all placeholder:text-outline-variant font-body-md" id="password" placeholder="Enter your password" type="password" />
                                    <button className="absolute right-md top-1/2 -translate-y-1/2 text-outline hover:text-primary transition-colors" type="button">
                                        <span className="material-symbols-outlined">visibility</span>
                                    </button>
                                </div>
                            </div>
                            <div className="flex items-center gap-sm ml-xs">
                                <input className="w-5 h-5 rounded-md border-outline-variant text-primary focus:ring-primary cursor-pointer" id="remember" type="checkbox" />
                                <label className="font-body-md text-on-surface-variant cursor-pointer select-none" htmlFor="remember">Remember me for 30 days</label>
                            </div>
                            <button className="w-full py-md bg-primary text-on-primary rounded-xl font-headline-sm hover:bg-primary-container active:scale-[0.98] transition-all shadow-md mt-base">
                                Log In
                            </button>
                        </form>
                        {/* Divider */}
                        <div className="relative my-xl text-center">
                            <div className="absolute inset-0 flex items-center">
                                <div className="w-full border-t border-outline-variant"></div>
                            </div>
                            <span className="relative px-md bg-surface text-label-sm text-outline uppercase tracking-wider">Or continue with</span>
                        </div>
                        {/* Social Logins */}
                        <div className="grid grid-cols-2 gap-md">
                            <button className="flex items-center justify-center gap-sm py-md px-lg border border-outline-variant rounded-xl hover:bg-surface-container-low transition-all active:scale-95 group">
                                <img alt="Google Logo" className="w-5 h-5 object-contain" src="https://lh3.googleusercontent.com/aida-public/AB6AXuCJj5KPCEVkXRzQJBj78GJDWw8ItytL0Qyi8nP5kGaQ1FyR0MtyZHQDD3-ioonjfVIdIgfOUD3OISvJCngjMj_lzxXQfT-VpCyvl-sfPu-_pOD8fxRoT6vCNvfS53XgRRU7EumYJOI1pazrDGZi_XCN_6Q00w8xnwlhmSHbWejb1qotDmIXS4Q3jvBSx-NpBigOpINUEkrDfZj_4r1QpGibvJXUv9nq98TFdyIopeRW4rog0vRx_OFLmVovpUTBixTT_wB7UPAqxPo" />
                                <span className="font-label-md text-on-surface">Google</span>
                            </button>
                            <button className="flex items-center justify-center gap-sm py-md px-lg border border-outline-variant rounded-xl hover:bg-surface-container-low transition-all active:scale-95 group">
                                <svg className="w-5 h-5 text-[#1877F2]" fill="currentColor" viewBox="0 0 24 24">
                                    <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"></path>
                                </svg>
                                <span className="font-label-md text-on-surface">Facebook</span>
                            </button>
                        </div>
                        {/* Footer Link */}
                        <p className="text-center mt-xl font-body-md text-on-surface-variant">
                            Don't have an account? 
                            <a className="text-primary font-bold hover:underline" href="#">Sign up for free</a>
                        </p>
                    </div>
                </main>
                {/* Simple Footer for Auth Page */}
                <footer className="w-full py-xl border-t border-outline-variant/30 text-center">
                    <p className="font-label-md text-outline">© 2024 TutorConnect Nepal. All rights reserved.</p>
                    <div className="flex justify-center gap-lg mt-sm">
                        <a className="font-label-sm text-outline hover:text-primary transition-colors" href="#">Privacy Policy</a>
                        <a className="font-label-sm text-outline hover:text-primary transition-colors" href="#">Terms of Service</a>
                        <a className="font-label-sm text-outline hover:text-primary transition-colors" href="#">Support</a>
                    </div>
                </footer>
                <script>{`
                    function switchTab(role) {
                        const studentTab = document.getElementById('student-tab');
                        const teacherTab = document.getElementById('teacher-tab');
                        
                        if (role === 'student') {
                            studentTab.classList.add('bg-primary', 'text-on-primary', 'shadow-sm');
                            studentTab.classList.remove('text-on-surface-variant', 'hover:bg-surface-container-high');
                            
                            teacherTab.classList.remove('bg-primary', 'text-on-primary', 'shadow-sm');
                            teacherTab.classList.add('text-on-surface-variant', 'hover:bg-surface-container-high');
                        } else {
                            teacherTab.classList.add('bg-primary', 'text-on-primary', 'shadow-sm');
                            teacherTab.classList.remove('text-on-surface-variant', 'hover:bg-surface-container-high');
                            
                            studentTab.classList.remove('bg-primary', 'text-on-primary', 'shadow-sm');
                            studentTab.classList.add('text-on-surface-variant', 'hover:bg-surface-container-high');
                        }
                    }
                `}</script>
            </body>
        </html>
    );
};

export default Login;