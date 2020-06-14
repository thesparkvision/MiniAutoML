import streamlit as st
import numpy as np
import pandas as pd

def sidebr():
    st.sidebar.title("Welcome to A^2-AutoML")
    file=st.sidebar.file_uploader("Choose a file",type="csv")
    if file is None:
            st.sidebar.warning("No file selected")
    else:
        df=pd.read_csv(file)
        print(type(df))
        print(df.head())
            
    model = st.sidebar.selectbox("Choose your model: ",["SVM","LinearRegression","LogisticRegression","DecisionTree"])
    if model == "SVM":
        svm_model()
    elif model == "LinearRegression":
        linear_reg()
    elif model == "LogisticRegression":
        logistic_reg()
    elif model == "side":
        decision_tree()

def main():
    sidebr()

if __name__=="__main__":
    main()

    
