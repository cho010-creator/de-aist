import streamlit as st
import streamlit.components.v1 as components
import os
from typing import Dict, List, Optional

# --- Streamlit 페이지 설정 ---
# 페이지 제목과 레이아웃을 설정합니다.
st.set_page_config(
    page_title="정보과제연구 프로젝트 포트폴리오",
    layout="wide", # 넓은 레이아웃 사용
    initial_sidebar_state="expanded", # 사이드바를 기본으로 확장
)

st.sidebar.title("✅ 프로젝트 목록")

# --- HTML 파일 경로 및 매핑 설정 ---
# 이 Python 파일(app.py)과 같은 위치에 'htmls' 폴더가 있어야 합니다.
# os.path.dirname(__file__)은 현재 스크립트의 디렉토리를 가져옵니다.
HTML_DIR = os.path.join(os.path.dirname(__file__), "htmls")

# 파일 이름과 사용자 친화적인 프로젝트 이름을 매핑합니다.
# 이 순서가 사이드바에 표시되는 순서가 됩니다.
PAGE_NAME_MAPPING: Dict[str, str] = {
    "index.html": "팝업 스토어 성공 예측 모델",
    "index2.html": "실시간 재난 대응 대시보드",
    "index3.html": "연금술사 카드게임 시연",
    "index4.html": "AI 주간 학습 계획 생성기",
    "index5.html": "키보드 입력 메트릭스 AI 분석"
}

# 'htmls' 디렉토리에서 모든 .html 파일을 찾아 경로와 매핑합니다.
pages: Dict[str, str] = {}
if os.path.exists(HTML_DIR):
    for filename in os.listdir(HTML_DIR):
        # 매핑 대상에 있고 .html 파일인 경우만 처리
        if filename in PAGE_NAME_MAPPING and filename.endswith(".html"):
            page_name = PAGE_NAME_MAPPING[filename]
            file_path = os.path.join(HTML_DIR, filename)
            pages[page_name] = file_path

# --- 사이드바 구성 및 페이지 렌더링 ---

if not pages:
    st.error(f"🚨 'htmls' 폴더를 찾을 수 없거나 지정된 HTML 파일({', '.join(PAGE_NAME_MAPPING.keys())})이 없습니다. 폴더 구조를 확인해 주세요.")
else:
    # 매핑된 이름 목록 (순서 유지를 위해 매핑 딕셔너리의 순서를 사용합니다)
    ordered_page_names: List[str] = list(PAGE_NAME_MAPPING.values())
    
    # 실제로 찾은 파일만 유효한 프로젝트 목록에 포함
    valid_page_names: List[str] = [name for name in ordered_page_names if name in pages]
    
    if not valid_page_names:
        st.warning("경고: HTML 파일은 찾았으나, 매핑된 이름과 일치하는 유효한 프로젝트가 없습니다.")
    else:
        # 사이드바 라디오 버튼으로 프로젝트 선택
        selected_page_name: str = st.sidebar.radio("🔎 시연할 프로젝트를 선택하세요:", valid_page_names)
        
        # 선택된 파일 경로 가져오기
        selected_file_path: Optional[str] = pages.get(selected_page_name)

        # --- HTML 파일 불러오기 및 렌더링 ---
        if selected_file_path and os.path.exists(selected_file_path):
            try:
                # 파일 읽기
                with open(selected_file_path, "r", encoding="utf-8") as f:
                    html_code: str = f.read()

                # 메인 화면에 제목 표시
                st.header(f"🖥️ {selected_page_name}")
                
                # HTML 코드를 Streamlit 컴포넌트로 렌더링합니다.
                # height를 충분히 높게 설정하여 스크롤 없이 전체 콘텐츠를 볼 수 있도록 합니다.
                components.html(html_code, height=1200, scrolling=True) 
            except Exception as e:
                st.exception(f"❌ 파일을 읽거나 렌더링하는 도중 오류가 발생했습니다: {e}")
        else:
            st.error(f"🚨 선택된 파일 경로({selected_file_path})를 찾을 수 없습니다.")
