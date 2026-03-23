#🏡 Impacto da Renda Média Regional na Precificação de Imóveis Residenciais

Análise exploratória, modelagem e insights sobre relação entre renda e valor de imóveis

📌 Sobre o Projeto

Este projeto investiga como a renda média regional influencia o preço de imóveis residenciais.
Foram aplicadas técnicas de análise de dados, visualização e modelagem estatística para identificar padrões, correlações e variáveis que mais impactam a precificação imobiliária.

O estudo foi desenvolvido em Python dentro de um notebook Jupyter, permitindo reprodutibilidade e explicação passo a passo.

🎯 Objetivos

Analisar dados de renda e preços de imóveis por região.

Explorar correlações entre variáveis socioeconômicas e o mercado imobiliário.

Desenvolver um modelo preditivo inicial para estimar preços residenciais.

Identificar regiões com maior discrepância entre renda e valorização de imóveis.

📂 Estrutura do Projeto
├── data/
│   ├── raw/               # Dados brutos
│   ├── processed/         # Dados tratados
├── notebooks/
│   ├── analise_renda_precos.ipynb
├── src/
│   ├── preprocess.py      # Funções de tratamento dos dados
│   ├── models.py          # Algoritmos e treinamentos
│   ├── utils.py           # Funções auxiliares
├── README.md
└── requirements.txt

🧰 Tecnologias Utilizadas

Python 3.x

Pandas

NumPy

Matplotlib / Seaborn

Scikit-Learn

Jupyter Notebook

📊 Principais Etapas Realizadas
✔ 1. Carregamento e limpeza dos dados

Tratamento de inconsistências, valores ausentes, padronização de colunas e normalização.

✔ 2. Análise Exploratória (EDA)

Distribuição de preços por região

Análise da renda média

Boxplots, heatmaps e mapas de correlação

✔ 3. Engenharia de Atributos

Criação de variáveis regionais

Normalização e encoding de variáveis categóricas

✔ 4. Modelagem Preditiva

Modelos testados:

Regressão Linear

Random Forest Regressor

Gradient Boosting

✔ 5. Avaliação

Métricas utilizadas:

MAE

RMSE

R²

📈 Resultados e Insights

Alguns achados importantes (exemplo — personalize conforme seu notebook):

Há uma correlação positiva moderada entre renda regional e preços de imóveis.

Algumas regiões apresentam preços acima do esperado, indicando valorização extra.

O modelo com melhor desempenho foi o Random Forest, com R² acima de 80%# Impacto-da-Renda-M-dia-Regional-na-Precifica-o-de-Im-veis-Residenciais
