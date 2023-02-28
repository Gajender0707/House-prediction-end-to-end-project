import streamlit as st
import pandas as pd
import numpy as np
import pickle
import sklearn
from PIL import Image

##load the model which you save in the pickle format
pickle_in=open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

##create the function which take the input of model feature and return predication according to given feature to ML model
def prediction(bedrooms,bathrooms,sqft_lot, floors, view, condition,grade, yr_built, zipcode, lat, long, sqft_living15,sqft_lot15):
    pred=classifier.predict([[bedrooms,bathrooms,sqft_lot, floors, view, condition,grade, yr_built, zipcode, lat, long, sqft_living15,sqft_lot15]])
    return st.success(f"The House Price According to your Requiremnt will be {round(pred[0],0)} Lakh")



## creating main function which give the streamlit interface
def main():
    st.set_page_config(page_title="House-Prediction",page_icon=":smiley:")
    img=Image.open("home.jpg")
    st.image(img)
    st.title("House Price Prediction")
    html_temp="<h1 style='text-align: center; color: red;'>House prices</h1>"
    st.markdown(html_temp,unsafe_allow_html=True)
    bedrooms=st.number_input("Enter the Bedrooms")
    bathrooms=st.number_input("Enter the Bathrooms")
    sqft_lot=st.number_input("Enter the sqft_lot")
    floors=st.number_input("Enter the Floors")
    view=st.number_input("Select the View")
    condition=st.number_input("Enter the Condition")
    grade=st.number_input("Enter the Grade")
    yr_built=st.number_input("Enter the Yr_built")
    zipcode=st.number_input("Enter the Zipcode")
    lat=st.number_input("Enter the Latitutde")
    longi=st.number_input("Enter the Longitude")
    sqft_living15=st.number_input("Enter the sqft_living15")
    sqft_lot15=st.number_input("Enter the sqft_lot15")

    if st.button("Submit"):
        prediction(bedrooms,bathrooms,sqft_lot, floors, view, condition,grade, yr_built, zipcode, lat, longi, sqft_living15,sqft_lot15)
        st.markdown("<h5 style='text-align: center; color: black;'>@Gajender2023</h5>",unsafe_allow_html=True)
        with st.expander("Know More"):
            st.write("""This is about the Kc house price where there are
              bedrooms,bathrooms,sqft_lot, floors, view, condition,grade,
                yr_built, zipcode, lat, longi, sqft_living15,sqft_lot15 Features. 
                If you want you can select according to you ...""")


 
if __name__=="__main__":
    main()