import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------------
# ⚠️ 가공된 예시 데이터 (실제 통계 아님)
# -----------------------------
data = {
    "region": ["서울"] * 5 + ["안동"] * 5,
    "district": ["강남구", "마포구", "송파구", "강서구", "종로구",
                 "안동시 북구", "안동시 서구", "안동시 동구", "안동시 남구", "안동시 중구"],
    "revenue": [5200, 4300, 4800, 3900, 3700, 2800, 2600, 2400, 2000, 2200],
    "rent": [1300, 1100, 1200, 900, 800, 700, 600, 500, 450, 480],
}

df = pd.DataFrame(data)
df["ratio"] = (df["revenue"] / df["rent"]).round(2)

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="약국 임대료 대비 매출 대시보드", layout="wide")
st.title("💊 약국 임대료 대비 매출 분석")
st.caption("※ 본 데이터는 가공된 예시이며 실제 통계가 아닙니다.")

# 지역 선택
region = st.selectbox("📍 지역을 선택하세요", df["region"].unique())

# 선택된 지역 데이터 필터링
filtered = df[df["region"] == region].sort_values("ratio", ascending=False)

# 색상 설정: 1등은 빨간색, 나머지는 점점 연한 색의 그라데이션
colors = ["#FF4B4B"] + [f"rgba(255,100,100,{0.9 - i*0.15})" for i in range(1, len(filtered))]

# 그래프 생성 (color 인자를 직접 지정)
fig = px.bar(
    filtered,
    x="district",
    y="ratio",
    text="ratio",
    title=f"{region} 약국 임대료 대비 매출 비율",
)

# ✅ 색상을 전체 리스트로 적용
fig.update_traces(marker_color=colors, textposition="outside")

fig.update_layout(
    yaxis_title="임대료 대비 매출 비율",
    xaxis_title="구/지역",
    template="plotly_white",
    showlegend=False,
)

# 그래프 출력
st.plotly_chart(fig, use_container_width=True)

# 데이터 테이블 표시
with st.expander("📊 데이터 보기"):
    st.dataframe(filtered, use_container_width=True)

