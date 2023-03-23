# -*- coding: utf-8 -*-


# -*- coding: utf-8 -*-
"""


@author: Darshan H M 
"""


import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 
# from House_PP  import RandomForestRegressor
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("rfr.pkl","rb")
rfr=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(UNDER_CONSTRUCTION,RERA,BHK_NO,SQUARE_FT,READY_TO_MOVE,RESALE,LONGITUDE,LATITUDE,
                                POSTED_BY_Dealer, POSTED_BY_Owner, BHK_OR_RK_RK):
    
    
   
    prediction=rfr.predict([[UNDER_CONSTRUCTION,RERA,BHK_NO,SQUARE_FT,READY_TO_MOVE,RESALE,LONGITUDE,LATITUDE,
                                POSTED_BY_Dealer, POSTED_BY_Owner, BHK_OR_RK_RK]])
    print(prediction)
    return prediction



def main():
    st.title("House Price Prediction")
    html_temp = """
    <body style="background-image: url("F:\Dockers-master\g1.jpg");
    background-size: cover;">
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">StreamlitHouse Sales Analysis ML App </h2>
    </div>
    </body>
    """
   
    st.markdown(html_temp,unsafe_allow_html=True)

    
    UNDER_CONSTRUCTION= st.text_input("UNDER_CONSTRUCTION","Type Here")
    
   
   
    RERA=st.text_input("RERA","Type Here")
    
    BHK_NO = st.text_input("BHK_NO","Type Here")
    
    SQUARE_FT = st.text_input("SQUARE_FT","Type Here")

    READY_TO_MOVE = st.text_input("READY_TO_MOVE","Type Here")
    
    RESALE = st.text_input("RESALE","Type Here")
    
    LONGITUDE = st.text_input("LONGITUDE","Type Here")
    
    LATITUDE = st.text_input("LATITUDE","Type Here")

    
    POSTED_BY_Dealer = st.text_input("POSTED_BY_Dealer","Type Here")
    POSTED_BY_Owner = st.text_input("POSTED_BY_Owner","Type Here")
    BHK_OR_RK_RK = st.text_input("BHK_OR_RK_RK","Type Here")
   
    
    result=""
    if st.button("Predict"):
        
        UNDER_CONSTRUCTION=float(UNDER_CONSTRUCTION)
        RERA=float(RERA)
        BHK_NO=float(BHK_NO)
        SQUARE_FT=float(SQUARE_FT)
        READY_TO_MOVE=float(READY_TO_MOVE)
        RESALE=float(RESALE)
        LONGITUDE=float(LONGITUDE)
        LATITUDE=float(LATITUDE)
        POSTED_BY_Dealer=float(POSTED_BY_Dealer)
        POSTED_BY_Owner=float(POSTED_BY_Owner)
        BHK_OR_RK_RK=float(BHK_OR_RK_RK)
        
        
        
        
        result=predict_note_authentication(UNDER_CONSTRUCTION,RERA,BHK_NO,SQUARE_FT,READY_TO_MOVE,RESALE,LONGITUDE,LATITUDE,POSTED_BY_Dealer, POSTED_BY_Owner, BHK_OR_RK_RK)
    st.success('House Price Prediction is  {}'.format(result))
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")
        option = st.selectbox('How would you like to be contacted?',({'Email':1, 'Home phone':2, 'Mobile phone':3}))
        st.write('You selected:', option)

if __name__=='__main__':
    main()
    
    
    