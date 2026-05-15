import streamlit as st
import random
from datetime import datetime

# --- 1. Page Config & CSS ---
st.set_page_config(page_title="Bon Voyage Prototype", layout="centered")

st.markdown("""
    <style>
    /* 隱藏預設頂部列 */
    [data-testid="stHeader"] { display: none !important; }
    .block-container { padding-top: 2rem !important; padding-bottom: 100px !important; }
    
    /* === 底部導航列 === */
    div[role="radiogroup"] {
        position: fixed !important; bottom: 0px !important; left: 50% !important;
        transform: translateX(-50%) !important; width: 100% !important; 
        max-width: 400px !important; background: rgba(255, 255, 255, 0.98) !important;
        backdrop-filter: blur(10px) !important; display: flex !important;
        flex-direction: row !important; justify-content: space-around !important;
        padding: 10px 0px 20px 0px !important; border-top: 1px solid #f0f2f6 !important;
        z-index: 9999 !important;
    }
    div[role="radiogroup"] label > div:first-child { display: none !important; }
    div[role="radiogroup"] label {
        display: flex !important; flex-direction: column !important;
        align-items: center !important; justify-content: center !important;
        background: transparent !important; margin: 0 !important; cursor: pointer !important;
    }
    
    /* 關鍵修復 1：用萬用字元 * 確保所有文字標籤都吃得到顏色，不會消失 */
    div[role="radiogroup"] label * { 
        font-size: 11px !important; margin-top: 4px !important; 
        color: #b0b0b0 !important; text-align: center !important; font-weight: 500 !important; 
    }
    div[role="radiogroup"] label[data-baseweb="radio"] * { 
        color: #FF4B4B !important; font-weight: 800 !important; 
    }
    
    /* === 行程卡片基礎樣式 (淺色模式) === */
    .trip-card { background-color: #f8f9fa; padding: 15px; border-radius: 15px; border-left: 5px solid #FF4B4B; margin-bottom: 15px; }
    .trip-card h4 { margin: 0; color: #333333; font-size: 16px; }
    .trip-card p { margin: 5px 0 0 0; color: #666666; font-size: 14px; }
    .stImage img { border-radius: 15px !important; }

    /* === 關鍵修復 2：完美支援手機的「深色模式 Dark Mode」 === */
    @media (prefers-color-scheme: dark) {
        /* 深色模式下的導航列 */
        div[role="radiogroup"] {
            background: rgba(30, 30, 30, 0.98) !important;
            border-top: 1px solid #444 !important;
        }
        div[role="radiogroup"] label * { color: #777777 !important; }
        div[role="radiogroup"] label[data-baseweb="radio"] * { color: #FF4B4B !important; }
        
        /* 深色模式下的行程卡片 */
        .trip-card { background-color: #262730 !important; }
        .trip-card h4 { color: #FFFFFF !important; }
        .trip-card p { color: #CCCCCC !important; }
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 🌍 Global Expanded Database (Using Your High-Res URLs)
# ==========================================

DATABASE = [
    # --- 🇹🇼 Taipei, Taiwan ---
    {"city": "Taipei, Taiwan", "name": "Taipei 101", "time": "04:30 PM", "icon": "🏙️", "img": "https://images.unsplash.com/photo-1601534621622-8587a8a0da11?q=80&w=987&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", "desc": "Breathtaking views from the top.", "tags": ["City Skylines 🏙️", "Instagrammable 📸"]},
    {"city": "Taipei, Taiwan", "name": "Ximending", "time": "01:00 PM", "icon": "🛍️", "img": "https://images.unsplash.com/photo-1687423964435-5460a43b9516?q=80&w=1035&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", "desc": "Youth culture, shopping, and street art.", "tags": ["Anime & Manga ⛩️", "Shopping 🛍️", "Thrift Stores 👗"]},
    {"city": "Taipei, Taiwan", "name": "Raohe Night Market", "time": "07:00 PM", "icon": "🍗", "img": "https://images.unsplash.com/photo-1706723406868-4c60e9df8115?q=80&w=983&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", "desc": "The best black pepper buns in town.", "tags": ["Street Food 🍜", "Historical Sites 🏛️"]},
    {"city": "Taipei, Taiwan", "name": "Elephant Mountain", "time": "03:00 PM", "icon": "⛰️", "img": "https://images.unsplash.com/photo-1674491927611-ad16d141903d?q=80&w=987&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", "desc": "Short hike with a million-dollar view.", "tags": ["Nature & Hiking ⛰️", "Instagrammable 📸"]},
    {"city": "Taipei, Taiwan", "name": "Dadaocheng", "time": "10:30 AM", "icon": "🏮", "img": "https://images.unsplash.com/photo-1644718959933-8a05cf37fc36?q=80&w=2232&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", "desc": "Historic streets and traditional tea.", "tags": ["Historical Sites 🏛️", "Local Cafes ☕"]},
    {"city": "Taipei, Taiwan", "name": "Beitou Onsen", "time": "09:00 AM", "icon": "🛀", "img": "https://images.unsplash.com/photo-1705584208372-6e0151cfda9a?q=80&w=1035&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", "desc": "Relax in natural geothermal hot springs.", "tags": ["Wellness 🛀", "Nature & Hiking ⛰️"]},

    # --- 🇯🇵 Tokyo, Japan ---
    {"city": "Tokyo, Japan", "name": "TeamLab Planets", "time": "09:30 AM", "icon": "✨", "img": "https://images.unsplash.com/photo-1558637845-c8b7ead71a3e?w=400", "desc": "Mind-blowing digital art museum.", "tags": ["Art & Museums 🎨", "Instagrammable 📸"]},
    {"city": "Tokyo, Japan", "name": "Senso-ji Temple", "time": "08:30 AM", "icon": "🏮", "img": "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e?w=400", "desc": "Tokyo's oldest and most iconic temple.", "tags": ["Historical Sites 🏛️", "Instagrammable 📸"]},
    {"city": "Tokyo, Japan", "name": "Harajuku Takeshita St", "time": "01:30 PM", "icon": "🍭", "img": "https://images.unsplash.com/photo-1542051841857-5f90071e7989?w=400", "desc": "Kawaii culture and crazy street snacks.", "tags": ["Shopping 🛍️", "Street Food 🍜", "Anime & Manga ⛩️"]},
    {"city": "Tokyo, Japan", "name": "Shibuya Sky", "time": "05:00 PM", "icon": "🏙️", "img": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?w=400", "desc": "Stunning 360-degree view of Tokyo.", "tags": ["City Skylines 🏙️", "Instagrammable 📸"]},
    {"city": "Tokyo, Japan", "name": "Shimokitazawa", "time": "03:00 PM", "icon": "👗", "img": "https://images.unsplash.com/photo-1524413840807-0b3cb6fa808d?w=400", "desc": "Thrift shopping and indie music scene.", "tags": ["Thrift Stores 👗", "Local Cafes ☕"]},
    {"city": "Tokyo, Japan", "name": "Golden Gai Bars", "time": "08:30 PM", "icon": "🍸", "img": "https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=400", "desc": "Tiny hidden bars with unique vibes.", "tags": ["Hidden Bars 🍸", "Live Music 🎸"]},

    # --- 🇨🇳 Beijing, China ---
    {"city": "Beijing, China", "name": "Forbidden City", "time": "09:00 AM", "icon": "🏯", "img": "https://images.unsplash.com/photo-1598420006067-77f1c052daea?q=80&w=988&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", "desc": "The majestic heart of old China.", "tags": ["Historical Sites 🏛️", "Art & Museums 🎨"]},
    {"city": "Beijing, China", "name": "Temple of Heaven", "time": "08:00 AM", "icon": "⛩️", "img": "https://images.unsplash.com/photo-1603638672033-9d8bef363b29?q=80&w=987&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", "desc": "Iconic circular sacrificial altar.", "tags": ["Historical Sites 🏛️", "Art & Museums 🎨"]},
    {"city": "Beijing, China", "name": "Great Wall (Mutianyu)", "time": "07:30 AM", "icon": "🧱", "img": "https://images.unsplash.com/photo-1712298111306-ae2785ebf6ce?q=80&w=1035&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", "desc": "Slide down from the world wonder!", "tags": ["Nature & Hiking ⛰️", "Instagrammable 📸"]},
    {"city": "Beijing, China", "name": "798 Art District", "time": "02:30 PM", "icon": "🎨", "img": "https://images.unsplash.com/photo-1583716919760-015beb03746f?q=80&w=2054&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", "desc": "Industrial spaces turned art galleries.", "tags": ["Art & Museums 🎨", "Local Cafes ☕"]},
    {"city": "Beijing, China", "name": "Houhai Lakes", "time": "06:00 PM", "icon": "🛶", "img": "https://images.unsplash.com/photo-1630666351618-24e00de12b92?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", "desc": "Bar street by the lake with history.", "tags": ["Hidden Bars 🍸", "Street Food 🍜"]},

    # --- 🇮🇳 New Delhi, India ---
    {"city": "New Delhi, India", "name": "Red Fort", "time": "09:30 AM", "icon": "🏰", "img": "https://plus.unsplash.com/premium_photo-1697730373510-51b7fcf2ff52?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", "desc": "Grand Mughal-era fortress.", "tags": ["Historical Sites 🏛️"]},
    {"city": "New Delhi, India", "name": "Humayun's Tomb", "time": "11:00 AM", "icon": "🕌", "img": "https://plus.unsplash.com/premium_photo-1697729555861-e406b4989ee1?q=80&w=2071&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", "desc": "Stunning architecture, the inspiration for Taj Mahal.", "tags": ["Historical Sites 🏛️", "Instagrammable 📸"]},
    {"city": "New Delhi, India", "name": "Lotus Temple", "time": "03:00 PM", "icon": "🪷", "img": "https://images.unsplash.com/photo-1688257609244-3f2a893f19d6?q=80&w=1538&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", "desc": "Peaceful floral-inspired sanctuary.", "tags": ["Art & Museums 🎨", "Wellness 🛀"]},
    {"city": "New Delhi, India", "name": "Chandni Chowk", "time": "12:30 PM", "icon": "🍛", "img": "https://images.unsplash.com/photo-1624858020896-4a558c5d7042?q=80&w=1036&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", "desc": "Spicy street food and chaotic markets.", "tags": ["Street Food 🍜", "Shopping 🛍️"]},
    {"city": "New Delhi, India", "name": "Hauz Khas Village", "time": "06:00 PM", "icon": "🍷", "img": "https://images.unsplash.com/photo-1728384028318-6e2e22da8345?q=80&w=2128&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", "desc": "Trendy cafes among ancient ruins.", "tags": ["Local Cafes ☕", "Hidden Bars 🍸", "Live Music 🎸"]},
    {"city": "New Delhi, India", "name": "India Gate", "time": "05:00 PM", "icon": "🎖️", "img": "https://images.unsplash.com/photo-1678966432189-d58296e45ad2?q=80&w=927&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D", "desc": "Iconic war memorial and evening park.", "tags": ["Historical Sites 🏛️", "Instagrammable 📸"]}
]

# Helper to sort time strings
def time_to_int(time_str):
    return datetime.strptime(time_str, '%I:%M %p')

def get_recommendations(target_city, user_vibes, limit=3, exclude=[]):
    city_spots = [spot for spot in DATABASE if spot["city"] == target_city and spot["name"] not in exclude]
    
    scored_spots = []
    for spot in city_spots:
        match_score = len(set(spot["tags"]).intersection(set(user_vibes))) if user_vibes != ["Standard Tourist"] else 0
        random_boost = random.uniform(0, 10.0) # Massive boost for diversity
        scored_spots.append({"spot": spot, "score": match_score + random_boost})
    
    scored_spots.sort(key=lambda x: x["score"], reverse=True)
    results = [item["spot"] for item in scored_spots[:limit]]
    
    # Chronological sort for Trip page
    results.sort(key=lambda x: time_to_int(x['time']))
    return results

# ==========================================
# UI Logic
# ==========================================

if 'onboarded' not in st.session_state:
    st.session_state.onboarded = False
    st.session_state.user_vibes = []
    st.session_state.destination = "Taipei, Taiwan"

if not st.session_state.onboarded:
    st.title("Bon Voyage ✈️")
    # Updated Selectbox
    st.session_state.destination = st.selectbox("Where to next?", 
                                                ["Taipei, Taiwan", "Tokyo, Japan", "Beijing, China", "New Delhi, India"])
    
    interests_options = ["Street Food 🍜", "Hidden Bars 🍸", "Art & Museums 🎨", "Nature & Hiking ⛰️", "Historical Sites 🏛️", "Shopping 🛍️", "Instagrammable 📸", "Anime & Manga ⛩️", "Local Cafes ☕", "Thrift Stores 👗", "Live Music 🎸", "Wellness 🛀", "City Skylines 🏙️"]
    interests = st.pills("Pick your vibes:", options=interests_options, selection_mode="multi")
    
    if st.button("Start Journey 🚀", disabled=not interests, use_container_width=True):
        st.session_state.user_vibes = interests 
        st.session_state.onboarded = True
        st.rerun()
    if st.button("Skip for now", use_container_width=True):
        st.session_state.user_vibes = ["Standard Tourist"]
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
        st.session_state.current_trip = [s['name'] for s in daily_plan]
        
        for i, spot in enumerate(daily_plan):
            color = ["#FF4B4B", "#4CAF50", "#2196F3"][i % 3]
            st.markdown(f'<div class="trip-card" style="border-left-color: {color};"><h4>{spot["time"]} {spot["icon"]} {spot["name"]}</h4><p>{spot["desc"]}</p></div>', unsafe_allow_html=True)

    elif nav == "📸\nExplore":
        st.title("Discovery")
        exclude_list = st.session_state.get('current_trip', [])
        explore_spots = get_recommendations(current_city, vibes, limit=4, exclude=exclude_list)
        
        col1, col2 = st.columns(2)
        for i, spot in enumerate(explore_spots):
            with (col1 if i % 2 == 0 else col2):
                st.image(spot['img'], use_container_width=True)
                st.markdown(f"**{spot['name']}**\n\n⭐ 4.8 | {spot['icon']}")

    elif nav == "🧰\nTools":
        st.title("Tools")
        st.subheader("Menu Scanner 🥢")
        st.file_uploader("Upload menu photo", label_visibility="collapsed")
        st.divider()
        st.info(f"💡 Budget Tip: Local transport in {current_city.split(',')[0]} is best managed via QR codes.")

    elif nav == "👤\nProfile":
        st.title("Profile")
        st.write(f"Destination: **{current_city}**")
        st.write(f"Vibes: **{', '.join(vibes)}**")
        if st.button("Reset Demo", use_container_width=True, type="primary"):
            st.session_state.onboarded = False
            st.rerun()