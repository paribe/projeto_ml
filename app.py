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

diametro = st.number_input("Digite o tamanho do diametro da pizza: ")

if diametro:
    preco_previsto = modelo.predict([[diametro]])[0][0]
    st.write(f"O valor da pizza do diâmetro de {diametro:.2f} cm é de R$ {preco_previsto:.2f}")
    st.balloons()
