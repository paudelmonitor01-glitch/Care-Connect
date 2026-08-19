import streamlit as st


def render():
    page = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800;900&display=swap');

    :root{
      --ink:#172033;
      --muted:#667085;
      --teal:#0fa69c;
      --teal-dark:#078a82;
      --coral:#f45e68;
      --cream:#fffaf0;
      --mint:#dcf6ef;
      --yellow:#fff0c8;
      --lavender:#f3def8;
      --pink:#ffe3e1;
      --line:#e7efed;
      --white:#ffffff;
    }

    *{
      box-sizing:border-box;
    }

    html{
      scroll-behavior:smooth;
    }

    .care-page{
      margin:0;
      width:100%;
      overflow:hidden;
      font-family:"Nunito",sans-serif;
      color:var(--ink);
      background:#fff;
      line-height:1.5;
    }

    .care-page img{
      display:block;
      width:100%;
    }

    .care-page a{
      color:inherit;
      text-decoration:none;
    }

    .care-page .container{
      width:min(1180px, calc(100% - 56px));
      margin:0 auto;
    }

    /* ---------------- HEADER ---------------- */
    .care-header{
      width:100%;
      background:rgba(255,255,255,.98);
      border-bottom:1px solid #edf1f1;
      position:relative;
      z-index:20;
    }

    .nav-wrap{
      height:102px;
      display:flex;
      align-items:center;
      justify-content:space-between;
      gap:30px;
    }

    .brand{
      min-width:205px;
      display:flex;
      align-items:center;
      gap:12px;
    }

    .brand svg{
      width:56px;
      height:56px;
      flex:none;
    }

    .brand-text{
      display:flex;
      flex-direction:column;
      font-size:24px;
      line-height:.88;
      font-weight:900;
      letter-spacing:-.4px;
      color:var(--teal);
    }

    .brand-text span:last-child{
      margin-top:5px;
      color:var(--coral);
    }

    .nav-links{
      display:flex;
      align-items:center;
      gap:48px;
      font-size:15px;
      font-weight:700;
    }

    .nav-links a{
      position:relative;
      padding:40px 0 35px;
      transition:.2s ease;
    }

    .nav-links a:hover,
    .nav-links a.active{
      color:var(--teal-dark);
    }

    .nav-links a.active:after{
      content:"";
      position:absolute;
      height:2px;
      left:0;
      right:0;
      bottom:27px;
      background:var(--teal);
      border-radius:99px;
    }

    .btn{
      display:inline-flex;
      align-items:center;
      justify-content:center;
      gap:11px;
      min-height:54px;
      padding:0 27px;
      border-radius:14px;
      font-size:15px;
      font-weight:800;
      border:1px solid transparent;
      transition:.22s ease;
      white-space:nowrap;
    }

    .btn:hover{
      transform:translateY(-2px);
    }

    .btn-coral{
      color:white !important;
      background:linear-gradient(135deg,#ff6973,#ef505e);
      box-shadow:0 10px 24px rgba(244,94,104,.18);
    }

    .btn-teal{
      color:white !important;
      background:linear-gradient(135deg,#12ada3,#078e86);
      box-shadow:0 10px 24px rgba(15,166,156,.16);
    }

    .btn-outline{
      color:var(--teal-dark) !important;
      background:#fff;
      border-color:#80cec8;
    }

    /* ---------------- HERO ---------------- */
    .hero{
      position:relative;
      padding:62px 0 56px;
      background:#fff;
    }

    .hero:after{
      content:"";
      position:absolute;
      right:-100px;
      bottom:-75px;
      width:290px;
      height:290px;
      border-radius:50%;
      background:#fff1c9;
      z-index:0;
    }

    .hero-grid{
      position:relative;
      z-index:1;
      display:grid;
      grid-template-columns:.88fr 1.12fr;
      align-items:center;
      gap:58px;
    }

    .hero-copy{
      padding:8px 0 10px;
    }

    .eyebrow{
      width:max-content;
      max-width:100%;
      display:flex;
      align-items:center;
      gap:8px;
      padding:8px 14px;
      border-radius:999px;
      background:#fff5f3;
      color:#ef6670;
      font-size:13px;
      font-weight:800;
    }

    .eyebrow svg{
      width:15px;
      height:15px;
      fill:currentColor;
    }

    .hero h1{
      margin:22px 0 18px;
      font-size:67px;
      line-height:1.01;
      letter-spacing:-2.4px;
      font-weight:900;
    }

    .hero h1 .accent{
      color:var(--coral);
    }

    .hero-copy > p{
      max-width:535px;
      margin:0 0 29px;
      color:#626b78;
      font-size:16.5px;
      line-height:1.72;
    }

    .hero-actions{
      display:flex;
      flex-wrap:wrap;
      gap:18px;
    }

    .supporters{
      display:flex;
      align-items:center;
      gap:18px;
      margin-top:32px;
      color:#6e7682;
      font-size:13px;
    }

    .supporters strong{
      color:#515965;
      font-size:14px;
    }

    .avatar-stack{
      display:flex;
      padding-left:8px;
      flex:none;
    }

    .avatar-stack img{
      width:43px;
      height:43px;
      border-radius:50%;
      object-fit:cover;
      border:3px solid #fff;
      margin-left:-10px;
      box-shadow:0 2px 8px rgba(0,0,0,.07);
    }

    .hero-visual{
      position:relative;
      min-height:570px;
      display:flex;
      align-items:center;
    }

    .hero-image-shell{
      width:100%;
      height:540px;
      overflow:hidden;
      position:relative;
      border-radius:45% 0 0 45%;
      background:#e5f5f1;
    }

    .hero-image{
      height:100%;
      object-fit:cover;
      object-position:center;
    }

    .scribble{
      position:absolute;
      left:5%;
      top:0;
      z-index:2;
      color:#efc13b;
      font-size:48px;
      line-height:1;
      transform:rotate(-18deg);
      font-weight:900;
    }

    .smile-card{
      position:absolute;
      right:2%;
      bottom:30px;
      z-index:3;
      min-width:337px;
      display:grid;
      grid-template-columns:50px 1fr 28px;
      align-items:center;
      gap:14px;
      padding:24px 27px;
      border-radius:18px;
      background:#fff;
      color:#555e6a;
      font-size:14px;
      box-shadow:0 14px 36px rgba(33,55,60,.14);
    }

    .smile-icon{
      width:46px;
      height:46px;
      display:grid;
      place-items:center;
      border-radius:50%;
      background:var(--teal);
      color:#fff;
      font-size:25px;
    }

    .smile-card strong{
      color:var(--teal);
      font-size:16px;
      font-style:italic;
    }

    .tiny-heart{
      color:#efbf38;
      font-size:28px;
      transform:rotate(-15deg);
    }

    /* ---------------- SECTIONS ---------------- */
    .section{
      padding:68px 0;
    }

    .section-heading{
      text-align:center;
      margin-bottom:36px;
    }

    .section-heading span{
      display:block;
      color:var(--teal);
      font-size:11px;
      font-weight:900;
      letter-spacing:.55px;
    }

    .section-heading h2{
      margin:8px 0 0;
      font-size:35px;
      line-height:1.15;
      font-weight:900;
      letter-spacing:-.4px;
    }

    /* ---------------- MISSION ---------------- */
    .mission{
      position:relative;
      overflow:hidden;
      background:linear-gradient(180deg,#ffffff 0%,#fcfffe 100%);
    }

    .mission:after{
      content:"";
      position:absolute;
      right:-98px;
      bottom:-122px;
      width:270px;
      height:350px;
      border-radius:55% 0 0 0;
      background:#dbf4ee;
      transform:rotate(13deg);
    }

    .mission-grid{
      position:relative;
      z-index:2;
      display:grid;
      grid-template-columns:repeat(4,1fr);
      gap:20px;
    }

    .mission-card{
      min-height:266px;
      padding:18px 22px 20px;
      border-radius:19px;
      background:#fff;
      text-align:center;
    }

    .icon-circle{
      width:78px;
      height:78px;
      margin:0 auto 17px;
      display:grid;
      place-items:center;
      border-radius:50%;
    }

    .icon-circle svg{
      width:38px;
      height:38px;
      fill:none;
      stroke:currentColor;
      stroke-width:1.7;
      stroke-linecap:round;
      stroke-linejoin:round;
    }

    .mint{background:var(--mint);color:var(--teal);}
    .yellow{background:var(--yellow);color:#dfa926;}
    .lavender{background:var(--lavender);color:#9d61ad;}
    .pink{background:var(--pink);color:var(--coral);}

    .mission-card h3{
      margin:0 0 10px;
      font-size:16px;
      font-weight:900;
    }

    .mission-card p{
      max-width:220px;
      margin:0 auto;
      color:#6b7380;
      font-size:13.5px;
      line-height:1.62;
    }

    .mini-line{
      display:block;
      width:38px;
      height:3px;
      margin:19px auto 0;
      border-radius:10px;
    }

    .teal-line{background:var(--teal);}
    .yellow-line{background:#efbe39;}
    .lavender-line{background:#c16ed2;}
    .coral-line{background:var(--coral);}

    .decor-heart{
      position:absolute;
      z-index:1;
      font-size:43px;
      opacity:.52;
    }

    .decor-left{
      left:6%;
      top:50px;
      color:var(--coral);
      transform:rotate(-18deg);
    }

    .decor-right{
      right:7%;
      top:48px;
      color:var(--teal);
      transform:rotate(20deg);
    }

    /* ---------------- CAUSES ---------------- */
    .causes{
      padding-bottom:36px;
      background:var(--cream);
    }

    .cause-grid{
      display:grid;
      grid-template-columns:repeat(3,1fr);
      gap:26px;
    }

    .cause-card{
      overflow:hidden;
      border-radius:16px;
      background:#fff;
      box-shadow:0 8px 22px rgba(53,55,42,.055);
    }

    .cause-card > img{
      height:178px;
      object-fit:cover;
    }

    .cause-body{
      padding:17px 19px 20px;
    }

    .cause-body h3{
      margin:0 0 5px;
      font-size:17px;
      font-weight:900;
    }

    .cause-body p{
      min-height:42px;
      margin:0;
      color:#6d7480;
      font-size:13.5px;
      line-height:1.5;
    }

    .cause-footer{
      margin-top:17px;
      display:flex;
      align-items:flex-end;
      justify-content:space-between;
      gap:12px;
    }

    .cause-money{
      color:#7a818b;
      font-size:12px;
    }

    .cause-money strong{
      color:#252b37;
      font-size:13px;
    }

    .heart-btn{
      width:43px;
      height:43px;
      display:grid;
      place-items:center;
      flex:none;
      border:1px solid #ffb6bc;
      border-radius:12px;
      color:var(--coral);
      background:#fff;
      font-size:23px;
    }

    .progress{
      height:4px;
      margin-top:-5px;
      margin-right:63px;
      overflow:hidden;
      border-radius:7px;
      background:#dce9e7;
    }

    .progress span{
      display:block;
      height:100%;
      background:var(--teal);
    }

    .center{
      margin:32px 0 25px;
      text-align:center;
    }

    .view-more{
      min-height:49px;
      padding:0 28px;
    }

    /* ---------------- STATS ---------------- */
    .stats-strip{
      margin-top:17px;
      padding:21px 34px;
      display:grid;
      grid-template-columns:repeat(4,1fr);
      gap:18px;
      border-radius:14px;
      background:#edf9f6;
    }

    .stat-item{
      display:flex;
      align-items:center;
      gap:15px;
    }

    .stat-icon{
      width:58px;
      height:58px;
      display:grid;
      place-items:center;
      flex:none;
      border-radius:50%;
      font-size:24px;
      font-weight:900;
    }

    .stat-item strong{
      display:block;
      font-size:21px;
      font-weight:900;
      line-height:1.1;
    }

    .stat-item span{
      display:block;
      margin-top:4px;
      color:#626b76;
      font-size:12px;
    }

    /* ---------------- RESPONSIVE ---------------- */
    @media (max-width:1000px){
      .nav-links{gap:23px;}
      .hero-grid{grid-template-columns:1fr;gap:28px;}
      .hero-copy{text-align:center;}
      .eyebrow{margin:0 auto;}
      .hero-copy > p{margin-left:auto;margin-right:auto;}
      .hero-actions,.supporters{justify-content:center;}
      .hero-visual{min-height:500px;}
      .hero-image-shell{height:500px;border-radius:40px;}
      .mission-grid{grid-template-columns:repeat(2,1fr);}
      .stats-strip{grid-template-columns:repeat(2,1fr);}
    }

    @media (max-width:760px){
      .care-page .container{width:min(100% - 28px,1180px);}
      .nav-wrap{height:78px;}
      .nav-links{display:none;}
      .brand{min-width:auto;}
      .brand svg{width:46px;height:46px;}
      .brand-text{font-size:20px;}
      .nav-donate{min-height:44px;padding:0 18px;}
      .hero{padding-top:42px;}
      .hero h1{font-size:49px;}
      .hero-visual{min-height:420px;}
      .hero-image-shell{height:420px;}
      .smile-card{left:16px;right:16px;bottom:17px;min-width:0;padding:18px;}
      .mission-grid{grid-template-columns:1fr;}
      .cause-grid{grid-template-columns:1fr;}
      .stats-strip{grid-template-columns:1fr;padding:20px;}
    }

    @media (max-width:480px){
      .nav-donate{width:48px;padding:0;font-size:0;}
      .nav-donate .heart-only{font-size:22px;}
      .hero h1{font-size:40px;}
      .section-heading h2{font-size:29px;}
      .hero-image-shell{height:360px;}
      .hero-visual{min-height:360px;}
      .smile-card{grid-template-columns:42px 1fr;bottom:10px;}
      .tiny-heart{display:none;}
    }
    </style>

    <div class="care-page">

      <header class="care-header">
        <div class="container nav-wrap">
          <a class="brand" href="#home">
            <svg viewBox="0 0 64 64" aria-hidden="true">
              <circle cx="23" cy="10" r="6" fill="#0fa69c"/>
              <circle cx="43" cy="10" r="6" fill="#f45e68"/>
              <path d="M23 19 C10 18, 8 32, 17 40 C23 46, 30 52, 32 56 C33 48, 26 40, 23 34 C19 28, 18 23, 23 19Z" fill="#0fa69c"/>
              <path d="M43 19 C56 18, 58 32, 49 40 C43 46, 36 52, 32 56 C31 48, 38 40, 41 34 C45 28, 48 23, 43 19Z" fill="#f45e68"/>
              <path d="M29 27 C31 23, 34 23, 36 27 C38 30, 35 34, 32 37 C29 34, 27 30, 29 27Z" fill="#ffffff"/>
            </svg>
            <span class="brand-text">
              <span>care</span>
              <span>connect</span>
            </span>
          </a>

          <nav class="nav-links" aria-label="Primary navigation">
            <a class="active" href="#home">Home</a>
            <a href="#product">Product</a>
            <a href="#about">About Us</a>
            <a href="#contact">Contact</a>
          </nav>

          <a class="btn btn-coral nav-donate" href="#causes">
            Donate Us <span class="heart-only">♡</span>
          </a>
        </div>
      </header>

      <main>
        <section class="hero" id="home">
          <div class="container hero-grid">

            <div class="hero-copy">
              <div class="eyebrow">
                <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7-4.4-9.5-8.4C.7 9.5 2.4 5.5 6.1 5.1c2-.2 3.7.8 4.9 2.3 1.2-1.5 2.9-2.5 4.9-2.3 3.7.4 5.4 4.4 3.6 7.5C19 16.6 12 21 12 21z"/></svg>
                Together, We Can Make a Difference
              </div>

              <h1>
                Small Help,<br>
                <span class="accent">Big Change</span>
              </h1>

              <p>
                Care Connect is dedicated to helping the helpless, homeless, and elderly
                people live with dignity, love, and hope.
              </p>

              <div class="hero-actions">
                <a class="btn btn-teal" href="#causes">Donate Now <span>♡</span></a>
                <a class="btn btn-outline" href="#about">Learn More <span>→</span></a>
              </div>

              <div class="supporters">
                <div class="avatar-stack">
                  <img src="https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=100&q=85" alt="">
                  <img src="https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=100&q=85" alt="">
                  <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=100&q=85" alt="">
                  <img src="https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=100&q=85" alt="">
                </div>
                <div>
                  <strong>10,000+ People</strong><br>
                  <span>are already making a difference</span>
                </div>
              </div>
            </div>

            <div class="hero-visual">
              <div class="scribble">♡</div>

              <div class="hero-image-shell">
                <img
                  class="hero-image"
                  src="https://images.unsplash.com/photo-1488521787991-ed7bbaae773c?auto=format&fit=crop&w=1400&q=90"
                  alt="Child receiving care and support"
                >
              </div>

              <div class="smile-card">
                <div class="smile-icon">♡</div>
                <div>
                  Be the reason<br>
                  <strong>someone smiles today</strong>
                </div>
                <span class="tiny-heart">♡</span>
              </div>
            </div>

          </div>
        </section>

        <section class="mission section" id="about">
          <div class="container">

            <div class="section-heading">
              <span>WHAT WE DO</span>
              <h2>Our Mission is Simple</h2>
            </div>

            <div class="mission-grid">

              <article class="mission-card">
                <div class="icon-circle mint">
                  <svg viewBox="0 0 48 48">
                    <path d="M7 28c7 0 10-5 15-5 4 0 6 2 6 5 0 3-2 5-6 5h-6"/>
                    <path d="M7 28v10h14c8 0 13-6 20-12"/>
                    <path d="M25 13c0-5 7-7 10-2 3-5 10-3 10 2 0 7-10 12-10 12S25 20 25 13z"/>
                  </svg>
                </div>
                <h3>Help the Helpless</h3>
                <p>We reach out to those in need and provide food, shelter, and support.</p>
                <i class="mini-line teal-line"></i>
              </article>

              <article class="mission-card">
                <div class="icon-circle yellow">
                  <svg viewBox="0 0 48 48">
                    <path d="M6 22L24 8l18 14"/>
                    <path d="M10 20v20h28V20"/>
                    <path d="M18 30c0-5 6-6 8-2 2-4 8-3 8 2 0 5-8 9-8 9s-8-4-8-9z"/>
                  </svg>
                </div>
                <h3>Support the Homeless</h3>
                <p>We work to provide shelter, care, and new beginnings for the homeless.</p>
                <i class="mini-line yellow-line"></i>
              </article>

              <article class="mission-card">
                <div class="icon-circle lavender">
                  <svg viewBox="0 0 48 48">
                    <circle cx="18" cy="18" r="6"/>
                    <circle cx="31" cy="18" r="6"/>
                    <path d="M8 39c1-8 5-12 10-12s9 4 10 12"/>
                    <path d="M23 39c1-8 4-12 9-12 5 0 8 4 9 12"/>
                    <path d="M13 14c1-5 4-8 7-8"/>
                    <path d="M27 14c1-5 4-8 7-8"/>
                  </svg>
                </div>
                <h3>Care for the Elderly</h3>
                <p>We bring comfort, respect, and love to our senior citizens.</p>
                <i class="mini-line lavender-line"></i>
              </article>

              <article class="mission-card">
                <div class="icon-circle pink">
                  <svg viewBox="0 0 48 48">
                    <circle cx="24" cy="13" r="5"/>
                    <circle cx="11" cy="19" r="4"/>
                    <circle cx="37" cy="19" r="4"/>
                    <path d="M15 39c0-9 4-14 9-14s9 5 9 14"/>
                    <path d="M3 39c0-7 3-11 8-11 3 0 5 2 7 5"/>
                    <path d="M45 39c0-7-3-11-8-11-3 0-5 2-7 5"/>
                  </svg>
                </div>
                <h3>Build a Better Tomorrow</h3>
                <p>Together with kind hearts like you, we build a more compassionate world.</p>
                <i class="mini-line coral-line"></i>
              </article>

            </div>
          </div>

          <span class="decor-heart decor-left">♡</span>
          <span class="decor-heart decor-right">♡</span>
        </section>

        <section class="causes section" id="causes">
          <div class="container">

            <div class="section-heading">
              <span>FEATURED CAUSES</span>
              <h2>Every Contribution Counts</h2>
            </div>

            <div class="cause-grid">

              <article class="cause-card">
                <img
                  src="https://images.unsplash.com/photo-1509099836639-18ba1795216d?auto=format&fit=crop&w=900&q=85"
                  alt="Helping children with food"
                >
                <div class="cause-body">
                  <h3>Feed the Hungry</h3>
                  <p>Provide meals to homeless and helpless people.</p>
                  <div class="cause-footer">
                    <div class="cause-money"><strong>$4,250</strong> raised of $7,000</div>
                    <div class="heart-btn">♡</div>
                  </div>
                  <div class="progress"><span style="width:61%"></span></div>
                </div>
              </article>

              <article class="cause-card">
                <img
                  src="https://images.unsplash.com/photo-1469571486292-0ba58a3f068b?auto=format&fit=crop&w=900&q=85"
                  alt="Volunteer helping an elderly person"
                >
                <div class="cause-body">
                  <h3>Warmth for the Elderly</h3>
                  <p>Help us provide warm clothing and essential items.</p>
                  <div class="cause-footer">
                    <div class="cause-money"><strong>$3,120</strong> raised of $5,000</div>
                    <div class="heart-btn">♡</div>
                  </div>
                  <div class="progress"><span style="width:62%"></span></div>
                </div>
              </article>

              <article class="cause-card">
                <img
                  src="https://images.unsplash.com/photo-1542810634-71277d95dcbb?auto=format&fit=crop&w=900&q=85"
                  alt="Shelter support for families"
                >
                <div class="cause-body">
                  <h3>Shelter for the Homeless</h3>
                  <p>Help us build safe and secure shelters.</p>
                  <div class="cause-footer">
                    <div class="cause-money"><strong>$6,780</strong> raised of $10,000</div>
                    <div class="heart-btn">♡</div>
                  </div>
                  <div class="progress"><span style="width:68%"></span></div>
                </div>
              </article>

            </div>

            <div class="center">
              <a class="btn btn-teal view-more" href="#causes">
                View More Causes <span>→</span>
              </a>
            </div>

            <div class="stats-strip">

              <div class="stat-item">
                <div class="stat-icon mint">♧</div>
                <div>
                  <strong>25,000+</strong>
                  <span>Lives Impacted</span>
                </div>
              </div>

              <div class="stat-item">
                <div class="stat-icon yellow">♧</div>
                <div>
                  <strong>1,200+</strong>
                  <span>Volunteers</span>
                </div>
              </div>

              <div class="stat-item">
                <div class="stat-icon lavender">▣</div>
                <div>
                  <strong>500+</strong>
                  <span>Projects Completed</span>
                </div>
              </div>

              <div class="stat-item">
                <div class="stat-icon pink">♡</div>
                <div>
                  <strong>100%</strong>
                  <span>Transparency</span>
                </div>
              </div>

            </div>
          </div>
        </section>
      </main>
    </div>
    """

    # st.html renders raw HTML directly instead of Markdown.
    # This is the important fix: Streamlit will no longer show the HTML
    # as black code blocks like in the screenshot.
    if hasattr(st, "html"):
        st.html(page)
    else:
        # Fallback for older Streamlit versions.
        # The string starts at column 0, so Markdown won't interpret it
        # as an indented code block.
        st.markdown(page, unsafe_allow_html=True)
