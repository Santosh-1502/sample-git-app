import streamlit as st

st.title(' This project for GIT Learning ')
st.sidebar.title('This is SIDE BAR Menu')
col1 , col2 = st.columns(2)

with col1:
    st.write(' This is columns first')
with col2:
    st.write(' This is columns Two')

st.header('Course offered')
st.subheader('BCA')
st.subheader('MCA')
st.subheader('BBA')
st.image('MarriageCertificate.jpg')