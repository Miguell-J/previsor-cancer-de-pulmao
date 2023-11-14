import joblib as jb
import streamlit as st
import pandas as pd
import numpy as np
from streamlit.components.v1 import html
import matplotlib.pyplot as plt
import os

model_path = os.path.join(os.path.dirname(__file__), 'LogisticRegressor.joblib')
model = jb.load(model_path)


image_url = "https://www.bhtorax.com.br/wp-content/uploads/2021/01/O-que-e-o-cancer-de-pulmao_-Foto-5.jpg"
st.image(image_url, caption='Previsor de Câncer de Pulmão', use_column_width=True)


st.write("""
# Previsor de Câncer de Pulmão 🫁

Este site consegue prever a existência de **câncer de pulmão** com base em dados médicos e algorítimos de inteligência artificial
""")

st.sidebar.header("Informações Médicas")

st.sidebar.subheader("Insira os dados correspondentes às suas características médicas:")


gender = st.sidebar.selectbox("Gênero", ["Masculino", "Feminino"])
age = st.sidebar.slider("Idade", 18, 100, 40)
smoking = st.sidebar.selectbox("Fumante", ["Sim", "Não"])
yellow_fingers = st.sidebar.selectbox("Dedos Amarelados", ["Sim", "Não"])
anxiety = st.sidebar.selectbox("Ansiedade", ["Sim", "Não"])
peer_pressure = st.sidebar.selectbox("Pressão alta", ["Sim", "Não"])
chronic_disease = st.sidebar.selectbox("Doença Crônica", ["Sim", "Não"])
fatigue = st.sidebar.selectbox("Fadiga", ["Sim", "Não"])
allergy = st.sidebar.selectbox("Alergia", ["Sim", "Não"])
wheezing = st.sidebar.selectbox("Chiado no peito", ["Sim", "Não"])
alcohol_consuming = st.sidebar.selectbox("Consumo de Álcool", ["Sim", "Não"])
coughing = st.sidebar.selectbox("Tosse", ["Sim", "Não"])
shortness_of_breath = st.sidebar.selectbox("Falta de Ar", ["Sim", "Não"])
swallowing_difficulty = st.sidebar.selectbox("Dificuldade ao Engolir", ["Sim", "Não"])
chest_pain = st.sidebar.selectbox("Dor no Peito", ["Sim", "Não"])

# Create a DataFrame with user input
user_data = pd.DataFrame({
    'Gênero': [1 if gender == 'Masculino' else 0],
    'Idade': [age],
    'Fumante': [1 if smoking == 'Sim' else 0],
    'Dedos Amarelados': [1 if yellow_fingers == 'Sim' else 0],
    'Ansiedade': [1 if anxiety == 'Sim' else 0],
    'Pressão Alta': [1 if peer_pressure == 'Sim' else 0],
    'Doença Crônica': [1 if chronic_disease == 'Sim' else 0],
    'Fadiga ': [1 if fatigue == 'Sim' else 0],
    'Alergia ': [1 if allergy == 'Sim' else 0],
    'Chiado no peito': [1 if wheezing == 'Sim' else 0],
    'Consumo de Álcool': [1 if alcohol_consuming == 'Sim' else 0],
    'Tosse': [1 if coughing == 'Sim' else 0],
    'Falta de Ar': [1 if shortness_of_breath == 'Sim' else 0],
    'Dificuldade ao Engolir': [1 if swallowing_difficulty == 'Sim' else 0],
    'Dor no Peito': [1 if chest_pain == 'Sim' else 0]
})


prediction_proba = model.predict_proba(user_data)[:, 1]
prediction = model.predict(user_data)[0]
    
if st.button("Prever"):
    st.subheader("Resultado da Previsão:")
    if prediction == 1:
        st.error("⚠️ Você tem uma alta probabilidade de ter câncer de pulmão!")
    else:
        st.success("🩺 Você tem uma baixa probabilidade de ter câncer de pulmão!")

    st.subheader("Probabilidade:")
    st.write(f"A probabilidade do usuário ter a doença é de: {prediction_proba[0]:.2%}")

    st.subheader("Relação entre Dados Médicos e o Resultado da Previsão:")
    fig, ax = plt.subplots()
    ax.pie(user_data.iloc[0], labels=user_data.columns, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)
    pass

st.markdown("---")
st.markdown("Criado por Miguel Julio 🚀")
