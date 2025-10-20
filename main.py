import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 진로 추천기", page_icon="🎓")

st.title("🎯 MBTI 진로 추천기")
st.write("너의 MBTI를 선택하면 어울리는 진로를 추천해줄게! 😎")

# MBTI 목록
mbti_types = [
    "ISTJ", "ISFJ", "INFJ", "INTJ",
    "ISTP", "ISFP", "INFP", "INTP",
    "ESTP", "ESFP", "ENFP", "ENTP",
    "ESTJ", "ESFJ", "ENFJ", "ENTJ"
]

# 사용자 입력
selected_mbti = st.selectbox("👉 너의 MBTI는?", mbti_types)

# 진로 추천 데이터
career_data = {
    "ISTJ": {
        "careers": ["공무원 🏛️", "회계사 💼"],
        "majors": ["행정학과, 법학과", "경영학과, 회계학과"],
        "personality": "체계적이고 책임감이 강한 친구들에게 딱이야!"
    },
    "ISFJ": {
        "careers": ["간호사 🏥", "사회복지사 🤝"],
        "majors": ["간호학과, 보건학과", "사회복지학과, 상담심리학과"],
        "personality": "배려심 많고 따뜻한 성격이라 사람을 돕는 일이 잘 맞아 😊"
    },
    "INFJ": {
        "careers": ["상담가 💬", "작가 ✍️"],
        "majors": ["심리학과, 교육학과", "국어국문학과, 문예창작과"],
        "personality": "깊이 있는 생각과 감수성을 가진 친구에게 딱이야!"
    },
    "INTJ": {
        "careers": ["데이터 과학자 📊", "연구원 🔬"],
        "majors": ["컴퓨터공학과, 통계학과", "자연과학계열, 공학계열"],
        "personality": "논리적이고 분석적인 성격이라 문제 해결에 강해!"
    },
    "ISTP": {
        "careers": ["엔지니어 🔧", "파일럿 ✈️"],
        "majors": ["기계공학과, 전기전자공학과", "항공운항과"],
        "personality": "실용적이고 손으로 직접 하는 걸 좋아하는 친구!"
    },
    "ISFP": {
        "careers": ["디자이너 🎨", "플로리스트 🌸"],
        "majors": ["시각디자인과, 패션디자인과", "원예학과, 플로리스트학과"],
        "personality": "감성적이고 조용하지만 창의적인 면이 있어!"
    },
    "INFP": {
        "careers": ["작가 ✍️", "심리상담사 🧠"],
        "majors": ["문예창작과, 국문과", "심리학과, 상담학과"],
        "personality": "이상과 가치가 뚜렷해서 의미 있는 일을 추구해!"
    },
    "INTP": {
        "careers": ["개발자 👨‍💻", "과학자 🔭"],
        "majors": ["컴퓨터공학과, 수학과", "물리학과, 생명과학과"],
        "personality": "호기심 많고 새로운 아이디어를 좋아하는 스타일!"
    },
    "ESTP": {
        "careers": ["마케터 📣", "기업가 💼"],
        "majors": ["경영학과, 마케팅학과", "경제학과, 무역학과"],
        "personality": "에너지가 넘치고 실행력이 강한 친구들에게 좋아!"
    },
    "ESFP": {
        "careers": ["연예인 🎤", "이벤트 플래너 🎉"],
        "majors": ["공연예술과, 연극영화과", "관광학과, 이벤트기획과"],
        "personality": "사교적이고 밝은 성격, 사람들과 어울리는 걸 좋아해!"
    },
    "ENFP": {
        "careers": ["기획자 🧠", "여행 작가 🌍"],
        "majors": ["광고홍보학과, 콘텐츠학과", "관광학과, 문예창작과"],
        "personality": "열정 넘치고 상상력 풍부한 자유로운 영혼이야!"
    },
    "ENTP": {
        "careers": ["창업가 🚀", "전략 컨설턴트 🧩"],
        "majors": ["경영학과, IT창업과", "경제학과, 산업공학과"],
        "personality": "도전 정신이 강하고 말발(?) 좋은 스타일!"
    },
    "ESTJ": {
        "careers": ["군인 🪖", "경영 관리자 🏢"],
        "majors": ["군사학과, 경찰학과", "경영학과, 행정학과"],
        "personality": "리더십 있고 규칙 잘 지키는 친구들에게 딱!"
    },
    "ESFJ": {
        "careers": ["교사 👩‍🏫", "간호사 🏥"],
        "majors": ["교육학과, 유아교육과", "간호학과, 보건행정학과"],
        "personality": "사람들과 잘 어울리고 도와주는 걸 좋아해!"
    },
    "ENFJ": {
        "careers": ["강연자 🎤", "홍보 담당자 📰"],
        "majors": ["교육학과, 커뮤니케이션학과", "광고홍보학과, 미디어학과"],
        "personality": "리더십 있고 따뜻한 조언자 같은 친구!"
    },
    "ENTJ": {
        "careers": ["CEO 👔", "전략가 ♟️"],
        "majors": ["경영학과, 경제학과", "정치외교학과, 산업공학과"],
        "personality": "계획적이고 추진력 강한 야망가 스타일!"
    }
}

# 결과 출력
if selected_mbti:
    data = career_data[selected_mbti]
    st.subheader("💼 추천 진로")
    for career in data["careers"]:
        st.markdown(f"- {career}")
    
    st.subheader("🎓 관련 학과")
    st.markdown(f"👉 {', '.join(data['majors'])}")

    st.subheader("🧠 이런 성격이라면 잘 어울려요!")
    st.markdown(f"💬 {data['personality']}")
