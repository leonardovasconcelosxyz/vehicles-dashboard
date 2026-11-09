# Painel de anúncios de venda de carros

Aplicativo web (dashboard) que permite explorar um conjunto de dados de anúncios de venda de carros usados nos EUA.

🔗 **Aplicativo online:** https://vehicles-dashboard-9gdv.onrender.com/

> O app está hospedado no plano gratuito do Render. Se ele estiver "dormindo", a primeira abertura pode levar até 1 minuto. É só atualizar a página.

## Funcionalidades
- **Histograma da quilometragem** (`odometer`): mostra como a quilometragem dos carros anunciados se distribui.
- **Gráfico de dispersão preço × quilometragem**: mostra a relação entre a quilometragem e o preço dos anúncios.
- Cada gráfico aparece ao marcar a **caixa de seleção** correspondente, e os dois podem ser exibidos ao mesmo tempo.

## Dados
`vehicles_us.csv`: 51.525 anúncios com preço, ano, modelo, condição, quilometragem, tipo de combustível, cor, entre outros.
A análise exploratória está em [`notebooks/EDA.ipynb`](notebooks/EDA.ipynb).

## Tecnologias
Python · pandas · Plotly Express · Streamlit · Render

## Como rodar localmente
```bash
git clone https://github.com/leonardovasconcelosxyz/vehicles-dashboard.git
cd vehicles-dashboard
python3 -m venv vehicles_env
source vehicles_env/bin/activate
pip install -r requirements.txt
streamlit run app.py
```
Depois, abra `http://localhost:10000` no navegador.