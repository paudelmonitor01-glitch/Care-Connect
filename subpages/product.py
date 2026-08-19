import streamlit as st


PRODUCTS = [
    {
        "title": "Harmony in Colors",
        "price": "$49.00",
        "category": "Abstract",
        "image": "https://images.unsplash.com/photo-1541701494587-cb58502866ab?auto=format&fit=crop&w=900&q=82",
    },
    {
        "title": "Bloom of Hope",
        "price": "$39.00",
        "category": "Floral",
        "image": "https://images.unsplash.com/photo-1490750967868-88aa4486c946?auto=format&fit=crop&w=900&q=82",
    },
    {
        "title": "Strength Within",
        "price": "$59.00",
        "category": "Portrait",
        "image": "https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91?auto=format&fit=crop&w=900&q=82",
    },
    {
        "title": "Peaceful Reflections",
        "price": "$44.00",
        "category": "Landscape",
        "image": "https://images.unsplash.com/photo-1500534314209-a25ddb2bd4297?auto=format&fit=crop&w=900&q=82",
    },
    {
        "title": "Light Up the Night",
        "price": "$35.00",
        "category": "Digital Art",
        "image": "https://images.unsplash.com/photo-1519608487953-e999c86e7455?auto=format&fit=crop&w=900&q=82",
    },
    {
        "title": "Nature's Embrace",
        "price": "$42.00",
        "category": "Illustration",
        "image": "https://images.unsplash.com/photo-1501004318641-b39e6451bec6?auto=format&fit=crop&w=900&q=82",
    },
]


def _product_cards():
    cards = []
    for item in PRODUCTS:
        cards.append(
            f"""
            <article class="cc-product-card">
                <div class="cc-thumb-wrap">
                    <img class="cc-thumb" src="{item['image']}" alt="{item['title']}">
                    <div class="cc-preview-mask"></div>
                    <div class="cc-lock-badge" aria-label="Locked preview">
                        <svg viewBox="0 0 24 24" aria-hidden="true">
                            <rect x="5" y="10" width="14" height="10" rx="2"></rect>
                            <path d="M8 10V7a4 4 0 0 1 8 0v3"></path>
                        </svg>
                    </div>
                    <div class="cc-preview-label">Preview</div>
                </div>

                <div class="cc-product-body">
                    <div class="cc-category">{item['category']}</div>
                    <h3>{item['title']}</h3>
                    <div class="cc-price">{item['price']}</div>

                    <div class="cc-unlock-note">
                        <svg viewBox="0 0 24 24" aria-hidden="true">
                            <rect x="5" y="10" width="14" height="10" rx="2"></rect>
                            <path d="M8 10V7a4 4 0 0 1 8 0v3"></path>
                        </svg>
                        <span>Pay to unlock full view and download</span>
                    </div>

                    <div class="cc-card-actions">
                        <a class="cc-buy-btn" href="#purchase-info">Buy Now</a>
                        <button class="cc-heart-btn" type="button" aria-label="Save artwork">♡</button>
                    </div>
                </div>
            </article>
            """
        )
    return "\n".join(cards)


