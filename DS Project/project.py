import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from pickle import load


loaded_model = load(open('model_final.sav', 'rb'))

x = load(open('data.sav','rb'))

def predict_price(location,sqft,bath,balcony,rooms):    
    loc_index = np.where(x.columns==location)[0][0]

    X = np.zeros(len(x.columns))
    X[0] = sqft
    X[1] = bath
    X[2] = balcony
    X[3] = rooms
    if loc_index >= 0:
        X[loc_index] = 1

    return loaded_model.predict([X])[0]



st.set_page_config(page_title='House Price Prediction', page_icon='🏠')
st.title("House Price Prediction")


# Sidebar for user input
st.sidebar.title('Input Features')
location = st.sidebar.selectbox('Location', x.columns[4:])  # Assuming 'location' is a categorical feature
sqft = st.sidebar.number_input('Square Feet', min_value=500, max_value=10000, value=2000)
bath = st.sidebar.number_input('Bathrooms', min_value=1, max_value=10, value=2)
balcony = st.sidebar.number_input('Balcony', min_value=0, max_value=5, value=1)
rooms = st.sidebar.number_input('BHK', min_value=1, max_value=10, value=2)


input_data = pd.DataFrame({"Location" : [location],
                          "Square Feet" : [sqft],
                          "Bathrooms" : [bath],
                          "Balcony" : [balcony],
                          "BHK" : [rooms]})
st.write(input_data)

# Button to trigger prediction    
if st.sidebar.button('Predict Price', key='predict_button'):
    price_prediction = predict_price(location, sqft, bath, balcony, rooms)
    st.markdown(
        f"""<div style='background-color:#f0f0f0; padding:10px; border-radius:5px'>
        <h3 style='text-align:center'>Predicted Price</h3>
        <p style='text-align:center; font-size:20px'><strong>Rs. {price_prediction:.2f} Lakhs</strong></p>
        </div>""", unsafe_allow_html=True)
  
