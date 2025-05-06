# 📊 Leitor de Extrato do FGTS
Projeto em Python para a extração de dados de extratos do FGTS

## 🧠 Motivação
O Fundo de Garantia do Tempo de Serviço (FGTS), é um beneficio concedido aos trabalhadores com carteira assinada visando oferecer uma estabilidade financeira em uma situação de demissão sem justa causa.

O aplicativo da Caixa Econômica Federal, instituição responsável pela gestão do FGTS, possibilita a geração de um extrato bancário do fundo. 
Porém, o extrato contém apenas as datas e valores depositados, com dados dispersos e sem gráficos, análises ou informações que agregam na compreensão da situação do fundo. 
Desta forma, muitos trabalhadores podem enfrentar dificuldades para acompanhar a evolução dos valores depositados.

Pensando nesta limitação surgiu a ideia deste projeto: 
Uma ferramenta que transforma os dados do extrato do FGTS em gráficos informativos e de fácil entendimento. 
Com ele, o trabalhador pode visualizar a evolução dos depósitos, identificar possíveis inconsistências e ter um controle preciso de seus recursos.

## 🚀 Funcionalidades
- ✅ Leitura e extração de dados de extratos do FGTS
- ✅ Limpeza e organização dos dados
- ✅ Geração de gráficos interativos com base nos depósitos

## 🛠️ Bibliotecas Utilizadas
- [Pandas](https://pandas.pydata.org)
- [pdfplumber](https://pypi.org/project/pdfplumber/)
- [numpy](https://numpy.org)
- [streamlit](https://streamlit.io)
- [plotly.express](https://plotly.com/python/plotly-express/)
- [re](https://docs.python.org/3/library/re.html)

## 📦 Instalação
Com o projeto baixado, digitar o seguinte comando no terminal: streamlit run "read_pdf.py".
