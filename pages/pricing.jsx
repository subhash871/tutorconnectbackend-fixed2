import React, { useState } from 'react';

const Pricing = () => {
    const [activeFaq, setActiveFaq] = useState(null);

    const toggleFaq = (index) => {
        setActiveFaq(activeFaq === index ? null : index);
    };

    return (
        <html className="light" lang="en">
            <head>
                <meta charSet="utf-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>Pricing & Value | TutorConnect Nepal</title>
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
                    .material-symbols-outlined {
                        font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
                    }
                    .glass-card {
                        background: rgba(255, 255, 255, 0.7);
                        backdrop-filter: blur(12px);
                        border: 1px solid rgba(226, 232, 240, 0.8);
                    }
                    .bento-hover {
                        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
                    }
                    .bento-hover:hover {
                        transform: translateY(-4px);
                        box-shadow: 0 8px 24px rgba(0, 104, 95, 0.08);
                    }
                `}</style>
            </head>
            <body className="bg-background text-on-background font-body-md selection:bg-primary-fixed-dim selection:text-on-primary-fixed">
                {/* Top Navigation Bar */}
                <header className="docked full-width top-0 sticky z-50 bg-surface/80 backdrop-blur-xl border-b border-outline-variant shadow-sm transition-all duration-300" id="main-nav">
                    <div className="flex justify-between items-center w-full px-lg md:px-xxl py-md max-w-container-max mx-auto">
                        <div className="flex items-center gap-xl">
                            <a className="font-headline-md text-headline-md font-bold text-primary" href="#">TutorConnect Nepal</a>
                            <nav className="hidden md:flex gap-lg">
                                <a className="font-body-md text-body-md text-on-surface-variant hover:text-primary transition-colors" href="#">Find Tutors</a>
                                <a className="font-body-md text-body-md text-on-surface-variant hover:text-primary transition-colors" href="#">How it Works</a>
                                <a className="font-body-md text-body-md text-on-surface-variant hover:text-primary transition-colors" href="#">Categories</a>
                            </nav>
                        </div>
                        <div className="flex items-center gap-md">
                            <button className="hidden md:block font-body-md text-body-md text-on-surface-variant hover:text-primary transition-colors px-md">Log In</button>
                            <button className="bg-primary-container text-on-primary-container px-lg py-sm rounded-xl font-label-md text-label-md active:scale-95 transition-all duration-150 hover:shadow-lg">Join as Tutor</button>
                        </div>
                    </div>
                </header>
                <main className="max-w-container-max mx-auto px-md md:px-xxl py-xxl">
                    {/* Hero Section */}
                    <section className="text-center mb-xxl max-w-3xl mx-auto">
                        <span className="bg-primary-fixed text-on-primary-fixed px-md py-xs rounded-full font-label-sm text-label-sm uppercase tracking-wider mb-md inline-block">Transparent Pricing</span>
                        <h1 className="font-display-lg text-display-lg md:text-display-lg mb-md text-on-surface">Investing in Knowledge, <span className="text-primary">Without the Guesswork.</span></h1>
                        <p className="font-body-lg text-body-lg text-on-surface-variant">Simple, fair, and secure. We believe in empowering Nepal's academic community through a platform where value comes first.</p>
                    </section>
                    {/* Pricing Bento Grid */}
                    <div className="grid grid-cols-1 md:grid-cols-12 gap-lg mb-xxl">
                        {/* Tutor Proposition (The Large Card) */}
                        <div className="md:col-span-8 glass-card rounded-[24px] p-xl flex flex-col justify-between overflow-hidden relative bento-hover border-primary/10">
                            <div className="absolute top-0 right-0 w-64 h-64 bg-primary-fixed/20 blur-[100px] -mr-32 -mt-32"></div>
                            <div>
                                <div className="flex items-center gap-sm mb-lg">
                                    <span className="material-symbols-outlined text-primary text-[32px]">school</span>
                                    <h2 className="font-headline-lg text-headline-lg text-on-surface">For Tutors</h2>
                                </div>
                                <div className="grid md:grid-cols-2 gap-xl">
                                    <div className="space-y-md">
                                        <div className="flex flex-col">
                                            <span className="text-[56px] font-black text-primary leading-none">Free</span>
                                            <span className="font-label-md text-label-md text-on-surface-variant">to join and create profile</span>
                                        </div>
                                        <p className="text-on-surface-variant font-body-md">Start your digital teaching journey without any upfront costs. Only pay when you earn.</p>
                                        <ul className="space-y-sm">
                                            <li className="flex items-center gap-sm">
                                                <span className="material-symbols-outlined text-primary-container text-sm">check_circle</span>
                                                <span className="text-on-surface font-body-md">Customized teaching schedule</span>
                                            </li>
                                            <li className="flex items-center gap-sm">
                                                <span className="material-symbols-outlined text-primary-container text-sm">check_circle</span>
                                                <span className="text-on-surface font-body-md">Global visibility across Nepal</span>
                                            </li>
                                            <li className="flex items-center gap-sm">
                                                <span className="material-symbols-outlined text-primary-container text-sm">check_circle</span>
                                                <span className="text-on-surface font-body-md">Integrated student management</span>
                                            </li>
                                        </ul>
                                    </div>
                                    <div className="bg-surface-container-low rounded-xl p-lg border border-outline-variant/30 flex flex-col justify-center">
                                        <h3 className="font-headline-sm text-headline-sm text-on-surface mb-sm">10% Platform Fee</h3>
                                        <p className="text-on-surface-variant font-body-md mb-lg">A small commission on successful bookings to keep the platform running smoothly for everyone.</p>
                                        <div className="flex items-baseline gap-xs">
                                            <span className="text-on-surface-variant font-label-sm">Example:</span>
                                            <span className="text-on-surface font-bold">Earn रू1000 → Keep रू900</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div className="mt-xl flex items-center gap-md">
                                <button className="bg-primary text-on-primary px-xl py-md rounded-xl font-label-md text-label-md hover:bg-primary-container active:scale-95 transition-all shadow-md">Become a Tutor</button>
                                <a className="text-primary font-label-md underline hover:text-primary-container" href="#">Learn more about payouts</a>
                            </div>
                        </div>
                        {/* Student Proposition (The Vertical Card) */}
                        <div className="md:col-span-4 bg-secondary-container rounded-[24px] p-xl text-on-secondary-container flex flex-col bento-hover shadow-xl">
                            <div className="mb-xl">
                                <div className="flex items-center gap-sm mb-lg">
                                    <span className="material-symbols-outlined text-on-primary-container text-[32px]">person_search</span>
                                    <h2 className="font-headline-lg text-headline-lg">For Students</h2>
                                </div>
                                <div className="mb-xl">
                                    <div className="text-[56px] font-black leading-none mb-xs"> रू0</div>
                                    <div className="font-label-md">Platform fees for students</div>
                                </div>
                                <p className="opacity-90 font-body-md mb-xl">Students pay exactly what the tutor lists. No hidden convenience fees or service charges at checkout.</p>
                                <div className="space-y-lg">
                                    <div className="flex gap-md">
                                        <span className="material-symbols-outlined">verified_user</span>
                                        <div>
                                            <p className="font-bold">No Hidden Fees</p>
                                            <p className="text-sm opacity-80">What you see on the profile is what you pay.</p>
                                        </div>
                                    </div>
                                    <div className="flex gap-md">
                                        <span className="material-symbols-outlined">account_balance_wallet</span>
                                        <div>
                                            <p className="font-bold">Secure Escrow</p>
                                            <p className="text-sm opacity-80">Funds are held until the lesson is completed.</p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div className="mt-auto">
                                <button className="w-full bg-surface-container-lowest text-secondary font-label-md py-md rounded-xl hover:bg-white transition-colors">Browse Tutors</button>
                            </div>
                        </div>
                    </div>
                    {/* Value Propositions Grid */}
                    <section className="grid grid-cols-1 md:grid-cols-3 gap-xl mb-xxl">
                        <div className="flex flex-col gap-md p-lg border border-outline-variant rounded-xl bento-hover bg-surface">
                            <div className="w-12 h-12 bg-primary-fixed rounded-lg flex items-center justify-center">
                                <span className="material-symbols-outlined text-primary" data-weight="fill">verified</span>
                            </div>
                            <h3 className="font-headline-sm text-headline-sm text-on-surface">Verified Tutors</h3>
                            <p className="text-on-surface-variant font-body-md">Every educator on our platform undergoes a rigorous identity and academic credential verification process for your peace of mind.</p>
                        </div>
                        <div className="flex flex-col gap-md p-lg border border-outline-variant rounded-xl bento-hover bg-surface">
                            <div className="w-12 h-12 bg-primary-fixed rounded-lg flex items-center justify-center">
                                <span className="material-symbols-outlined text-primary" data-weight="fill">shield_person</span>
                            </div>
                            <h3 className="font-headline-sm text-headline-sm text-on-surface">Secure Escrow</h3>
                            <p className="text-on-surface-variant font-body-md">Our integrated payment system protects both parties. We hold the payment and only release it once the session is marked successful.</p>
                        </div>
                        <div className="flex flex-col gap-md p-lg border border-outline-variant rounded-xl bento-hover bg-surface">
                            <div className="w-12 h-12 bg-primary-fixed rounded-lg flex items-center justify-center">
                                <span className="material-symbols-outlined text-primary" data-weight="fill">support_agent</span>
                            </div>
                            <h3 className="font-headline-sm text-headline-sm text-on-surface">24/7 Support</h3>
                            <p className="text-on-surface-variant font-body-md">From booking issues to payment queries, our dedicated Nepali support team is available around the clock to assist you.</p>
                        </div>
                    </section>
                    {/* FAQ Micro-Interaction Section */}
                    <section className="max-w-3xl mx-auto mb-xxl">
                        <h2 className="font-headline-lg text-headline-lg text-center mb-xl">Frequently Asked Questions</h2>
                        <div className="space-y-md">
                            <div className="faq-item border border-outline-variant rounded-xl overflow-hidden bg-white">
                                <button className="w-full flex justify-between items-center p-lg text-left" onClick={() => toggleFaq(0)}>
                                    <span className="font-label-md text-on-surface">When do tutors get paid?</span>
                                    <span className="material-symbols-outlined text-outline transition-transform duration-200" style={{ transform: activeFaq === 0 ? 'rotate(180deg)' : 'rotate(0deg)' }}>expand_more</span>
                                </button>
                                <div className="faq-content" style={{ height: activeFaq === 0 ? 'auto' : '0px', overflow: 'hidden', transition: 'all 0.3s ease' }}>
                                    <p className="px-lg pb-lg text-on-surface-variant">Tutors receive their earnings immediately after the student confirms the session completion or 24 hours after the scheduled time if no dispute is raised.</p>
                                </div>
                            </div>
                            <div className="faq-item border border-outline-variant rounded-xl overflow-hidden bg-white">
                                <button className="w-full flex justify-between items-center p-lg text-left" onClick={() => toggleFaq(1)}>
                                    <span className="font-label-md text-on-surface">Are there any monthly subscription fees?</span>
                                    <span className="material-symbols-outlined text-outline transition-transform duration-200" style={{ transform: activeFaq === 1 ? 'rotate(180deg)' : 'rotate(0deg)' }}>expand_more</span>
                                </button>
                                <div className="faq-content" style={{ height: activeFaq === 1 ? 'auto' : '0px', overflow: 'hidden', transition: 'all 0.3s ease' }}>
                                    <p className="px-lg pb-lg text-on-surface-variant">No, TutorConnect Nepal operates on a per-booking basis. There are no monthly maintenance or subscription fees for either students or tutors.</p>
                                </div>
                            </div>
                            <div className="faq-item border border-outline-variant rounded-xl overflow-hidden bg-white">
                                <button className="w-full flex justify-between items-center p-lg text-left" onClick={() => toggleFaq(2)}>
                                    <span className="font-label-md text-on-surface">What payment methods are supported in Nepal?</span>
                                    <span className="material-symbols-outlined text-outline transition-transform duration-200" style={{ transform: activeFaq === 2 ? 'rotate(180deg)' : 'rotate(0deg)' }}>expand_more</span>
                                </button>
                                <div className="faq-content" style={{ height: activeFaq === 2 ? 'auto' : '0px', overflow: 'hidden', transition: 'all 0.3s ease' }}>
                                    <p className="px-lg pb-lg text-on-surface-variant">We support all major Nepali payment gateways including eSewa, Khalti, ConnectIPS, and direct Bank Transfers for seamless transactions.</p>
                                </div>
                            </div>
                        </div>
                    </section>
                    {/* CTA Section */}
                    <section className="bg-primary text-on-primary rounded-[32px] p-xl md:p-xxl flex flex-col md:flex-row items-center justify-between gap-xl relative overflow-hidden">
                        <div className="absolute inset-0 opacity-10 pointer-events-none">
                            <div className="absolute top-0 left-0 w-96 h-96 bg-white blur-[80px] -ml-48 -mt-48"></div>
                            <div className="absolute bottom-0 right-0 w-96 h-96 bg-secondary blur-[100px] -mr-48 -mb-48"></div>
                        </div>
                        <div className="relative z-10 max-w-xl">
                            <h2 className="font-display-lg-mobile md:text-headline-lg font-bold mb-md">Ready to share your knowledge?</h2>
                            <p className="font-body-md opacity-90 mb-lg">Join over 2,000+ verified tutors across Nepal and start earning today. Setting up your profile takes less than 5 minutes.</p>
                            <div className="flex flex-wrap gap-md">
                                <button className="bg-white text-primary px-xl py-md rounded-xl font-label-md hover:shadow-xl transition-all active:scale-95">Get Started as Tutor</button>
                                <button className="border border-white text-white px-xl py-md rounded-xl font-label-md hover:bg-white/10 transition-all">Schedule a Demo</button>
                            </div>
                        </div>
                        <div className="relative z-10 w-full md:w-1/3 aspect-square rounded-2xl overflow-hidden shadow-2xl">
                            <img className="w-full h-full object-cover" data-alt="A professional Nepali educator smiling warmly in a bright, modern home office setting, wearing professional attire. The lighting is soft and natural, emphasizing a light-mode academic aesthetic with primary teal accents in the background. The style is high-quality commercial photography, evoking trust, competence, and pedagogical excellence." src="https://lh3.googleusercontent.com/aida-public/AB6AXuAwckqH-TFEIltqCwCAbMZgYPv0xWe2S6UkJx-jOrWuc4gsGan-KxQH8ePMThwKAqun3wqVsHu3h3OOsv9xBMfRhG1y2IHbqcT8OngsikhXDC_wk9U_DtGXqxoZePKVP33i10bHEOMFrh4hleXnB3Z28ZA6B0J5hvYeXtaEhOT0Gcc07Xacrvu3TfP6GVMpdNdfCBn5QnUOgUXJTzMwBk4iMv9pBQ6PT1pte0PaM29Q4Re-cab2-BFi7leSPesJpDuFw_XRJJMkyOI" />
                        </div>
                    </section>
                </main>
                <footer className="w-full bg-surface-container-highest border-t border-outline-variant">
                    <div className="grid grid-cols-1 md:grid-cols-4 gap-xl px-lg md:px-xxl py-xxl max-w-container-max mx-auto">
                        <div className="space-y-md">
                            <div className="font-headline-md text-headline-md font-bold text-primary">TutorConnect Nepal</div>
                            <p className="text-on-surface-variant font-body-md">Empowering the next generation of Nepali scholars through accessible, quality education.</p>
                        </div>
                        <div>
                            <h4 className="font-label-md mb-lg text-on-surface">Platform</h4>
                            <ul className="space-y-sm text-on-surface-variant font-body-md">
                                <li><a className="hover:text-primary transition-colors" href="#">Find Tutors</a></li>
                                <li><a className="hover:text-primary transition-colors" href="#">Become a Tutor</a></li>
                                <li><a className="hover:text-primary transition-colors" href="#">Subject Categories</a></li>
                                <li><a className="hover:text-primary transition-colors" href="#">Safety Guide</a></li>
                            </ul>
                        </div>
                        <div>
                            <h4 className="font-label-md mb-lg text-on-surface">Company</h4>
                            <ul className="space-y-sm text-on-surface-variant font-body-md">
                                <li><a className="hover:text-primary transition-colors" href="#">About Us</a></li>
                                <li><a className="hover:text-primary transition-colors" href="#">Careers</a></li>
                                <li><a className="hover:text-primary transition-colors" href="#">Privacy Policy</a></li>
                                <li><a className="hover:text-primary transition-colors" href="#">Terms of Service</a></li>
                            </ul>
                        </div>
                        <div>
                            <h4 className="font-label-md mb-lg text-on-surface">Connect</h4>
                            <div className="flex gap-md mb-lg">
                                <a className="w-10 h-10 bg-surface-container rounded-full flex items-center justify-center hover:bg-primary-container hover:text-on-primary-container transition-all" href="#">
                                    <span className="material-symbols-outlined text-sm">alternate_email</span>
                                </a>
                                <a className="w-10 h-10 bg-surface-container rounded-full flex items-center justify-center hover:bg-primary-container hover:text-on-primary-container transition-all" href="#">
                                    <span className="material-symbols-outlined text-sm">public</span>
                                </a>
                            </div>
                            <p className="text-on-surface-variant font-label-sm">© 2024 TutorConnect Nepal. All rights reserved.</p>
                        </div>
                    </div>
                </footer>
                <script>{`
                    function toggleFaq(button, index) {
                        const content = button.nextElementSibling;
                        const icon = button.querySelector('.material-symbols-outlined');
                        
                        if (content.style.height === 'auto') {
                            content.style.height = '0px';
                            icon.style.transform = 'rotate(0deg)';
                        } else {
                            // Close all other FAQs
                            document.querySelectorAll('.faq-content').forEach(el => {
                                el.style.height = '0px';
                            });
                            document.querySelectorAll('.faq-item .material-symbols-outlined').forEach(i => {
                                i.style.transform = 'rotate(0deg)';
                            });

                            content.style.height = 'auto';
                            icon.style.transform = 'rotate(180deg)';
                        }
                    }

                    // Navbar scroll effect
                    window.addEventListener('scroll', () => {
                        const nav = document.getElementById('main-nav');
                        if (window.scrollY > 20) {
                            nav.classList.add('py-sm', 'shadow-md');
                            nav.classList.remove('py-md', 'shadow-sm');
                        } else {
                            nav.classList.add('py-md', 'shadow-sm');
                            nav.classList.remove('py-sm', 'shadow-md');
                        }
                    });
                `}</script>
            </body>
        </html>
    );
};

export default Pricing;