import streamlit as st

st.title('오픈소스 소프트웨어 과제')

options=["부산", "서울", "대전", "광주"]

answer1=st.radio("다음 중 대한민국의 수도는 어디인가요??",options)

answer2=st.text_input("데이터 애플리케이션을 빠르게 구축할 수 있는 파이썬 기반 오픈 소스 프레임워크는?")

if st.button("제출"):
    if answer1 == "서울":
        st.success("정답입니다!")
    else:
        st.error("틀렸습니다. 정답은 서울입니다.")
    if answer2 == "streamlit":
        st.success("정답입니다")
    else:
        st.error("틀렸습니다. 정답은 streamlit입니다.")
        