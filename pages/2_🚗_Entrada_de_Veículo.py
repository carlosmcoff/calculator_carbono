import streamlit as st
import matplotlib.pyplot as plt
from functions.emissaoCarbono import *

# Inicializa o session state se não existir
if 'calculos' not in st.session_state:
    st.session_state['calculos'] = []  # Inicializar com lista vazia se ainda não existir

# Função para mostrar inputs e realizar cálculos
def mostrar_input():
    st.header("Entrada de Veículo")

    # Seleção do tipo de veículo
    tipo_veiculo = st.selectbox("Selecione o tipo de veículo:", ["Carro", "Caminhão", "Moto"], key="tipo_veiculo")
    
    # Placeholder para entradas adicionais com base no tipo de veículo
    if tipo_veiculo == "Carro":
        potencia = st.selectbox("Potência do Motor:", ["1.0 a 1.2", "1.4 a 1.6", "1.8 a 2.0", "Acima de 2.0"], key="potencia")
        tipo_combustivel = st.selectbox("Tipo de combustível:", [
            "Gasolina", 
            "Diesel", 
            "Etanol",
            "Gás Natural Veicular (GNV)", 
            "Gás Liquefeito de Petróleo (GLP)",
            "Elétrico"
        ], key="tipo_combustivel")
        
        km_percorrido = st.number_input("Distância percorrida em km:", min_value=1, key="km_percorrido")

        if km_percorrido > 0:
            if st.button("Calcular", key="calcular_button"):
                # Cálculo da emissão
                resultado = calculoEmissaoCO2(km_percorrido, potencia, tipo_combustivel)
                
                # Armazenar o resultado com informações detalhadas no session state
                st.session_state['calculos'].append({
                    'tipo_veiculo': tipo_veiculo,
                    'potencia': potencia,
                    'combustivel': tipo_combustivel,
                    'emissao': resultado
                })

                st.write(f"Emissão: {resultado} KG de CO₂")
                st.success("Cálculo realizado! Visualize o histórico de cálculos e a análise de dados nos menus ao lado.")

        else:
            st.warning("Distância precisa ser maior que zero!")
            
    elif tipo_veiculo == "Caminhão":        
        st.warning("Função para caminhão ainda não implementada.")
    elif tipo_veiculo == "Moto":
        st.warning("Função para moto ainda não implementada.")


mostrar_input()




