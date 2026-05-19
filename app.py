import streamlit as st
import random
from datetime import datetime
from PIL import Image

# --- 1. Page Config & Favicon Setup (終極強制讀取圖片法) ---
try:
    # 直接讀取圖片實體，破除雲端路徑快取 Bug
    logo_img = Image.open("logo.jpg")
except Exception:
    logo_img = "✈️" # 萬一圖片還沒傳上來，先用飛機代替，絕不報錯

st.set_page_config(
    page_title="Bon Voyage Prototype", 
    page_icon=logo_img, 
    layout="centered"
)

st.markdown("""
    <style>
    /* 🛑 導入高級字體：Plus Jakarta Sans 🛑 */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');

    /* 全局字體強制綁定 */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stMainViewContainer"], .main, .stButton, .stPills, p, span, label {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }

    /* 高級感「粉橘 - 白 - 蜜桃粉」三色線性漸層背景 */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stMainViewContainer"], .main, [data-testid="stHeader"] {
        background: linear-gradient(135deg, #FFC0A8 0%, #FFFFFF 50%, #FFDEE9 100%) !important;
        background-attachment: fixed !important;
        color: #1E293B !important;
    }
    
    .block-container { 
        padding-top: 2rem !important; 
        padding-bottom: 100px !important; 
        background-color: transparent !important;
    }
    
    /* 徹底隱藏頂部所有預設欄位 */
    [data-testid="stHeader"] { display: none !important; }
    
    /* === 🚀 標題樣式優化 (強制靠左對齊 Logo) === */
    h1 { 
        font-weight: 800 !important; 
        font-size: 2.6rem !important; 
        color: #1E293B !important; 
        text-align: left !important; /* 強制靠左 */
        margin-top: 0px !important;
        padding-top: 5px !important;
        line-height: 1.2 !important;
    }
    
    h2, h3 { font-weight: 700 !important; color: #1E293B !important; }
    
    /* 藥丸按鈕樣式 */
    div[data-testid="stPills"] button {
        background-color: #FFFFFF !important;
        border: 2px solid #FFD1C1 !important;
        border-radius: 24px !important;
        padding: 6px 14px !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.03) !important;
    }
    div[data-testid="stPills"] button * {
        color: #475569 !important;
        font-weight: 600 !important;
    }
    div[data-testid="stPills"] button[aria-selected="true"] {
        background-color: #FF4B4B !important;
        border: 2px solid #FF4B4B !important;
    }
    div[data-testid="stPills"] button[aria-selected="true"] * {
        color: #FFFFFF !important;
    }
    
    /* === 🛑 導航列去點化修復 (強制圖文上下分行) === */
    div[role="radiogroup"] {
        position: fixed !important; bottom: 0px !important; left: 50% !important;
        transform: translateX(-50%) !important; width: 100% !important; 
        max-width: 400px !important; 
        background: rgba(255, 255, 255, 0.97) !important;
        backdrop-filter: blur(20px) !important; 
        padding: 12px 10px 25px 10px !important; 
        border-top: 1px solid rgba(255, 192, 168, 0.3) !important;
        z-index: 9999 !important;
        display: flex !important;
        flex-direction: row !important;
        justify-content: space-around !important;
    }
    div[role="radiogroup"] label > div:first-child, 
    div[role="radiogroup"] [data-testid="stRadioDot"] { display: none !important; }
    
    div[role="radiogroup"] label {
        display: flex !important; 
        flex-direction: column !important;
        align-items: center !important; 
        justify-content: center !important;
        margin: 0 !important;
    }
    
    /* 這裡加入 white-space: pre-wrap 強制讓 \n 發生作用 */
    div[role="radiogroup"] label p { 
        font-size: 11px !important; 
        color: #64748B !important; 
        font-weight: 600 !important; 
        text-align: center !important;
        white-space: pre-wrap !important; 
        line-height: 1.3 !important;
        margin: 0 !important;
    }
    div[role="radiogroup"] label[data-baseweb="radio"] p { color: #FF4B4B !important; font-weight: 800 !important; }
    
    /* 探索卡片與行程卡片 */
    .explore-card, .trip-card {
        background-color: #FFFFFF !important;
        border-radius: 20px !important;
        padding: 18px !important;
        margin-bottom: 20px !important;
        box-shadow: 0 8px 24px rgba(223, 110, 71, 0.08) !important;
    }
    .trip-card { border-left: 6px solid #FF4B4B !important; }
    .trip-card h4 { margin: 0; color: #1E293B !important; font-weight: 700; }
    .trip-card p.desc { margin: 6px 0; color: #475569 !important; font-size: 14px; line-height: 1.4 !important; }
    .trip-card p.info-line { margin: 3px 0 0 0; font-size: 12px; font-weight: 600; }
    .stImage img { border-radius: 16px !important; }
    
    /* 工具頁面淨化 */
    div[data-testid="stFileUploader"] { 
        background-color: #FFFFFF !important; 
        border: 2px dashed #CBD5E1 !important; 
        border-radius: 16px !important; 
        padding: 10px !important; 
        margin-bottom: 24px !important;
        box-shadow: 0 4px 12px rgba(0,0,0,0.03) !important;
    }
    div[data-testid="stFileUploader"] section { background-color: transparent !important; }
    div[data-testid="stNotification"] { background-color: #F8FAFC !important; border: 1px solid #E2E8F0 !important; border-radius: 14px !important; }
    div.stButton button { background-color: #1E293B !important; border-radius: 24px !important; border: none !important; }
    div.stButton button p { color: #FFFFFF !important; font-weight: 700 !important; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 🌍 Fully Hardened Pure Text Database
# ==========================================

DATABASE = [
    {
        "city": "Taipei, Taiwan", "name": "Taipei 101", "time": "04:30 PM", 
        "img": "https://images.unsplash.com/photo-1601534621622-8587a8a0da11?q=80&w=987&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", 
        "desc": "Breathtaking views from the top.", "tags": ["City Skylines", "Instagrammable", "Shopping"],
        "best_photo": "04:30 PM - 05:40 PM (Golden Hour)", "holiday_status": "Open (Normal Hours)"
    },
    {
        "city": "Taipei, Taiwan", "name": "Ximending", "time": "01:00 PM", 
        "img": "https://images.unsplash.com/photo-1687423964435-5460a43b9516?q=80&w=1035&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", 
        "desc": "Youth culture, shopping, and street art.", "tags": ["Anime & Manga", "Shopping", "Thrift Stores", "Live Music"],
        "best_photo": "06:30 PM - 09:00 PM (Neon Lights)", "holiday_status": "Open (Normal Hours)"
    },
    {
        "city": "Taipei, Taiwan", "name": "Raohe Night Market", "time": "07:00 PM", 
        "img": "https://images.unsplash.com/photo-1706723406868-4c60e9df8115?q=983&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", 
        "desc": "The best black pepper buns in town.", "tags": ["Street Food", "Historical Sites", "Local Cafes"],
        "best_photo": "07:30 PM - 08:30 PM", "holiday_status": "Open (Normal Hours)"
    },
    {
        "city": "Taipei, Taiwan", "name": "Elephant Mountain", "time": "03:00 PM", 
        "img": "https://images.unsplash.com/photo-1674491927611-ad16d141903d?q=80&w=987&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", 
        "desc": "Short hike with a million-dollar view.", "tags": ["Nature & Hiking", "Instagrammable", "Wellness"],
        "best_photo": "05:00 PM - 06:15 PM (Sunset Look)", "holiday_status": "Open (Normal Hours)"
    },
    {
        "city": "Taipei, Taiwan", "name": "Dadaocheng", "time": "10:30 AM", 
        "img": "https://images.unsplash.com/photo-1644718959933-8a05cf37fc36?q=80&w=2232&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", 
        "desc": "Historic streets and traditional tea.", "tags": ["Historical Sites", "Local Cafes", "Shopping"],
        "best_photo": "10:30 AM - 12:00 PM", "holiday_status": "Open (Normal Hours)"
    },
    {
        "city": "Taipei, Taiwan", "name": "Beitou Onsen", "time": "09:00 AM", 
        "img": "https://images.unsplash.com/photo-1705584208372-6e0151cfda9a?q=80&w=1035&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", 
        "desc": "Relax in natural geothermal hot springs.", "tags": ["Wellness", "Nature & Hiking", "Art & Museums"],
        "best_photo": "09:00 AM - 11:00 AM", "holiday_status": "Closed Today (Local Dynamic Holiday Notice)"
    },
    {
        "city": "Tokyo, Japan", "name": "TeamLab Planets", "time": "09:30 AM", 
        "img": "https://images.unsplash.com/photo-1558637845-c8b7ead71a3e?w=400", 
        "desc": "Mind-blowing digital art museum.", "tags": ["Art & Museums", "Instagrammable", "Wellness", "Live Music"],
        "best_photo": "10:00 AM - 12:00 PM", "holiday_status": "Open (Normal Hours)"
    },
    {
        "city": "Tokyo, Japan", "name": "Senso-ji Temple", "time": "08:30 AM", 
        "img": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?w=400", 
        "desc": "Tokyo's oldest and most iconic temple complex.", "tags": ["Historical Sites", "Instagrammable", "Street Food"],
        "best_photo": "06:30 AM - 08:00 AM (Avoid Crowds)", "holiday_status": "Closed Today (Temple Festival Special Shut)"
    },
    {
        "city": "Tokyo, Japan", "name": "Harajuku Takeshita St", "time": "01:30 PM", 
        "img": "https://images.unsplash.com/photo-1542051841857-5f90071e7989?w=400", 
        "desc": "Kawaii culture and crazy street snacks.", "tags": ["Shopping", "Street Food", "Anime & Manga", "Thrift Stores"],
        "best_photo": "02:00 PM - 04:00 PM", "holiday_status": "Open (Normal Hours)"
    },
    {
        "city": "Tokyo, Japan", "name": "Shibuya Sky", "time": "05:00 PM", 
        "img": "https://images.unsplash.com/photo-106744038136-46273834b3fb?w=400", 
        "desc": "Stunning 360-degree view of Tokyo rooftop cityscape.", "tags": ["City Skylines", "Instagrammable", "Shopping", "Live Music"],
        "best_photo": "05:00 PM - 06:00 PM (Sunset Peak)", "holiday_status": "Open (Normal Hours)"
    },
    {
        "city": "Tokyo, Japan", "name": "Shimokitazawa", "time": "03:00 PM", 
        "img": "https://images.unsplash.com/photo-1524413840807-0b3cb6fa808d?w=400", 
        "desc": "Thrift shopping and indie music scene.", "tags": ["Thrift Stores", "Local Cafes", "Live Music", "Shopping"],
        "best_photo": "03:00 PM - 05:00 PM", "holiday_status": "Open (Normal Hours)"
    },
    {
        "city": "Tokyo, Japan", "name": "Golden Gai Bars", "time": "08:30 PM", 
        "img": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=400", 
        "desc": "Tiny hidden bars with unique vibes.", "tags": ["Hidden Bars", "Live Music", "Local Cafes"],
        "best_photo": "09:00 PM - 11:00 PM", "holiday_status": "Open (Normal Hours)"
    },
    {
        "city": "Beijing, China", "name": "Forbidden City", "time": "09:00 AM", 
        "img": "https://images.unsplash.com/photo-1598420006067-77f1c052daea?q=80&w=988&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", 
        "desc": "The majestic heart of ancient dynasties.", "tags": ["Historical Sites", "Art & Museums", "Instagrammable"],
        "best_photo": "08:30 AM - 10:00 AM", "holiday_status": "Open (Normal Hours)"
    },
    {
        "city": "Beijing, China", "name": "Temple of Heaven", "time": "08:00 AM", 
        "img": "https://images.unsplash.com/photo-1603638672033-9d8bef363b29?q=987&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", 
        "desc": "Iconic circular sacrificial altar.", "tags": ["Historical Sites", "Art & Museums", "Wellness"],
        "best_photo": "08:00 AM - 09:30 AM", "holiday_status": "Open (Normal Hours)"
    },
    {
        "city": "Beijing, China", "name": "Great Wall (Mutianyu)", "time": "07:30 AM", 
        "img": "https://images.unsplash.com/photo-1712298111306-ae2785ebf6ce?q=1035&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", 
        "desc": "Slide down from the wonder of the world.", "tags": ["Nature & Hiking", "Instagrammable", "Wellness", "Live Music"],
        "best_photo": "07:30 AM - 09:30 AM (Clear View)", "holiday_status": "Open (Normal Hours)"
    },
    {
        "city": "Beijing, China", "name": "798 Art District", "time": "02:30 PM", 
        "img": "https://images.unsplash.com/photo-1583716919760-015beb03746f?q=80&w=2054&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", 
        "desc": "Industrial spaces turned art galleries.", "tags": ["Art & Museums", "Local Cafes", "Shopping", "Thrift Stores"],
        "best_photo": "02:30 PM - 04:30 PM", "holiday_status": "Open (Normal Hours)"
    },
    {
        "city": "Beijing, China", "name": "Houhai Lakes", "time": "06:00 PM", 
        "img": "https://images.unsplash.com/photo-1630666351618-24e00de12b92?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", 
        "desc": "Bar street by the lake with history.", "tags": ["Hidden Bars", "Street Food", "Live Music", "Anime & Manga"],
        "best_photo": "06:00 PM - 08:00 PM", "holiday_status": "Open (Normal Hours)"
    },
    {
        "city": "New Delhi, India", "name": "Red Fort", "time": "09:30 AM", 
        "img": "https://plus.unsplash.com/premium_photo-1697730373510-51b7fcf2ff52?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", 
        "desc": "Grand historic sandstone fortress complex.", "tags": ["Historical Sites", "Art & Museums", "Shopping"],
        "best_photo": "09:30 AM - 11:00 AM", "holiday_status": "Closed Today (National Holiday Observance)"
    },
    {
        "city": "New Delhi, India", "name": "Humayun's Tomb", "time": "11:00 AM", 
        "img": "https://plus.unsplash.com/premium_photo-1697729555861-e406b4989ee1?q=80&w=2071&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", 
        "desc": "Stunning architecture, the inspiration for Taj Mahal.", "tags": ["Historical Sites", "Instagrammable", "Live Music", "Nature & Hiking"],
        "best_photo": "11:00 AM - 01:00 PM", "holiday_status": "Open (Normal Hours)"
    },
    {
        "city": "New Delhi, India", "name": "Lotus Temple", "time": "03:00 PM", 
        "img": "https://images.unsplash.com/photo-1688257609244-3f2a893f19d6?q=80&w=1538&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", 
        "desc": "Peaceful floral-inspired sanctuary.", "tags": ["Art & Museums", "Wellness", "Instagrammable", "Local Cafes"],
        "best_photo": "03:00 PM - 05:00 PM", "holiday_status": "Open (Normal Hours)"
    },
    {
        "city": "New Delhi, India", "name": "Chandni Chowk", "time": "12:30 PM", 
        "img": "https://images.unsplash.com/photo-1624858020896-4a558c5d7042?q=80&w=1036&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", 
        "desc": "Spicy street food and chaotic markets.", "tags": ["Street Food", "Shopping", "Thrift Stores", "Anime & Manga"],
        "best_photo": "12:30 PM - 02:30 PM", "holiday_status": "Open (Normal Hours)"
    },
    {
        "city": "New Delhi, India", "name": "Hauz Khas Village", "time": "06:00 PM", 
        "img": "https://images.unsplash.com/photo-1728384028318-6e2e22da8345?q=80&w=2128&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", 
        "desc": "Trendy cafes among ancient ruins.", "tags": ["Local Cafes", "Hidden Bars", "Live Music", "Thrift Stores"],
        "best_photo": "06:00 PM - 08:00 PM", "holiday_status": "Open (Normal Hours)"
    },
    {
        "city": "New Delhi, India", "name": "India Gate", "time": "05:00 PM", 
        "img": "https://images.unsplash.com/photo-1678966432189-d58296e45ad2?q=80&w=927&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", 
        "desc": "Iconic war memorial and evening park.", "tags": ["Historical Sites", "Instagrammable", "Live Music", "City Skylines"],
        "best_photo": "05:00 PM - 07:00 PM", "holiday_status": "Open (Normal Hours)"
    }
]

def time_to_int(time_str):
    return datetime.strptime(time_str, '%I:%M %p')

def get_recommendations(target_city, user_vibes, limit=3, exclude=[]):
    city_spots = [spot for spot in DATABASE if spot["city"] == target_city and spot["name"] not in exclude]
    scored_spots = []
    for spot in city_spots:
        match_score = len(set(spot["tags"]).intersection(set(user_vibes))) if user_vibes != ["Standard Tourist"] else 0
        random_boost = random.uniform(0, 1.0)
        scored_spots.append({"spot": spot, "score": match_score + random_boost})
    scored_spots.sort(key=lambda x: x["score"], reverse=True)
    results = [item["spot"] for item in scored_spots[:limit]]
    if len(results) < limit:
        remaining_spots = [spot for spot in city_spots if spot not in results]
        random.shuffle(remaining_spots)
        while len(results) < limit and remaining_spots:
            results.append(remaining_spots.pop())
    results.sort(key=lambda x: time_to_int(x['time']))
    return results

# ==========================================
# UI Logic
# ==========================================

if 'onboarded' not in st.session_state:
    st.session_state.onboarded = False

if not st.session_state.onboarded:
    
    # === 🚀 首頁 Logo 與 標題左右完美並排 ===
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1.2, 4]) # 精準調整左右寬度比例
    with col1:
        try:
            st.image("logo.jpg", use_container_width=True)
        except Exception:
            pass 
    with col2:
        st.title("Bon Voyage")
        
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.session_state.destination = st.selectbox(
        "Where to next?", 
        ["Taipei, Taiwan", "Tokyo, Japan", "Beijing, China", "New Delhi, India"]
    )
    
    interests_options = ["Street Food", "Hidden Bars", "Art & Museums", "Nature & Hiking", "Historical Sites", "Shopping", "Instagrammable", "Anime & Manga", "Local Cafes", "Thrift Stores", "Live Music", "Wellness", "City Skylines"]
    interests = st.pills("Pick your vibes:", options=interests_options, selection_mode="multi")
    
    if st.button("Start Journey", disabled=not interests, use_container_width=True):
        st.session_state.user_vibes = interests 
        st.session_state.onboarded = True
        st.rerun()

else:
    # 底部導航欄 - 標籤字串加上 \n，CSS 已經強制換行
    nav = st.radio("", ["📅\nTrip", "📸\nExplore", "🧰\nTools", "👤\nProfile"], horizontal=True, label_visibility="collapsed")
    vibes = st.session_state.user_vibes
    current_city = st.session_state.destination

    if nav == "📅\nTrip":
        st.title("My Plan")
        st.caption(f"📍 {current_city}")
        daily_plan = get_recommendations(current_city, vibes, limit=3)
        for i, spot in enumerate(daily_plan):
            color = ["#FF4B4B", "#1E293B", "#FFC0A8"][i % 3]
            status_color = "#DC2626" if "Closed" in spot["holiday_status"] else "#16A34A"
            st.markdown(f"""
            <div class="trip-card" style="border-left-color: {color};">
                <h4>{spot["time"]} - {spot["name"]}</h4>
                <p class="desc">{spot["desc"]}</p>
                <p class="info-line" style="color: #B45309;">📸 Best Photo: {spot["best_photo"]}</p>
                <p class="info-line" style="color: {status_color};">🔔 {spot["holiday_status"]}</p>
            </div>
            """, unsafe_allow_html=True)

    elif nav == "📸\nExplore":
        st.title("Discovery")
        explore_spots = get_recommendations(current_city, vibes, limit=4)
        for spot in explore_spots:
            status_color = "#DC2626" if "Closed" in spot["holiday_status"] else "#16A34A"
            st.markdown(f"""
            <div class="explore-card">
                <img src="{spot['img']}" style="width:100%; border-radius:14px; object-fit:cover; aspect-ratio:16/10;" />
                <div class="explore-card-meta">
                    <p class="explore-card-title">{spot['name']} &nbsp;<span style="font-size:13px; font-weight:500; color:#64748B;">⭐ 4.8</span></p>
                    <p class="explore-card-info" style="color: #B45309;">📸 {spot['best_photo']}</p>
                    <p class="explore-card-info" style="color: {status_color};">🔔 {spot['holiday_status']}</p>
                </div>
            </div>
            """, unsafe_allow_html=True)

    elif nav == "🧰\nTools":
        st.title("Travel Tools")
        st.subheader("AI Menu Scanner")
        uploaded_file = st.file_uploader("Upload menu photo", label_visibility="collapsed")
        if uploaded_file is not None:
            st.success("Translating... Traditional dish names mapped to local English ingredients!")
        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("Smart Transport Tip")
        city_short = current_city.split(',')[0]
        st.markdown(f'<p style="font-size: 14px; color: #475569; margin: 4px 0 12px 0;">Based on your current destination ({city_short}), the AI recommends:</p>', unsafe_allow_html=True)
        st.info("Do not buy separate single tickets. Link your Apple Pay or Google Wallet directly to local digital transit bar-codes for a 20% flat discount on inter-city transfers.")

    elif nav == "👤\nProfile":
        st.title("Profile")
        # 這裡的 Profile Logo 維持置中
        _, p_mid, _ = st.columns([1.5, 1, 1.5])
        with p_mid:
            try:
                st.image("logo.jpg", use_container_width=True)
            except Exception:
                pass
        st.write(f"Destination: **{current_city}**")
        st.write(f"Vibes: **{', '.join(vibes)}**")
        if st.button("Reset Demo", use_container_width=True):
            st.session_state.onboarded = False
            st.rerun()
