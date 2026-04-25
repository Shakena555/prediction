import numpy as np
import pandas as pd
import pickle
import streamlit as st
loaded_model = pickle.load(open('random_forest_model.pkl', 'rb'))
def grade_prediction(input_data):
    input_df=pd.DataFrame([{'Attendance_Percentage':input_data[0],'Study_Hours_Per_Day':input_data[1],'Assignments_Completed':input_data[2]}])
    prediction = loaded_model.predict(input_df)
    grade_mapping={0:'A',1:'B',2:'C',3:'D'}
    return grade_mapping[prediction[0]]
def main():
   st.title('Student Grade Prediction')
   input_data = []
   input_data.append(st.number_input('Enter the Attendence percentage:'))
   input_data.append(st.number_input('Enter the number of Study hours:'))
   input_data.append(st.number_input('Enter the number of Assignment completed:'))
   if st.button('Predict Grade'):
        grade = grade_prediction(input_data)
        st.success(f'The predicted grade is: {grade}')
if __name__ == '__main__':
    main()
    