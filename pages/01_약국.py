import streamlit as st
import pandas as pd
import plotly.express as px

# -----------------------
# 데이터 불러오기
# -----------------------
@st.cache_data
def load_data():
    df = pd.read_csv("pharmacy_data.csv")  # 약국 데이터
    return df

df = load_data()

# -----------------------
# UI 구성
# -----------------------
st.title("💊 지역별 약국 임대료 대비 매출 분석")
st.markdown("서울과 안동 지역의 구별 **약국 임대료 대비 매출 비율**을 시각화합니다.")

# 지역 선택
city = st.selectbox("📍 지역을 선택하세요", ["서울", "안동"])

# -----------------------
# 데이터 전처리
# -----------------------
df_city = df[df["도시"] == city].copy()

# 임대료 0 또는 결측 제거
df_city = df_city[df_city["임대료"] > 0].dropna(subset=["매출", "임대료", "구"])

# 구별 평균 계산
summary = (
    df_city.groupby("구")[["매출", "임대료"]]
    .mean()
    .assign(매출임대비=lambda x: x["매출"] / x["임대료"])
    .reset_index()
)

# 정렬 (내림차순)
summary = summary.sort_values("매출임대비", ascending=False)

# 색상 설정: 1등 빨강 + 나머지 그라데이션
colors = ["#ff0000"] + px.colors.sequential.Reds[len(summary) - 1 : 0 : -1]

# -----------------------
# Plotly 그래프
# -----------------------
fig = px.bar(
    summary,
    x="구",
    y="매출임대비",
    title=f"{city} 지역 약국 임대료 대비 매출 비율",
    color="매출임대비",
    color_continuous_scale="Reds",
)

# 1등만 빨간색 강조
fig.update_traces(marker=dict(line=dict(color="black", width=0.5)))
fig.update_layout(
    xaxis_title="구",
    yaxis_title="매출 ÷ 임대료 비율",
    coloraxis_showscale=False,
    template="plotly_white",
)

# -----------------------
# 출력
# -----------------------
st.plotly_chart(fig, use_container_width=True)

# -----------------------
# 데이터 표시
# -----------------------
st.subheader("📊 구별 요약 데이터")
st.dataframe(summary.style.format({"매출": "{:,.0f}", "임대료": "{:,.0f}", "매출임대비": "{:.2f}"}))
