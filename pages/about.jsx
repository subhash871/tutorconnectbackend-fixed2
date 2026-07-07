import React from 'react';

const AboutUs = () => {
    return (
        <html className="scroll-smooth" lang="en">
            <head>
                <meta charSet="utf-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>About Us | TutorConnect Nepal</title>
                <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
                <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet" />
                <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet" />
                <link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet" />
                <style>{`
                    .material-symbols-outlined {
                        font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
                    }
                    .glass-card {
                        background: rgba(255, 255, 255, 0.7);
                        backdrop-filter: blur(10px);
                        border: 1px solid rgba(226, 232, 240, 0.8);
                    }
                    .academic-gradient {
                        background: linear-gradient(135deg, #f8f9ff 0%, #eef4ff 100%);
                    }
                `}</style>
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
            </head>
            <body className="bg-background text-on-surface font-body-md overflow-x-hidden">
                {/* Top Navigation Bar */}
                <header className="bg-surface/80 backdrop-blur-xl docked full-width top-0 sticky z-50 border-b border-outline-variant shadow-sm">
                    <nav className="flex justify-between items-center w-full px-lg md:px-xxl py-md max-w-container-max mx-auto">
                        <div className="flex items-center gap-xl">
                            <span className="font-headline-md text-headline-md font-bold text-primary">TutorConnect Nepal</span>
                            <div className="hidden md:flex gap-lg items-center">
                                <a className="font-body-md text-body-md text-on-surface-variant hover:text-primary transition-colors" href="#">Find Tutors</a>
                                <a className="font-body-md text-body-md text-on-surface-variant hover:text-primary transition-colors" href="#">How it Works</a>
                                <a className="font-body-md text-body-md text-on-surface-variant hover:text-primary transition-colors" href="#">Categories</a>
                            </div>
                        </div>
                        <div className="flex items-center gap-md">
                            <button className="hidden md:block font-label-md text-label-md px-md py-sm rounded-xl text-primary hover:bg-surface-container-low transition-all active:scale-95">Log In</button>
                            <button className="bg-primary text-on-primary font-label-md text-label-md px-lg py-sm rounded-xl shadow-sm hover:shadow-md transition-all active:scale-95">Join as Tutor</button>
                        </div>
                    </nav>
                </header>
                <main>
                    {/* Hero Section */}
                    <section className="relative py-xxl overflow-hidden academic-gradient">
                        <div className="absolute inset-0 opacity-10 pointer-events-none">
                        </div>
                        <div className="max-w-container-max mx-auto px-lg md:px-xxl relative z-10 flex flex-col items-center text-center">
                            <span className="text-primary font-label-md text-label-md tracking-widest uppercase mb-md">Our Mission</span>
                            <h1 className="font-display-lg text-display-lg max-w-4xl text-on-background mb-lg">Empowering Nepal through Personalized Learning</h1>
                            <p className="font-body-lg text-body-lg text-on-surface-variant max-w-2xl">We bridge the gap between ambitious students and the most talented educators in Nepal, fostering a community built on academic excellence and trust.</p>
                        </div>
                    </section>
                    {/* Our Story Section */}
                    <section className="py-xxl bg-surface">
                        <div className="max-w-container-max mx-auto px-lg md:px-xxl">
                            <div className="grid grid-cols-1 lg:grid-cols-2 gap-xxl items-center">
                                <div className="relative group">
                                    <div className="absolute -inset-4 bg-primary/5 rounded-xxl blur-2xl group-hover:bg-primary/10 transition-all"></div>
                                    <img className="relative rounded-xxl shadow-lg w-full aspect-[4/3] object-cover border border-outline-variant" data-alt="A cinematic, high-quality photograph of a modern, bright study space in Kathmandu. Through a large window, the Himalayan peaks are faintly visible under a soft blue sky. The interior features warm wooden textures, neatly stacked academic books, and a clean workspace, symbolizing the blend of traditional values and modern education technology in Nepal. The lighting is soft and natural, evoking a sense of calm and focused intellect." src="https://lh3.googleusercontent.com/aida-public/AB6AXuBsSsiBE4Mh_JjGlJ2DjswuSnft66_Qm5pHX7ld_CZph_kWfHgLNWlDwf3HMZRErQ7KMtFX7Xgd9kMHwysYrWNArH1BN28Ce19x9O2XyMn0mEvMILwbnN_u7fSBHuE4X5HrfcddukbAP2ZqJCWMI9asZUECCkT_xXQx2xOCuZQ9S0-XXuJIb5-_m1_W0fAF-_8cnfWmNGmftq5DzxHBJnQSoEhXicwhw3FwozGqYbxkm3UcQ4MDHRiBWsCfWnnM6wN8zTn8LxhMcYY" />
                                </div>
                                <div className="flex flex-col gap-lg">
                                    <h2 className="font-headline-lg text-headline-lg text-on-background">Our Story</h2>
                                    <p className="font-body-md text-body-md text-on-surface-variant leading-relaxed">
                                        TutorConnect Nepal was founded with a single realization: the traditional classroom model often fails to address the unique learning pace of every student. In 2021, a group of educators and technology enthusiasts came together to solve the lack of accessible, high-quality personalized tuition across the country.
                                    </p>
                                    <p className="font-body-md text-body-md text-on-surface-variant leading-relaxed">
                                        What started as a small initiative in Kathmandu has now evolved into a nationwide platform, connecting thousands of learners with verified experts in fields ranging from STEM to fine arts and local languages.
                                    </p>
                                    <div className="grid grid-cols-2 gap-md mt-base">
                                        <div className="p-lg rounded-xl bg-surface-container-lowest border border-outline-variant">
                                            <span className="font-display-lg text-headline-lg text-primary block">5,000+</span>
                                            <span className="font-label-md text-label-md text-on-surface-variant uppercase tracking-tighter">Verified Tutors</span>
                                        </div>
                                        <div className="p-lg rounded-xl bg-surface-container-lowest border border-outline-variant">
                                            <span className="font-display-lg text-headline-lg text-primary block">15,000+</span>
                                            <span className="font-label-md text-label-md text-on-surface-variant uppercase tracking-tighter">Success Stories</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>
                    {/* Why Choose Us: Bento Grid */}
                    <section className="py-xxl bg-surface-container-low">
                        <div className="max-w-container-max mx-auto px-lg md:px-xxl">
                            <div className="text-center mb-xxl">
                                <h2 className="font-headline-lg text-headline-lg text-on-background mb-md">Why Choose TutorConnect</h2>
                                <p className="font-body-md text-body-md text-on-surface-variant max-w-xl mx-auto">We prioritize safety, affordability, and results to provide the best learning experience in the country.</p>
                            </div>
                            <div className="grid grid-cols-1 md:grid-cols-3 gap-lg">
                                {/* Feature 1 */}
                                <div className="md:col-span-2 p-xxl rounded-xxl glass-card group hover:shadow-xl transition-all duration-300">
                                    <div className="flex flex-col h-full justify-between">
                                        <div>
                                            <span className="material-symbols-outlined text-primary text-[40px] mb-lg" style={{ fontVariationSettings: "'FILL' 1" }}>verified_user</span>
                                            <h3 className="font-headline-md text-headline-md mb-md">100% Verified Tutors</h3>
                                            <p className="font-body-md text-body-md text-on-surface-variant max-w-md">Every educator on our platform undergoes a rigorous 4-step background check, including academic credential verification and teaching demos.</p>
                                        </div>
                                        <div className="mt-xl flex -space-x-4">
                                            <div className="w-12 h-12 rounded-full border-4 border-white bg-surface-dim overflow-hidden shadow-sm">
                                                <img className="w-full h-full object-cover" data-alt="A professional portrait of a male tutor in his 30s, wearing business casual attire, smiling warmly against a soft-focus library background. The image has a clean, high-end photography feel with soft lighting and natural skin tones, representing trustworthiness and expertise in the academic field." src="https://lh3.googleusercontent.com/aida-public/AB6AXuB46ni1G-40L8r53Cjy1ZTfhdB2eHMRJa_2fNFfkJbGP7_vtprLrmey8TXV4u2K9qkRwZFfn5k9amHGDL2-AsQePiP_vBvmJA44qxYQMgjMmKySAQHyizoj0glMS_flOK-LrAnEGuV2G6bbVjdzM2jMeKxXbcjkW70KNzrghdcmtN9gjU7ChKs_AsX3hIW1tRjH8k5ptENtTWJqtD1sajLos6a3sU8a9zl0MfmAG7jTRUdM3jQWoQp3zN9afeTwCARJCU4wjH7XEIg" />
                                            </div>
                                            <div className="w-12 h-12 rounded-full border-4 border-white bg-surface-dim overflow-hidden shadow-sm">
                                                <img className="w-full h-full object-cover" data-alt="A professional portrait of a female science educator in her 40s, wearing professional attire and glasses, with a bright and encouraging expression. Behind her is a modern classroom setting with subtle scientific diagrams, illuminated by soft studio lighting. The aesthetic is clean and institutional, conveying reliability and academic authority." src="https://lh3.googleusercontent.com/aida-public/AB6AXuBR66109GF7PuaWlIhP--p40E6_xXAFp1sOjWPHyuoZk0vZjSeb5odRXi3QY5kissFp0sqEYPcZAtlvamsAvunqwObGUkoWm9wEXlEclq2FKT6_wCLYZslPNxBpmH-6ltIHsVv6f2stq_b6oeg7POYQRp6oeEfRAIh_1s02M1-XULaAsLMXQkfywr5Vmm5sONmibQWYiDtD_qKHrw8jMb-VL8F-mwYN9ZYSoDvmQNADs6efgCJBM28SJ8ULN7vcUBCLVYUnaqgxAFQ" />
                                            </div>
                                            <div className="w-12 h-12 rounded-full border-4 border-white bg-surface-dim overflow-hidden shadow-sm">
                                                <img className="w-full h-full object-cover" data-alt="A close-up portrait of a young male math tutor in his 20s, with a friendly and approachable look. He is wearing a clean white shirt, standing against a minimalist light blue wall. The lighting is crisp and modern, emphasizing clarity and professionalism suitable for a premium educational platform." src="https://lh3.googleusercontent.com/aida-public/AB6AXuASEAOj5QOIIMqgC9FdfNUaqvb5o_ehFu6Eg1Kga-PanSu7b52-yqmJ3jlPpzCUbPBjJNZlSG-mQLVPAnwOL6IQDe3n6UGqibv4w_V49yJLs7jyf25eyQuOpa8OZ-k3_A_3n_8rDU_zfJflC7Zj5vXJXgRSXqqKLHrVkK8-5k2xzMjISDYBsvlno9Z2TBr99VuEtvrVTAiuEob71zpgCxhQYnBIflUGiRLpRvHZwHobCxuLl9ehgUd9lWEXw7szMv-RjIGN-o6H96U" />
                                            </div>
                                            <div className="w-12 h-12 rounded-full border-4 border-white bg-primary-container flex items-center justify-center text-on-primary-container font-label-md text-label-md">+5k</div>
                                        </div>
                                    </div>
                                </div>
                                {/* Feature 2 */}
                                <div className="p-xl rounded-xxl bg-primary-container text-on-primary-container flex flex-col justify-center items-center text-center shadow-lg group hover:scale-[1.02] transition-all">
                                    <span className="material-symbols-outlined text-[64px] mb-lg" style={{ fontVariationSettings: "'FILL' 1" }}>payments</span>
                                    <h3 className="font-headline-md text-headline-md mb-md">Affordable Pricing</h3>
                                    <p className="font-body-md text-body-md opacity-90">Education should be accessible. Find tutors that fit your budget without compromising on quality.</p>
                                </div>
                                {/* Feature 3 */}
                                <div className="p-xl rounded-xxl bg-surface-container-highest border border-outline-variant flex flex-col items-start hover:bg-white transition-colors duration-300">
                                    <span className="material-symbols-outlined text-secondary text-[40px] mb-lg">calendar_month</span>
                                    <h3 className="font-headline-sm text-headline-sm mb-md">Flexible Modes</h3>
                                    <p className="font-body-md text-body-md text-on-surface-variant mb-xl">Choose between in-person home tuition or interactive online sessions that fit your busy schedule.</p>
                                    <button className="mt-auto text-primary font-label-md text-label-md flex items-center gap-xs hover:gap-sm transition-all">
                                        Learn more <span className="material-symbols-outlined text-[18px]">arrow_forward</span>
                                    </button>
                                </div>
                                {/* Feature 4 */}
                                <div className="md:col-span-2 p-xl rounded-xxl bg-surface-container-highest border border-outline-variant flex items-center gap-xl overflow-hidden group">
                                    <div className="flex-1">
                                        <h3 className="font-headline-sm text-headline-sm mb-md">Tutor matching AI</h3>
                                        <p className="font-body-md text-body-md text-on-surface-variant">Our smart matching algorithm pairs students with tutors based on learning style, language preference, and academic goals.</p>
                                    </div>
                                    <div className="w-48 h-full hidden lg:block opacity-40 group-hover:opacity-100 transition-opacity">
                                    </div>
                                </div>
                            </div>
                        </div>
                    </section>
                    {/* Leadership Team */}
                    <section className="py-xxl bg-surface">
                        <div className="max-w-container-max mx-auto px-lg md:px-xxl">
                            <div className="mb-xxl max-w-2xl">
                                <h2 className="font-headline-lg text-headline-lg text-on-background mb-md">The Visionaries</h2>
                                <p className="font-body-md text-body-md text-on-surface-variant">Our leadership team brings together decades of experience in Nepalese education and global technology standards.</p>
                            </div>
                            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-lg">
                                {/* Team Member 1 */}
                                <div className="flex flex-col group">
                                    <div className="relative overflow-hidden rounded-xxl mb-md aspect-[3/4]">
                                        <img className="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-500 scale-100 group-hover:scale-110" data-alt="A high-end executive portrait of a male CEO in his 40s, wearing a tailored navy blazer and a subtle smile. He is standing in a modern office with large windows overlooking the city of Kathmandu at dusk. The lighting is dramatic yet professional, focusing on his determined expression. The overall style is clean, corporate, and inspires confidence and leadership." src="https://lh3.googleusercontent.com/aida-public/AB6AXuAHtpHMUP8wka1yggR9q9mPcPeni89Jtg_xWRaTxBNz1W8WJ6WNher0e84hoGmMaFQ-EgBSK1rvDdoiP1SvajMeMLa9f1IoowNxBG4O2KKhokLMognFCHFppLek9nP1ezJVdgWnapWSwCMizHbHwjar7D8WC_FcHcbvxYb4x9By5MekqWaK7pJHWDX0OL3LB1VFB0mt_Tlnh45FIpNdS0VKJhEOJu7b-cjTbGk5QDDJuqyqWTXeJd7yuJ_IO0WYH_15oz-Fiit6yfo" />
                                        <div className="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent opacity-0 group-hover:opacity-100 transition-opacity"></div>
                                    </div>
                                    <h4 className="font-headline-sm text-headline-sm text-on-background">Dr. Arpan Sharma</h4>
                                    <p className="font-label-md text-label-md text-primary uppercase tracking-wider">Founder & CEO</p>
                                </div>
                                {/* Team Member 2 */}
                                <div className="flex flex-col group">
                                    <div className="relative overflow-hidden rounded-xxl mb-md aspect-[3/4]">
                                        <img className="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-500 scale-100 group-hover:scale-110" data-alt="A professional headshot of a female Chief Operating Officer in her late 30s, looking intelligent and focused. She is wearing elegant professional attire and is posed in a contemporary workspace with bright, even studio lighting. The background is a clean white wall with a hint of a green plant, symbolizing growth and fresh perspectives in education." src="https://lh3.googleusercontent.com/aida-public/AB6AXuBL-faMnFg6zdhDwi2WcKDD33fm8a-68nPBxEAjuTVYB-sf97ms_J_H817biNyTbJAihR0KdzkI7sXlxLOAcFaajHtbn8wEgd1SuwQU9Z9lW2MBQujcLnK_2tlx0Sw3hYP7YQNWOE-ZO1OpIo5VQ8RoNjRVk3UvTxPOCKfJmUr5aTHdpVU8VQZhLw1D1ALvRzpzyjIhCMTiSlrcBDQBATfaFnWCoG9BUNgJmKyRhMXkFSqvLdbCo5gSa3QqVb17w5YGOcu8Ubpdz2k" />
                                    </div>
                                    <h4 className="font-headline-sm text-headline-sm text-on-background">Megha Rajbhandari</h4>
                                    <p className="font-label-md text-label-md text-primary uppercase tracking-wider">Head of Academics</p>
                                </div>
                                {/* Team Member 3 */}
                                <div className="flex flex-col group">
                                    <div className="relative overflow-hidden rounded-xxl mb-md aspect-[3/4]">
                                        <img className="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-500 scale-100 group-hover:scale-110" data-alt="A professional portrait of a male CTO in his early 30s, featuring a modern tech-entrepreneur look. He is wearing a minimalist dark sweater and standing in front of a subtly glowing screen showing complex code or data visualizations. The lighting is cool-toned and futuristic, reflecting a commitment to innovation and cutting-edge educational technology." src="https://lh3.googleusercontent.com/aida-public/AB6AXuAJjHIdSWPY2eYtsLGn4lz8HhmfE8DVm6dGyjWJCS_tkrzNpx5Vq5dLEeO_mPIlmYdfceFs-eVFzPZPU_MvwOvAZpd4lPDR8sbavX6BEtcl_CksXAuWAOKUvf4Q3yVSnDP_Jo_Dm06ybWGp6gqtRRndH2wi1KPLAv1vJ8tgC7WGjI5FzMS38m4LHI9WERmNczRDwYeppNvgCPO11Twf_X5C3hnetpN7VJwn6UX55w08fr4VcE9gQ4CJY0BiKVeRpwVZX7G61ELW_FQ" />
                                    </div>
                                    <h4 className="font-headline-sm text-headline-sm text-on-background">Sujan K.C.</h4>
                                    <p className="font-label-md text-label-md text-primary uppercase tracking-wider">Chief Technology Officer</p>
                                </div>
                                {/* Team Member 4 */}
                                <div className="flex flex-col group">
                                    <div className="relative overflow-hidden rounded-xxl mb-md aspect-[3/4]">
                                        <img className="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all duration-500 scale-100 group-hover:scale-110" data-alt="A portrait of a senior female educator acting as a Strategic Advisor, with a wise and kind appearance. She is wearing traditional yet professional Nepalese attire, sitting in a room filled with books and artifacts. The lighting is warm and golden, conveying a sense of heritage, wisdom, and deep-rooted knowledge in the Nepalese educational landscape." src="https://lh3.googleusercontent.com/aida-public/AB6AXuCpo68mCLYrU8XNWytr0YcZaXV6yzAqryJ9IPQXq__R8k2qtF9BgXQ6aag6CkLVT4IzZU3DgkcgmKhOokltDPav0sqapuIl_rf4npdySRnj31udPZuulJkUtMxAitrpudoObbly0O39zHc3G-AELylU8NTK_qC3Wq9DdTwbNqVvjzbV5ew8QinFj_0WbIiXYwKSFSal00cZ0zJJgfxG2hdRMp7tHirMFOCSuLpAd1KJ3_N0sRJMjYS_l-WO3iybSHatfzyVdskLXeQ" />
                                    </div>
                                    <h4 className="font-headline-sm text-headline-sm text-on-background">Prof. Binita Shah</h4>
                                    <p className="font-label-md text-label-md text-primary uppercase tracking-wider">Strategic Advisor</p>
                                </div>
                            </div>
                        </div>
                    </section>
                    {/* Call to Action */}
                    <section className="py-xxl px-lg md:px-xxl">
                        <div className="max-w-container-max mx-auto bg-primary rounded-[32px] p-xl md:p-xxl relative overflow-hidden text-center">
                            <div className="absolute inset-0 opacity-20 pointer-events-none">
                            </div>
                            <div className="relative z-10">
                                <h2 className="font-display-lg text-display-lg text-on-primary mb-lg">Ready to start your journey?</h2>
                                <p className="font-body-lg text-body-lg text-on-primary/80 mb-xxl max-w-xl mx-auto">Join the thousands of students already achieving their dreams with TutorConnect Nepal.</p>
                                <div className="flex flex-col sm:flex-row gap-md justify-center">
                                    <button className="bg-on-primary text-primary font-headline-sm text-headline-sm px-xxl py-md rounded-xl hover:shadow-xl transition-all active:scale-95">Find a Tutor</button>
                                    <button className="border border-on-primary/30 text-on-primary font-headline-sm text-headline-sm px-xxl py-md rounded-xl hover:bg-on-primary/10 transition-all active:scale-95">Become a Partner</button>
                                </div>
                            </div>
                        </div>
                    </section>
                </main>
                {/* Footer */}
                <footer className="bg-surface-container-highest w-full border-t border-outline-variant">
                    <div className="grid grid-cols-1 md:grid-cols-4 gap-xl px-lg md:px-xxl py-xxl max-w-container-max mx-auto">
                        <div className="col-span-1 md:col-span-1">
                            <span className="font-headline-md text-headline-md font-bold text-primary mb-lg block">TutorConnect Nepal</span>
                            <p className="font-body-md text-body-md text-on-surface-variant mb-lg">
                                Elevating the standard of tuition in Nepal through quality, verification, and technology.
                            </p>
                            <div className="flex gap-md">
                                <a className="text-on-surface-variant hover:text-primary" href="#"><span className="material-symbols-outlined">public</span></a>
                                <a className="text-on-surface-variant hover:text-primary" href="#"><span className="material-symbols-outlined">mail</span></a>
                                <a className="text-on-surface-variant hover:text-primary" href="#"><span className="material-symbols-outlined">alternate_email</span></a>
                            </div>
                        </div>
                        <div>
                            <h5 className="font-label-md text-label-md text-on-surface font-bold mb-lg uppercase tracking-wider">Company</h5>
                            <ul className="space-y-sm">
                                <li><a className="text-on-surface-variant font-body-md text-body-md hover:text-primary underline transition-opacity" href="#">About Us</a></li>
                                <li><a className="text-on-surface-variant font-body-md text-body-md hover:text-primary transition-opacity" href="#">Safety Guide</a></li>
                                <li><a className="text-on-surface-variant font-body-md text-body-md hover:text-primary transition-opacity" href="#">Contact Support</a></li>
                            </ul>
                        </div>
                        <div>
                            <h5 className="font-label-md text-label-md text-on-surface font-bold mb-lg uppercase tracking-wider">Legal</h5>
                            <ul className="space-y-sm">
                                <li><a className="text-on-surface-variant font-body-md text-body-md hover:text-primary transition-opacity" href="#">Privacy Policy</a></li>
                                <li><a className="text-on-surface-variant font-body-md text-body-md hover:text-primary transition-opacity" href="#">Terms of Service</a></li>
                            </ul>
                        </div>
                        <div>
                            <h5 className="font-label-md text-label-md text-on-surface font-bold mb-lg uppercase tracking-wider">Newsletter</h5>
                            <p className="font-body-md text-body-md text-on-surface-variant mb-md">Get educational tips and platform updates.</p>
                            <div className="flex gap-xs">
                                <input className="bg-surface-container-low border border-outline-variant rounded-lg px-md py-sm w-full focus:ring-2 focus:ring-primary focus:border-primary" placeholder="Email address" type="email" />
                                <button className="bg-primary text-on-primary p-sm rounded-lg hover:bg-primary/90 transition-all">
                                    <span className="material-symbols-outlined">send</span>
                                </button>
                            </div>
                        </div>
                    </div>
                    <div className="border-t border-outline-variant py-lg px-lg md:px-xxl max-w-container-max mx-auto text-center">
                        <p className="font-body-md text-body-md text-on-surface-variant opacity-90">© 2024 TutorConnect Nepal. All rights reserved.</p>
                    </div>
                </footer>
                <script>{`
                    // Micro-interaction: Header scroll effect
                    window.addEventListener('scroll', () => {
                        const header = document.querySelector('header');
                        if (window.scrollY > 20) {
                            header.classList.add('shadow-md');
                            header.classList.remove('shadow-sm');
                        } else {
                            header.classList.add('shadow-sm');
                            header.classList.remove('shadow-md');
                        }
                    });

                    // Hover effect for team images: add a subtle float
                    document.querySelectorAll('.group').forEach(el => {
                        el.addEventListener('mouseenter', () => {
                            const img = el.querySelector('img');
                            if(img) img.style.transform = 'scale(1.05) translateY(-4px)';
                        });
                        el.addEventListener('mouseleave', () => {
                            const img = el.querySelector('img');
                            if(img) img.style.transform = 'scale(1) translateY(0)';
                        });
                    });
                `}</script>
            </body>
        </html>
    );
};

export default AboutUs;