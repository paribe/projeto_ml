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

#st.divider()
# Usar st.text_input para permitir entrada nula
#diametro_input = st.text_input("Digite o tamanho do diâmetro da pizza em cm:")
diametro_input = st.number_input("Digite o tamanho do diâmetro da pizza em cm:", min_value=0.0, max_value=100.0, value=0.0, step=0.1)
#  , min_value=0.0, max_value=100.0, value=30.0, step=0.1
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

st.divider()    

st.image("diametro2.gif")
# Adicionar a legendass
st.write('Diâmetro: é a linha reta que passa pelo centro da circunferência e toca dois pontos opostos da mesma.')
st.write('40 cm ou 39 cm - pizza extra grande com 10 pedaços; 35 cm - pizza grande (padrão) com 8 pedaços; 30 cm - pizza média com 6 pedaços; 25 cm - pizza pequena com 4 pedaços.')