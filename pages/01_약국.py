import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- 페이지 설정 ---
st.set_page_config(page_title="임대료 대비 매출 분석", page_icon="🏙️", layout="wide")

# --- 샘플 데이터 생성 ---
@st.cache_data
def load_data():
    np.random.seed(42)
    regions = ["서울", "안동"]
    seoul_districts = ["강남구", "서초구", "송파구", "관악구", "마포구", "영등포구"]
    andong_districts = ["안동시청", "옥동", "정하동", "송하동", "용상동", "태화동"]

    data = []
    for region, districts in zip(regions, [seoul_districts, andong_districts]):
        for gu in districts:
            rent = np.random.randint(300, 1000) * 10000   # 임대료
            sales = rent * np.random.uniform(0.8, 2.0)    # 매출
            ratio = sales / rent
            data.append([region, gu, rent, sales, ratio])

    df = pd.DataFrame(data, columns=["지역", "구", "임대료", "매출", "임대료대비매출"])
    return df

df = load_data()

# --- 제목 / 설명 ---
st.title("🏙️ 서울·안동 지역 임대료 대비 매출 분석")
st.write("지역을 선택하면 각 구별 임대료 대비 매출 비율을 시각화합니다.")

# --- 지역 선택 ---
region = st.selectbox("📍 지역을 선택하세요:", df["지역"].unique())

# --- 선택한 지역의 데이터 ---
region_df = df[df["지역"] == region].sort_values("임대료대비매출", ascending=False)

# --- 색상 설정 (1등 빨강, 나머지 파랑 계열 그라데이션) ---
colors = ["#ff4b4b"] + px.colors.sequential.Blues[len(region_df) - 1:0:-1]

# --- Plotly 막대그래프 ---
fig = px.bar(
    region_df,
    x="구",
    y="임대료대비매출",
    color="구",
    text="임대료대비매출",
    color_discrete_sequence=colors
)

fig.update_traces(
    texttemplate="%{text:.2f}",
    textposition="outside"
)
fig.update_layout(
    title=f"📊 {region} 지역 구별 임대료 대비 매출 비율",
    xaxis_title="구(區)",
    yaxis_title="임대료 대비 매출 비율",
    showlegend=False,
    plot_bgcolor="white",
    title_x=0.5,
    font=dict(size=14),
    margin=dict(l=20, r=20, t=60, b=20)
)

# --- 그래프 출력 ---
st.plotly_chart(fig, use_container_width=True)

# --- 데이터 테이블 ---
with st.expander("📋 데이터 보기"):
    st.dataframe(region_df.reset_index(drop=True))
