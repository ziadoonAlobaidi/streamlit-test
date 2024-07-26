from utils.openspace import Openspace
import pandas as pd
import streamlit as st


n_tables = 3
n_seats = 3

tables  = st.number_input("enter a number of tables")
seats  = st.number_input("enter a number of seats")

if seats and tables:
    st.write("Enter you class mates names") 
    names  = st.text_input("enter a list")
    if names:
        n_list = [name.strip() for name in names.split(',')]
        space= Openspace(n_tables,n_seats)
        print(space.organize(n_list))
        print(space.display())
        st.write(space.display())