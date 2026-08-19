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
      --mint:#eaf8f5;
      --mint-2:#dff5ef;
      --yellow:#fff0c8;
      --pink:#fff0f1;
      --line:#e7efed;
      --white:#ffffff;
    }

    *{box-sizing:border-box;}
    html{scroll-behavior:smooth;}

    .donate-page{
      margin:0;
      width:100%;
      overflow:hidden;
      font-family:"Nunito",sans-serif;
      color:var(--ink);
      background:#fff;
      line-height:1.5;
    }

    .donate-page a{
      color:inherit;
      text-decoration:none;
    }

    .donate-container{
      width:min(1180px, calc(100% - 56px));
      margin:0 auto;
    }

    /* HEADER */
    .donate-header{
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

    .nav-links a:hover{
      color:var(--teal-dark);
    }

    .donate-active{
      min-height:54px;
      display:inline-flex;
      align-items:center;
      justify-content:center;
      gap:10px;
      padding:0 27px;
      border-radius:14px;
      color:#fff !important;
      background:linear-gradient(135deg,#ff6973,#ef505e);
      box-shadow:0 10px 24px rgba(244,94,104,.18);
      font-size:15px;
      font-weight:800;
    }

    /* HERO */
    .donate-hero{
      position:relative;
      padding:70px 0 54px;
      background:
        radial-gradient(circle at 92% 12%, #fff2cb 0 145px, transparent 146px),
        linear-gradient(180deg,#fff 0%,#fbfffe 100%);
    }

    .hero-grid{
      display:grid;
      grid-template-columns:1fr .95fr;
      gap:60px;
      align-items:center;
    }

    .hero-pill{
      width:max-content;
      display:inline-flex;
      align-items:center;
      gap:8px;
      padding:8px 14px;
      border-radius:999px;
      background:#fff3f1;
      color:var(--coral);
      font-size:13px;
      font-weight:800;
    }

    .hero-copy h1{
      margin:20px 0 18px;
      max-width:640px;
      font-size:62px;
      line-height:1.04;
      letter-spacing:-2.1px;
      font-weight:900;
    }

    .hero-copy h1 span{
      color:var(--coral);
    }

    .hero-copy p{
      max-width:600px;
      margin:0;
      color:#626b78;
      font-size:17px;
      line-height:1.72;
    }

    .hero-note{
      margin-top:26px;
      max-width:585px;
      display:flex;
      align-items:flex-start;
      gap:13px;
      padding:17px 18px;
      border-radius:15px;
      background:var(--mint);
      color:#53606b;
      font-size:13px;
      line-height:1.55;
    }

    .hero-note-icon{
      width:40px;
      height:40px;
      display:grid;
      place-items:center;
      flex:none;
      border-radius:50%;
      background:var(--teal);
      color:#fff;
      font-size:22px;
    }

    .hero-note strong{
      display:block;
      color:var(--teal-dark);
      margin-bottom:2px;
      font-size:14px;
    }

    .impact-card{
      position:relative;
      min-height:390px;
      display:flex;
      align-items:center;
      justify-content:center;
    }

    .impact-blob{
      position:absolute;
      width:350px;
      height:350px;
      border-radius:46% 54% 57% 43% / 50% 41% 59% 50%;
      background:linear-gradient(135deg,#dff5ef,#f8e4e7);
      transform:rotate(-7deg);
    }

    .impact-box{
      position:relative;
      z-index:2;
      width:min(390px,90%);
      padding:34px 32px;
      border-radius:24px;
      background:#fff;
      box-shadow:0 20px 60px rgba(31,64,65,.13);
      text-align:center;
    }

    .impact-heart{
      width:72px;
      height:72px;
      display:grid;
      place-items:center;
      margin:0 auto 18px;
      border-radius:50%;
      background:#fff0f1;
      color:var(--coral);
      font-size:39px;
    }

    .impact-box h3{
      margin:0 0 9px;
      font-size:24px;
      font-weight:900;
    }

    .impact-box p{
      margin:0;
      color:#68717e;
      font-size:14px;
      line-height:1.6;
    }

    /* ACCOUNT SECTION */
    .account-section{
      padding:60px 0 72px;
      background:var(--cream);
    }

    .section-heading{
      text-align:center;
      margin-bottom:32px;
    }

    .section-heading span{
      display:block;
      color:var(--teal);
      font-size:11px;
      font-weight:900;
      letter-spacing:.7px;
    }

    .section-heading h2{
      margin:8px 0 8px;
      font-size:36px;
      line-height:1.15;
      font-weight:900;
    }

    .section-heading p{
      max-width:675px;
      margin:0 auto;
      color:#6b7380;
      font-size:14px;
      line-height:1.65;
    }

    .bank-shell{
      width:min(820px,100%);
      margin:0 auto;
      overflow:hidden;
      border:1px solid #e7eceb;
      border-radius:22px;
      background:#fff;
      box-shadow:0 14px 38px rgba(48,57,50,.07);
    }

    .bank-head{
      display:flex;
      align-items:center;
      justify-content:space-between;
      gap:20px;
      padding:24px 29px;
      color:#fff;
      background:linear-gradient(135deg,#11aaa0,#078d85);
    }

    .bank-head-left{
      display:flex;
      align-items:center;
      gap:15px;
    }

    .bank-icon{
      width:53px;
      height:53px;
      display:grid;
      place-items:center;
      border-radius:15px;
      background:rgba(255,255,255,.15);
      font-size:27px;
    }

    .bank-head strong{
      display:block;
      font-size:20px;
      font-weight:900;
    }

    .bank-head span{
      display:block;
      margin-top:2px;
      color:rgba(255,255,255,.82);
      font-size:12px;
    }

    .currency-badge{
      padding:7px 13px;
      border-radius:999px;
      background:#fff;
      color:var(--teal-dark);
      font-size:12px;
      font-weight:900;
    }

    .bank-body{
      padding:26px 29px 30px;
    }

    .detail-grid{
      display:grid;
      grid-template-columns:1fr 1fr;
      gap:14px;
    }

    .detail-card{
      padding:16px 18px;
      border:1px solid #e9eeee;
      border-radius:13px;
      background:#fbfdfd;
    }

    .detail-card.full{
      grid-column:1 / -1;
    }

    .detail-label{
      display:block;
      margin-bottom:5px;
      color:#8a929c;
      font-size:10.5px;
      font-weight:900;
      letter-spacing:.55px;
      text-transform:uppercase;
    }

    .detail-value{
      color:#25303d;
      font-size:16px;
      font-weight:800;
      overflow-wrap:anywhere;
    }

    .detail-value.number{
      font-size:19px;
      letter-spacing:.5px;
    }

    .transfer-notice{
      margin-top:19px;
      display:flex;
      align-items:flex-start;
      gap:12px;
      padding:15px 17px;
      border-radius:13px;
      background:#fff4e4;
      color:#6d6255;
      font-size:12.5px;
      line-height:1.55;
    }

    .notice-mark{
      width:29px;
      height:29px;
      display:grid;
      place-items:center;
      flex:none;
      border-radius:50%;
      background:#f3bd4a;
      color:#fff;
      font-weight:900;
    }

    /* HOW IT HELPS */
    .help-section{
      padding:64px 0;
      background:#fff;
    }

    .help-grid{
      display:grid;
      grid-template-columns:repeat(3,1fr);
      gap:20px;
    }

    .help-card{
      padding:25px 23px;
      border:1px solid #e9eeee;
      border-radius:17px;
      text-align:center;
      background:#fff;
    }

    .help-icon{
      width:65px;
      height:65px;
      display:grid;
      place-items:center;
      margin:0 auto 14px;
      border-radius:50%;
      font-size:29px;
    }

    .mint{background:#def5ef;color:var(--teal);}
    .yellow{background:#fff0c8;color:#dfa926;}
    .pink{background:#ffe3e1;color:var(--coral);}

    .help-card h3{
      margin:0 0 8px;
      font-size:16px;
      font-weight:900;
    }

    .help-card p{
      margin:0;
      color:#707985;
      font-size:12.5px;
      line-height:1.55;
    }

    .footer-message{
      margin-top:27px;
      padding:22px 26px;
      border-radius:16px;
      background:var(--mint);
      text-align:center;
    }

    .footer-message strong{
      color:var(--teal-dark);
      font-size:18px;
    }

    .footer-message p{
      margin:4px auto 0;
      max-width:700px;
      color:#63707b;
      font-size:12.5px;
      line-height:1.55;
    }

    @media (max-width:900px){
      .nav-links{gap:24px;}
      .hero-grid{grid-template-columns:1fr;}
      .hero-copy{text-align:center;}
      .hero-pill{margin:0 auto;}
      .hero-copy p,.hero-note{margin-left:auto;margin-right:auto;}
      .impact-card{min-height:340px;}
      .help-grid{grid-template-columns:1fr;}
    }

    @media (max-width:760px){
      .donate-container{width:min(100% - 28px,1180px);}
      .nav-wrap{height:78px;}
      .nav-links{display:none;}
      .brand{min-width:auto;}
      .brand svg{width:46px;height:46px;}
      .brand-text{font-size:20px;}
      .donate-active{min-height:44px;padding:0 17px;}
      .hero-copy h1{font-size:45px;}
      .detail-grid{grid-template-columns:1fr;}
      .detail-card.full{grid-column:auto;}
      .bank-head{padding:20px;}
      .bank-body{padding:20px;}
    }

    @media (max-width:480px){
      .donate-active{width:48px;padding:0;font-size:0;}
      .donate-active span{font-size:22px;}
      .hero-copy h1{font-size:38px;}
      .section-heading h2{font-size:29px;}
      .currency-badge{display:none;}
    }
    </style>

    <div class="donate-page">

      <header class="donate-header">
        <div class="donate-container nav-wrap">

          <a class="brand" href="?page=home">
            <svg viewBox="0 0 64 64" aria-hidden="true">
              <circle cx="23" cy="10" r="6" fill="#0fa69c"/>
              <circle cx="43" cy="10" r="6" fill="#f45e68"/>
              <path d="M23 19 C10 18, 8 32, 17 40 C23 46, 30 52, 32 56 C33 48, 26 40, 23 34 C19 28, 18 23, 23 19Z" fill="#0fa69c"/>
              <path d="M43 19 C56 18, 58 32, 49 40 C43 46, 36 52, 32 56 C31 48, 38 40, 41 34 C45 28, 48 23, 43 19Z" fill="#f45e68"/>
              <path d="M29 27 C31 23, 34 23, 36 27 C38 30, 35 34, 32 37 C29 34, 27 30, 29 27Z" fill="#fff"/>
            </svg>

            <span class="brand-text">
              <span>care</span>
              <span>connect</span>
            </span>
          </a>

          <nav class="nav-links">
            <a href="?page=home">Home</a>
            <a href="?page=product">Product</a>
            <a href="?page=home#about">About Us</a>
            <a href="?page=home#contact">Contact</a>
          </nav>

          <a class="donate-active" href="?page=donate">
            Donate Us <span>♡</span>
          </a>
        </div>
      </header>

      <main>

        <section class="donate-hero">
          <div class="donate-container hero-grid">

            <div class="hero-copy">
              <div class="hero-pill">♥ &nbsp; Give with Purpose</div>

              <h1>
                Your Donation Can<br>
                <span>Change a Life</span>
              </h1>

              <p>
                Every contribution helps us provide care, food, shelter, dignity, and hope
                to people who need support. Your kindness becomes direct help for someone in need.
              </p>

              <div class="hero-note">
                <div class="hero-note-icon">♡</div>
                <div>
                  <strong>Direct support through your generosity</strong>
                  Use the Philippine Peso account details below to make a domestic transfer
                  from a bank in the Philippines.
                </div>
              </div>
            </div>

            <div class="impact-card">
              <div class="impact-blob"></div>

              <div class="impact-box">
                <div class="impact-heart">♡</div>
                <h3>Give Hope. Share Care.</h3>
                <p>
                  Your donation supports the mission of Care Connect and helps create
                  meaningful assistance for helpless, homeless, elderly, and needy people.
                </p>
              </div>
            </div>

          </div>
        </section>

        <section class="account-section">
          <div class="donate-container">

            <div class="section-heading">
              <span>DONATION ACCOUNT</span>
              <h2>Donate by Bank Transfer</h2>
              <p>
                For domestic transfers from a bank in the Philippines, please use the
                Wise Pilipinas Inc. account details below exactly as shown.
              </p>
            </div>

            <div class="bank-shell">

              <div class="bank-head">
                <div class="bank-head-left">
                  <div class="bank-icon">🏦</div>
                  <div>
                    <strong>Philippine Bank Transfer</strong>
                    <span>Wise Pilipinas Inc.</span>
                  </div>
                </div>

                <div class="currency-badge">PHP</div>
              </div>

              <div class="bank-body">

                <div class="detail-grid">

                  <div class="detail-card full">
                    <span class="detail-label">Account Holder Name</span>
                    <div class="detail-value">JESEL JEAN DABALOS BASALO</div>
                  </div>

                  <div class="detail-card">
                    <span class="detail-label">Account Number</span>
                    <div class="detail-value number">2009905998</div>
                  </div>

                  <div class="detail-card">
                    <span class="detail-label">Bank Code / BRSTN</span>
                    <div class="detail-value number">01828-001-6</div>
                  </div>

                  <div class="detail-card full">
                    <span class="detail-label">Bank Name</span>
                    <div class="detail-value">Wise Pilipinas Inc.</div>
                  </div>

                </div>

                <div class="transfer-notice">
                  <div class="notice-mark">i</div>
                  <div>
                    These details are intended for a <strong>domestic PHP transfer from a bank in the Philippines.</strong>
                    Please review the account name, number, bank code, and bank name carefully before confirming your transfer.
                  </div>
                </div>

              </div>
            </div>

          </div>
        </section>

        <section class="help-section">
          <div class="donate-container">

            <div class="section-heading">
              <span>YOUR IMPACT</span>
              <h2>What Your Support Helps Provide</h2>
            </div>

            <div class="help-grid">

              <article class="help-card">
                <div class="help-icon mint">♡</div>
                <h3>Care &amp; Essential Support</h3>
                <p>Help provide basic assistance and compassionate support for people facing hardship.</p>
              </article>

              <article class="help-card">
                <div class="help-icon yellow">⌂</div>
                <h3>Food &amp; Shelter</h3>
                <p>Your contribution can support efforts to provide meals, shelter, and essential needs.</p>
              </article>

              <article class="help-card">
                <div class="help-icon pink">♥</div>
                <h3>Dignity &amp; Hope</h3>
                <p>Every act of kindness helps people feel seen, supported, respected, and hopeful.</p>
              </article>

            </div>

            <div class="footer-message">
              <strong>Thank you for choosing to help.</strong>
              <p>
                Every donation matters. Together, small acts of generosity can create meaningful
                change for people who need care and support.
              </p>
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
