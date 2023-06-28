import streamlit as st
import common

common.page_config()

st.title("2021-2022년 한국 박스오피스")

st.image("img/box_office.jpg")


st.sidebar.title("박스오피스")
year = st.sidebar.radio("년도 선택", ['2021', '2022'])

st.title("2021-2022년 한국 박스오피스")

if st.button("2021", key='2021'):
    with st.tabs(["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th"]) as tabs:
        for i, tab in enumerate(tabs):
            tab.image(f"./img/2021/{i+1}.png")

if st.button("2022", key='2022'):
    with st.tabs(["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th"]) as tabs:
        for i, tab in enumerate(tabs):
            if i == 2 or i == 3:
                continue  # Skip tabs 3 and 4 for 2022
            tab.image(f"./img/2022/{i+1}.jpg")
