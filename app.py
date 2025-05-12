import streamlit as st

st.title('오픈소스 소프트웨어 과제')

options=["a","b","c","d"]

answer1=st.radio("다음 중 피타고라스의 정리는?",options)

answer2=st.text_input("데이터 애플리케이션을 빠르게 구축할 수 있는 파이썬 기반 오픈 소스 프레임워크는?")

if st.button("제출"):
    if answer1 == "a":
        st.success("정답입니다")
    else:
        st.error("틀렸습니다.")
    if answer2 == "streamlit":
        st.success("정답입니다")
    else:
        st.error("틀렸습니다.")
        