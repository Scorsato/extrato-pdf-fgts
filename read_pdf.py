import streamlit as st
import pdfplumber
import numpy as np
import pandas as pd
import re
import plotly.express as px

st.set_page_config(
    layout='wide',
    page_title='FGTS',
    page_icon=':moneybag:'
)

st.title("Leitor de Extrato do FGTS")

arquivo = st.file_uploader('Selecione o arquivo contendo o extrato que deseja consultar', type='pdf')

if arquivo is not None:
    data = []

    # Abre o PDF
    with pdfplumber.open(arquivo) as pdf:
        for page_number, page in enumerate(pdf.pages, start=1):
            text = page.extract_text()
            if text:

                # Primeira página do extrato
                if page_number == 1:
                
                    lines1 = text.split("\n")
                    # Remover os dados de identificação
                    del lines1[0:13]
                    lines1.pop()

                    #Padronização dos dados
                    for linha in lines1:
                        padrao = re.match(r"(\d{2}/\d{2}/\d{4})\s+(.+?)\s+R\$\s*([\d.,]+)\s+R\$\s*([\d.,]+)", linha)
                        if padrao:
                            data.append([
                            padrao.group(1),  # Data
                            padrao.group(2).strip(),  # Lançamento
                            float(padrao.group(3).replace(".", "").replace(",", ".")),  # Valor
                            float(padrao.group(4).replace(".", "").replace(",", "."))  # Total
                            ])
                #Demais páginas do extrato
                else:
                    lines = text.split("\n")
                    del lines[0:1]
                    lines.pop()
                    for linha in lines:
                        padrao = re.match(r"(\d{2}/\d{2}/\d{4})\s+(.+?)\s+R\$\s*([\d.,]+)\s+R\$\s*([\d.,]+)", linha)
                        if padrao:
                            data.append([
                            padrao.group(1),  # Data
                            padrao.group(2).strip(),  # Lançamento
                            float(padrao.group(3).replace(".", "").replace(",", ".")),  # Valor
                            float(padrao.group(4).replace(".", "").replace(",", "."))  # Total
                            ])

    #Transformar em dataframe
    df = pd.DataFrame(data, columns=['Data', 'Lançamento', 'Valor', 'Total'])
    df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')
    df['Ano'] = df['Data'].dt.year
    df['Mês'] = df['Data'].dt.strftime('%b/%y').str.lower()

    df['Tipo'] = np.where(df['Lançamento'].str.lower().str.contains('deposito'), 'Depósito', 'Juros')

    #Opcão para selecionar um ano especifico e filtrando no dataframe
    opcao_ano = st.selectbox('Selecionar Ano', df['Ano'].unique(), index=None, placeholder='Ano')

    df_ano = df[df['Ano'] == opcao_ano]

    if df_ano.empty:
        df_ano = df

    df_acumulado = df_ano.groupby('Mês', as_index=False).tail(1)

    #Soma de Depósitos e Juros
    totalD = df_ano[df_ano['Tipo'] == 'Depósito']['Valor'].sum()
    totalJ = df_ano[df_ano['Tipo'] == 'Juros']['Valor'].sum()

    #Criação dos gráficos
    fig_pie = px.pie(df_ano, values='Valor', names='Tipo', title='% de Depósito x Rendimento')
    fig_line = px.line(df_ano, x='Mês', y='Valor', color='Tipo', title='Depósito x Rendimento')
    fig_bar = px.bar(df_acumulado, x='Mês', y='Total', title='Total Acumulado')

    col1, col2 = st.columns(2)
    col3, col4 = st.columns(2)

    col1.subheader(f'Total Depósito: R$ {"{:.2f}".format(totalD)}')
    col2.subheader(f'Total Juros: R$ {"{:.2f}".format(totalJ)}')

    col3.plotly_chart(fig_line)
    col4.plotly_chart(fig_pie)

    st.plotly_chart(fig_bar)