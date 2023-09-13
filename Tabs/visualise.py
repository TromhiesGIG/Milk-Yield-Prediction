"""This modules contains data about visualisation page"""

# Import necessary modules
import warnings
import matplotlib.pyplot as plt
import seaborn as sns


import streamlit as st


# Import necessary functions from web_functions
from web_functions import train_model

def app(df, X, y):
    """This function create the visualisation page"""
    
    # Remove the warnings
    warnings.filterwarnings('ignore')
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Set the page title
    st.title("Visualise the Harvest Yield Prediction Web app")

  
    if st.checkbox("Size_of_ROIs vs Gradient_Mean_value"):
        sns.color_palette("rocket", as_cmap=True)
        ax=sns.scatterplot(x="Size_of_ROIs",y="Gradient_Mean_value",data=df)
        st.pyplot()

    if st.checkbox("Homogenity vs Entropy"):
        sns.color_palette("rocket", as_cmap=True)
        ax=sns.scatterplot(x="Homogenity",y="Entropy",data=df)
        st.pyplot()

    if st.checkbox("Skewness vs Yearly_Production"):
        sns.color_palette("rocket", as_cmap=True)
        ax=sns.scatterplot(x="Skewness",y="Yearly_Production",data=df)
        st.pyplot()

   
