import streamlit as st
import pandas as pd
import plotly.express as px

# --- 페이지 기본 설정 ---
st.set_page_config(page_title="MBTI by Country", page_icon="🌍", layout="wide")

# --- 데이터 불러오기 ---
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

# --- UI 구성 ---
st.title("🌍 국가별 MBTI 유형 비율 대시보드")
st.write("국가를 선택하면 MBTI 16유형의 분포를 확인할 수 있습니다.")

# 국가 선택
country_list = df["Country"].sort_values().unique()
selected_country = st.selectbox("국가를 선택하세요:", country_list)

# --- 선택된 국가의 데이터 추출 ---
country_data = df[df["Country"] == selected_country].iloc[0, 1:]  # MBTI 16유형만 추출
country_df = pd.DataFrame({
    "MBTI": country_data.index,
    "Ratio": country_data.values
}).sort_values("Ratio", ascending=False)

# --- 색상 설정 ---
# 첫 번째(1등)는 빨간색, 나머지는 점점 연한 파랑 계열로
colors = ["#ff4b4b"] + px.colors.sequential.Blues[len(country_df) - 1:0:-1]

# --- Plotly 그래프 ---
fig = px.bar(
    country_df,
    x="MBTI",
    y="Ratio",
    color="MBTI",
    text="Ratio",
    color_discrete_sequence=colors
)

fig.update_traces(
    texttemplate="%{text:.2%}",
    textposition="outside"
)
fig.update_layout(
    title=f"🇨🇴 {selected_country}의 MBTI 비율",
    xaxis_title="MBTI 유형",
    yaxis_title="비율",
    yaxis_tickformat=".0%",
    showlegend=False,
    plot_bgcolor="white",
    title_x=0.5,
    font=dict(size=14)
)

# --- 그래프 출력 ---
st.plotly_chart(fig, use_container_width=True)

# --- 데이터 테이블 ---
with st.expander("📋 원본 데이터 보기"):
    st.dataframe(country_df.reset_index(drop=True))
