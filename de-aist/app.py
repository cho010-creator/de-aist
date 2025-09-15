import streamlit as st
import streamlit.components.v1 as components
import os

# Streamlit 페이지 설정
st.set_page_config(
    page_title="프로젝트 시연 페이지",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.title("프로젝트 선택")

# --- HTML 페이지 설정 ---
# HTML 파일이 있는 기본 디렉토리 설정
# 이 파이썬 파일과 같은 위치에 'htmls' 폴더가 있어야 합니다.
HTML_DIR = os.path.join(os.path.dirname(__file__), "htmls")

# 페이지 이름 매핑 (파일 이름 -> 표시할 이름)
# 'AI' 단어를 제거하고, 새로운 페이지를 추가했습니다.
PAGE_NAME_MAPPING = {
    "index.html": "팝업 스토어 성공 예측 모델",
    "index.2.html": "실시간 재난 대응 대시보드",
    "index.3.html": "연금술사 카드게임 시연",
    "index.4.html": "Ai 주간 학습 계획 생성기"
}

# 'htmls' 디렉토리에서 모든 .html 파일 찾기
pages = {}
if os.path.exists(HTML_DIR):
    for root, dirs, files in os.walk(HTML_DIR):
        for file in files:
            if file.endswith(".html"):
                # 매핑된 이름이 있으면 사용하고, 없으면 파일 이름을 그대로 사용
                page_name = PAGE_NAME_MAPPING.get(file, os.path.splitext(file)[0])
                pages[page_name] = os.path.join(root, file)

# --- 사이드바에서 페이지 선택 ---
if not pages:
    st.error(f"'htmls' 폴더를 찾을 수 없거나 폴더 안에 HTML 파일이 없습니다. {HTML_DIR}")
else:
    # 요청하신 순서대로 페이지 목록을 직접 정의합니다.
    ordered_page_names = [
        "팝업 스토어 성공 예측 모델",
        "실시간 재난 대응 대시보드",
        "연금술사 카드게임 시연",
        "Ai 주간 학습 계획 생성기"
    ]
    
    # ordered_page_names에 있는 이름만 사이드바에 표시되도록 필터링합니다.
    valid_page_names = [name for name in ordered_page_names if name in pages]
    
    selected_page_name = st.sidebar.radio("시연할 프로젝트를 선택하세요:", valid_page_names)
    
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
        components.html(html_code, height=1000, scrolling=True)
