# -*- coding: utf-8 -*-
"""predictionJJI.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/15l_FZ8e5qf20YJL4rz_xQBi46cBrorLU
"""

import pandas as pd
import pickle

from sklearn.preprocessing import MinMaxScaler, LabelEncoder

df = pd.read_csv('https://raw.githubusercontent.com/Ferfernanda/JayaJayaInstute-Submission/main/student_performance.csv')
df = df[df['Status'] == 'Enrolled']
df.info()

# Data digabungkan karena korelasi tinggi

df['Total_enrolled_grade'] = df['Curricular_units_1st_sem_grade'] + df['Curricular_units_2nd_sem_grade']
df['Total_enrolled_units'] = df['Curricular_units_1st_sem_enrolled'] + df['Curricular_units_2nd_sem_enrolled']
df['Total_approved_units'] = df['Curricular_units_1st_sem_approved'] + df['Curricular_units_2nd_sem_approved']
df['Total_evaluation_units'] = df['Curricular_units_1st_sem_evaluations'] + df['Curricular_units_2nd_sem_evaluations']

# Menghapus imbalance column
drop_col = ['Marital_status', 'Application_mode', 'Daytime_evening_attendance', 'Previous_qualification',
            'Nacionality', 'Educational_special_needs', 'Debtor', 'Tuition_fees_up_to_date', 'International',
            'Curricular_units_1st_sem_without_evaluations', 'Curricular_units_1st_sem_credited',
            'Curricular_units_2nd_sem_credited', 'Curricular_units_2nd_sem_without_evaluations',
            'Curricular_units_2nd_sem_without_evaluations' , 'Curricular_units_1st_sem_enrolled',
            'Curricular_units_2nd_sem_enrolled', 'Curricular_units_1st_sem_approved', 'Curricular_units_2nd_sem_approved',
            'Curricular_units_1st_sem_evaluations', 'Curricular_units_2nd_sem_evaluations',
            'Curricular_units_1st_sem_grade', 'Curricular_units_2nd_sem_grade', 'Status'
            ]

df = df.drop(columns=drop_col)

df.info()

# Load model yang sudah dilatih
with open('LR.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

numerical_col = ['Application_order', 'Previous_qualification_grade', 'Admission_grade', 'Age_at_enrollment', 'Unemployment_rate', 'Inflation_rate', 'GDP', 'Total_enrolled_grade', 'Total_enrolled_units', 'Total_approved_units', 'Total_evaluation_units']
categorical_col = ['Course', 'Displaced', 'Gender', 'Scholarship_holder', 'Mothers_qualification', 'Fathers_qualification', 'Mothers_occupation',
                 'Fathers_occupation', 'Displaced', 'Scholarship_holder', 'Gender']

print('Numerical:', numerical_col)
print('Categorical:', categorical_col)

# Fit and transform numerical columns
df[numerical_col] = MinMaxScaler().fit_transform(df[numerical_col])

# Encoding
for col in categorical_col:
    label_encoder = LabelEncoder()
    df[col] = label_encoder.fit_transform(df[col])

# Model akan memprediksi
y_pred = model.predict(df)

# Mapping dictionary
label_mapping = {0: 'Dropout', 1: 'Graduate'}

# Mengubah label
y_pred_mapped = [label_mapping[label] for label in y_pred]

print("Hasil Prediksi:\n", y_pred_mapped)

# Menambahkan kolom prediksi ke DataFrame
df_pred = df
df_pred['StatusPrediction'] = y_pred_mapped
df_pred.head()

# Mengubah y_pred menjadi pandas Series
print('Hasil Prediksi:')
df_pred.StatusPrediction.value_counts()

print('Presentase Label Prediksi:')
df_pred.StatusPrediction.value_counts(normalize=True) * 100

