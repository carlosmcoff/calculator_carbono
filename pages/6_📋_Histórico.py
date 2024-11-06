import streamlit as st

st.title("Histórico de Emissões")

# Inicializa o session state se não existir
if 'calculos' not in st.session_state:
    st.session_state['calculos'] = []

# Inicializa o session state se não existir
if 'calculos_de_consumo' not in st.session_state:
    st.session_state['calculos_de_consumo'] = []


# Gera um historico do consumo de energia   
def gerar_relatorio_veiculo(calculos_veiculo):
    if calculos_veiculo:
        st.title("Veículos")
        # Criar uma tabela para exibir os cálculos
        st.write("### Cálculos Realizados:")
        for i, calc in enumerate(calculos_veiculo, start=1):
            st.write(f"- Tipo de Veículo: {calc['tipo_veiculo']}")
            st.write(f"- Potência: {calc['potencia']}")
            st.write(f"- Combustível: {calc['combustivel']}")
            if calc['distancia'] == 1:
                st.write(f"- Distância percorrida: {calc['distancia']} quilômetro")
            else:
                st.write(f"- Distância percorrida: {calc['distancia']} quilômetros")
            st.write(f"- Emissão de CO₂: {calc['emissao']} KG")
            st.write("---")  # Separador entre cálculos
        
gerar_relatorio_veiculo(st.session_state['calculos'])


# Gera um historico dos veiculos e emissoes
def gerar_relatorio_energia(calculo_consumo):
    if calculo_consumo:
        st.title("Energia")
        # Criar uma tabela para exibir os cálculos
        st.write("### Cálculos Realizados:")
        for i, calc in enumerate(calculo_consumo, start=1):
            if calc['consumokWh']:
                st.write(f"- Matriz de Energia: {calc['matriz']}")
                st.write(f"- Consumo kWh: {calc['consumokWh']}")
                st.write(f"- Emissão de CO₂: {calc['emissao']} KG")
                st.write("---")  # Separador entre cálculos

gerar_relatorio_energia(st.session_state['calculos_de_consumo'])     


# Limpar as listas
if st.session_state['calculos'] or st.session_state['calculos_de_consumo']:
    if (st.button("Limpar cálculos")):
        st.session_state['calculos'] = []
        st.session_state['calculos_de_consumo'] = []