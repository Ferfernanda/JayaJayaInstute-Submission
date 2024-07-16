import pandas as pd
import streamlit as st
import pickle

# Business Understanding
st.title("Jaya Jaya Institute: Student's Status Predictions")
st.write("This app predicts whether a student will graduate or dropout based on various features.")

# Data Understanding & Preparation
@st.cache_data()
def load_data():
    # Load data (assuming the dataset is named 'student_data.csv')
    df = pd.read_csv('update_student_performance.csv')
    return df

@st.cache_data()
def load_model(model_path):
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
    return model

df = load_data()
model = load_model('LR.pkl')

# Fungsi untuk melakukan prediksi
def predict(model, input_data):
    X_new = pd.DataFrame(input_data, index=[0])
    y_pred = model.predict(X_new)
    return y_pred[0]

def preprocess(df_prepro):
    df_preprocess = df_prepro
    categorical_cols = ['Course', 'Gender', 'Displaced', 'Scholarship_holder', 'Mothers_qualification', 'Fathers_qualification', 'Mothers_occupation', 'Fathers_occupation']
    
    for col in categorical_cols:
        df_preprocess[col] = df_preprocess[col].map({val: idx for idx, val in enumerate(sorted(df[col].unique().tolist()))})
    
    return df_preprocess

    
def main():
    st.markdown('Please fill in the following columns with the student data')

    # Deployment: Predicting new data
    st.subheader("Make a Prediction")
    st.markdown("[Click Here for Data Value Description](https://github.com/dicodingacademy/dicoding_dataset/tree/main/students_performance/README.md)")
    input_data = {
        'Application_order': st.selectbox('Aplication Order', options=sorted(df['Application_order'].unique().tolist())),
        'Course': st.selectbox('Course', options=sorted(df['Course'].unique().tolist())),
        'Previous_qualification_grade': st.number_input('Previous Qualification Grade', min_value=0.0, max_value=200.0, value=0.0),
        'Mothers_qualification': st.selectbox('Mothers Qualification', options=sorted(df['Mothers_qualification'].unique().tolist())),
        'Fathers_qualification': st.selectbox('Fathers Qualification', options=sorted(df['Fathers_qualification'].unique().tolist())),
        'Mothers_occupation': st.selectbox('Mothers Occupation', options=sorted(df['Mothers_occupation'].unique().tolist())),
        'Fathers_occupation': st.selectbox('Fathers Occupation', options=sorted(df['Fathers_occupation'].unique().tolist())),
        'Admission_grade': st.number_input('Admission Grade', min_value=0.0, max_value=200.0, value=0.0),
        'Displaced': st.selectbox('Displaced', options=sorted(df['Displaced'].unique().tolist())),
        'Gender': st.selectbox('Gender', options=sorted(df['Gender'].unique().tolist())),
        'Scholarship_holder': st.selectbox('Scholarship Holder', options=sorted(df['Scholarship_holder'].unique().tolist())),
        'Age_at_enrollment': st.number_input('Age at Enrollment', min_value=0, max_value=100, value=0),
        'Unemployment_rate': st.number_input('Unemployment Rate', min_value=0.0, max_value=100.0, value=0.0),
        'Inflation_rate': st.number_input('Inflation Rate', min_value=-1.0, max_value=4.0, value=0.0),
        'GDP': st.number_input('GDP', min_value=-10.0, max_value=10.0, value=0.0),
        'Total_enrolled_grade': st.number_input('Total Enrolled Grade', min_value=0.0, max_value=100.0, value=0.0),
        'Total_enrolled_units': st.number_input('Total Enrolled Units', min_value=0, max_value=100, value=0),
        'Total_approved_units': st.number_input('Total Approved Units', min_value=0, max_value=100, value=0),
        'Total_evaluation_units': st.number_input('Total Evaluation Units', min_value=0, max_value=100, value=0),
    }

    # Convert input data to DataFrame
    input_df = pd.DataFrame([input_data])
    prepro_df = preprocess(input_df)
    
    
    # Prediction
    if st.button("Predict"):
        prediction = model.predict(prepro_df)
        prediction_label = 'Graduate Potential!' if prediction[0] == 1 else 'Dropout Potential!'
        st.subheader(f"The predicted status is: {prediction_label}")
        st.markdown('Data Inputed: ')
        input_df    
        st.markdown('Data Preprocessed: ')
        prepro_df

# Dropout: 1,Equinculture,120.0,4,4,3,6,120.0,No,Female,No,20,12.4,0.5,1.79,Dropout,23.666666669999998,12,6,24
# 1,Veterinary Nursing,149.0,38,37,5,5,137.1,Yes,Female,Yes,18,10.8,1.4,1.74,Graduate,25.25,10,9,12

if __name__ == '__main__':
    main()

st.caption('Copyright (c) Ferfernanda Dicoding Submissions Penerapan Data Science')
