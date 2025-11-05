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
HTML_DIR = os.path.join(os.path.dirname(__file__), "htmls")

# 파일 이름과 사용자 친화적인 프로젝트 이름을 매핑합니다.
# 이 순서가 사이드바에 표시되는 순서가 됩니다.
PAGE_NAME_MAPPING: Dict[str, str] = {
    "index.html": "팝업 스토어 성공 예측 모델",
    "index2.html": "실시간 재난 대응 대시보드",
    "index3.html": "연금술사 카드게임 시연",
    "index4.html": "AI 주간 학습 계획 생성기",
    "index5.html": "키보드 입력 메트릭스 AI 분석",
    # [수정됨] index6.html 파일과 프로젝트 이름을 추가했습니다.
    "index6.html": "정보과제연구 최종 보고서 (데이터 시뮬레이션 추가)"
}

# --- 파일 존재 여부 확인 및 목록 구성 ---

# 'htmls' 디렉토리 존재 여부 확인
if not os.path.exists(HTML_DIR):
    st.error(f"🚨 필수 폴더인 **`htmls`**를 찾을 수 없습니다. 이 폴더를 생성하고 그 안에 HTML 파일을 넣어주세요.")
else:
    all_expected_files: List[str] = list(PAGE_NAME_MAPPING.keys())
    found_pages: Dict[str, str] = {}
    missing_files: List[str] = []

    # 기대하는 모든 파일을 순회하며 존재 여부 확인
    for filename in all_expected_files:
        file_path = os.path.join(HTML_DIR, filename)
        
        if os.path.exists(file_path):
            # 파일이 존재하면 found_pages 딕셔너리에 추가
            page_name = PAGE_NAME_MAPPING[filename]
            found_pages[page_name] = file_path
        else:
            # 파일이 누락되었으면 missing_files 목록에 추가
            missing_files.append(filename)

    # --- 사이드바 구성 및 페이지 렌더링 ---
    
    valid_page_names: List[str] = list(found_pages.keys())

    if not valid_page_names:
        # 파일이 하나도 없는 경우
        st.warning("경고: 'htmls' 폴더 내에 시연 가능한 프로젝트 파일이 없습니다.")
        st.info(f"다음 HTML 파일을 **`htmls`** 폴더에 추가해 주세요: {', '.join(all_expected_files)}")
    else:
        # 유효한 프로젝트 목록이 있는 경우
        
        # 1. 누락된 파일 안내 (사용자 요청 사항 반영)
        if missing_files:
            st.sidebar.markdown("---")
            st.sidebar.info(f"⚠️ 다음 파일들은 현재 누락되어 목록에 표시되지 않습니다. **`htmls`** 폴더에 추가해 주세요: **{', '.join(missing_files)}**")
            st.sidebar.markdown("---")

        # 2. 프로젝트 선택
        selected_page_name: str = st.sidebar.radio("🔎 시연할 프로젝트를 선택하세요:", valid_page_names)
        
        # 선택된 파일 경로 가져오기
        selected_file_path: Optional[str] = found_pages.get(selected_page_name)

        # 3. HTML 파일 불러오기 및 렌더링
        if selected_file_path and os.path.exists(selected_file_path):
            try:
                # 파일 읽기
                with open(selected_file_path, "r", encoding="utf-8") as f:
                    html_code: str = f.read()

                # 메인 화면에 제목 표시
                st.header(f"🖥️ {selected_page_name}")
                
                # HTML 코드를 Streamlit 컴포넌트로 렌더링합니다.
                components.html(html_code, height=1200, scrolling=True)
            except Exception as e:
                st.exception(f"❌ 파일을 읽거나 렌더링하는 도중 오류가 발생했습니다: {e}")
        else:
            # 이 경로는 `found_pages` 로직 때문에 도달할 가능성이 낮습니다.
            st.error(f"🚨 선택된 파일 경로({selected_file_path})를 찾을 수 없습니다.")
