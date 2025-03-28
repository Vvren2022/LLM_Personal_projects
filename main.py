import streamlit as st
import langchain_helper

from langchain_community.llms import OpenAI
st.title("Restaurant NAME Generator")
cuisine=st.sidebar.selectbox("Pick a Cuisine",("Indian","Italian","Mexican","chinese","Pakistani"))



if cuisine:
    response=langchain_helper.generate_gestaurant_name_and_items(cuisine)

    st.header(response["restaurant_name"].strip())
    menu_items=response['menu_items'].strip().split(',')

    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-",item)
