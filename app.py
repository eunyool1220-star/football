import os
import streamlit as st
import streamlit.components.v1 as components

# 1. Streamlit 페이지 기본 설정 (와이드 모드 및 브라우저 탭 설정)
st.set_page_config(
    page_title="FotMob Clone Web App",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. htmls 폴더 내의 index.html 파일 경로 설정
html_file_path = os.path.join("htmls", "index.html")

# 3. HTML 파일 로드 및 렌더링
if os.path.exists(html_file_path):
    with open(html_file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    # Streamlit 컴포넌트를 이용해 iframe 내부에서 HTML/CSS/JS 구동 (높이 자동 조절 및 스크롤 허용)
    components.html(html_content, height=950, scrolling=True)
else:
    st.error(f"오류: '{html_file_path}' 경로에서 파일을 찾을 수 없습니다. 폴더 및 파일명을 확인해주세요.")
