readme_content = """# Análise e Previsão do Nível do Rio

Este projeto tem como objetivo analisar dados históricos de nível do rio e chuvas para treinar um modelo de machine learning capaz de prever o nível do rio em Rio do Sul, utilizando dados de outras cidades como Ituporanga e Taió.

## Estrutura do Projeto

- `dados_rio_e_chuva.xlsx`: arquivo Excel com os dados históricos das medições.
- Notebook (`.ipynb`): contém todo o passo a passo desde a limpeza dos dados, análise exploratória, treinamento e avaliação do modelo de regressão linear.
- Modelos salvos:
  - `modelo_nivel_rio.pkl`: modelo de regressão linear treinado.
  - `scaler_nivel_rio.pkl`: objeto para normalização dos dados (StandardScaler).

## Tecnologias Utilizadas

- Python 3.10
- Pandas
- Matplotlib e Seaborn para visualização
- Scikit-learn para modelagem e avaliação
- Joblib para salvar o modelo e scaler

## Como Usar

1. Instale as dependências:

```bash
pip install pandas matplotlib seaborn scikit-learn joblib tqdm

2. Abra o notebook e execute as células para:

Carregar e limpar os dados.
Fazer a análise exploratória.
Treinar o modelo e avaliar sua performance.
Salvar o modelo e o scaler.

3. Você pode usar os arquivos .pkl para carregar o modelo e fazer previsões em novas aplicações.

