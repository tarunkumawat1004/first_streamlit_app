import streamlit
streamlit.title('My Parents new healthy diner')
streamlit.header('Breaking News')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal !')
streamlit.text('🥗 Kale, Spanich and Rocket Smoothie !')
streamlit.text('🐔 Hard-Boiled free range Eggs !')
streamlit.text('🥑🍞 Avacado Toast !')
streamlit.header('🍌🥭Build Your Own Fruit Smoothie🥝🍇')

import pandas as pd
my_fruit_list=pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
