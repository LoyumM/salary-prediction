import streamlit as st
import pickle
import numpy as np

def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()
regressor = data['model']
le_country = data['le_country']
le_education = data['le_education']

def show_predict_page():
    st.title("Salary Prediction")
    
    st.write("""### We need some information to predict the salary""")
    
    countries = (
        'United States of America',
        'Germany',
        'United Kingdom of Great Britain and Northern Ireland',
        'India',
        'Canada',
        'France',
        'Brazil',
        'Spain',
        'Netherlands',
        'Poland',
        'Australia',
        'Italy',
        'Sweden',
        'Russian Federation',
        'Switzerland',
        'Turkey',
        'Israel',
        'Austria',
        'Portugal',
        'Norway',
        'Mexico'
    )
    
    education = (
        "Master's degree", 
        "Bachelor's degree", 
        'Less than a Bachelors',
        'Post grad'
    )
    
    country = st.selectbox("Country", countries)
    education = st.selectbox("Education Level", education)
    
    experience = st.slider("Years of experience", 0, 50, 3)
    
    ok = st.button("Calculate Salary")
    
    if ok:
        X = np.array([["United States of America","Master's degree", 15]])
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])
        X = X.astype(float)
        
        salary = regressor.predict(X)
        st.subheader(f"The estimated salary is ${salary[0]:.2f}")