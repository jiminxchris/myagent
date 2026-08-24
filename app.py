import streamlit as st
from google import genai

st.set_page_config(
    page_title="업무지원 AI 도우미",
    page_icon="🤖",
    layout="centered"
)

st.title("업무지원 AI 도우미")
st.caption("Gemini API를 활용한 교육용 AI 앱")

client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

user_input = st.text_area(
    "업무 요청 내용을 입력하세요.",
    height=150,
    placeholder="예: VPN 접속이 되지 않아 외부에서 업무시스템에 접속할 수 없습니다."
)

if st.button("AI 분석"):

    if not user_input.strip():
        st.warning("업무 요청 내용을 입력해주세요.")

    else:
        prompt = f"""
당신은 IT 업무지원 Agent입니다.

다음 요청을 단계적으로 처리하세요.

[입력]
{user_input}

STEP 1.
요청의 핵심 내용을 한 문장으로 요약하세요.

STEP 2.
다음 중 업무분류를 선택하세요.

- 계정 및 인증
- 네트워크
- 업무시스템
- PC 및 주변기기
- 소프트웨어
- 기타

STEP 3.
긴급도를 상/중/하 중 하나로 판단하세요.

단, 판단 근거가 부족하면 '확인 필요'라고 표시하세요.

STEP 4.
현재 정보만으로 확인할 수 없는 사항을 정리하세요.

STEP 5.
담당자가 다음에 수행해야 할 행동을 제안하세요.

STEP 6.
자신의 결과를 다시 검증하세요.

검증사항:
- 입력에 없는 내용을 만들지 않았는가?
- 장애 원인을 확정하지 않았는가?
- 판단 근거가 있는가?
"""

        with st.spinner("AI가 분석하고 있습니다..."):

            response = client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=prompt
            )

        st.subheader("AI 분석 결과")
        st.write(response.text)
