import requests
import json 
import pandas as pd 
import streamlit as st



st.title("INMET")
st.write("Escreva o código da estação e escolha o período")
estadoEstacao=st.text_input("Código da estação - exemplo A301:", "")
data_inicio = st.date_input("dataini")
data_fim = st.date_input("datafinal")
form_res=st.button("SUBMIT")


def recuperarDados(estadoEstacao):
  response = requests.get("https://apitempo.inmet.gov.br/estacao/diaria/"+str(data_inicio)+"/"+str(data_fim)+"/"+estadoEstacao)
  #st.write(response.text)
  data = json.loads(response.text)
  df = pd.json_normalize(data)
  st.dataframe(df)

if form_res: recuperarDados(estadoEstacao)