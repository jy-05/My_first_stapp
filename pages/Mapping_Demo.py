import streamlit as st  

st.set_page_config(     
    page_title="Ent.", 
    page_icon="📀",     
    layout="wide",  
    initial_sidebar_state="expanded",
    menu_items={       
        'Get help': 'https://docs.streamlit.io',
        'About': "# 이것은 헤더. \n - 마크다운 문법 지원 \n - [네이버](https://naver.com)"
    }
)
st.title(' ⋆˚࿔  SM  𝜗𝜚˚⋆ ')
st.sidebar.success("SM 소속 아티스트")  

st.markdown(   
    """ 대한민국의 대표 연예 기획사 SM
    ### SM 소속 아티스트
    - 보아; 2000년 08월 25일 데뷔
    - 동방신기; 2003년 12월 26일 데뷔
    - 슈퍼주니어; 2005월 11월 06일 데뷔
    - 소녀시대; 2007년 08월 05일 데뷔
    - SHINee; 2008년 05월 25일 데뷔
    - EXO; 2012년 04월 08일 데뷔
    - Red Velvet; 2014년 08월 01일 데뷔
    - NCT; 2016년 04월 09일 데뷔
    - SuperM; 2019년 10월 04일 데뷔
    - aespa; 2020년 11월 17일 데뷔
    - RIIZE; 2023년 09월 04일 데뷔


    ### SM에 대하여 더 알고싶으신가요?
    - [홈페이지](https://www.smentertainment.com/)
    - [인스타](https://www.instagram.com/smtown)
    - [X](https://x.com/SMTOWNGLOBAL)
    - [페이스북](https://www.facebook.com/smtown)
"""
)