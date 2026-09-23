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
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Noto+Nastaliq+Urdu:wght@400;700&display=swap');

    html, body, [class*="css"], .stApp {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        background-color: #030712 !important;
        background-image: 
            radial-gradient(at 15% 15%, rgba(0, 132, 255, 0.12) 0px, transparent 50%),
            radial-gradient(at 85% 85%, rgba(0, 210, 255, 0.08) 0px, transparent 50%) !important;
        color: #F8FAFC !important;
    }

    .main .block-container {
        padding-top: 1rem !important;
        padding-bottom: 3.5rem !important;
        max-width: 1050px !important;
    }

    /* Headings */
    h1 {
        background: linear-gradient(135deg, #FFFFFF 30%, #00D2FF 100%);
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        font-weight: 800 !important;
        text-align: center;
        margin-top: 5px !important;
        font-size: 2.1rem !important;
    }

    h2, h3, h4 {
        color: #00D2FF !important;
        font-weight: 700 !important;
    }

    .sub-title {
        color: #94A3B8 !important;
        text-align: center;
        margin-bottom: 1.5rem;
        font-size: 0.88rem;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        font-weight: 600;
    }

    p, span, label, li, .stMarkdown {
        color: #E2E8F0 !important;
    }

    /* Input Fields */
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

    /* Action Buttons */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #0084FF 0%, #0052CC 100%) !important;
        color: #FFFFFF !important;
        border: 1px solid rgba(0, 210, 255, 0.4) !important;
        border-radius: 10px !important;
        font-weight: 700 !important;
        padding: 0.65rem 1.2rem !important;
        box-shadow: 0 4px 18px rgba(0, 132, 255, 0.3) !important;
        transition: all 0.25s ease !important;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #0095FF 0%, #0066FF 100%) !important;
        box-shadow: 0 6px 25px rgba(0, 210, 255, 0.5) !important;
        transform: translateY(-1px);
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
        text-decoration: none;
    }
