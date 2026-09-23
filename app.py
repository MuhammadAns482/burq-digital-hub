from pathlib import Path
import os
import re
import urllib.parse
import requests
from bs4 import BeautifulSoup
import pandas as pd
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
# 1. B2B LOCAL CLIENT HUNTER (Lead Sheet with In-App WhatsApp & Social Links)
# ─────────────────────────────────────────────────────────────────────────────
with tabs[0]:
    st.subheader("🎯 Local B2B Client Hunter (Live Lead Sheet)")
    st.write("Niche aur City likhein — Tool andar hi live businesses ki complete sheet aur direct 1-click WhatsApp buttons ready karega.")

    c_niche, c_city = st.columns(2)
    with c_niche:
        niche_input = st.text_input("Business Niche / Category", value="toys", placeholder="e.g. Toys, Clothing, Real Estate, Clinics")
    with c_city:
        city_input = st.text_input("Target City", value="Faisalabad", placeholder="e.g. Faisalabad, Lahore, Karachi")

    custom_pitch = st.text_area(
        "WhatsApp Pre-filled Pitch Message (Direct Client Chat):",
        value=f"Assalam-o-Alaikum! Main Burq Digital Hub ki team se hoon. Humne {city_input} mein aapka business dekha. Hum local businesses ko Meta Ads aur Google ke zariye monthly 2x to 3x orders aur high-paying clients la kar dete hain. Kya hum 5 minute call par discuss kar sakte hain?",
        height=85
    )

    if st.button("🚀 Generate Live Client Lead Sheet"):
        if not niche_input.strip() or not city_input.strip():
            st.warning("Niche aur City dono likhein.")
        else:
            with st.spinner(f"Searching active {niche_input} businesses in {city_input}..."):
                clean_niche = niche_input.strip()
                clean_city = city_input.strip()
                encoded_msg = urllib.parse.quote(custom_pitch)
                
                query_web = f"{clean_niche} in {clean_city} phone OR contact OR whatsapp"
                leads_data = []
                headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
                
                try:
                    search_url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(query_web)}"
                    res = requests.get(search_url, headers=headers, timeout=12)
                    soup = BeautifulSoup(res.text, "html.parser")
                    results = soup.find_all("div", class_="result__body")
                    
                    phone_pattern = re.compile(r'(?:(?:\+92|0092|92)|0)?(3\d{2}[-\s]?\d{7})')

                    count = 0
                    for r in results:
                        link_tag = r.find("a", class_="result__url")
                        snippet_tag = r.find("a", class_="result__snippet")
                        raw_title = r.find("h2", class_="result__title")
                        
                        biz_name = raw_title.get_text(strip=True) if raw_title else "Local Business"
                        raw_link = link_tag.get("href", "") if link_tag else ""
                        snippet = snippet_tag.get_text(strip=True) if snippet_tag else ""
                        
                        actual_url = raw_link
                        if "uddg=" in raw_link:
                            parsed_actual = urllib.parse.parse_qs(urllib.parse.urlparse(raw_link).query).get("uddg")
                            if parsed_actual:
                                actual_url = parsed_actual[0]

                        full_text_to_scan = f"{biz_name} {snippet}"
                        found_phone = phone_pattern.findall(full_text_to_scan)
                        
                        clean_wa_num = ""
                        if found_phone:
                            raw_ph = found_phone[0].replace("-", "").replace(" ", "").strip()
                            clean_wa_num = "92" + raw_ph if raw_ph.startswith("3") else ("92" + raw_ph[1:] if raw_ph.startswith("03") else raw_ph)

                        is_fb = "facebook.com" in actual_url.lower()
                        is_insta = "instagram.com" in actual_url.lower()
                        
                        leads_data.append({
                            "Business / Brand Name": biz_name[:45],
                            "Website / Profile": actual_url if actual_url.startswith("http") else f"https://www.google.com/search?q={urllib.parse.quote(biz_name)}",
                            "Platform": "Facebook" if is_fb else ("Instagram" if is_insta else "Website / Store"),
                            "Detected Contact": clean_wa_num if clean_wa_num else "Search Profile",
                            "Snippet": snippet[:100] + "..." if snippet else f"Local Store in {clean_city}"
                        })
                        count += 1
                        if count >= 12:
                            break
                except Exception:
                    pass

                if not leads_data:
                    st.warning("Koi direct public snippet data nahi mila. Query ko mazeed specific karein.")
                else:
                    st.success(f"🎯 Total {len(leads_data)} Businesses Found in {clean_city}!")
                    
                    st.markdown("### 📋 Interactive Client Lead Directory")
                    
                    for idx, lead in enumerate(leads_data, 1):
                        wa_ready = lead["Detected Contact"] if lead["Detected Contact"] != "Search Profile" else None
                        
                        st.markdown(f"""
                        <div style="background: rgba(13, 22, 41, 0.6); border: 1px solid rgba(0, 132, 255, 0.25); border-radius: 12px; padding: 15px; margin-bottom: 12px;">
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <h4 style="margin: 0; color: #00D2FF;">#{idx} {lead['Business / Brand Name']}</h4>
                                <span style="background: #1E2D4A; color: #94A3B8; padding: 4px 10px; border-radius: 6px; font-size: 0.8rem;">{lead['Platform']}</span>
                            </div>
                            <p style="color: #94A3B8; font-size: 0.88rem; margin: 8px 0;">{lead['Snippet']}</p>
                            <div style="margin-top: 10px; display: flex; gap: 15px; flex-wrap: wrap;">
                                <a href="{lead['Website / Profile']}" target="_blank" style="background: #0084FF; color: white; padding: 6px 14px; border-radius: 6px; text-decoration: none; font-size: 0.85rem; font-weight: bold;">🌐 Open Website / Page</a>
                                {"<a href='https://wa.me/" + wa_ready + "?text=" + encoded_msg + "' target='_blank' style='background: #25D366; color: white; padding: 6px 14px; border-radius: 6px; text-decoration: none; font-size: 0.85rem; font-weight: bold;'>💬 Chat on WhatsApp (" + wa_ready + ")</a>" if wa_ready else "<span style='color: #64748B; font-size: 0.85rem; padding-top: 5px;'>WhatsApp: Check profile link</span>"}
                            </div>
                        </div>
                        """, unsafe_allow_html=True)

                    df = pd.DataFrame(leads_data)
                    csv = df.to_csv(index=False).encode('utf-8')
                    st.download_button(
                        label="📥 Download Full Lead Sheet as CSV / Excel",
                        data=csv,
                        file_name=f"{clean_niche}_{clean_city}_leads.csv",
                        mime="text/csv",
                    )

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
# 7. SKILL & COURSE ROADMAP
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
# 8. WEBSITE AUDITOR
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
# 9. META AD SPY
# ─────────────────────────────────────────────────────────────────────────────
with tabs[8]:
    st.subheader("📢 Meta Ad Library Competitor Spy")
    brand_name = st.text_input("Brand Name to Spy", placeholder="e.g. Outfitters, Nike")
    if st.button("Open Meta Ad Library"):
        if brand_name:
            ad_url = f"https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=PK&q={urllib.parse.quote(brand_name)}"
            st.markdown(f"👉 **[Click Here to View Active Ads of '{brand_name}']({ad_url})**")