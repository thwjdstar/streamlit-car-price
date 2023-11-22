import streamlit as st

def run_home_app():
    st.subheader('Welcome~~')
    st.text('이 앱은 고객 데이터와 자동차 구매 데이터에 대한 내용입니다.')
    st.text('고객 정보를 넣으면, 차 구매 금액도 예측해줍니다.')

    img_url = 'http://autotimes.hankyung.com/autotimesdata/images/photo/202203/0ad0cd5a2df34e36cd91fd08dcbb46c2.jpg'

    st.image(img_url)