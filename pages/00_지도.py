import streamlit as st
import folium
from streamlit_folium import folium_static

st.set_page_config(page_title="서울 관광지 지도", layout="wide")

st.title("🗺️ 외국인이 좋아하는 서울 관광지 Top 10")
st.markdown("아래 지도에는 외국인 관광객들에게 인기 있는 서울의 주요 관광 명소 10곳이 표시되어 있습니다.")

# 관광지 정보 (이름, 위도, 경도)
places = [
    ("경복궁", 37.5796, 126.9770),
    ("남산타워 (N서울타워)", 37.5512, 126.9882),
    ("명동", 37.5636, 126.9820),
    ("인사동", 37.5740, 126.9849),
    ("홍대거리", 37.5563, 126.9220),
    ("동대문디자인플라자(DDP)", 37.5665, 127.0095),
    ("롯데월드", 37.5110, 127.0980),
    ("청계천", 37.5702, 126.9920),
    ("북촌한옥마을", 37.5826, 126.9830),
    ("코엑스몰", 37.5126, 127.0606),
]

# 지도 초기 위치: 서울 중심
m = folium.Map(location=[37.5665, 126.9780], zoom_start=12)

# 마커 추가
for name, lat, lon in places:
    folium.Marker([lat, lon], popup=name, tooltip=name, icon=folium.Icon(color='blue')).add_to(m)

# Folium 지도 출력
folium_static(m)

st.success("지도가 정상적으로 표시되었습니다.")
