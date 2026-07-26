import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")
st.title("cric info app")

df=pd.read_csv("new_data.csv")

# st.dataframe(df)

select= option_menu(
    menu_title=None,
    options=["Home","Player Analysis","country insights","comparison","Data Explorer","About"],
    icons=["house","person","globe","bar-chart","table","line"],
    orientation="horizontal"


)

##______________Home_________________
if select=="Home":
    st.title("Cricket Analysis Dashboard")
elif select=="Player Analysis":
    st.title("Player Analysis Stats")
elif select=="country insights":
    st.title("country Wise Cricket Analysis")
    

    
