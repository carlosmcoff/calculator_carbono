import streamlit as st
from functions.compensacaoCarbono import *

# Inicializa o session state se não existir
if 'calculos' not in st.session_state:
    st.session_state['calculos'] = []  


def compensacoes(calculos):
  st.header("Compensação de Carbono")
  
  if calculos:
    # Separar tipos de veículos e suas emissões
    tipos_veiculos = []
    emissoes_valores = []
        
    # Preenche as listas com os dados de session_state
    for i in calculos:
      tipos_veiculos.append(f"{i['tipo_veiculo']} - {i['potencia']}: {i['emissao']} KG de CO₂")
      emissoes_valores.append(float(i['emissao']))  

    # Seleciona o veiculo e sua emissão
    veiculo = st.selectbox("Selecione a emissão para compensação.", tipos_veiculos)

    # Encontrar index da seleção e pegar na lista a emissão do mesmo
    index = tipos_veiculos.index(veiculo)
    emissao = emissoes_valores[index]

    # Extrair os títulos da lista formas_compensacao e exibe na seleção
    titulos = [item["titulo"] for item in formas_compensacao]
    compensacao = st.selectbox("Selecione a forma de compensação:", titulos)

    if st.button("Calcular investimento", key="compensar_button"):
      resultado = creditosCO2(compensacao, emissao)

      # Encontrar a forma de compensação selecionada
      forma_selecionada = next((item for item in formas_compensacao if item["titulo"] == compensacao), None)

      if forma_selecionada:
        st.title(compensacao)
        st.write(forma_selecionada["descricao"])
        st.markdown(f"[Leia mais]({forma_selecionada['link']})")
        st.success(f"Valor para investimento: R${resultado}")

  else:
     st.write("Nenhum cálculo realizado até o momento.")

compensacoes(st.session_state['calculos'])


