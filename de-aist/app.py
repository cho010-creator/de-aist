import streamlit as st
import streamlit.components.v1 as components
import os

# Streamlit 페이지 설정
st.set_page_config(
    page_title="연금술사의 의뢰서 - 게임 시연",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.title("게임 선택")

# --- HTML 페이지 설정 ---
# HTML 파일이 있는 기본 디렉토리 설정
# 이 파이썬 파일과 같은 위치에 'htmls' 폴더가 있어야 합니다.
HTML_DIR = os.path.join(os.path.dirname(__file__), "htmls")

# 'htmls' 디렉토리에서 모든 .html 파일 찾기
pages = {}
if os.path.exists(HTML_DIR):
    for root, dirs, files in os.walk(HTML_DIR):
        for file in files:
            if file.endswith(".html"):
                # 사용자 친화적인 페이지 이름 만들기
                # 예: htmls/index.3.html -> index.3
                page_name = os.path.splitext(file)[0]
                pages[page_name] = os.path.join(root, file)

# --- 사이드바에서 페이지 선택 ---
if not pages:
    st.error(f"'htmls' 폴더를 찾을 수 없거나 폴더 안에 HTML 파일이 없습니다. {HTML_DIR}")
else:
    # 사이드바에서 보여줄 페이지 목록 정렬
    sorted_page_names = sorted(pages.keys())
    selected_page_name = st.sidebar.radio("시연할 게임 버전을 선택하세요:", sorted_page_names)
    
    # 선택된 파일 경로 가져오기
    selected_file_path = pages[selected_page_name]

    # --- HTML 파일 불러오기 및 렌더링 ---
    if not os.path.exists(selected_file_path):
        st.error(f"선택한 HTML 파일을 찾을 수 없습니다: {selected_file_path}")
    else:
        # 선택된 HTML 파일 읽기
        with open(selected_file_path, "r", encoding="utf-8") as f:
            html_code = f.read()

        # Streamlit 화면에 HTML 코드 렌더링
        st.header(f"'{selected_page_name}' 게임 실행 화면")
        components.html(html_code, height=1000, scrolling=True)
