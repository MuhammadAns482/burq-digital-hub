from pathlib import Path
import os
import urllib.parse
import requests
from bs4 import BeautifulSoup
import streamlit as st

# ── Page Configuration ───────────────────────────────────────────────────────
st.set_page_config(
    page_title="BURQ DIGITAL HUB — AI Agency Suite",
    page_icon="⚡",
    layout="wide",
)

# ── Ultra-Premium SaaS Glassmorphism CSS ────────────────────────────────────
BURQ_THEME_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"], .stApp {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        background-color: #030712 !important;
        background-image: 
            radial-gradient(at 15% 15%, rgba(0, 132, 255, 0.12) 0px, transparent 50%),
            radial-gradient(at 85% 85%, rgba(0, 210, 255, 0.08) 0px, transparent 50%) !important;
        color: #F8FAFC !important;
    }

    .main .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 3.5rem !important;
        max-width: 1050px !important;
    }

    h1 {
        background: linear-gradient(135deg, #FFFFFF 30%, #00D2FF 100%);
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        font-weight: 800 !important;
        text-align: center;
    }

    h2, h3, h4 {
        color: #00D2FF !important;
        font-weight: 700 !important;
    }

    .sub-title {
        color: #94A3B8 !important;
        text-align: center;
        margin-bottom: 1.8rem;
        font-size: 0.95rem;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        font-weight: 600;
    }

    p, span, label, li, .stMarkdown {
        color: #E2E8F0 !important;
    }

    .stTabs [data-baseweb="tab-list"] {
        background: rgba(15, 23, 42, 0.7) !important;
        backdrop-filter: blur(10px) !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        border-radius: 12px !important;
        padding: 6px !important;
        gap: 6px !important;
        margin-bottom: 1.5rem !important;
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: 8px !important;
        color: #94A3B8 !important;
        font-weight: 600 !important;
        padding: 8px 14px !important;
        border: none !important;
        font-size: 0.9rem !important;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(0, 132, 255, 0.25) 0%, rgba(0, 82, 204, 0.25) 100%) !important;
        color: #00D2FF !important;
        border: 1px solid rgba(0, 210, 255, 0.35) !important;
    }

    input, textarea, select, [data-testid="stChatInput"] textarea {
        background-color: rgba(9, 14, 26, 0.8) !important;
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
        border: 1px solid rgba(0, 132, 255, 0.3) !important;
        border-radius: 10px !important;
        padding: 10px 12px !important;
    }

    input:focus, textarea:focus {
        border-color: #00D2FF !important;
        box-shadow: 0 0 0 3px rgba(0, 132, 255, 0.3) !important;
    }

    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #0084FF 0%, #0052CC 100%) !important;
        color: #FFFFFF !important;
        border: 1px solid rgba(0, 210, 255, 0.4) !important;
        border-radius: 10px !important;
        font-weight: 700 !important;
        padding: 0.65rem 1.2rem !important;
        box-shadow: 0 4px 18px rgba(0, 132, 255, 0.3) !important;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #0095FF 0%, #0066FF 100%) !important;
        box-shadow: 0 6px 25px rgba(0, 210, 255, 0.5) !important;
    }

    [data-testid="stMetricValue"] {
        color: #00D2FF !important;
        font-weight: 800 !important;
    }

    [data-testid="stAlert"] {
        background: rgba(13, 25, 48, 0.6) !important;
        border: 1px solid rgba(0, 132, 255, 0.3) !important;
        border-left: 4px solid #00D2FF !important;
        border-radius: 10px !important;
    }

    a {
        color: #00D2FF !important;
        font-weight: 600;
        text-decoration: none;
    }
