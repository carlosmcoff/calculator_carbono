import streamlit as st

# Inicializa o session state se não existir
if 'calculos' not in st.session_state:
    st.session_state['calculos'] = []

def mostrar_relatorio(calculos):
    st.header("Histórico de Emissões")
    
    if calculos:
        # Criar uma tabela para exibir os cálculos
        st.write("### Cálculos Realizados:")
        for i, calc in enumerate(calculos, start=1):
            st.write(f"**Cálculo {i}:**")
            st.write(f"- Tipo de Veículo: {calc['tipo_veiculo']}")
            st.write(f"- Potência: {calc['potencia']}")
            st.write(f"- Combustível: {calc['combustivel']}")
            if calc['distancia'] == 1:
                st.write(f"- Distância percorrida: {calc['distancia']} quilômetro")
            else:
                st.write(f"- Distância percorrida: {calc['distancia']} quilômetros")
            st.write(f"- Emissão de CO₂: {calc['emissao']} KG")
            st.write("---")  # Separador entre cálculos
    else:
        st.write("Nenhum cálculo realizado até o momento.")
        
if st.button("Limpar cálculos"):
    st.session_state['calculos'] = []
        
mostrar_relatorio(st.session_state.calculos)
