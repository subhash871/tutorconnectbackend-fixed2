import React, { useState } from 'react';

const BookTeacher = () => {
    const [selectedPayment, setSelectedPayment] = useState('esewa');

    return (
        <html className="light" lang="en">
            <head>
                <meta charSet="utf-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>Secure Checkout | TutorConnect Nepal</title>
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
                    .checkout-card {
                        border: 1px solid #E2E8F0;
                        box-shadow: 0 4px 6px -1px rgba(0, 104, 95, 0.04);
                        transition: all 0.3s ease;
                    }
                    .glass-header {
                        backdrop-filter: blur(12px);
                        -webkit-backdrop-filter: blur(12px);
                    }
                `}</style>
            </head>
            <body className="bg-background text-on-background font-body-md min-h-screen">
                {/* Top Navigation (Shell suppressed for Transactional focus as per rule) */}
                <header className="sticky top-0 z-50 glass-header bg-surface/80 border-b border-outline-variant/30">
                    <div className="max-w-container-max mx-auto px-lg md:px-xxl py-md flex justify-between items-center">
                        <div className="flex items-center gap-sm">
                            <span className="material-symbols-outlined text-primary text-3xl">school</span>
                            <h1 className="font-headline-md text-headline-md font-bold text-primary">TutorConnect Nepal</h1>
                        </div>
                        <div className="flex items-center gap-md">
                            <span className="hidden md:flex items-center gap-xs text-on-surface-variant font-label-md">
                                <span className="material-symbols-outlined text-sm" style={{ fontVariationSettings: "'FILL' 1" }}>lock</span>
                                Secure 256-bit SSL Connection
                            </span>
                            <button className="flex items-center gap-xs text-outline hover:text-primary transition-colors" onClick={() => window.history.back()}>
                                <span className="material-symbols-outlined">close</span>
                            </button>
                        </div>
                    </div>
                </header>
                <main className="max-w-container-max mx-auto px-lg md:px-xxl py-xl md:py-xxl">
                    <div className="grid grid-cols-1 lg:grid-cols-12 gap-xl">
                        {/* Left Column: Tutor & Slot Summary */}
                        <div className="lg:col-span-7 flex flex-col gap-xl">
                            <section>
                                <h2 className="font-headline-lg text-headline-lg text-on-background mb-lg">Complete Your Booking</h2>
                                <div className="checkout-card bg-surface-container-lowest rounded-xl p-lg md:p-xl flex flex-col md:flex-row gap-lg">
                                    <div className="w-full md:w-32 h-32 rounded-xl overflow-hidden flex-shrink-0">
                                        <img className="w-full h-full object-cover" data-alt="A professional headshot of Dr. Arpan Sharma, a middle-aged academic professional with a warm, confident smile. He is wearing a formal navy blazer over a crisp white shirt. The background is a blurred high-end university library with soft, warm golden lighting, emphasizing expertise and approachability in a clean, modern aesthetic." src="https://lh3.googleusercontent.com/aida-public/AB6AXuBQtUPnT89q87A2gIOwwni045jv3e3fltlwwgneGSQDsz_dk40W52V4Jqe67jclbL4QtnTEL9yQnyfWGBvzkL53K-GhQDZlnQPU5702zItVJsSqFRPvEEh8aH6mzXRBh5vp1AW3hL6vfWve6kST9irTFX8c5fd-3GeKUIlXlf6OKqpDVx081fE3itf6AJfIz9iSHKh6r7zFrzGUlc3anX_PnGShgS3V8x9SiAG6mtHQ3NrXGvFTvRCg5bBEVkpeIyBphUreE1StS5k" />
                                    </div>
                                    <div className="flex flex-col justify-center flex-grow">
                                        <div className="flex items-center gap-sm mb-xs">
                                            <span className="bg-primary-container text-on-primary-container text-xs font-bold px-sm py-0.5 rounded-full uppercase tracking-wider">Top Rated</span>
                                            <div className="flex items-center gap-xs text-tertiary">
                                                <span className="material-symbols-outlined text-sm" style={{ fontVariationSettings: "'FILL' 1" }}>star</span>
                                                <span className="font-label-md">4.9 (124 Reviews)</span>
                                            </div>
                                        </div>
                                        <h3 className="font-headline-sm text-headline-sm font-bold text-on-surface mb-xs">Dr. Arpan Sharma</h3>
                                        <p className="text-on-surface-variant font-body-md mb-md">Expert Physics & Mathematics • PhD, Tribhuvan University</p>
                                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-md pt-md border-t border-outline-variant/30">
                                            <div className="flex items-start gap-md">
                                                <div className="w-10 h-10 rounded-lg bg-surface-container-high flex items-center justify-center text-primary">
                                                    <span className="material-symbols-outlined">calendar_today</span>
                                                </div>
                                                <div>
                                                    <p className="text-label-sm text-outline uppercase">Date</p>
                                                    <p className="font-body-md font-bold">Tuesday, Oct 24, 2024</p>
                                                </div>
                                            </div>
                                            <div className="flex items-start gap-md">
                                                <div className="w-10 h-10 rounded-lg bg-surface-container-high flex items-center justify-center text-primary">
                                                    <span className="material-symbols-outlined">schedule</span>
                                                </div>
                                                <div>
                                                    <p className="text-label-sm text-outline uppercase">Time Slot</p>
                                                    <p className="font-body-md font-bold">04:00 PM - 05:00 PM (NPT)</p>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </section>
                            {/* Payment Method Selection */}
                            <section>
                                <h3 className="font-headline-sm text-headline-sm font-bold text-on-surface mb-lg">Select Payment Method</h3>
                                <div className="grid grid-cols-1 sm:grid-cols-2 gap-md">
                                    {/* eSewa */}
                                    <label className="relative flex items-center p-md rounded-xl border-2 border-outline-variant hover:border-primary-container cursor-pointer transition-all has-[:checked]:border-primary has-[:checked]:bg-primary-container/5">
                                        <input checked={selectedPayment === 'esewa'} className="hidden peer" name="payment" type="radio" onChange={() => setSelectedPayment('esewa')} />
                                        <div className="flex items-center gap-md w-full">
                                            <div className="w-12 h-12 bg-[#60bb46]/10 rounded-lg flex items-center justify-center">
                                                <span className="material-symbols-outlined text-[#60bb46]">account_balance_wallet</span>
                                            </div>
                                            <div className="flex-grow">
                                                <p className="font-label-md font-bold text-on-surface">eSewa</p>
                                                <p className="text-xs text-on-surface-variant">Instant digital payment</p>
                                            </div>
                                            <div className="w-5 h-5 rounded-full border-2 border-outline-variant peer-checked:border-primary peer-checked:bg-primary flex items-center justify-center">
                                                <div className="w-2 h-2 bg-white rounded-full"></div>
                                            </div>
                                        </div>
                                    </label>
                                    {/* Khalti */}
                                    <label className="relative flex items-center p-md rounded-xl border-2 border-outline-variant hover:border-primary-container cursor-pointer transition-all has-[:checked]:border-primary has-[:checked]:bg-primary-container/5">
                                        <input checked={selectedPayment === 'khalti'} className="hidden peer" name="payment" type="radio" onChange={() => setSelectedPayment('khalti')} />
                                        <div className="flex items-center gap-md w-full">
                                            <div className="w-12 h-12 bg-[#5c2d91]/10 rounded-lg flex items-center justify-center">
                                                <span className="material-symbols-outlined text-[#5c2d91]">wallet</span>
                                            </div>
                                            <div className="flex-grow">
                                                <p className="font-label-md font-bold text-on-surface">Khalti</p>
                                                <p className="text-xs text-on-surface-variant">Digital Wallet & SDK</p>
                                            </div>
                                            <div className="w-5 h-5 rounded-full border-2 border-outline-variant peer-checked:border-primary peer-checked:bg-primary flex items-center justify-center">
                                                <div className="w-2 h-2 bg-white rounded-full"></div>
                                            </div>
                                        </div>
                                    </label>
                                    {/* Bank Transfer */}
                                    <label className="relative flex items-center p-md rounded-xl border-2 border-outline-variant hover:border-primary-container cursor-pointer transition-all has-[:checked]:border-primary has-[:checked]:bg-primary-container/5">
                                        <input checked={selectedPayment === 'bank'} className="hidden peer" name="payment" type="radio" onChange={() => setSelectedPayment('bank')} />
                                        <div className="flex items-center gap-md w-full">
                                            <div className="w-12 h-12 bg-secondary/10 rounded-lg flex items-center justify-center">
                                                <span className="material-symbols-outlined text-secondary">account_balance</span>
                                            </div>
                                            <div className="flex-grow">
                                                <p className="font-label-md font-bold text-on-surface">Bank Transfer</p>
                                                <p className="text-xs text-on-surface-variant">Connect via Fonepay</p>
                                            </div>
                                            <div className="w-5 h-5 rounded-full border-2 border-outline-variant peer-checked:border-primary peer-checked:bg-primary flex items-center justify-center">
                                                <div className="w-2 h-2 bg-white rounded-full"></div>
                                            </div>
                                        </div>
                                    </label>
                                    {/* Card */}
                                    <label className="relative flex items-center p-md rounded-xl border-2 border-outline-variant hover:border-primary-container cursor-pointer transition-all has-[:checked]:border-primary has-[:checked]:bg-primary-container/5">
                                        <input checked={selectedPayment === 'card'} className="hidden peer" name="payment" type="radio" onChange={() => setSelectedPayment('card')} />
                                        <div className="flex items-center gap-md w-full">
                                            <div className="w-12 h-12 bg-primary/10 rounded-lg flex items-center justify-center">
                                                <span className="material-symbols-outlined text-primary">credit_card</span>
                                            </div>
                                            <div className="flex-grow">
                                                <p className="font-label-md font-bold text-on-surface">Debit/Credit Card</p>
                                                <p className="text-xs text-on-surface-variant">Visa, Mastercard, UnionPay</p>
                                            </div>
                                            <div className="w-5 h-5 rounded-full border-2 border-outline-variant peer-checked:border-primary peer-checked:bg-primary flex items-center justify-center">
                                                <div className="w-2 h-2 bg-white rounded-full"></div>
                                            </div>
                                        </div>
                                    </label>
                                </div>
                            </section>
                        </div>
                        {/* Right Column: Payment Summary Card */}
                        <div className="lg:col-span-5">
                            <div className="sticky top-24">
                                <div className="checkout-card bg-white rounded-xl p-lg md:p-xl overflow-hidden relative">
                                    {/* Decorative Header Gradient */}
                                    <div className="absolute top-0 left-0 w-full h-2 bg-gradient-to-r from-primary to-secondary"></div>
                                    <h3 className="font-headline-sm text-headline-sm font-bold text-on-surface mb-xl">Payment Summary</h3>
                                    <div className="space-y-md">
                                        <div className="flex justify-between items-center">
                                            <span className="text-on-surface-variant font-body-md">Hourly Rate (1 hr)</span>
                                            <span className="font-label-md font-bold text-on-surface">NPR 2,500.00</span>
                                        </div>
                                        <div className="flex justify-between items-center">
                                            <span className="text-on-surface-variant font-body-md">Platform Service Fee (5%)</span>
                                            <span className="font-label-md font-bold text-on-surface">NPR 125.00</span>
                                        </div>
                                        <div className="flex justify-between items-center text-primary">
                                            <span className="text-primary font-body-md flex items-center gap-xs">
                                                <span className="material-symbols-outlined text-sm">redeem</span>
                                                Discount applied
                                            </span>
                                            <span className="font-label-md font-bold">- NPR 0.00</span>
                                        </div>
                                        <hr className="border-outline-variant/30 my-xl" />
                                        <div className="flex justify-between items-end">
                                            <div>
                                                <p className="text-outline font-label-sm uppercase tracking-tighter">Total Amount</p>
                                                <p className="font-headline-md text-headline-md font-black text-on-surface">NPR 2,625.00</p>
                                            </div>
                                            <div className="text-right">
                                                <p className="text-outline text-[10px]">Approx. $19.75 USD</p>
                                            </div>
                                        </div>
                                    </div>
                                    {/* Promo Code */}
                                    <div className="mt-xl">
                                        <div className="relative">
                                            <input className="w-full bg-surface-container-low border border-outline-variant rounded-lg px-md py-sm pr-20 focus:ring-2 focus:ring-primary/20 focus:border-primary transition-all" placeholder="Promo code" type="text" />
                                            <button className="absolute right-2 top-1.5 px-md py-1 bg-on-surface text-white rounded-md text-xs font-bold hover:bg-on-surface-variant transition-colors">Apply</button>
                                        </div>
                                    </div>
                                    {/* CTA */}
                                    <button className="w-full mt-xl bg-primary hover:bg-primary-container text-white py-lg rounded-xl font-headline-sm shadow-lg shadow-primary/20 active:scale-95 transition-all flex items-center justify-center gap-md">
                                        Confirm and Pay Securely
                                        <span className="material-symbols-outlined">arrow_forward</span>
                                    </button>
                                    <div className="mt-xl space-y-md">
                                        <div className="flex items-center gap-md p-md bg-surface-container-low rounded-lg">
                                            <span className="material-symbols-outlined text-primary">verified_user</span>
                                            <p className="text-xs text-on-surface-variant leading-relaxed">
                                                <strong>Cancellation Policy:</strong> Free cancellation up to 12 hours before the session.
                                            </p>
                                        </div>
                                        <div className="flex justify-center items-center gap-xl opacity-40 grayscale hover:grayscale-0 transition-all">
                                            <img alt="Visa" className="h-4" src="https://lh3.googleusercontent.com/aida-public/AB6AXuC_IU6UlTHuYF72w0wgvgxXFaChWQDnN6bunwz5Kcw-oSe07txKONtOQKeTmmCmKn7wuK50nJj_fmcL63X7QjJSuQg63LfNNUUJwgG9SQ2SL-3JvxxoixnxrEO0LXkFHmLoKeFAQRmzWpGrqVMEZuOBh4MMJiPP6OHyWXS7zD52aTYTpgBsRhSBHnY9BdeUzewCFmrsZXSvJGpQrAXy5Lz0ugcYB_JkscWlTKq0VaI6g13lmeS9MJ9Z_5SmjrqX3t2XXWJT_VXM2lE" />
                                            <img alt="Mastercard" className="h-6" src="https://lh3.googleusercontent.com/aida-public/AB6AXuB0jYTuya6kSdpfWG-rMAITfh6p6UwWP2-ppkvbFzF6m6iLNEUqNi8xehG8PsE3AcfCd-P6AnpHMIxMR9bDYD6fVk_Fq-HTKVyR5JoIsJ_Hr9NvhgnYyaDJx8sBaiYZ1iry8BZuwLWGxsjyt3kIrfyc1CM7Wj3bN7zF9Lxgp_eP_3RjFl_PdsUs6MziliBBI4e9PSb3OjsPdwrBi29hEipiTvNuE50O7tBGUCEYU6Dy0v7Y7_o9iWjNPOYRakIYfg11zEFwkhwgA4M" />
                                            <div className="font-black text-xs">ESEWA</div>
                                            <div className="font-black text-xs">KHALTI</div>
                                        </div>
                                    </div>
                                </div>
                                {/* Trust Signals Below Card */}
                                <div className="mt-lg px-md text-center">
                                    <p className="text-xs text-outline flex items-center justify-center gap-xs">
                                        <span className="material-symbols-outlined text-[14px]">shield</span>
                                        Your payment information is never stored on our servers.
                                    </p>
                                </div>
                            </div>
                        </div>
                    </div>
                </main>
                {/* Footer Summary (Compact) */}
                <footer className="mt-xxl border-t border-outline-variant/30 bg-surface-container-lowest py-xl">
                    <div className="max-w-container-max mx-auto px-lg md:px-xxl flex flex-col md:flex-row justify-between items-center gap-lg">
                        <p className="text-on-surface-variant text-label-md">© 2024 TutorConnect Nepal. All rights reserved.</p>
                        <div className="flex gap-xl text-label-md text-outline">
                            <a className="hover:text-primary transition-colors" href="#">Safety Guide</a>
                            <a className="hover:text-primary transition-colors" href="#">Refund Policy</a>
                            <a className="hover:text-primary transition-colors" href="#">Help Center</a>
                        </div>
                    </div>
                </footer>
                <script>{`
                    // Simple Interaction for Radio Buttons
                    document.querySelectorAll('input[name="payment"]').forEach(input => {
                        input.addEventListener('change', (e) => {
                            // Potential for adding dynamic UI changes based on selected method
                            console.log('Selected payment method:', e.target.parentElement.textContent.trim());
                        });
                    });

                    // CTA Click Animation
                    document.querySelector('button.bg-primary').addEventListener('click', function() {
                        this.innerHTML = '<span class="material-symbols-outlined animate-spin">sync</span> Processing...';
                        this.classList.add('opacity-80', 'cursor-not-allowed');
                        setTimeout(() => {
                            window.location.reload(); // Simulate redirect or success
                        }, 2000);
                    });
                `}</script>
            </body>
        </html>
    );
};

export default BookTeacher;