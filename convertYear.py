import streamlit as st
st.title("แอปพลิเคชั่นแปลงปี พ.ศ. ที่ต้องแปล",value=2569)

bh_year=st.number_input("กรอกปี พ.ศ. ที่ต้องแปลง",value=2569)
ce_year=bh_year-543
st.heaer(f"ปี ค.ศ. คือ : {ce_year}")
