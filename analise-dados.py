import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure

st.title('ANÁLISE EXPLORATÓRIA DE DADOS (VERSÃO 1)')
st.markdown('Feito por: Lucas de Melo Souza')

@st.cache(allow_output_mutation=True)
def PegaFile(file):
    dataset = pd.read_excel(file)
    return dataset

@st.cache(allow_output_mutation=True)
def PegaFile2(file,separador):
    dataset = pd.read_csv(file,sep = separador)
    return dataset



formato = st.radio('Qual o formato do arquivo?',("csv","xlsx"))

if formato == "csv":
    separador = st.radio('Qual o separador?',(';',','))
    st.write('Selecionado: Arquivo .csv separado por: ',separador)
    file = st.file_uploader('Importe a base de dados para análise:',type = formato)
    if file is not None:
        
        dataset = PegaFile2(file,separador)
        #exibindo um pedaço dos dados
        n_heads = st.slider('Nº de linhas exibidas',min_value = 0, max_value = len(dataset),value = 1,step = 1)
        st.write(dataset.head(n_heads))
        ##---------------------TIPO DE ANÁLISE DE DADOS-------------------------##
        analise = st.selectbox('Selecione o tipo de análise exploratória:',('Análise de dados faltantes','Distribuição de dados','Estatísticas','Correlações','modelo de Machine Learning'))
            
        if analise == 'Análise de dados faltantes':
            
            explorer = pd.DataFrame({'Variaveis':dataset.columns,'Num de faltantes' :dataset.isna().sum(axis=0).values,'Tipo de dado':dataset.dtypes.values})
                    
            if sum(explorer['Num de faltantes'].values) > 0:
                
                st.text('Existem dados faltantes na base de dados!')
                st.header('Imputação de dados')
                var  = st.selectbox('Selecione a variavel para avaliar',options = dataset.columns)
                st.subheader('Selecione a estratégia de imputação:')
                if dataset[var].dtypes =='float64' or dataset[var].dtypes =='int64':
                    
                    opt = st.selectbox('',options = ('média','mediana','moda','zeros','apagar dados faltantes'))
                            
                    if opt == 'média':
                        
                                
                        st.write('Os dados da coluna ',var,' serão substituídos por: ',dataset[var].mean(),'.')
                        botao = st.button('Imputar dados')
                                
                        if botao:
                            dataset[var] = dataset[var].fillna(dataset[var].mean())
                            
                    if opt == 'mediana':
                        
                                
                        st.write('Os dados da coluna ',var,' serão substituídos por: ',dataset[var].median(),'.')
                        botao = st.button('Imputar dados')
                                
                        if botao:
                            dataset[var] = dataset[var].fillna(dataset[var].median())
                    if opt == 'moda':
                                
                        st.write('Os dados da coluna ',var,' serão substituídos por: ',dataset[var].mode()[0],'.')
                        botao = st.button('Imputar dados')
                                
                        if botao:
                            dataset[var] = dataset[var].fillna(dataset[var].mode()[0])
                    if opt == 'zeros':
                                
                        st.write('Os dados da coluna ',var,' serão substituídos por: 0.')
                        botao = st.button('Imputar dados')
                                
                        if botao:
                            dataset[var] = dataset[var].fillna(0)
                    if opt == 'apagar dados faltantes':
                        
                        st.write('Cuidado ao utilizar, pois você perderá',(dataset[var].isna().sum()/len(dataset)) *100,"% dos dados.")
                        botao = st.button('Imputar dados')
                                
                        if botao:
                            dataset[var] = dataset[var].dropna()
                                    
                    explorer = pd.DataFrame({'Variaveis':dataset.columns,'Num de faltantes' :dataset.isna().sum(axis=0).values,'Tipo de dado':dataset.dtypes.values})
                    st.write('Sumário da base de dados',explorer)
                else:
                    
                    opt = st.selectbox('',options = ('moda','unknown','apagar dados faltantes'))
                    if opt == 'moda':
                        
                        
                        st.write('Os dados da coluna ',var,' serão substituídos por: ',dataset[var].mode()[0],'.')
                        botao = st.button('Imputar dados')
                                
                        if botao:
                            
                            dataset[var] = dataset[var].fillna(dataset[var].mode()[0])
                    if opt == 'unknown':
                        st.write('Os dados da coluna ',var,' serão substituídos por: "unknown".')
                        botao = st.button('Imputar dados')
                                
                        if botao:
                            dataset[var] = dataset[var].fillna("unknown")
                    if opt == 'apagar dados faltantes':
                        
                        st.write('Cuidado ao utilizar, pois você perderá',(dataset[var].isna().sum()/len(dataset)) *100,"% dos dados.")
                        botao = st.button('Imputar dados')
                                    
                        if botao:
                            dataset[var] = dataset[var].dropna()
                                    
                            
                    explorer = pd.DataFrame({'Variaveis':dataset.columns,'Num de faltantes' :dataset.isna().sum(axis=0).values,'Tipo de dado':dataset.dtypes.values})
                    st.write('Sumário da base de dados',explorer)
        if analise ==  'Distribuição de dados':
            
            var  = st.selectbox('Selecione a variavel para avaliar',options = dataset.columns)
            if dataset[var].dtypes == 'object' or dataset[var].dtypes == 'bool':
                hist_data = dataset[var].value_counts()
                figure(figsize = (10,10))
                plt.bar(x = hist_data.index,height = hist_data.values,align = 'center')
                plt.xlabel(var)
                plt.ylabel('Ocorrências')
                plt.title('Distribuição do dataset')
                st.pyplot()
            if dataset[var].dtypes == 'int64' or dataset[var].dtypes == 'float64':
                n_bins = st.slider('Número de divisões do histograma',min_value = 0, max_value = 30,value = 5,step = 1)
                plt.hist(dataset[var].values,bins = n_bins)
                plt.xlabel(var)
                plt.ylabel('Ocorrências')
                plt.title('Distribuição do dataset')
                st.pyplot()
        if analise == 'Estatísticas':
            
                
            var  = st.selectbox('Selecione a variavel para avaliar',options = dataset.columns)
            if dataset[var].dtypes == 'object' or dataset[var].dtypes == 'bool':
                    
                moda = dataset[var].mode()[0]
                st.write('Valor mais ocorrente: ',moda)
            if dataset[var].dtypes == 'int64' or dataset[var].dtypes == 'float64':
                
                    
                moda = dataset[var].mode()[0]
                media = dataset[var].mean()
                mediana = dataset[var].median()
                skewness = dataset[var].skew()
                curtose = dataset[var].kurtosis()
                st.write('moda: ' ,moda)
                st.write('média: ',media)
                st.write('mediana: ',mediana)
                st.write('Assimetria: ',skewness)
                st.write('Curtose: ',curtose)
        if analise == 'Correlações':
            figure(figsize =(10,5))  
            plt.matshow(dataset.corr())
            plt.xticks(range(len(dataset.columns)),dataset.columns,rotation = 90)
            plt.yticks(range(len(dataset.columns)),dataset.columns)
            plt.title('Matriz de correlações')
            plt.colorbar()
            st.pyplot()
        if analise == "modelo de Machine Learning":
            st.subheader('EM BREVE! :)')
        
    if file is None:
        
        st.markdown('Aguardando arquivo...')


