import streamlit as st
import pandas as pd
import plost
#Setting Page Configuration
st.set_page_config(page_title="Streamlit Dashboard",layout="wide",initial_sidebar_state="expanded")
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
#Setting the Sidebar Configuration
st.sidebar.header("Dashboard `version 2`")

st.sidebar.subheader("Heatmap Parameter")
time_hist_color=st.sidebar.selectbox("Color by",["temp_min","temp_max"])

st.sidebar.subheader("Donut Chart Parameters")
donut_theta=st.sidebar.selectbox("Select Data",["q2","q3"])

st.sidebar.subheader("Line Chart Parameter")
plot_data=st.sidebar.multiselect("Select Data",["temp_min","temp_max"])
plot_height=st.sidebar.slider("Specify Plot Height",200,500,250)

st.sidebar.markdown('''
---
created with ❤️ by [HamzaLogicAI](https://hamzalogicai.netlify.app/)                    
                    ''')
#End of Setting the Sidebar Configuration----------------------------                    
                    
#Settiing the Homepage Configuration
#Row A
st.markdown("### Metrics")
col1,col2,col3=st.columns(3)
col1.metric("Temperature","70 °F","1.2°F")
col2.metric("Wind","9mph","-8%")
col3.metric("Humidity","86%","4%")
#Row B
seatle_weather=pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])
stocks=pd.read_csv("https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv")
c1,c2=st.columns((7,3))
with c1:
    st.markdown("### Heatmap")
    plost.time_hist(data=seatle_weather, date="date", x_unit="week", y_unit="day",color=time_hist_color,aggregate="median",legend=None,height=345,use_container_width=True)
with c2:
    st.markdown("### Donut Chart")    
    plost.donut_chart(data=stocks, theta=donut_theta, color="company",legend="button",use_container_width=True)                    
#Row C
st.markdown("### Line Chart")  
st.line_chart(data=seatle_weather,x="date",y=plot_data,height=plot_height)  