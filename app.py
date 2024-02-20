import streamlit as st
import pickle
import pandas as pd
from sklearn.linear_model import LinearRegression

# import the model
# loaded_model = pickle.load(open('linear_model.pkl', 'rb'))
with open('linear_model.pkl', 'rb') as h:
    loaded_model = pickle.load(h) 

st.title('House Price Predection')

bedrooms = st.text_input('Bedrooms', value=3)	
bathrooms = st.text_input('Bathrooms', value=1)	

floors = st.text_input('Floors', value=1)	
waterfront = st.text_input('Waterfront', value=0)	
view = st.text_input('View', value=0)	
condition = st.text_input('Condition', value=3)	
grade = st.text_input('Grade', value=7)	
yr_built = st.text_input('Year Built', value=1955)	
lat = st.text_input('Latitude', value=47.5112)	
long = st.text_input('Longitude',value=-122.257)
meters_living	= st.text_input('Meters Living', value=238.758826)	
meters_lot = st.text_input('Meters Lot', value=672.798216)	
meters_above = st.text_input('Meters Above', value=201.597919)	
meters_basement = st.text_input('Meters Basement', value=37.160907)

			
all_features = [[bedrooms, bathrooms, meters_living, meters_lot, floors, waterfront, view, condition, grade, meters_above, meters_basement, yr_built, lat, long]]
data = pd.DataFrame(all_features)

predicted_price = loaded_model.predict(data)[0]

formated_price = "{:,.0f}".format(predicted_price)

st.header(f'The Predicted Price is: ${formated_price}')