</style>
"""
st.markdown(BURQ_THEME_CSS, unsafe_allow_html=True)

# ── App Header ───────────────────────────────────────────────────────────────
logo_file = "logo.png" if Path("logo.png").exists() else ("logo.png.png" if Path("logo.png.png").exists() else None)
if logo_file:
    c1, c2, c3 = st.columns([1.5, 1, 1.5])
    with c2:
        st.image(logo_file, use_container_width=True)
else:
    st.markdown("<div style='text-align: center; font-size: 3rem;'>⚡</div>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>BURQ DIGITAL HUB</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>B2B CLIENT HUNTER • GROWTH SUITE • SAAS PLATFORM</p>", unsafe_allow_html=True)

# ── All Tabs Definition ──────────────────────────────────────────────────────
tabs = st.tabs([
    "🎯 Client Hunter",
    "📊 ROAS Calculator",
    "✍️ Ad Copy Studio",
    "🛠️ Meta Audit Checklist",
    "📦 COD Loss Minimizer",
    "📲 WhatsApp Linker",
    "🎓 Skill Roadmap",
    "🌐 Website Auditor",
    "📢 Meta Ad Spy"
])

# ─────────────────────────────────────────────────────────────────────────────
# 1. B2B LOCAL CLIENT HUNTER (WhatsApp & Social Extractor)
# ─────────────────────────────────────────────────────────────────────────────
with tabs[0]:
    st.subheader("🎯 Local B2B Client Hunter (High-Ticket Lead Discovery)")
    st.write("Apni digital marketing agency ke liye kisi bhi city ke local businesses, social media pages aur unke direct WhatsApp numbers dhoondein.")

    c_niche, c_city = st.columns(2)
    with c_niche:
        niche_input = st.text_input("Business Niche / Category", placeholder="e.g. Clothing Brands, Real Estate, Dental Clinics, Cafes")
    with c_city:
        city_input = st.text_input("Target City", placeholder="e.g. Faisalabad, Lahore, Karachi, Islamabad")

    if st.button("Hunt Local Businesses & Contacts"):
        if not niche_input.strip() or not city_input.strip():
            st.warning("Niche aur City dono likhein.")
        else:
            q_niche = niche_input.strip()
            q_city = city_input.strip()
            
            # Deep Search URLs
            maps_url = f"https://www.google.com/maps/search/{urllib.parse.quote(q_niche + ' in ' + q_city)}"
            insta_wa_url = f"https://www.google.com/search?q={urllib.parse.quote('site:instagram.com \"' + q_niche + '\" \"' + q_city + '\" (\"03\" OR \"+92\")')}"
            fb_url = f"https://www.google.com/search?q={urllib.parse.quote('site:facebook.com \"' + q_niche + '\" \"' + q_city + '\"')}"
            linkedin_url = f"https://www.google.com/search?q={urllib.parse.quote('site:linkedin.com/company \"' + q_niche + '\" \"' + q_city + '\"')}"

            st.success(f"'{q_niche}' in '{q_city}' ke liye high-intent lead sources generate ho chuki hain! ✅")
            
            st.markdown(f"""
            ### 📍 Direct Business Discovery Links:
            1. 🗺️ **[Google Maps Active Businesses in {q_city}]({maps_url})**  
               *(Tamam registered shops, phone numbers, customer reviews aur location yahan milegi)*
            2. 📱 **[Instagram Profiles with Direct WhatsApp Numbers ({q_city})]({insta_wa_url})**  
               *(Yeh link direct un brands ke Instagram pages nikalega jinki bio mein phone/WhatsApp likha hai)*
            3. 👥 **[Facebook Business Pages in {q_city}]({fb_url})**  
               *(Unke official pages aur direct chat options)*
            4. 💼 **[LinkedIn Corporate Profiles]({linkedin_url})**  
               *(Business owners aur decision makers se connect karne ke liye)*

            ---
            ### 💬 Ready-Made WhatsApp Outreach Script (Copy & Send):
            ```text
            Assalam-o-Alaikum! 

            Main Burq Digital Hub ki team se hoon. Humne {q_city} mein aapka brand collection dekha, zabardast work hai! 

            Lekin aapki online presence aur Meta Ads funnel optimize na hone ki wajah se aap monthly bohot se orders miss kar rahe hain. 

            Kya hum 5 minute ki quick call par discuss kar sakte hain ke aapke brand ki monthly sales ko 2x kaise kiya jaye?
            ```
            """)

# ─────────────────────────────────────────────────────────────────────────────
# 2. ROAS & AD PROFITABILITY CALCULATOR
# ─────────────────────────────────────────────────────────────────────────────
with tabs[1]:
    st.subheader("📊 Media Buying ROAS & Profitability Engine")
    st.write("Ads chalane se pehle apna Break-even ROAS aur Net Profit calculate karein.")

    col_r1, col_r2 = st.columns(2)
    with col_r1:
        selling_price = st.number_input("Product Selling Price (PKR)", value=3000, step=100)
        product_cost = st.number_input("Product Sourcing Cost (PKR)", value=1200, step=100)
        courier_charge = st.number_input("Courier Fee per Order (PKR)", value=250, step=50)
    with col_r2:
        ad_spend = st.number_input("Total Ad Budget (PKR)", value=15000, step=1000)
        expected_orders = st.number_input("Expected Orders", value=15, step=1)
        rto_percent = st.slider("Expected Return / Cancellation %", 0, 50, 15)

    if st.button("Calculate Ad Profit & Break-Even"):
        margin_per_order = selling_price - product_cost - courier_charge
        break_even_roas = (selling_price / margin_per_order) if margin_per_order > 0 else 0
        actual_delivered = expected_orders * (1 - (rto_percent / 100))
        total_revenue = actual_delivered * selling_price
        total_cog = actual_delivered * (product_cost + courier_charge)
        net_profit = total_revenue - total_cog - ad_spend
        actual_roas = (total_revenue / ad_spend) if ad_spend > 0 else 0

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Break-Even ROAS", f"{break_even_roas:.2f}x")
        m2.metric("Projected ROAS", f"{actual_roas:.2f}x")
        m3.metric("Delivered Orders", f"{int(actual_delivered)}")
        m4.metric("Estimated Net Profit", f"PKR {net_profit:,.0f}")

        if net_profit > 0:
            st.success("Ye campaign profitable rahegi! ✅")
        else:
            st.error("Warning: Is setup mein loss ka khatra hai. Sourcing ya Ad target optimize karein! ❌")

# ─────────────────────────────────────────────────────────────────────────────
# 3. HIGH-CONVERTING AD COPY STUDIO
# ─────────────────────────────────────────────────────────────────────────────
with tabs[2]:
    st.subheader("✍️ High-Converting Ad Copy & Hook Studio")
    product_name = st.text_input("Product / Service Name", placeholder="e.g. Premium Leather Wallets")
    offer_details = st.text_input("Offer / Discount", placeholder="e.g. Flat 30% Off + Free Delivery")

    if st.button("Generate Ad Copies & Hooks"):
        if not product_name.strip():
            st.warning("Product ka naam likhein.")
        else:
            st.markdown(f"""
            ### 🔥 Viral Hooks (For Reels & TikTok Ads):
            1. *"Stop wasting money on cheap alternatives—yeh check karein!"*
            2. *"{product_name} jo aapke daily lifestyle ko upgrade kar dega."*
            3. *"Kya aap bhi is common issue se pareshan hain? Here is the exact fix."*

            ---
            ### 📜 Primary Ad Caption (Meta Ads):
            Looking for the perfect **{product_name}**? ✨  
            Aapki talash yahan khatam hoti hai! Premium quality, verified durability, aur ab mil raha hai special discount par.

            ⚡ **Limited Time Offer:** {offer_details}  
            🚚 **Cash On Delivery Available Nationwide**  
            👉 Click 'Order Now' button to claim yours before stock runs out!

            ---
            ### 🎯 High-CTR Headlines:
            * `⚡ {product_name} - Flat Discount Today Only!`
            * `🔥 Premium Quality Guaranteed | Cash On Delivery`
            """)

# ─────────────────────────────────────────────────────────────────────────────
# 4. META ADS READINESS CHECKLIST
# ─────────────────────────────────────────────────────────────────────────────
with tabs[3]:
    st.subheader("🛠️ Meta Ads Client Technical Audit Checklist")
    st.write("Client ko onboard karne se pehle technical setup verify karein:")

    c_box1 = st.checkbox("Meta Pixel installed and firing correctly on store")
    c_box2 = st.checkbox("Domain verified inside Meta Business Manager")
    c_box3 = st.checkbox("Aggregated Event Measurement (Purchase, Lead) configured")
    c_box4 = st.checkbox("Catalog sync active with Shopify / Website")
    c_box5 = st.checkbox("Fast loading speed on mobile (< 3 seconds)")
    c_box6 = st.checkbox("Clear WhatsApp Chat button present on store")

    score = sum([c_box1, c_box2, c_box3, c_box4, c_box5, c_box6]) * (100 / 6)
    st.progress(score / 100)
    st.metric("Store Ads Readiness Score", f"{int(score)}%")

    if score == 100:
        st.success("Setup complete hai! Store ads scale karne ke liye tayyar hai. 🚀")
    else:
        st.info("Kuch points baki hain. Inhe theek kar ke ads ki conversion rate barhayen.")

# ─────────────────────────────────────────────────────────────────────────────
# 5. COD LOSS MINIMIZER
# ─────────────────────────────────────────────────────────────────────────────
with tabs[4]:
    st.subheader("📦 Cash-on-Delivery (COD) Loss Calculator")
    tot_orders = st.number_input("Total Dispatched Orders", value=100, step=10)
    ret_orders = st.number_input("Returned / Cancelled Orders", value=20, step=5)
    courier_cost_per_return = st.number_input("Courier return penalty per parcel (PKR)", value=350, step=50)

    if st.button("Calculate Delivery Losses"):
        loss_val = ret_orders * courier_cost_per_return
        rto_rate = (ret_orders / tot_orders * 100) if tot_orders > 0 else 0
        
        c1, c2 = st.columns(2)
        c1.metric("Return Ratio (RTO)", f"{rto_rate:.1f}%")
        c2.metric("Direct Courier Loss", f"PKR {loss_val:,.0f}")
        
        st.markdown("""
        💡 **Burq Digital Hub Pro-Tip to Reduce RTO:**
        * Orders bhejne se pehle automated WhatsApp audio/text confirmation lein.
        * Fake / incomplete address walay parcels dispatch na karein.
        """)

# ─────────────────────────────────────────────────────────────────────────────
# 6. INSTANT WHATSAPP LINK GENERATOR
# ─────────────────────────────────────────────────────────────────────────────
with tabs[5]:
    st.subheader("📲 Instant WhatsApp Direct Lead Linker")
    wa_num = st.text_input("WhatsApp Number (with Country Code, no spaces)", placeholder="e.g. 923001234567")
    wa_msg = st.text_area("Pre-filled Message", placeholder="e.g. Hello Burq Digital Hub, I want to grow my business online.")

    if st.button("Generate Clickable WhatsApp Link"):
        if not wa_num.strip():
            st.warning("Number enter karein.")
        else:
            clean_num = wa_num.replace("+", "").replace("-", "").replace(" ", "")
            enc_msg = urllib.parse.quote(wa_msg)
            wa_link = f"https://wa.me/{clean_num}?text={enc_msg}"
            st.success("WhatsApp Link Ready! ✅")
            st.code(wa_link, language="text")
            st.markdown(f"👉 **[Test Link Directly on WhatsApp]({wa_link})**")

# ─────────────────────────────────────────────────────────────────────────────
# 7. SKILL & COURSE ROADMAP (Purana Feature)
# ─────────────────────────────────────────────────────────────────────────────
with tabs[6]:
    st.subheader("🎓 Free Learning & Skill Roadmap Finder")
    course_query = st.text_input("Skill / Course", placeholder="e.g. Meta Ads, Shopify, Python")
    if st.button("Search Roadmaps"):
        if course_query:
            enc = urllib.parse.quote(course_query)
            st.markdown(f"""
            * 🔴 **[YouTube Playlist Search](https://www.youtube.com/results?search_query={enc}+full+course)**
            * 🇵🇰 **[Urdu/Hindi Tutorials](https://www.youtube.com/results?search_query={enc}+course+in+urdu)**
            * 🎓 **[Coursera Free Search](https://www.coursera.org/search?query={enc})**
            """)

# ─────────────────────────────────────────────────────────────────────────────
# 8. WEBSITE AUDITOR (Purana Feature)
# ─────────────────────────────────────────────────────────────────────────────
with tabs[7]:
    st.subheader("🌐 Quick Website Business Auditor")
    web_url = st.text_input("Website Link", placeholder="https://example.com")
    if st.button("Audit Website"):
        if web_url.startswith("http"):
            try:
                r = requests.get(web_url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
                s = BeautifulSoup(r.text, "html.parser")
                st.success("Analysis Complete! ✅")
                st.write(f"**Page Title:** {s.title.string.strip() if s.title else 'N/A'}")
            except Exception as e:
                st.error(f"Error scanning site: {e}")
        else:
            st.warning("Valid URL enter karein.")

# ─────────────────────────────────────────────────────────────────────────────
# 9. META AD SPY (Purana Feature)
# ─────────────────────────────────────────────────────────────────────────────
with tabs[8]:
    st.subheader("📢 Meta Ad Library Competitor Spy")
    brand_name = st.text_input("Brand Name to Spy", placeholder="e.g. Outfitters, Nike")
    if st.button("Open Meta Ad Library"):
        if brand_name:
            ad_url = f"https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=PK&q={urllib.parse.quote(brand_name)}"
            st.markdown(f"👉 **[Click Here to View Active Ads of '{brand_name}']({ad_url})**")