def creditosCO2(projeto_compensacao, co2gasto):
    # Projetos de compensação de carbono e seus respectivos valores em reais por kg de CO2 emitido na atmosfera
    florestamento_Reflorestamento = 0.10
    conservacaoFlorestas = 0.075
    energiaRenovavel = 0.05
    ccs = 0.40
    melhoriasAgricolas_Manejos = 0.125
    biocombustiveis_biomassa = 0.075

    projeto = projeto_compensacao

    if projeto == "Florestamento e Reflorestamento":
        compensacao = florestamento_Reflorestamento * co2gasto
    
    if projeto == "Conservação de Florestas (REDD+)":
        compensacao = conservacaoFlorestas * co2gasto
    
    if projeto == "Energia Renovável (Eólica, Solar, Hidrelétrica)":
        compensacao = energiaRenovavel * co2gasto
    
    if projeto == "Captura e Armazenamento de Carbono (CCS)":
        compensacao = ccs * co2gasto
    
    if projeto == "Melhorias na Agricultura e Manejo de Solo":
        compensacao =  melhoriasAgricolas_Manejos * co2gasto
    
    if projeto == "Biocombustíveis e Biomassa":
        compensacao = biocombustiveis_biomassa * co2gasto

    # Resultado em reais
    roundCompensacao = round(compensacao, 2)
    return roundCompensacao


formas_compensacao = [
  {
    "titulo": "Florestamento e Reflorestamento",
    "descricao": "Plante árvores em áreas desmatadas para restaurar florestas e absorver CO₂ da atmosfera. Esse processo não só remove carbono, mas também recupera a biodiversidade, protege o solo contra erosão, e oferece habitats para inúmeras espécies. Projetos de reflorestamento podem ser combinados com práticas de manejo sustentável para garantir a saúde das florestas a longo prazo.",
    "link": "https://eos.com/pt/blog/florestamento/?form=MG0AV3"
  },
  {
    "titulo": "Conservação de Florestas (REDD+)",
    "descricao": "Proteja as florestas existentes para evitar desmatamento e degradação, mantendo valiosos reservatórios de carbono intactos. O REDD+ (Redução das Emissões por Desmatamento e Degradação Florestal) também promove benefícios sociais e econômicos para as comunidades locais, incentivando práticas de manejo sustentável e conservação da biodiversidade.",
    "link": "https://www.ipef.br/publicacoes/ctecnica/nr061.pdf"
  },
  {
    "titulo": "Energia Renovável (Eólica, Solar, Hidrelétrica)",
    "descricao": "Invista em fontes de energia limpa e sustentável, como eólica, solar e hidrelétrica, para reduzir a dependência de combustíveis fósseis e diminuir as emissões de CO₂. Essas fontes de energia renovável são inesgotáveis e oferecem uma alternativa ambientalmente amigável, reduzindo a poluição do ar e os impactos negativos das mudanças climáticas.",
    "link": "https://www.scielo.br/j/rarv/a/MRtjXRXX84cfQrZpBG3YPvk/"
  },
  {
    "titulo": "Captura e Armazenamento de Carbono (CCS)",
    "descricao": "Implemente tecnologias avançadas para capturar CO₂ diretamente da fonte de emissão, como usinas de energia, e armazená-lo em locais seguros subterrâneos, evitando sua liberação na atmosfera. O CCS é uma solução tecnológica que pode ser integrada com outras práticas de redução de emissões, ajudando a mitigar os efeitos das mudanças climáticas.",
    "link": "https://bing.com/search?q=Florestamento+e+Reflorestamento+artigos"
  },
  {
    "titulo": "Melhorias na Agricultura e Manejo de Solo",
    "descricao": "Adote práticas agrícolas sustentáveis que aumentem a captura de carbono no solo e reduzam as emissões de CO₂ da agricultura. Técnicas como plantio direto, rotação de culturas, e agroflorestas não apenas sequestrem carbono, mas também melhoram a saúde do solo, aumentam a produtividade agrícola, e promovem a sustentabilidade alimentar.",
    "link": "https://bing.com/search?q=Florestamento+e+Reflorestamento+artigos"
  },
  {
    "titulo": "Biocombustíveis e Biomassa",
    "descricao": "Utilize fontes renováveis de energia derivadas de matéria orgânica, como resíduos agrícolas e florestais, para substituir combustíveis fósseis. Biocombustíveis e biomassa podem ser convertidos em energia através de processos como fermentação e combustão, oferecendo uma alternativa sustentável e reduzindo as emissões de CO₂.",
    "link": "https://bing.com/search?q=Florestamento+e+Reflorestamento+artigos"
  }
]