if formato == "xlsx":
        #importando os dados
        st.markdown('Selecionado: Arquivo .xlsx')
        file = st.file_uploader('Importe a base de dados para análise:',type = formato)
        
        if file is not None:
            
            dataset = PegaFile(file)
            #exibindo um pedaço dos dados
            n_heads = st.slider('Nº de linhas exibidas',min_value = 0, max_value = len(dataset),value = 1,step = 1)
            st.write(dataset.head(n_heads))
            ##---------------------TIPO DE ANÁLISE DE DADOS-------------------------##
            analise = st.selectbox('Selecione o tipo de análise exploratória:',('Análise de dados faltantes','Distribuição de dados','Estatísticas','Correlações','modelo de Machine Learning'))
            
            if analise == 'Análise de dados faltantes':
                    explorer = pd.DataFrame({'Variaveis':dataset.columns,'Num de faltantes' :dataset.isna().sum(axis=0).values,'Tipo de dado':dataset.dtypes.values})
                    
                    if sum(explorer['Num de faltantes'].values) > 0:
                        st.text('Existem dados faltantes na base de dados!')
                        st.header('Imputação de dados')
                        var  = st.selectbox('Selecione a variavel para avaliar',options = dataset.columns)
                        st.subheader('Selecione a estratégia de imputação:')
                        if dataset[var].dtypes =='float64' or dataset[var].dtypes =='int64':
                            
                            opt = st.selectbox('',options = ('média','mediana','moda','zeros','apagar dados faltantes'))
                            
                            if opt == 'média':
                                
                                st.write('Os dados da coluna ',var,' serão substituídos por: ',dataset[var].mean(),'.')
                                botao = st.button('Imputar dados')
                                
                                if botao:
                                    dataset[var] = dataset[var].fillna(dataset[var].mean())
                            
                            if opt == 'mediana':
                                
                                st.write('Os dados da coluna ',var,' serão substituídos por: ',dataset[var].median(),'.')
                                botao = st.button('Imputar dados')
                                
                                if botao:
                                    dataset[var] = dataset[var].fillna(dataset[var].median())
                            if opt == 'moda':
                                
                                st.write('Os dados da coluna ',var,' serão substituídos por: ',dataset[var].mode()[0],'.')
                                botao = st.button('Imputar dados')
                                
                                if botao:
                                    dataset[var] = dataset[var].fillna(dataset[var].mode()[0])
                            if opt == 'zeros':
                                
                                st.write('Os dados da coluna ',var,' serão substituídos por: 0.')
                                botao = st.button('Imputar dados')
                                
                                if botao:
                                    dataset[var] = dataset[var].fillna(0)
                            if opt == 'apagar dados faltantes':
                                
                                st.write('Cuidado ao utilizar, pois você perderá',(dataset[var].isna().sum()/len(dataset)) *100,"% dos dados.")
                                botao = st.button('Imputar dados')
                                
                                if botao:
                                    dataset[var] = dataset[var].dropna()
                                    
                            explorer = pd.DataFrame({'Variaveis':dataset.columns,'Num de faltantes' :dataset.isna().sum(axis=0).values,'Tipo de dado':dataset.dtypes.values})
                            st.write('Sumário da base de dados',explorer)
                        else:
                            opt = st.selectbox('',options = ('moda','unknown','apagar dados faltantes'))
                            if opt == 'moda':
                                st.write('Os dados da coluna ',var,' serão substituídos por: ',dataset[var].mode()[0],'.')
                                botao = st.button('Imputar dados')
                                
                                if botao:
                                    dataset[var] = dataset[var].fillna(dataset[var].mode()[0])
                            if opt == 'unknown':
                                st.write('Os dados da coluna ',var,' serão substituídos por: "unknown".')
                                botao = st.button('Imputar dados')
                                
                                if botao:
                                    dataset[var] = dataset[var].fillna("unknown")
                            if opt == 'apagar dados faltantes':
                            
                                st.write('Cuidado ao utilizar, pois você perderá',(dataset[var].isna().sum()/len(dataset)) *100,"% dos dados.")
                                botao = st.button('Imputar dados')
                                
                                if botao:
                                    dataset[var] = dataset[var].dropna()
                                    
                            explorer = pd.DataFrame({'Variaveis':dataset.columns,'Num de faltantes' :dataset.isna().sum(axis=0).values,'Tipo de dado':dataset.dtypes.values})
                            st.write('Sumário da base de dados',explorer)
            if analise ==  'Distribuição de dados':
                var  = st.selectbox('Selecione a variavel para avaliar',options = dataset.columns)
                if dataset[var].dtypes == 'object' or dataset[var].dtypes == 'bool':
                    hist_data = dataset[var].value_counts()
                    figure(figsize = (10,10))
                    plt.bar(x = hist_data.index,height = hist_data.values,align = 'center')
                    plt.xlabel(var)
                    plt.ylabel('Ocorrências')
                    plt.title('Distribuição do dataset')
                    st.pyplot()
                if dataset[var].dtypes == 'int64' or dataset[var].dtypes == 'float64':
                    n_bins = st.slider('Número de divisões do histograma',min_value = 0, max_value = 30,value = 5,step = 1)
                    plt.hist(dataset[var].values,bins = n_bins)
                    plt.xlabel(var)
                    plt.ylabel('Ocorrências')
                    plt.title('Distribuição do dataset')
                    st.pyplot()
            if analise == 'Estatísticas':
                 var  = st.selectbox('Selecione a variavel para avaliar',options = dataset.columns)
                 if dataset[var].dtypes == 'object' or dataset[var].dtypes == 'bool':
                     moda = dataset[var].mode()[0]
                     st.write('Valor mais ocorrente: ',moda)
                 if dataset[var].dtypes == 'int64' or dataset[var].dtypes == 'float64':
                     
                     moda = dataset[var].mode()[0]
                     media = dataset[var].mean()
                     mediana = dataset[var].median()
                     skewness = dataset[var].skew()
                     curtose = dataset[var].kurtosis()
                     st.write('moda: ' ,moda)
                     st.write('média: ',media)
                     st.write('mediana: ',mediana)
                     st.write('Assimetria: ',skewness)
                     st.write('Curtose: ',curtose)
            if analise == 'Correlações':
                plt.matshow(dataset.corr())
                plt.xticks(range(len(dataset.columns)),dataset.columns,rotation = 90)
                plt.yticks(range(len(dataset.columns)),dataset.columns)
                plt.title('Matriz de correlações')
                plt.colorbar()
                st.pyplot()
            if analise == "modelo de Machine Learning":
                st.subheader('EM BREVE! :)')
                
        if file is None:
            st.markdown('Aguardando arquivo...')