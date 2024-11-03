### **Estrutura do Projeto**

A estrutura do projeto é organizada da seguinte forma:

`CALCULATOR_RASC/`  
`│`  
`├── functions/`  
`│   └── emissaoCarbono.py      # Contém funções para cálculos de emissão de carbono`  
`│`  
`├── pages/`  
`│   ├── 2_Entrada_de_Veiculo.py # Página para entrada de dados do veículo`  
`│   ├── 3_Histórico.py          # Página para exibir o histórico de cálculos`  
`│   ├── 4_Resultados.py         # Página para visualização dos resultados (gráficos)`  
`│`  
`└── 1_Inicio.py                 # Página inicial da aplicação`

---

### **Arquivos e Explicações**

#### **1\. 1\_Inicio.py \- Página Inicial**

Este arquivo é responsável por apresentar a página inicial da aplicação. Aqui, o usuário é recebido com uma mensagem de boas-vindas e instruções para navegar pelo menu lateral.

##### **Código Explicado:**

* **`st.title`**: Define o título principal da página, que aparece em negrito no topo da aplicação. Neste caso, o título é "Calculadora de Compensação de Carbono".  
* **`st.write`**: Exibe uma mensagem informativa ao usuário, que dá instruções sobre como utilizar a aplicação.

A função desta página é simples: fornecer um ponto de entrada para a aplicação, com navegação pelas abas laterais. Aqui, não há cálculos ou dados processados; apenas uma interface introdutória.

---

#### **2\. 2\_Entrada\_de\_Veiculo.py \- Entrada de Dados do Veículo**

#### 

Este arquivo permite ao usuário inserir as informações sobre seu veículo, como o tipo de veículo, potência do motor, tipo de combustível e a distância percorrida. Com base nesses dados, a aplicação calcula as emissões de CO₂.

##### **Explicação das Funcionalidades:**

* **Sessão de Estado (`st.session_state`)**: O uso de `st.session_state` permite que os cálculos sejam armazenados de forma persistente enquanto o usuário navega pela aplicação. Se o estado ainda não foi inicializado, ele cria uma lista vazia para armazenar os cálculos.  
* **Função `mostrar_input`**:  
  * **`st.header`**: Define o cabeçalho da página "Entrada de Veículo".  
  * **`st.selectbox`**: Cria um menu suspenso onde o usuário pode selecionar o tipo de veículo e o combustível.  
  * **`st.number_input`**: Recebe a distância percorrida pelo veículo em quilômetros.  
  * **Cálculo da emissão**: O botão "Calcular" utiliza a função `calculoEmissaoCO2` (importada de `emissaoCarbono.py`) para calcular a emissão de CO₂ com base nos inputs fornecidos.  
  * **Armazenamento dos dados**: Após o cálculo, os dados são armazenados no `session_state` para que possam ser acessados posteriormente.

##### **Comportamento:**

Quando o usuário seleciona um veículo, insere os dados e clica no botão "Calcular", a aplicação realiza o cálculo e exibe o resultado diretamente na página.

---

#### **3\. 3\Compensação.py \- Compensação de Carbono**

Este arquivo é responsável por calcular a compensação de carbono com base em emissões de veículos e diferentes métodos de compensação.

##### **Explicação das Funcionalidades:**

* **Função `compensação`**:  
  * **`st.header`**: Compensação de Carbono".  
  * **Verificação do histórico**: Se houver cálculos armazenados, separa os tipos de veículos e suas emissões em duas listas.
  * **Selecionar um cálculo**: Cria um selectbox para selecionar um veículo e sua emissão.
  * **Selecionar forma de compensação"**: Cria um selectbox para selecionar uma forma de compensação de carbono.


##### **Comportamento:**

Ao clicar no botão "Calcular investimento", a função: Chama a função creditosCO2 para calcular o investimento necessário.
Exibe o título, descrição e link da forma de compensação selecionada.
Mostra o valor necessário para o investimento.

---

#### **4\. 4\_Histórico.py \- Histórico de Cálculos**

Este arquivo é responsável por exibir um histórico de todos os cálculos de emissões realizados durante a sessão. Ele acessa os dados armazenados no `session_state` e exibe os detalhes de cada cálculo.

##### **Explicação das Funcionalidades:**

* **Função `mostrar_relatorio`**:  
  * **`st.header`**: Define o cabeçalho "Histórico de Emissões".  
  * **Verificação do histórico**: Se houver cálculos armazenados, a função os exibe em uma lista formatada, mostrando o tipo de veículo, potência do motor, tipo de combustível e a emissão de CO₂ para cada cálculo.  
  * **Botão "Limpar cálculos"**: Permite ao usuário limpar todo o histórico de cálculos, removendo os dados armazenados no `session_state`.

##### **Comportamento:**

O usuário pode revisar todos os cálculos feitos anteriormente e, se desejar, limpar o histórico de emissões com o clique de um botão.

---

#### **5\. 5\_Resultados.py \- Visualização dos Resultados (Gráficos)**

Este arquivo cria um gráfico de barras para visualização das emissões de carbono com base nos cálculos armazenados.

##### **Explicação das Funcionalidades:**

**Função `atualizar_grafico()`**: Esta função é responsável por atualizar o gráfico de barras dinâmico, baseado nos cálculos de emissão de CO₂ realizados e armazenados na sessão do usuário. Aqui, vamos detalhar os principais passos:

**Verificação de Dados**:

* **Sessão de Estado (`st.session_state`)**: O uso de `st.session_state` permite que os cálculos sejam armazenados de forma persistente enquanto o usuário navega pela aplicação. Se o estado ainda não foi inicializado, ele cria uma lista vazia para armazenar os cálculos.

**Preparação dos Dados**:

* Aqui, duas listas são criadas: `tipos_veiculos` e `emissoes_valores`. A função itera sobre cada item armazenado no histórico de cálculos da sessão do usuário (`st.session_state['calculos']`) e extrai os nomes dos veículos e as respectivas emissões de CO₂. Esses dados serão utilizados para plotar o gráfico.

**Criação do Gráfico**:

* **`plt.subplots()`**: Cria uma figura (`fig`) e um eixo (`ax`). A figura é o container geral do gráfico, enquanto o eixo é onde o gráfico propriamente dito será desenhado.  
* **`ax.bar()`**: Gera um gráfico de barras, onde o eixo X recebe os nomes dos veículos e o eixo Y recebe as emissões de CO₂ correspondentes. Cada barra representa um veículo e sua respectiva emissão.

**Personalização do Gráfico**:

* As linhas acima adicionam rótulos aos eixos X e Y, respectivamente, e também um título ao gráfico. Isso ajuda a contextualizar as informações e tornar o gráfico mais legível.

**Rotacionar os Nomes dos Veículos**:  
`ax.set_xticklabels(nomes_veiculos, rotation=45, ha="right")`

* Esta linha ajusta a rotação dos nomes dos veículos no eixo X. Como os nomes dos veículos podem ser longos, a rotação de 45 graus garante que eles não se sobreponham e permaneçam legíveis. O parâmetro `ha="right"` significa que a ancoragem dos textos estará à direita, o que melhora a estética da apresentação.

**Renderização do Gráfico**:

* Esta linha é responsável por exibir o gráfico gerado na interface do Streamlit. O método `st.pyplot(fig)` pega a figura `fig` criada anteriormente com o `matplotlib` e a renderiza diretamente na página web.

##### **Comportamento:**

O gráfico é atualizado automaticamente com os dados das emissões calculadas e fornece uma visualização rápida da quantidade de CO₂ emitida por cada veículo.

