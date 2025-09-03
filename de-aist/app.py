import streamlit as st
import streamlit.components.v1 as components
import os

# Streamlit 페이지 설정
st.set_page_config(
    page_title="AI 팝업 스튜디오 웹페이지",
    layout="wide",
    initial_sidebar_state="expanded",
)

# HTML 파일의 경로 설정
# 현재 스크립트 파일이 위치한 디렉토리에서 'html' 폴더 안의 'index.html'을 찾습니다.
html_file_path = os.path.join(os.path.dirname(__file__), "htmls", "index.html")

# HTML 파일이 존재하는지 확인
if not os.path.exists(html_file_path):
    st.error(f"HTML 파일을 찾을 수 없습니다: {html_file_path}")
else:
    # HTML 파일 읽기
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_code = f.read()

    # Streamlit에 HTML 코드 렌더링
    # 너비와 높이를 조정하여 전체 페이지를 표시하도록 설정합니다.
    components.html(html_code, height=1000, scrolling=True)

# 페이지 하단에 간단한 설명 추가 (선택 사항)
st.markdown("""
<style>
    .streamlit-container {
        padding-top: 0;
    }
</style>
""", unsafe_allow_html=True)
