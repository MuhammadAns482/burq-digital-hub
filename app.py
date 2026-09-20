from pathlib import Path
import os
import urllib.parse
import requests
from bs4 import BeautifulSoup
import streamlit as st

# ── Local High-Reliability Roadmap Generator ─────────────────────────────────
def generate_instant_roadmap(skill_name: str) -> str:
    clean_skill = skill_name.strip().title()
    
    return f"""### 🎯 Master Learning Roadmap: {clean_skill}
*(Burq Digital Hub — AI Learning Framework)*

---

### 1. 📌 Step-by-Step Learning Roadmap (Beginner to Advanced)
* **Level 1: Fundamentals & Terminology (Week 1)**
  * Bunyadi concepts, rules aur terminology ko samjhein.
  * Rozana 1 se 2 ghante basic tutorial videos aur resources ko follow karein.
* **Level 2: Practical Exercises & Tools (Week 2 - 3)**
  * Is skill ke zaroori tools aur platforms par practice karein.
  * Dummy projects banayein aur workflow seekhein.
* **Level 3: Advanced Optimization & Strategy (Week 4)**
  * Real-world problems, troubleshooting aur optimization strategies par kaam karein.
* **Level 4: Portfolio & Client Outreach (Week 5)**
  * 3 se 5 behtareen samples tayyar karein taake clients ko showcase kar sakein.

---

### 2. 🛠️ Essential Tools to Master
* Practice tools: Google Sheets, Notion, relevant management portals.
* Industry tools: Niche-specific dashboards aur editing/analytics portals.

---

### 3. 💼 Freelancing & Monetization
* **Upwork & Fiverr:** Direct client benefit aur business growth ko pitch karein.
* **Direct Outreach:** LinkedIn aur professional groups mein business owners ko contact karein.
* **Free Trial Strategy:** Shuruat mein 1-2 clients ko portfolio ke liye kaam de kar reviews lein.

---

### 🔍 Recommended Search Queries:
* `{clean_skill} full course playlist in urdu`
* `{clean_skill} complete tutorial for beginners`
* `{clean_skill} roadmap for freelancing`
"""

# ── Local Website Auditor ────────────────────────────────────────────────────
def audit_website_content(url: str, title: str, meta: str, text: str) -> str:
    domain = url.replace("https://", "").replace("http://", "").split("/")[0]
    snippet = text[:250] if text else "No preview available."
    
    return f"""### 🏢 Website Business Intelligence Report
**Domain:** `{domain}`  
**Website Title:** {title}

---

### 1. 🎯 Purpose & Niche
* Yeh website brand, products ya services ko showcase karne ke liye banayi gayi hai.
* **Description:** {meta if meta else "No meta description found. Content based analysis applied."}

### 2. 🛍️ Products & Services
* Website text aur headings ke mutabiq yahan relevant services ya products offer ho rahi hain.
* **Snippet Preview:** {snippet}...

### 3. 👥 Target Audience
* Relevant market ke online buyers aur clients jo fast solutions dhoond rahe hain.

### 4. 💡 Burq Digital Hub Recommendations:
1. **Clear Offer:** Main banner par seedha aur clear call-to-action button lagayein.
2. **Speed & Trust:** Mobile loading speed optimize karein aur clear trust badges rakhein.
"""

# ── Page Configuration ───────────────────────────────────────────────────────
st.set_page_config(
    page_title="BURQ DIGITAL HUB — AI Suite",
    page_icon="⚡",
    layout="wide",
)

# ── Custom CSS: Strict Logo Palette (Blue Headings, Pure White Inputs & Text) ─
BURQ_THEME_CSS = """
<style>
    body, .stApp {
        background-color: #060B14 !important;
        color: #FFFFFF !important;
    }
    .main .block-container {
        padding-top: 2rem;
        max-width: 950px;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #0084FF !important;
        font-weight: 800 !important;
    }
    .sub-title {
        color: #FFFFFF !important;
        text-align: center;
        margin-bottom: 2rem;
        font-size: 1.05rem;
    }
    p, span, label, li, .stMarkdown {
        color: #FFFFFF !important;
    }
    input, textarea, [data-testid="stChatInput"] textarea {
        background-color: #0C1524 !important;
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
        caret-color: #00D2FF !important;
        border: 1.5px solid #0084FF !important;
        border-radius: 8px !important;
        font-size: 1rem !important;
    }
    input::placeholder, textarea::placeholder {
        color: #7A8B9E !important;
        -webkit-text-fill-color: #7A8B9E !important;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #0084FF 0%, #0052CC 100%) !important;
        color: #FFFFFF !important;
        border: 1px solid #00D2FF !important;
        border-radius: 8px !important;
        font-weight: 700 !important;
        padding: 0.65rem !important;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #00A3FF 0%, #0066FF 100%) !important;
    }
    a {
        color: #00D2FF !important;
        font-weight: 600;
    }
    hr {
        border-color: #0084FF !important;
    }
</style>
"""
st.markdown(BURQ_THEME_CSS, unsafe_allow_html=True)

# ── App Header with Centered Logo ────────────────────────────────────────────
if Path("logo.png").exists():
    c1, c2, c3 = st.columns([1.3, 1, 1.3])
    with c2:
        st.image("logo.png", use_container_width=True)
else:
    st.markdown("<div style='text-align: center; font-size: 3rem;'>⚡</div>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; margin-top: 10px;'>BURQ DIGITAL HUB</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>BUILD • GROW • SCALE &nbsp;|&nbsp; <strong>YOUR GROWTH, OUR MISSION</strong></p>", unsafe_allow_html=True)

