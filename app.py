import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle
from sklearn.preprocessing import StandardScaler
st.title('Medical DiagnosticApp 👩‍⚕️')
st.markdown('Does the woman have diabetes or not? 👩‍⚕️')

# step1 : load the pickled model
model=open('rfc.pickle','rb')
clf=pickle.load(model)
model.close()

# Step.2: Get the user input from the front end
pregs = st.number_input('Pregnancies',0,20,step=1)
glucose=st.slider('Glucose',40,200,40)
bp=st.slider('BloodPressure',20,140,20)
skin=st.slider('skinThickness',5,100,5)
insulin=st.slider('insulin',14.0,846.0,14.0)
bmi=st.slider('bmi',15.0,70.0,15.0)
dpf=st.slider('DiabetesPedigreeFunction',0.05,2.50,0.05)
age=st.slider('age',21,90,21)

# Step.3: Converting user input to model input
data = {
    'Pregnancies':pregs,
    'Glucose':glucose,
    'BloodPressure':bp,
    'SkinThickness':skin,
    'Insulin':insulin,
    'BMI':bmi,
    'DiabetesPedigreeFunction':dpf,
    'Age':age
}
input_data=pd.DataFrame([data])
#st.write(input_data)

# #Step.4: get the model prediction and print it
prediction = clf.predict(input_data)
if st.button('Prediction'):
    if prediction==1:
        st.error('the woman has diabetes')
    if prediction==0:
        st.success('the woman is Healthy')

