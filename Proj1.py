import streamlit as st
import numpy as np
import pandas as pd

def sidebr():
    st.sidebar.title("Welcome to A^2-AutoML")
    with st.sidebar.file_input() as input:
        if input == None:
            st.sidebar.warning("No file selected")
        else:
            file_contents = input.read()
            
    model = st.sidebar.selectbox("Choose your model: ",["SVM","LinearRegression","LogisticRegression","DescionTree"])
    if model == "SVM":
        Svm_Model()
    elif model == "LinearRegression":
        Linear_Reg()
    elif model == "LogisticRegression":
        Logistic_Reg()
    elif model == "DescisionTree":
        Descision_Tree()



    
