### **Estrutura do Projeto**

A estrutura do projeto é organizada da seguinte forma:

`CALCULATOR_RASC/`  
`├── data/`  
`│   └── formas_compensacao.py      # Contém dados sobre as compensações`  
`│`  
`├── functions/`  
`│   └── compensacao_carbono.py      # Contém função para cálculos de compensação de carbono`  
`│   └── emissao_carbono.py      # Contém função para cálculos de emissão de carbono`  
`│`  
`├── pages/`  
`│   ├── 2_Entrada_de_Veiculo.py    # Página para calculo de emissao de veículo`  
`│   ├── 3_Consumo_de_Energia.py     # Página para calculo de consumo de energia`  
`│   ├── 4_Compensação.py     # Página para calcular e exibir as compensações de carbono`  
`│   ├── 5_Resultados.py   # Página para visualização dos dados/gráficos`                    
`│   ├── 6_Histórico.py   # Página para vizualização dos calculos feitos` 
`│`  
`└── 1_Inicio.py                 # Página inicial da aplicação`

---

### **Arquivos e Explicações**

# Calculadora de Carbono 🌱

Projeto desenvolvido para cálculo e compensação de emissões de carbono com base em inputs do usuário. O sistema inclui a interface desenvolvida em **Streamlit** e a lógica de cálculos estruturada separadamente. A aplicação busca promover conscientização ambiental e facilitar o acesso a informações sobre emissões de carbono e formas de compensação.

---

## Estrutura do Projeto 📂

### Principais Arquivos e Funcionalidades:

1. **`Inicio.py`**  
   Arquivo principal da aplicação, que gerencia a estruturação das abas e a navegação entre elas.  

2. **`Entrada de Veiculo.py`**  
   Aba para cálculos relacionados a emissões de carbono de veículos. Solicita informações como tipo de veículo, combustível utilizado e distância percorrida, e calcula as emissões associadas.  

4. **`Consumo de Energia.py`**  
   Aba dedicada aos cálculos de emissões relacionadas ao consumo de energia elétrica. Solicita dados como o consumo em kWh e a matriz energética utilizada.  

5. **`Compensacao.py`**  
   Aba para sugerir e calcular formas de compensação para as emissões geradas. Inclui investimentos estimados em projetos de compensação, como reflorestamento.  

6. **`Historico de Emissoes.py`**  
   Aba que exibe o **histórico de cálculos de emissões** realizadas pelo usuário, separadas por categorias: veículos e energia. Permite a visualização detalhada de cada cálculo e a opção de limpar o histórico armazenado no estado da aplicação.  

7. **`Historico de Compensacoes.py`**  
   Aba que apresenta o **histórico de compensações realizadas**. Mostra os itens compensados, formas de compensação utilizadas e os valores de investimento. Também oferece a opção de limpar o histórico das compensações.  

---

## Como Utilizar 🚀

1. Certifique-se de ter o **Python** e **Streamlit** instalado em sua máquina.  
3. Na pasta principal execute o comando `streamlit run 1_🏠_Início.py.py` para iniciar a aplicação.  

---

**Desenvolvido com 💚 pela equipe do projeto Calculadora de Carbono**  

