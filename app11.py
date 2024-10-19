import streamlit as st
import pandas as pd 
import plotly.express as px 

st.set_page_config(layout='wide')

df = px.data.tips()
def page1():

    tab1 , tab2 , tab3 = st.tabs(['histogram' , 'box-plot' , 'violin'])

    # start put charts in each tab 
    
    with tab1 :
    
        st.plotly_chart(px.histogram(data_frame=df , x = 'total_bill'))
        
    with tab2 :
    
        st.plotly_chart(px.box(data_frame=df , x = 'tip' , y = 'time'))
    
    
    with tab3 :
    
        st.plotly_chart(px.violin(data_frame=df , x = 'total_bill' , y = 'sex'))
    

    

def page2():
    sex = st.sidebar.selectbox('select sex' , df['sex'].unique())
    st.plotly_chart(px.histogram(data_frame = df[df['sex'] == sex] , x = 'total_bill'))
    
def page3():

    day = st.sidebar.selectbox('select day' , df['day'].unique())
    st.plotly_chart(px.histogram(data_frame = df[df['day'] == day] , x = 'total_bill'))

pgs = {
    'time' : page1,
    'sex' : page2,
    'days' : page3
}
pg = st.sidebar.radio('Navigate pages ' ,options= pgs.keys())

pgs[pg]()
