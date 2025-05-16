import streamlit as st
import pickle
import numpy as np

@st.cache_resource
def load_ordinal(path: str = 'model/ordinal.pkl'):
    with open(path, 'rb') as f:
        return pickle.load(f)
    

@st.cache_resource
def load_scaler(path: str = 'model/scaler.pkl'):
    with open(path, 'rb') as f:
        return pickle.load(f)
    
@st.cache_resource
def load_model(path: str = 'model/grid.pkl'):
    with open(path, 'rb') as f:
        return pickle.load(f)
    
ordinal=load_ordinal()
scaler = load_scaler()
model  = load_model()


industries=['EdTech','FinTech','E-Commerce','Gaming','AI','IoT','Cybersecurity','HealthTech']
status=['Private','Acquired','IPO']

st.title("Start-Up Predictor")
st.write("Enter the values to predict that the start-up is profitable or not")

funding_round=st.number_input("funding round",min_value=1,max_value=5,value=3,step=1)

funding_amount=st.number_input("funding amount",min_value=0.50,max_value=300.0,value=156.0,step=0.50)

valuation=st.number_input("valuation",min_value=2.5,max_value=4500.0,value=1222.0,step=100.0)

revenue=st.number_input("revenue",min_value=0.10,max_value=100.0,value=48.0,step=0.10)

market_share=st.number_input("market share",min_value=0.10,max_value=10.0,value=5.13,step=0.10)

industry=st.selectbox("select industry",industries)

exit_status=st.selectbox("select exit status",status)


if st.button("predict"):

    industry_encoded, exit_status_encoded = ordinal.transform([[industry, exit_status]])[0]

    x=np.array([[
        funding_round,
        funding_amount,
        valuation,
        revenue,
        market_share,
        industry_encoded ,
        exit_status_encoded
    ]])

    x = scaler.transform(x)

    prediction=model.predict(x)[0]

    st.write("Predicted Profit:", "Profitable" if prediction == 1 else "Not Profitable")