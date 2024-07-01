import streamlit as st
import pandas as pd
import numpy as np


st.title("🔴 Streamlit")

st.write("Hello World")

if st.button("❄ Snowflakes"):
    st.snow()

st.write("Tabela")

df = pd.DataFrame({
    'ID' : [1, 2, 3, 4, 5],
    'Produto' : ["Arroz", "Batata", "Carne", "Feijão", "Tomate"],
    'Preço' : [30, 5, 25, 10, 2]
})

st.write(df)

st.header("Teste")

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')

st.subheader('Slider de intervalo')

values = st.slider(
     'Escolha um intervalo de valores',
     0.0, 100.0, (25.0, 75.0))
st.write('Valores:', values)


qtd = st.slider(
    'Escolha um numero',
    1, 6
)
st.write("Qtd", qtd)

st.bar_chart(df)
st.line_chart(df)

option = st.selectbox(
     'Qual a sua cor favorita?',
     ('Azul', 'Vermelho', 'Verde'))


st.write('Sua cor favorita é ', option)


options = st.multiselect(
     'Quais são suas cores favoritas?',
     ['Verde', 'Amarelo', 'Vermelho', 'Azul'],
     ['Amarelo', 'Vermelho'])


st.write('Você selecionou:', options)


icecream = st.checkbox('Sorvete')
coffee = st.checkbox('Café')
cola = st.checkbox('Refrigerante')


if icecream:
     st.write("Sucesso! Aqui está o seu 🍦")


if coffee:
     st.write("Ok, aqui está o seu café ☕")


if cola:
     st.write("E lá vamos nós 🥤")


import streamlit as st


st.title('Customizando o tema de aplicações Streamlit')


st.write('Conteúdo do arquivo `.streamlit/config.toml` desta aplicação')

st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
""")

number = st.sidebar.slider('Selecione um número:', 0, 10, 5)
st.write('O número selecionado no controle deslizante é:', number)

st.subheader('Upload de CSV')
uploaded_file = st.file_uploader("Escolha um arquivo")