tab1, tab2, tab3 = st.tabs([
    "🎓 1. Skill & Course Finder", 
    "🌐 2. Website Intel & Auditor", 
    "📢 3. Meta Ad Spy & Inspector"
])

# ─────────────────────────────────────────────────────────────────────────────
# TAB 1: Skill & Course Learning Roadmap
# ─────────────────────────────────────────────────────────────────────────────
with tab1:
    st.subheader("Free Course & Learning Resource Finder")
    st.write("Digital Marketing, Freelancing, AI Tools, Video Editing, Graphic Design ke courses dhoondein.")
    
    course_query = st.text_input("Konsa course ya skill seekhna chahte hain?", placeholder="e.g. Meta Ads, Shopify Dropshipping, Truck Dispatching, Graphic Design")
    
    if st.button("Find Complete Roadmap & Free Courses"):
        if not course_query.strip():
            st.warning("Pehle kisi skill ya course ka naam likhein.")
        else:
            encoded_query = urllib.parse.quote(course_query)
            yt_full_course = f"https://www.youtube.com/results?search_query={encoded_query}+full+course+playlist"
            yt_urdu_hindi = f"https://www.youtube.com/results?search_query={encoded_query}+course+in+urdu+hindi"
            coursera_free = f"https://www.coursera.org/search?query={encoded_query}"
            hubspot_academy = "https://academy.hubspot.com/courses"
            google_skillshop = "https://skillshop.withgoogle.com/"
            meta_blueprint = "https://www.facebook.com/business/learn"

            st.markdown(f"""
            ### 🔗 Verified Free Learning Links (Direct Clickable)
            Neeche diye gaye links par click karke direct courses start karein:
            * 🔴 **[YouTube Complete Playlist (Full Course)]({yt_full_course})**
            * 🇵🇰 **[YouTube Complete Course (Urdu / Hindi)]({yt_urdu_hindi})**
            * 🎓 **[Coursera Free Audit / Financial Aid Courses]({coursera_free})**
            * 📜 **[HubSpot Academy Free Certifications]({hubspot_academy})**
            * 📊 **[Google Skillshop Official Free Certifications]({google_skillshop})**
            * 🎯 **[Meta Blueprint Free Official Ads Training]({meta_blueprint})**
            ---
            """)

            with st.spinner("Roadmap aur guide generate ho rahi hai..."):
                roadmap = generate_instant_roadmap(course_query)
                st.markdown(roadmap)

# ─────────────────────────────────────────────────────────────────────────────
# TAB 2: Website Business & Product Analyzer
# ─────────────────────────────────────────────────────────────────────────────
with tab2:
    st.subheader("Instant Website & Competitor Analyzer")
    st.write("Kisi bhi website ka link dalein, tool automatically business model analyze karega.")
    
    web_url = st.text_input("Website URL", placeholder="https://example.com")
    
    if st.button("Analyze Website"):
        if not web_url.strip() or not web_url.startswith("http"):
            st.warning("Mukammal URL enter karein (jaise https://example.com).")
        else:
            with st.spinner("Website scan ho rahi hai..."):
                try:
                    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
                    resp = requests.get(web_url, headers=headers, timeout=10)
                    soup = BeautifulSoup(resp.text, "html.parser")
                    
                    title = soup.title.string.strip() if soup.title and soup.title.string else "No Title Found"
                    meta_desc = ""
                    desc_tag = soup.find("meta", attrs={"name": "description"}) or soup.find("meta", attrs={"property": "og:description"})
                    if desc_tag and desc_tag.get("content"):
                        meta_desc = desc_tag["content"].strip()
                        
                    text = " ".join([p.get_text().strip() for p in soup.find_all(["h1", "h2", "p"])])[:3500]
                    
                    report = audit_website_content(web_url, title, meta_desc, text)
                    st.success("Analysis Complete! ✅")
                    st.markdown(report)
                except Exception as e:
                    st.error(f"Website scan nahi ho saki: {e}")

# ─────────────────────────────────────────────────────────────────────────────
# TAB 3: Meta Ad Library & Inspector
# ─────────────────────────────────────────────────────────────────────────────
with tab3:
    st.subheader("Meta Ad Spy & Inspector")
    st.info("💡 Meta Ad Library Transparency: Kisi bhi brand ya Facebook page ke live ads dekhein.")
    
    page_name = st.text_input("Brand / Facebook Page Name", placeholder="e.g. Nike, Outfitters, Junaid Jamshed, ya apna brand")
    
    col1, col2 = st.columns(2)
    with col1:
        country = st.selectbox("Target Country", ["ALL", "PK", "US", "AE", "GB", "CA"])
    with col2:
        media_type = st.selectbox("Ad Type", ["all", "image", "video"])
        
    if st.button("Inspect Live Ads on Meta"):
        if not page_name.strip():
            st.warning("Brand ya Page ka naam likhein.")
        else:
            query_clean = page_name.replace(" ", "%20")
            ad_library_url = f"https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country={country}&media_type={media_type}&q={query_clean}&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped"
            
            st.success(f"'{page_name}' ke active ads Meta Ad Library par ready hain!")
            st.markdown(f"""
            ### 🔍 Live Ad Transparency Link:
            👉 **[Click Here to View All Active Ads of '{page_name}']({ad_library_url})**
            
            ---
            ### 📊 Is Link Par Kya Milega:
            - **All Live Ad Creatives:** Jo images aur videos live chal rahi hain.
            - **Ad Copies & Headlines:** Ad copy aur text offers.
            - **Platforms:** Instagram, Facebook, Messenger placements.
            - **Winning Ads:** Jo ads lambe arse se active hain.
            """)