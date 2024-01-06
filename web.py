import streamlit as st
import pickle

model=pickle.load(open('model1.pkl','rb'))

st.title('Salary prediction system')

yoe=st.text_input("Enter years of experience: ")

if st.button("predict"):
 yoe=float(yoe)
 data=[[yoe]]
 result=model.predict(data)
 st.success(result)