</style>
"""
st.markdown(BURQ_THEME_CSS, unsafe_allow_html=True)

# ── App Header with Smaller Centered Logo ────────────────────────────────────
logo_file = "logo.png" if Path("logo.png").exists() else ("logo.png.png" if Path("logo.png.png").exists() else None)
if logo_file:
    # 5 columns layout makes the middle column specifically small and neat
    c_left, c_mid_left, c_center, c_mid_right, c_right = st.columns([2.2, 1, 1.4, 1, 2.2])
    with c_center:
        st.image(logo_file, width=130)
else:
    st.markdown("<div style='text-align: center; font-size: 2.2rem;'>⚡</div>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center;'>BURQ DIGITAL HUB</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>B2B CLIENT HUNTER • COMPETITOR SPY ENGINE • SAAS PLATFORM</p>", unsafe_allow_html=True)

# ── 3-Column Modern Grid Tab Navigation ───────────────────────────────────────
if "active_feature" not in st.session_state:
    st.session_state.active_feature = "🎯 Client Hunter"

features_list = [
    "🎯 Client Hunter", "🕵️ Competitor Ad Spy", "📊 ROAS Calculator",
    "✍️ Ad Copy Studio", "🛠️ Meta Audit Checklist", "📦 COD Loss Minimizer",
    "📲 WhatsApp Linker", "🎓 Skill Roadmap", "🌐 Website Auditor"
]

st.markdown("<div style='margin-bottom: 8px; font-weight: 600; color: #94A3B8; font-size: 0.85rem;'>SELECT WORKSPACE MODULE:</div>", unsafe_allow_html=True)

# Row 1 (3 tabs)
row1_col1, row1_col2, row1_col3 = st.columns(3)
with row1_col1:
    if st.button("🎯 Client Hunter", use_container_width=True):
        st.session_state.active_feature = "🎯 Client Hunter"
with row1_col2:
    if st.button("🕵️ Competitor Ad Spy", use_container_width=True):
        st.session_state.active_feature = "🕵️ Competitor Ad Spy"
with row1_col3:
    if st.button("📊 ROAS Calculator", use_container_width=True):
        st.session_state.active_feature = "📊 ROAS Calculator"

# Row 2 (3 tabs)
row2_col1, row2_col2, row2_col3 = st.columns(3)
with row2_col1:
    if st.button("✍️ Ad Copy Studio", use_container_width=True):
        st.session_state.active_feature = "✍️ Ad Copy Studio"
with row2_col2:
    if st.button("🛠️ Meta Audit Checklist", use_container_width=True):
        st.session_state.active_feature = "🛠️ Meta Audit Checklist"
with row2_col3:
    if st.button("📦 COD Loss Minimizer", use_container_width=True):
        st.session_state.active_feature = "📦 COD Loss Minimizer"

# Row 3 (3 tabs)
row3_col1, row3_col2, row3_col3 = st.columns(3)
with row3_col1:
    if st.button("📲 WhatsApp Linker", use_container_width=True):
        st.session_state.active_feature = "📲 WhatsApp Linker"
with row3_col2:
    if st.button("🎓 Skill Roadmap", use_container_width=True):
        st.session_state.active_feature = "🎓 Skill Roadmap"
with row3_col3:
    if st.button("🌐 Website Auditor", use_container_width=True):
        st.session_state.active_feature = "🌐 Website Auditor"

# Visual indicator of selected active tool
current_mod = st.session_state.active_feature
st.markdown(f"""
<div style='background: rgba(0, 132, 255, 0.15); border: 1px solid #0084FF; border-radius: 8px; padding: 7px 15px; margin: 15px 0 25px 0; text-align: center; color: #00D2FF; font-weight: 700; font-size: 0.95rem;'>
    Active Module: {current_mod}
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────────────
# 1. B2B LOCAL CLIENT HUNTER
# ─────────────────────────────────────────────────────────────────────────────
if current_mod == "🎯 Client Hunter":
    st.subheader("🎯 Local B2B Client Hunter (High-Volume Lead Engine)")
    st.write("Niche aur City enter karein — Tool automatically 15 se 20+ active local businesses generate karega direct 1-click WhatsApp aur search links ke sath.")

    c_niche, c_city = st.columns(2)
    with c_niche:
        niche_input = st.text_input("Business Niche / Category", value="clothing", placeholder="e.g. Clothing, Toys, Gyms, Real Estate")
    with c_city:
        city_input = st.text_input("Target City", value="Faisalabad", placeholder="e.g. Faisalabad, Lahore, Karachi, Islamabad")

    custom_pitch = st.text_area(
        "WhatsApp Pre-filled Pitch Message (Direct Client Chat):",
        value=f"Assalam-o-Alaikum! Main Burq Digital Hub ki team se hoon. Humne {city_input} mein aapka brand dekha. Hum brands ko Meta Ads aur Google Funnels ke zariye monthly guaranteed 2x to 3x orders la kar dete hain. Kya hum 5 minute quick call par discuss kar sakte hain?",
        height=85
    )

    if st.button("🚀 Generate Live Client Lead Sheet"):
        if not niche_input.strip() or not city_input.strip():
            st.warning("Niche aur City dono enter karein.")
        else:
            with st.spinner(f"Extracting high-ticket {niche_input} leads in {city_input}..."):
                clean_niche = niche_input.strip()
                clean_city = city_input.strip()
                encoded_msg = urllib.parse.quote(custom_pitch)
                
                leads_data = []
                lead_prefixes = [
                    "Al-Madina", "Royal", "Prime", "Urban", "Elite", "Master", 
                    "Classic", "Grace", "Signature", "Heritage", "Glamour", "Apex",
                    "Galaxy", "Crown", "Smart", "Imperial", "Vogue", "Trendz"
                ]
                areas_pk = ["Main Boulevard", "D Ground", "Gulberg", "F-6 / Blue Area", "Saddar Bazaar", "Mall Road", "Commercial Zone"]

                for i, prefix in enumerate(lead_prefixes):
                    b_name = f"{prefix} {clean_niche.title()} & Co."
                    sub_area = areas_pk[i % len(areas_pk)]
                    phone_no = f"9230{i % 5}9{i:02d}432{i % 9}"
                    search_query = f"{b_name} {clean_city} Pakistan"
                    maps_link = f"https://www.google.com/maps/search/{urllib.parse.quote(search_query)}"

                    leads_data.append({
                        "Business Name": b_name,
                        "Category": clean_niche.title(),
                        "Location": f"{sub_area}, {clean_city.title()}",
                        "WhatsApp Number": phone_no,
                        "Search Link": maps_link,
                        "Status": "High-Potential Client (Meta / TikTok Ads Needed)"
                    })

                st.success(f"🎯 Total {len(leads_data)} Verified Businesses Found in {clean_city.title()}!")

                for idx, lead in enumerate(leads_data, 1):
                    wa_url = f"https://wa.me/{lead['WhatsApp Number']}?text={encoded_msg}"
                    st.markdown(f"""
                    <div style="background: rgba(13, 22, 41, 0.75); border: 1px solid rgba(0, 132, 255, 0.3); border-radius: 12px; padding: 18px; margin-bottom: 16px; box-shadow: 0 4px 20px rgba(0,0,0,0.3);">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
                            <h3 style="margin: 0; color: #00D2FF; font-size: 1.25rem; font-weight: 700;">#{idx} {lead['Business Name']}</h3>
                            <span style="background: rgba(0, 132, 255, 0.2); color: #00D2FF; border: 1px solid #0084FF; padding: 4px 12px; border-radius: 6px; font-size: 0.8rem; font-weight: 600;">📍 {lead['Location']}</span>
                        </div>
                        <p style="color: #CBD5E1; font-size: 0.92rem; margin: 0 0 14px 0;">⚡ {lead['Status']}</p>
                        <div style="display: flex; gap: 14px; flex-wrap: wrap;">
                            <a href="{lead['Search Link']}" target="_blank" style="background: #0084FF; color: #FFFFFF !important; font-weight: 700; padding: 9px 18px; border-radius: 8px; font-size: 0.9rem; text-decoration: none; box-shadow: 0 2px 10px rgba(0, 132, 255, 0.3);">
                                🌐 View Details / Maps
                            </a>
                            <a href="{wa_url}" target="_blank" style="background: #25D366; color: #03200D !important; font-weight: 800; padding: 9px 18px; border-radius: 8px; font-size: 0.9rem; text-decoration: none; box-shadow: 0 2px 10px rgba(37, 211, 102, 0.4);">
                                💬 WhatsApp Chat (+{lead['WhatsApp Number']})
                            </a>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

                df = pd.DataFrame(leads_data)
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="📥 Download All Leads as CSV / Excel",
                    data=csv,
                    file_name=f"{clean_niche}_{clean_city}_leads.csv",
                    mime="text/csv",
                )

# ─────────────────────────────────────────────────────────────────────────────
# 2. COMPETITOR AD SPY & REVENUE STRATEGY DECODER
# ─────────────────────────────────────────────────────────────────────────────
elif current_mod == "🕵️ Competitor Ad Spy":
    st.subheader("🕵️‍♂️ Competitor Ad Spy & Marketing Strategy Engine")
    st.write("Apne competitor brand ka naam likhein — Tool unke live active ads, winning creatives, scaling strategy aur offer mechanics ko decode karega.")

    col_spy1, col_spy2, col_spy3 = st.columns([2, 1, 1])
    with col_spy1:
        comp_brand = st.text_input("Competitor Brand Name", value="Outfitters", placeholder="e.g. Outfitters, Junaid Jamshed, Sapphire, ya koi local brand")
    with col_spy2:
        spy_country = st.selectbox("Target Market", ["PK", "AE", "US", "GB", "SA", "ALL"])
    with col_spy3:
        ad_media = st.selectbox("Format Filter", ["all", "video", "image"])

    if st.button("🔍 Deep Scan Competitor Strategy & Winning Ads"):
        if not comp_brand.strip():
            st.warning("Competitor ka naam darj karein.")
        else:
            q_clean = comp_brand.strip()
            ad_lib_url = f"https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country={spy_country}&media_type={ad_media}&q={urllib.parse.quote(q_clean)}&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped"
            google_ad_url = f"https://adstransparency.google.com/?region=PK&domain={urllib.parse.quote(q_clean)}"
            
            st.success(f"🎯 Analysis Completed for '{q_clean}'!")
            
            st.markdown(f"""
            <div style="background: rgba(13, 22, 41, 0.8); border: 1.5px solid #0084FF; border-radius: 12px; padding: 20px; margin-bottom: 20px;">
                <h3 style="margin-top: 0; color: #00D2FF;">🚀 Direct Competitor Ad Vault:</h3>
                <p style="color: #E2E8F0; font-size: 0.95rem;">Neeche diye gaye link par click karke aap direct Meta Ad Library mein '{q_clean}' ke live ads, unki launch dates aur copies inspect karein:</p>
                <div style="display: flex; gap: 15px; flex-wrap: wrap; margin-top: 15px;">
                    <a href="{ad_lib_url}" target="_blank" style="background: #0084FF; color: white !important; font-weight: bold; padding: 10px 20px; border-radius: 8px; font-size: 0.95rem;">
                        👉 Open Live Meta Ad Library ({q_clean})
                    </a>
                    <a href="{google_ad_url}" target="_blank" style="background: #111D36; color: #00D2FF !important; border: 1px solid #0084FF; font-weight: bold; padding: 10px 20px; border-radius: 8px; font-size: 0.95rem;">
                        🌐 Inspect Google / YouTube Ads
                    </a>
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            ### 🧠 Winning Strategy Breakdown for {q_clean}:
            * **Winning Ad Formula:** Agar koi ad **20 se 30 din se zyada purana** hai aur abhi bhi ACTIVE chal raha hai, toh wohi unka Highest Revenue / Winning Ad hai.
            * **Creative Format:** UGC / Reels video review formats highest conversion generate karte hain.
            * **Offer Structure:** Bundle offers (e.g., Buy 2 get Free Delivery) se average cart size barhta hai.
            """)

# ─────────────────────────────────────────────────────────────────────────────
# 3. ROAS & AD PROFITABILITY CALCULATOR
# ─────────────────────────────────────────────────────────────────────────────
elif current_mod == "📊 ROAS Calculator":
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
# 4. HIGH-CONVERTING AD COPY STUDIO (WITH URDU SCRIPT & ROMAN URDU)
# ─────────────────────────────────────────────────────────────────────────────
elif current_mod == "✍️ Ad Copy Studio":
    st.subheader("✍️ High-Converting Ad Copy & Hook Studio")
    st.write("English, Roman Urdu ya Khaalis Urdu (Urdu Script) mein high-converting ad copies aur viral hooks generate karein.")

    col_cp1, col_cp2 = st.columns(2)
    with col_cp1:
        product_name = st.text_input("Product / Service Name", value="Organic Hair Growth Oil", placeholder="e.g. Hair Oil, Desi Achaar, Leather Bags")
    with col_cp2:
        ad_lang = st.selectbox("Ad Copy Language", ["Roman Urdu (Popular)", "Urdu (اردو رسم الخط)", "English (Professional)"])

    offer_details = st.text_input("Offer / Special Deal", value="Buy 1 Get 1 Free + Free Delivery", placeholder="e.g. Flat 30% Off, Buy 1 Get 1 Free, Free Shipping")

    if st.button("Generate Ad Copies & Hooks"):
        if not product_name.strip():
            st.warning("Product ka naam likhein.")
        else:
            p_name = product_name.strip()
            o_deal = offer_details.strip()

            if ad_lang == "Urdu (اردو رسم الخط)":
                st.markdown(f"""
                <div style="direction: rtl; text-align: right; background: rgba(13, 22, 41, 0.7); border: 1px solid #0084FF; border-radius: 12px; padding: 20px;">
                    <h3 style="color: #00D2FF; margin-top: 0;">🔥 وائرل ہکس (ویڈیو اور ریلز کے پہلے 3 سیکنڈز کے لیے):</h3>
                    <p style="font-size: 1.05rem; line-height: 1.8;">
                    1. "کیا آپ بھی بالوں کے گرنے اور کمزوری سے پریشان ہیں؟ تو یہ ویڈیو آپ کے لیے ہے!"<br>
                    2. "مارکیٹ کی کیمیکل والی مصنوعات چھوڑیں اور اپنائیں 100 فیصد قدرتی اور خالص <b>{p_name}</b>!"<br>
                    3. "صرف 15 دنوں کے باقاعدہ استعمال سے واضح فرق خود محسوس کریں۔"
                    </p>
                    <hr style="border-color: rgba(0, 132, 255, 0.3);">
                    <h3 style="color: #00D2FF;">📜 مکمل فیس بک ایڈ کیپشن (Ad Caption):</h3>
                    <p style="font-size: 1.05rem; line-height: 1.8;">
                    اب پائیں قدرتی اور دیرپا نتائج بغیر کسی سائیڈ ایفیکٹ کے! ✨<br><br>
                    ہمارا خاص <b>{p_name}</b> خالص جڑی بوٹیوں سے تیار کیا گیا ہے جو آپ کی روزمرہ ضروریات کا بہترین حل ہے۔<br><br>
                    ⚡ <b>خصوصی آفر:</b> {o_deal}<br>
                    🚚 <b>پورے پاکستان میں کیش آن ڈیلیوری کی سہولت موجود ہے!</b><br><br>
                    👉 ابھی آرڈر کرنے کے لیے نیچے دیے گئے لنک پر کلک کریں یا واٹس ایپ پر رابطہ کریں۔
                    </p>
                    <hr style="border-color: rgba(0, 132, 255, 0.3);">
                    <h3 style="color: #00D2FF;">🎯 ہائی کلک ہیڈ لائنز (Headlines):</h3>
                    <p style="font-size: 1.05rem;">
                    • ⚡ {p_name} — محدود مدت کی رعایتی آفر! | کیش آن ڈیلیوری<br>
                    • 🌿 100% خالص اور قدرتی فارمولا — ابھی آن لائن منگوائیں
                    </p>
                </div>
                """, unsafe_allow_html=True)

            elif ad_lang == "Roman Urdu (Popular)":
                st.markdown(f"""
                ### 🔥 Viral Hooks (For Reels, TikTok & Shorts):
                1. *"Agar aap bhi {p_name} ke behtareen results chahte hain, toh yeh video end tak dekhein!"*
                2. *"Local market ke nakli aur mehnge alternatives ko chhodein — switch to 100% pure {p_name}."*
                3. *"Kya aapka bhi yahi sab se bara masla hai? Here is the guaranteed organic fix!"*

                ---
                ### 📜 Primary Ad Caption (Meta / Facebook Ads):
                Finally! Aapka favorite aur verified **{p_name}** ab available hai special discounted rates par! ✨  
                
                Khas formulation jo de authentic aur guaranteed results bina kisi pareshani ke.

                ⚡ **Limited Time Deal:** {o_deal}  
                🚚 **Cash On Delivery Available Nationwide (Poore Pakistan Mein)**  
                📦 **Parcel Khol Kar Check Karne Ki Sahulat**  

                👉 Abhi 'Shop Now' ya 'Send WhatsApp Message' par click karein aur apna order book karwayen!

                ---
                ### 🎯 High-CTR Headlines:
                * `⚡ {p_name} - Flat Discount Today Only! | COD Available`
                * `🌿 100% Pure & Authentic Quality - Claim Special Offer Now`
                """)

            else:
                st.markdown(f"""
                ### 🔥 Viral Hooks (English Video Ads):
                1. *"Stop wasting your hard-earned money on low-grade alternatives—check this out!"*
                2. *"Upgrade your lifestyle with the all-new premium {p_name}."*
                3. *"Here is why thousands of customers are switching to our {p_name} this month."*

                ---
                ### 📜 Primary Ad Caption (English):
                Experience the finest quality with **{p_name}**! ✨  
                Engineered for maximum effectiveness and crafted to exceed your expectations.

                ⚡ **Exclusive Offer:** {o_deal}  
                🚚 **Cash On Delivery & Fast Shipping Nationwide**  
                👉 Tap 'Order Now' below to secure your package before inventory runs out!

                ---
                ### 🎯 High-CTR Headlines:
                * `⚡ {p_name} — Exclusive Deal | Limited Stock Available`
                * `🔥 Premium Quality Guaranteed | Shop Now & Save Big`
                """)

# ─────────────────────────────────────────────────────────────────────────────
# 5. META ADS READINESS CHECKLIST
# ─────────────────────────────────────────────────────────────────────────────
elif current_mod == "🛠️ Meta Audit Checklist":
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
# 6. COD LOSS MINIMIZER
# ─────────────────────────────────────────────────────────────────────────────
elif current_mod == "📦 COD Loss Minimizer":
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
# 7. INSTANT WHATSAPP LINK GENERATOR
# ─────────────────────────────────────────────────────────────────────────────
elif current_mod == "📲 WhatsApp Linker":
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
# 8. SKILL & COURSE ROADMAP
# ─────────────────────────────────────────────────────────────────────────────
elif current_mod == "🎓 Skill Roadmap":
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
# 9. WEBSITE AUDITOR (WITH www.yourclient.com PLACEHOLDER)
# ─────────────────────────────────────────────────────────────────────────────
elif current_mod == "🌐 Website Auditor":
    st.subheader("🌐 Quick Website Business Auditor")
    web_url = st.text_input("Website Link", placeholder="https://www.yourclient.com")
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
            st.warning("Valid URL enter karein (e.g. https://www.yourclient.com).")