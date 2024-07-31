import streamlit as st
import pandas as  pd
from sklearn.linear_model import LinearRegression

#ler arquivo csv
df = pd.read_csv("pizzas.csv")

#criar um modelo
# ensinar esse modelo com dataframe pizza com as colunas diametro e preco

modelo = LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]
modelo.fit(x,y)

#  web
st.title("Prevendo valor de uma pizza")

st.divider()
# Usar st.text_input para permitir entrada nula
diametro_input = st.text_input("Digite o tamanho do diâmetro da pizza em cm:")

if diametro_input:
    try:
        diametro = float(diametro_input)
        preco_previsto = modelo.predict([[diametro]])[0][0]
        st.write(f"O valor da pizza do diâmetro de {diametro:.2f} cm é de R$ {preco_previsto:.2f}")
        st.balloons()
    except ValueError:
        st.error("Por favor, insira um valor numérico válido para o diâmetro.")
else:
    st.write("Por favor, insira o diâmetro da pizza para calcular o valor.")