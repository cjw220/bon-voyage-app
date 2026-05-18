import streamlit as st
import random
from datetime import datetime

# --- 1. Page Config & Macaron Gradient with Premium Typography ---
st.set_page_config(page_title="Bon Voyage Prototype", layout="centered")

st.markdown("""
    <style>
    /* 🛑 導入高級字體：Plus Jakarta Sans 🛑 */
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&display=swap');

    /* 🛑 應用字體到全域元件 🛑 */
    html, body, [data-testid="stAppViewContainer"], [data-testid="stMainViewContainer"], .main, .stButton, .stPills, p {
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }

    /* 🛑 三色漸層背景優化 🛑 */
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
    
    [data-testid="stHeader"] { display: none !important; }
    
    /* 標題與文字對比度強化 */
    h1 { font-weight: 800 !important; font-size: 2.5rem !important; color: #1E293B !important; }
    h2, h3 { font-weight: 700 !important; color: #1E293B !important; }
    
    label[data-testid="stWidgetLabel"] p {
        color: #1E293B !important;
        font-size: 15px !important;
        font-weight: 700 !important;
    }
    
    /* === 🛑 st.pills 藥丸按鈕樣式（字體對比強化） === */
    div[data-testid="stPills"] button {
        background-color: #FFFFFF !important;
        border: 2px solid #FFD1C1 !important;
        border-radius: 24px !important;
        padding: 6px 14px !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04) !important;
    }
    
    /* 藥丸文字強制為深藍灰 */
    div[data-testid="stPills"] button p {
        color: #475569 !important;
        font-weight: 600 !important;
        font-size: 13px !important;
    }
    
    div[data-testid="stPills"] button[aria-selected="true"] {
        background-color: #FF4B4B !important;
        border: 2px solid #FF4B4B !important;
    }
    div[data-testid="stPills"] button[aria-selected="true"] p {
        color: #FFFFFF !important;
        font-weight: 700 !important;
    }
    
    /* === 🛑 st.button 按鈕樣式（字體加粗） === */
    div.stButton button {
        background-color: #1E293B !important; /* 按鈕改為深色更顯眼 */
        border: none !important;
        border-radius: 24px !important;
        padding: 10px 24px !important;
        box-shadow: 0 4px 12px rgba(30, 41, 59, 0.2) !important;
    }
    div.stButton button p {
        color: #FFFFFF !important;
        font-size: 16px !important;
        font-weight: 700 !important;
    }
    
    /* 底部導航列 */
    div[role="radiogroup"] {
        position: fixed !important; bottom: 0px !important; left: 50% !important;
        transform: translateX(-50%) !important; width: 100% !important; 
        max-width: 400px !important; 
        background: rgba(255, 255, 255, 0.96) !important;
        backdrop-filter: blur(20px) !important; 
        padding: 10px 0px 20px 0px !important; 
        border-top: 1px solid rgba(255, 192, 168, 0.3) !important;
        z-index: 9999 !important;
    }
    div[role="radiogroup"] label * { 
        font-family: 'Plus Jakarta Sans', sans-serif !important;
        font-size: 11px !important;
        color: #64748B !important;
        font-weight: 600 !important; 
    }
    div[role="radiogroup"] label[data-baseweb="radio"] * { color: #FF4B4B !important; }
    
    /* 行程卡片 */
    .trip-card { 
        background-color: #FFFFFF !important; 
        padding: 18px; 
        border-radius: 20px; 
        border-left: 6px solid #FF4B4B; 
        margin-bottom: 16px;
        box-shadow: 0 8px 24px rgba(223, 110, 71, 0.08);
    }
    .trip-card h4 { margin: 0; color: #1E293B !important; font-weight: 700; }
    .trip-card p.desc { margin: 6px 0; color: #475569 !important; font-size: 14px; }
    .trip-card p.info-line { margin: 3px 0 0 0; font-size: 12px; font-weight: 600; }
    
    .stImage img { border-radius: 20px !important; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 🌍 Database (Your Original URLs Strictly Preserved)
# ==========================================

DATABASE = [
    {
        "city": "Taipei, Taiwan", "name": "Taipei 101", "time": "04:30 PM", 
        "img": "https://images.unsplash.com/photo-1601534621622-8587a8a0da11?q=80&w=987&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", 
        "desc": "Breathtaking views from the top.", "tags": ["City Skylines", "Instagrammable"],
        "best_photo": "04:30 PM - 05:40 PM (Golden Hour)", "holiday_status": "Open (Normal Hours)"
    },
    {
        "city": "Taipei, Taiwan", "name": "Ximending", "time": "01:00 PM", 
        "img": "https://images.unsplash.com/photo-1687423964435-5460a43b9516?q=80&w=1035&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", 
        "desc": "Youth culture, shopping, and street art.", "tags": ["Anime & Manga", "Shopping", "Thrift Stores"],
        "best_photo": "06:30 PM - 09:00 PM (Neon Lights)", "holiday_status": "Open (Normal Hours)"
    },
    {
        "city": "Taipei, Taiwan", "name": "Raohe Night Market", "time": "07:00 PM", 
        "img": "https://images.unsplash.com/photo-1706723406868-4c60e9df8115?q=80&w=983&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", 
        "desc": "The best black pepper buns in town.", "tags": ["Street Food", "Historical Sites"],
        "best_photo": "07:30 PM - 08:30 PM", "holiday_status": "Open (Normal Hours)"
    },
    {
        "city": "Taipei, Taiwan", "name": "Elephant Mountain", "time": "03:00 PM", 
        "img": "https://images.unsplash.com/photo-1674491927611-ad16d141903d?q=80&w=987&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", 
        "desc": "Short hike with a million-dollar view.", "tags": ["Nature & Hiking", "Instagrammable"],
        "best_photo": "05:00 PM - 06:15 PM (Sunset Look)", "holiday_status": "Open (Normal Hours)"
    },
    {
        "city": "Taipei, Taiwan", "name": "Dadaocheng", "time": "10:30 AM", 
        "img": "https://images.unsplash.com/photo-1644718959933-8a05cf37fc36?q=80&w=2232&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", 
        "desc": "Historic streets and traditional tea.", "tags": ["Historical Sites", "Local Cafes"],
        "best_photo": "10:30 AM - 12:00 PM", "holiday_status": "Open (Normal Hours)"
    },
    {
        "city": "Taipei, Taiwan", "name": "Beitou Onsen", "time": "09:00 AM", 
        "img": "https://images.unsplash.com/photo-1705584208372-6e0151cfda9a?q=80&w=1035&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", 
        "desc": "Relax in natural geothermal hot springs.", "tags": ["Wellness", "Nature & Hiking"],
        "best_photo": "09:00 AM - 11:00 AM", "holiday_status": "Closed Today (Local Dynamic Holiday Notice)"
    }
]

def time_to_int(time_str):
    return datetime.strptime(time_str, '%I:%M %p')

def get_recommendations(target_city, user_vibes, limit=3, exclude=[]):
    city_spots = [spot for spot in DATABASE if spot["city"] == target_city and spot["name"] not in exclude]
    scored_spots = []
    for spot in city_spots:
        match_score = len(set(spot["tags"]).intersection(set(user_vibes))) if user_vibes != ["Standard Tourist"] else 0
        scored_spots.append({"spot": spot, "score": match_score + random.uniform(0, 5)})
    scored_spots.sort(key=lambda x: x["score"], reverse=True)
    results = [item["spot"] for item in scored_spots[:limit]]
    results.sort(key=lambda x: time_to_int(x['time']))
    return results

# ==========================================
# UI Logic
# ==========================================

if 'onboarded' not in st.session_state:
    st.session_state.onboarded = False

if not st.session_state.onboarded:
    st.title("Bon Voyage")
    st.session_state.destination = st.selectbox("Where to next?", ["Taipei, Taiwan", "Tokyo, Japan", "Beijing, China", "New Delhi, India"])
    
    interests_options = ["Street Food", "Hidden Bars", "Art & Museums", "Nature & Hiking", "Historical Sites", "Shopping", "Instagrammable", "Anime & Manga", "Local Cafes", "Thrift Stores", "Live Music", "Wellness", "City Skylines"]
    interests = st.pills("Pick your vibes:", options=interests_options, selection_mode="multi")
    
    if st.button("Start Journey", disabled=not interests, use_container_width=True):
        st.session_state.user_vibes = interests 
        st.session_state.onboarded = True
        st.rerun()

else:
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
        col1, col2 = st.columns(2)
        for i, spot in enumerate(explore_spots):
            with (col1 if i % 2 == 0 else col2):
                st.image(spot['img'], use_container_width=True)
                st.markdown(f"**{spot['name']}**  \n⭐ 4.8")
                status_color = "#DC2626" if "Closed" in spot["holiday_status"] else "#16A34A"
                st.markdown(f"""
                <p style="margin: 0; font-size: 11px; color: #B45309; font-weight: 600;">📸 {spot['best_photo']}</p>
                <p style="margin: 0; font-size: 11px; color: {status_color}; font-weight: 600;">🔔 {spot['holiday_status']}</p>
                """, unsafe_allow_html=True)

    elif nav == "🧰\nTools":
        st.title("Tools")
        st.info(f"💡 Budget Tip: Local transport in {current_city} is best managed via Apple Pay.")

    elif nav == "👤\nProfile":
        if st.button("Reset Demo", use_container_width=True):
            st.session_state.onboarded = False
            st.rerun()
