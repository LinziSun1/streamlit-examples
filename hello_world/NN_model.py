import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image

# loading in the model to predict on the data
pickle_in = open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)


def welcome():
    return 'welcome all'


# defining the function which will make the prediction using
# the data which the user inputs
def prediction(sepal_length, sepal_width, petal_length, petal_width):
    prediction = classifier.predict(
        [[sepal_length, sepal_width, petal_length, petal_width]])
    map = {0:'Iris-setosa', 1:'Iris-versicolor', 2:'Iris-virginica'}
    result=map[prediction[0]]
    print(result)
    return result



# this is the main function in which we define our webpage
def main():

    st.title("Iris Flower Prediction")


    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Streamlit Iris Flower Classifier ML App </h1>
    </div>
    """


    st.markdown(html_temp, unsafe_allow_html=True)


    sepal_length = st.text_input("Sepal Length", "")
    sepal_width = st.text_input("Sepal Width", "")
    petal_length = st.text_input("Petal Length", "")
    petal_width = st.text_input("Petal Width", "")
    result = ""


    if st.button("Predict"):
        result = prediction(sepal_length, sepal_width, petal_length, petal_width)

    st.success('The output is {}'.format(result))


if __name__ == '__main__':
    main()