def render():
    cards_html = _product_cards()

    page = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800;900&display=swap');

    :root {{
        --cc-ink: #172033;
        --cc-muted: #687180;
        --cc-teal: #0fa69c;
        --cc-teal-dark: #078b84;
        --cc-coral: #f45e68;
        --cc-coral-soft: #fff1f1;
        --cc-cream: #fffaf1;
        --cc-mint: #edf9f6;
        --cc-yellow: #fff1ca;
        --cc-lavender: #f3e6f8;
        --cc-line: #e8eeed;
        --cc-white: #ffffff;
    }}

    * {{
        box-sizing: border-box;
    }}

    html {{
        scroll-behavior: smooth;
    }}

    .cc-page {{
        width: 100%;
        margin: 0;
        overflow: hidden;
        background: #ffffff;
        color: var(--cc-ink);
        font-family: "Nunito", sans-serif;
        line-height: 1.5;
    }}

    .cc-page a {{
        color: inherit;
        text-decoration: none;
    }}

    .cc-page img {{
        display: block;
        width: 100%;
    }}

    .cc-container {{
        width: min(1180px, calc(100% - 56px));
        margin: 0 auto;
    }}

    /* HEADER */
    .cc-header {{
        position: relative;
        z-index: 30;
        width: 100%;
        background: rgba(255,255,255,.98);
        border-bottom: 1px solid #eef2f2;
    }}

    .cc-nav {{
        height: 102px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 30px;
    }}

    .cc-brand {{
        min-width: 205px;
        display: flex;
        align-items: center;
        gap: 12px;
    }}

    .cc-brand svg {{
        width: 56px;
        height: 56px;
        flex: none;
    }}

    .cc-brand-text {{
        display: flex;
        flex-direction: column;
        font-size: 24px;
        line-height: .88;
        font-weight: 900;
        letter-spacing: -.4px;
        color: var(--cc-teal);
    }}

    .cc-brand-text span:last-child {{
        margin-top: 5px;
        color: var(--cc-coral);
    }}

    .cc-nav-links {{
        display: flex;
        align-items: center;
        gap: 48px;
        font-size: 15px;
        font-weight: 700;
    }}

    .cc-nav-links a {{
        position: relative;
        padding: 40px 0 35px;
    }}

    .cc-nav-links a.active {{
        color: var(--cc-teal-dark);
    }}

    .cc-nav-links a.active::after {{
        content: "";
        position: absolute;
        left: 0;
        right: 0;
        bottom: 27px;
        height: 2px;
        border-radius: 20px;
        background: var(--cc-teal);
    }}

    .cc-btn {{
        min-height: 54px;
        padding: 0 27px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        border-radius: 14px;
        font-size: 15px;
        font-weight: 800;
        transition: .2s ease;
    }}

    .cc-btn:hover,
    .cc-buy-btn:hover {{
        transform: translateY(-2px);
    }}

    .cc-btn-coral {{
        color: #fff !important;
        background: linear-gradient(135deg, #ff6973, #ef505e);
        box-shadow: 0 10px 24px rgba(244,94,104,.18);
    }}

    .cc-btn-teal {{
        color: #fff !important;
        background: linear-gradient(135deg, #11aea3, #078d86);
        box-shadow: 0 10px 24px rgba(15,166,156,.16);
    }}

    /* HERO */
    .cc-hero {{
        position: relative;
        padding: 58px 0 48px;
        background: #fff;
    }}

    .cc-hero::after {{
        content: "";
        position: absolute;
        right: -95px;
        bottom: -85px;
        width: 270px;
        height: 270px;
        border-radius: 50%;
        background: #fff2cc;
    }}

    .cc-hero-grid {{
        position: relative;
        z-index: 2;
        display: grid;
        grid-template-columns: .88fr 1.12fr;
        gap: 54px;
        align-items: center;
    }}

    .cc-purpose-pill {{
        width: max-content;
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 8px 14px;
        border-radius: 999px;
        background: #fff3f1;
        color: #ef6570;
        font-size: 13px;
        font-weight: 800;
    }}

    .cc-hero h1 {{
        margin: 20px 0 17px;
        font-size: 66px;
        line-height: 1.02;
        letter-spacing: -2.5px;
        font-weight: 900;
    }}

    .cc-hero h1 span {{
        color: var(--cc-coral);
    }}

    .cc-hero-copy p {{
        max-width: 540px;
        margin: 0 0 28px;
        color: #626c78;
        font-size: 16.5px;
        line-height: 1.72;
    }}

    .cc-hero-art {{
        position: relative;
        min-height: 500px;
    }}

    .cc-gallery-photo {{
        height: 490px;
        overflow: hidden;
        border-radius: 46% 0 0 46%;
        background: #eee;
    }}

    .cc-gallery-photo img {{
        height: 100%;
        object-fit: cover;
        object-position: center;
    }}

    .cc-easel-note {{
        position: absolute;
        right: 22px;
        bottom: 30px;
        width: 235px;
        padding: 27px 23px;
        border-radius: 16px;
        background: rgba(255,255,255,.95);
        box-shadow: 0 14px 38px rgba(33,55,60,.16);
        text-align: center;
    }}

    .cc-easel-note strong {{
        display: block;
        color: #4b535f;
        font-family: Georgia, serif;
        font-size: 20px;
        line-height: 1.45;
        font-style: italic;
        font-weight: 500;
    }}

    .cc-easel-note span {{
        display: block;
        margin-top: 7px;
        color: var(--cc-coral);
        font-size: 28px;
    }}

    /* MISSION STRIP */
    .cc-mission-strip {{
        position: relative;
        z-index: 5;
        margin-top: -2px;
    }}

    .cc-mission-box {{
        display: grid;
        grid-template-columns: 72px 1fr 45px;
        gap: 22px;
        align-items: center;
        padding: 24px 38px;
        border-radius: 18px;
        background: linear-gradient(90deg, #edf9f6, #e9f7f4);
    }}

    .cc-mission-icon {{
        width: 66px;
        height: 66px;
        display: grid;
        place-items: center;
        border-radius: 50%;
        color: #fff;
        background: var(--cc-teal);
        font-size: 32px;
    }}

    .cc-mission-copy strong {{
        color: var(--cc-teal-dark);
        font-size: 22px;
        font-weight: 900;
    }}

    .cc-mission-copy b {{
        color: #3d4654;
        font-size: 16px;
        font-weight: 800;
    }}

    .cc-mission-copy p {{
        margin: 4px 0 0;
        color: #68717f;
        font-size: 13.5px;
    }}

    .cc-mission-heart {{
        color: #ff9da5;
        font-size: 31px;
        transform: rotate(-18deg);
    }}

    /* SHOP */
    .cc-shop {{
        padding: 42px 0 60px;
        background: #fff;
    }}

    .cc-shop-layout {{
        display: grid;
        grid-template-columns: 205px 1fr;
        gap: 28px;
        align-items: start;
    }}

    .cc-sidebar-title {{
        margin-bottom: 12px;
        font-size: 15px;
        font-weight: 900;
    }}

    .cc-category-list {{
        display: flex;
        flex-direction: column;
        gap: 7px;
    }}

    .cc-category-link {{
        min-height: 43px;
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 0 14px;
        border-radius: 11px;
        color: #5e6775;
        font-size: 13.5px;
        font-weight: 700;
    }}

    .cc-category-link.active {{
        color: #fff;
        background: linear-gradient(135deg, #12aca1, #078e86);
    }}

    .cc-category-icon {{
        width: 19px;
        text-align: center;
        font-size: 16px;
    }}

    .cc-sidebar-message {{
        margin-top: 39px;
        padding: 21px 17px;
        border: 1px solid #e5ebea;
        border-radius: 15px;
        background: #fff;
    }}

    .cc-sidebar-message .heart {{
        color: var(--cc-coral);
        font-size: 32px;
    }}

    .cc-sidebar-message strong {{
        display: block;
        margin: 9px 0 7px;
        font-size: 15px;
        line-height: 1.35;
    }}

    .cc-sidebar-message p {{
        margin: 0;
        color: #737b86;
        font-size: 12px;
        line-height: 1.5;
    }}

    .cc-preview-banner {{
        margin-bottom: 17px;
        padding: 14px 19px;
        display: flex;
        align-items: center;
        gap: 10px;
        border-radius: 13px;
        color: #525a67;
        background: #fff2ed;
        font-size: 13.5px;
    }}

    .cc-preview-banner svg {{
        width: 20px;
        height: 20px;
        fill: none;
        stroke: #e9a223;
        stroke-width: 1.8;
        flex: none;
    }}

    .cc-preview-banner strong {{
        color: #242c39;
    }}

    .cc-products-grid {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 17px;
    }}

    .cc-product-card {{
        overflow: hidden;
        border: 1px solid #e6eceb;
        border-radius: 16px;
        background: #fff;
        box-shadow: 0 5px 16px rgba(42,56,58,.045);
    }}

    .cc-thumb-wrap {{
        position: relative;
        height: 195px;
        margin: 9px 9px 0;
        overflow: hidden;
        border-radius: 12px;
        background: #edf2f1;
    }}

    .cc-thumb {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        filter: saturate(.88) contrast(.96);
        transform: scale(1.015);
    }}

    .cc-preview-mask {{
        position: absolute;
        inset: 0;
        background: rgba(255,255,255,.08);
        backdrop-filter: blur(.5px);
    }}

    .cc-lock-badge {{
        position: absolute;
        left: 50%;
        top: 50%;
        width: 50px;
        height: 50px;
        display: grid;
        place-items: center;
        transform: translate(-50%,-50%);
        border-radius: 50%;
        background: rgba(255,255,255,.88);
        box-shadow: 0 6px 18px rgba(0,0,0,.12);
    }}

    .cc-lock-badge svg {{
        width: 23px;
        height: 23px;
        fill: none;
        stroke: #4d5862;
        stroke-width: 1.7;
    }}

    .cc-preview-label {{
        position: absolute;
        left: 10px;
        top: 10px;
        padding: 5px 9px;
        border-radius: 999px;
        background: rgba(23,32,51,.78);
        color: #fff;
        font-size: 10px;
        font-weight: 800;
        letter-spacing: .35px;
        text-transform: uppercase;
    }}

    .cc-product-body {{
        padding: 12px 13px 13px;
    }}

    .cc-category {{
        color: #8b929a;
        font-size: 10px;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: .7px;
    }}

    .cc-product-body h3 {{
        margin: 3px 0 3px;
        font-size: 15.5px;
        font-weight: 900;
    }}

    .cc-price {{
        color: var(--cc-teal-dark);
        font-size: 15px;
        font-weight: 900;
    }}

    .cc-unlock-note {{
        min-height: 42px;
        margin-top: 8px;
        display: flex;
        align-items: flex-start;
        gap: 7px;
        color: #6d7682;
        font-size: 11.3px;
        line-height: 1.35;
    }}

    .cc-unlock-note svg {{
        width: 15px;
        height: 15px;
        margin-top: 1px;
        fill: none;
        stroke: #66717b;
        stroke-width: 1.8;
        flex: none;
    }}

    .cc-card-actions {{
        display: grid;
        grid-template-columns: 1fr 48px;
        gap: 9px;
        align-items: center;
        margin-top: 10px;
    }}

    .cc-buy-btn {{
        height: 42px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 10px;
        color: #fff !important;
        background: linear-gradient(135deg, #11aaa0, #078e86);
        font-size: 13px;
        font-weight: 800;
        transition: .2s ease;
    }}

    .cc-heart-btn {{
        height: 42px;
        border: 1px solid #ff9ea6;
        border-radius: 10px;
        background: #fff;
        color: var(--cc-coral);
        font: inherit;
        font-size: 22px;
        cursor: pointer;
    }}

    /* PURCHASE CTA */
    .cc-purchase-cta {{
        margin-top: 28px;
        padding: 20px 27px;
        display: grid;
        grid-template-columns: 62px 1fr auto;
        gap: 18px;
        align-items: center;
        border-radius: 16px;
        background: #eaf8f5;
    }}

    .cc-purchase-icon {{
        width: 60px;
        height: 60px;
        display: grid;
        place-items: center;
        border-radius: 50%;
        background: var(--cc-teal);
        color: #fff;
        font-size: 29px;
    }}

    .cc-purchase-copy strong {{
        display: block;
        color: #242c39;
        font-size: 20px;
        font-weight: 900;
    }}

    .cc-purchase-copy p {{
        margin: 3px 0 0;
        color: #66717d;
        font-size: 12.5px;
    }}

    /* TRUST */
    .cc-trust {{
        padding: 0 0 46px;
        background: #fff;
    }}

    .cc-trust-box {{
        display: grid;
        grid-template-columns: repeat(4,1fr);
        border: 1px solid #ebefef;
        border-radius: 15px;
        overflow: hidden;
        background: #fff;
    }}

    .cc-trust-item {{
        min-height: 100px;
        padding: 18px;
        display: grid;
        grid-template-columns: 48px 1fr;
        gap: 12px;
        align-items: center;
        border-right: 1px solid #edf1f0;
    }}

    .cc-trust-item:last-child {{
        border-right: 0;
    }}

    .cc-trust-icon {{
        width: 46px;
        height: 46px;
        display: grid;
        place-items: center;
        border-radius: 50%;
        font-size: 21px;
    }}

    .cc-trust-item strong {{
        display: block;
        font-size: 13px;
        font-weight: 900;
    }}

    .cc-trust-item span {{
        display: block;
        margin-top: 3px;
        color: #747c87;
        font-size: 10.7px;
        line-height: 1.4;
    }}

    .cc-mint {{background:#ddf6ef;color:#0a948b;}}
    .cc-yellow {{background:#fff0c8;color:#dcaa24;}}
    .cc-lavender {{background:#f0ddf8;color:#9b59aa;}}
    .cc-pink {{background:#ffe3e1;color:#ef5d68;}}

    /* RESPONSIVE */
    @media (max-width: 1020px) {{
        .cc-nav-links {{ gap: 24px; }}
        .cc-hero-grid {{ grid-template-columns: 1fr; }}
        .cc-hero-copy {{ text-align: center; }}
        .cc-purpose-pill {{ margin: 0 auto; }}
        .cc-hero-copy p {{ margin-left: auto; margin-right: auto; }}
        .cc-hero-art {{ min-height: 440px; }}
        .cc-gallery-photo {{ height: 440px; border-radius: 36px; }}
        .cc-shop-layout {{ grid-template-columns: 1fr; }}
        .cc-sidebar {{ display: none; }}
        .cc-products-grid {{ grid-template-columns: repeat(2,1fr); }}
        .cc-trust-box {{ grid-template-columns: repeat(2,1fr); }}
        .cc-trust-item:nth-child(2) {{ border-right: 0; }}
        .cc-trust-item:nth-child(-n+2) {{ border-bottom: 1px solid #edf1f0; }}
    }}

    @media (max-width: 760px) {{
        .cc-container {{ width: min(100% - 28px, 1180px); }}
        .cc-nav {{ height: 78px; }}
        .cc-nav-links {{ display: none; }}
        .cc-brand {{ min-width: auto; }}
        .cc-brand svg {{ width: 46px; height: 46px; }}
        .cc-brand-text {{ font-size: 20px; }}
        .cc-header .cc-btn {{ min-height: 44px; padding: 0 17px; }}
        .cc-hero {{ padding-top: 38px; }}
        .cc-hero h1 {{ font-size: 47px; }}
        .cc-hero-art {{ min-height: 370px; }}
        .cc-gallery-photo {{ height: 370px; }}
        .cc-easel-note {{ right: 14px; bottom: 14px; width: 205px; padding: 19px; }}
        .cc-easel-note strong {{ font-size: 17px; }}
        .cc-mission-box {{ grid-template-columns: 56px 1fr; padding: 20px; }}
        .cc-mission-icon {{ width: 54px; height: 54px; }}
        .cc-mission-heart {{ display: none; }}
        .cc-products-grid {{ grid-template-columns: 1fr; }}
        .cc-purchase-cta {{ grid-template-columns: 54px 1fr; }}
        .cc-purchase-cta .cc-btn {{ grid-column: 1 / -1; }}
    }}

    @media (max-width: 520px) {{
        .cc-header .cc-btn {{ width: 48px; padding: 0; font-size: 0; }}
        .cc-header .cc-btn span {{ font-size: 22px; }}
        .cc-hero h1 {{ font-size: 39px; }}
        .cc-mission-copy strong {{ font-size: 18px; }}
        .cc-trust-box {{ grid-template-columns: 1fr; }}
        .cc-trust-item {{
            border-right: 0 !important;
            border-bottom: 1px solid #edf1f0;
        }}
        .cc-trust-item:last-child {{ border-bottom: 0; }}
    }}
    </style>

    <div class="cc-page">

        <header class="cc-header">
            <div class="cc-container cc-nav">
                <a class="cc-brand" href="?page=home">
                    <svg viewBox="0 0 64 64" aria-hidden="true">
                        <circle cx="23" cy="10" r="6" fill="#0fa69c"/>
                        <circle cx="43" cy="10" r="6" fill="#f45e68"/>
                        <path d="M23 19 C10 18, 8 32, 17 40 C23 46, 30 52, 32 56 C33 48, 26 40, 23 34 C19 28, 18 23, 23 19Z" fill="#0fa69c"/>
                        <path d="M43 19 C56 18, 58 32, 49 40 C43 46, 36 52, 32 56 C31 48, 38 40, 41 34 C45 28, 48 23, 43 19Z" fill="#f45e68"/>
                        <path d="M29 27 C31 23, 34 23, 36 27 C38 30, 35 34, 32 37 C29 34, 27 30, 29 27Z" fill="#fff"/>
                    </svg>
                    <span class="cc-brand-text">
                        <span>care</span>
                        <span>connect</span>
                    </span>
                </a>

                <nav class="cc-nav-links">
                    <a href="?page=home">Home</a>
                    <a class="active" href="?page=product">Product</a>
                    <a href="?page=home#about">About Us</a>
                    <a href="?page=home#contact">Contact</a>
                </nav>

                <a class="cc-btn cc-btn-coral" href="?page=home#causes">
                    Donate Us <span>♡</span>
                </a>
            </div>
        </header>

        <main>
            <section class="cc-hero">
                <div class="cc-container cc-hero-grid">
                    <div class="cc-hero-copy">
                        <div class="cc-purpose-pill">♥ &nbsp; Art with Purpose</div>

                        <h1>
                            Art That<br>
                            <span>Gives Back</span>
                        </h1>

                        <p>
                            Every artwork you purchase directly supports helpless, homeless,
                            elderly, and needy people with care, food, shelter, and hope.
                        </p>

                        <a class="cc-btn cc-btn-teal" href="#art-shop">
                            Shop Art &amp; Make an Impact <span>♡</span>
                        </a>
                    </div>

                    <div class="cc-hero-art">
                        <div class="cc-gallery-photo">
                            <img
                                src="https://images.unsplash.com/photo-1549490349-8643362247b5?auto=format&fit=crop&w=1300&q=88"
                                alt="Art gallery"
                            >
                        </div>

                        <div class="cc-easel-note">
                            <strong>Your purchase brings hope and creates real change.</strong>
                            <span>♡</span>
                        </div>
                    </div>
                </div>
            </section>

            <section class="cc-mission-strip">
                <div class="cc-container">
                    <div class="cc-mission-box">
                        <div class="cc-mission-icon">♡</div>
                        <div class="cc-mission-copy">
                            <div>
                                <strong>100%</strong>
                                <b> of proceeds from these art sales go toward supporting people in need.</b>
                            </div>
                            <p>Every artwork you buy directly helps provide care, food, shelter, dignity, and hope.</p>
                        </div>
                        <div class="cc-mission-heart">♡</div>
                    </div>
                </div>
            </section>

            <section class="cc-shop" id="art-shop">
                <div class="cc-container cc-shop-layout">

                    <aside class="cc-sidebar">
                        <div class="cc-sidebar-title">Browse Art</div>

                        <div class="cc-category-list">
                            <a class="cc-category-link active" href="#art-shop"><span class="cc-category-icon">▦</span>All Artwork</a>
                            <a class="cc-category-link" href="#art-shop"><span class="cc-category-icon">✎</span>Paintings</a>
                            <a class="cc-category-link" href="#art-shop"><span class="cc-category-icon">▣</span>Digital Art</a>
                            <a class="cc-category-link" href="#art-shop"><span class="cc-category-icon">▧</span>Charity Prints</a>
                            <a class="cc-category-link" href="#art-shop"><span class="cc-category-icon">✐</span>Illustrations</a>
                            <a class="cc-category-link" href="#art-shop"><span class="cc-category-icon">◌</span>Abstract</a>
                            <a class="cc-category-link" href="#art-shop"><span class="cc-category-icon">⌁</span>Landscapes</a>
                            <a class="cc-category-link" href="#art-shop"><span class="cc-category-icon">♙</span>Portraits</a>
                            <a class="cc-category-link" href="#art-shop"><span class="cc-category-icon">✿</span>Floral</a>
                        </div>

                        <div class="cc-sidebar-message">
                            <div class="heart">♡</div>
                            <strong>Every purchase makes a difference</strong>
                            <p>Thank you for supporting our mission and spreading kindness.</p>
                        </div>
                    </aside>

                    <div class="cc-products">
                        <div class="cc-preview-banner">
                            <svg viewBox="0 0 24 24" aria-hidden="true">
                                <rect x="5" y="10" width="14" height="10" rx="2"></rect>
                                <path d="M8 10V7a4 4 0 0 1 8 0v3"></path>
                            </svg>
                            <span>
                                <strong>Preview only.</strong>
                                Full image access and download are unlocked after payment.
                            </span>
                        </div>

                        <div class="cc-products-grid">
                            {cards_html}
                        </div>
                    </div>
                </div>

                <div class="cc-container" id="purchase-info">
                    <div class="cc-purchase-cta">
                        <div class="cc-purchase-icon">♥</div>
                        <div class="cc-purchase-copy">
                            <strong>Your purchase creates real change.</strong>
                            <p>Together, we can bring care, dignity, food, shelter and hope to those who need it most.</p>
                        </div>
                        <a class="cc-btn cc-btn-coral" href="#art-shop">Shop Art &amp; Support Now ♡</a>
                    </div>
                </div>
            </section>

            <section class="cc-trust">
                <div class="cc-container">
                    <div class="cc-trust-box">

                        <div class="cc-trust-item">
                            <div class="cc-trust-icon cc-mint">♧</div>
                            <div>
                                <strong>100% for People</strong>
                                <span>Art sale proceeds directly support people in need.</span>
                            </div>
                        </div>

                        <div class="cc-trust-item">
                            <div class="cc-trust-icon cc-yellow">♡</div>
                            <div>
                                <strong>Safe &amp; Secure</strong>
                                <span>Secure payment flow will be connected here.</span>
                            </div>
                        </div>

                        <div class="cc-trust-item">
                            <div class="cc-trust-icon cc-lavender">◇</div>
                            <div>
                                <strong>Authentic Art</strong>
                                <span>Original art offered with a meaningful purpose.</span>
                            </div>
                        </div>

                        <div class="cc-trust-item">
                            <div class="cc-trust-icon cc-pink">▣</div>
                            <div>
                                <strong>Gift Kindness</strong>
                                <span>Share art that spreads hope and compassion.</span>
                            </div>
                        </div>

                    </div>
                </div>
            </section>
        </main>
    </div>
    """

    if hasattr(st, "html"):
        st.html(page)
    else:
        st.markdown(page, unsafe_allow_html=True)
