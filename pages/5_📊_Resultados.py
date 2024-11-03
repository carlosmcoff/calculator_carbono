import streamlit as st
import matplotlib.pyplot as plt

def atualizar_grafico():
    st.header("Análise de Dados")
    
    # Inicializa 'calculos' em session_state, se ainda não estiver presente
    if 'calculos' not in st.session_state:
        st.session_state['calculos'] = []

    # Verifica se há cálculos armazenados
    if st.session_state['calculos']:
        plt.clf()  # Limpa a figura para evitar sobreposição de gráficos anteriores

        # Separar tipos de veículos e suas emissões
        tipos_de_veiculos = []
        emissao_valores = []
        
        # Preenche as listas com os dados de session_state
        for i in st.session_state['calculos']:
            tipos_de_veiculos.append(f"{i['tipo_veiculo']} - {i['potencia']} ({i['combustivel']})")
            emissao_valores.append(float(i['emissao']))  # Garantir que 'emissao' seja numérico

        print(tipos_de_veiculos)
        print(emissao_valores)

        # Criar gráfico de barras com todos os elementos armazenados
        fig, ax = plt.subplots(figsize=(10, 5))  # Cria um único gráfico
        ax.bar(tipos_de_veiculos, emissao_valores, color='blue')
        ax.set_title('Emissões de CO₂ por Tipo de Veículo')
        ax.set_xlabel('Tipo de Veículo')
        ax.set_ylabel('Emissão de CO₂ (kg)')
        ax.set_xticks(range(len(tipos_de_veiculos)))  # Definir o número de rótulos
        ax.set_xticklabels(tipos_de_veiculos, rotation=45, ha='right')  # Rotacionar rótulos para facilitar a leitura
        plt.tight_layout()

        # Renderizar gráfico no Streamlit
        st.pyplot(fig)
    else:
        st.write("Nenhum cálculo realizado até o momento.")


# Botão para limpar os cálculos (opcional para teste)
if st.button("Limpar cálculos"):
    st.session_state['calculos'] = []

# Chamada da função para mostrar o gráfico
atualizar_grafico()
