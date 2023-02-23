 
import pickle
import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import sklearn
from sklearn.ensemble import RandomForestRegressor



# loading the trained model
pickle_in = open('AQI_Delhi.pkl', 'rb') 
AQI_Delhi = pickle.load(pickle_in)
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(PM2x5, PM10, NO, NO2, NOx, NH3, CO, SO2, O3,Benzene, Toluene, Day, Month):      
      
    # Making predictions 
    prediction = AQI_Delhi.predict([[PM2x5, PM10, NO, NO2, NOx, NH3, CO, SO2, O3,Benzene, Toluene, Day, Month]])
    return prediction    
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:cyan;padding:13px"> 
    <h1 style ="color:black;text-align:center;">AQI of Delhi Prediction</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
   
    
    Month= st.selectbox('Month',(1,2,3,4,5,6,7,8,9,10,11,12))
    Day = st.selectbox('Month',(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31))
    PM2x5 = st.number_input( "PM2.5" )
    PM10 = st.number_input( "PM10" )
    NO= st.number_input( "NO" )
    NO2 = st.number_input( "NO2" )
    NOx = st.number_input( "NOx" )
    NH3 = st.number_input( "NH3" )
    CO = st.number_input( "CO" )
    SO2 = st.number_input( "SO2" )
    O3 = st.number_input( "O3" )
    Benzene = st.number_input( "Benzene" )
    Toluene = st.number_input( "Toluene" )
    

    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction( PM2x5, PM10, NO, NO2, NOx, NH3, CO, SO2, O3,Benzene, Toluene, Day, Month) 
        st.success('AQI of Delhi: {}'.format(result))
        
     
if __name__=='__main__': 
    main()
