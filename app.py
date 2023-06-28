import streamlit as st
import common

common.page_config()

st.title("21-22년 기간별 박스오피스")

st.image("img/box_office.jpg")

# Year selection
year = st.selectbox("년도 선택", ['2021년', '2022년'])

if year == '2021년':
    df = common.get_2021()  # Get 2021 data
    next_page = 'https://230627movie-nh972165qyg.streamlit.app/._2021_sales_top10?next_page=..%2Fpages%2F04.+2022_sales_top10.py'
else:
    df = common.get_2022()  # Get 2022 data
    next_page = 'https://230627movie-nh972165qyg.streamlit.app/._2022_sales_top10?next_page=..%2Fpages%2F04.+2022_sales_top10.py'

# Show the selected year's data
st.write(f"{year} 데이터:")
st.write(df)

# Visualization on the next page
if st.button("해당 년도 페이지로"):
    # Store the selected year's data in session state
    st.session_state['selected_year_data'] = df
    # Store the selected year in session state
    st.session_state['selected_year'] = year
    # Open the next page in a new tab
    st.markdown(f'<a href="{next_page}" target="_blank">Go to {year} 페이지</a>', unsafe_allow_html=True)
