#!/usr/bin/env python
# coding: utf-8

# ## Relatório de Análise V

# #### Importando Bibliotecas

# In[1]:


import pandas as pd


# ####  Tratamento de dados faltantes

# In[10]:


dados = pd.read_csv('dados/aluguel_residencial.csv', sep  = ';')  #carregamento dos dados
dados


# #### Vou fazer o tratamento dos dados de forma individual nas series (valor, condominio, IPTU)

# In[26]:


dados[dados['Valor'].isnull()]          #detectando os dados nulos NA dos valores


# #### Caso o imóvel seja um apartamento, os dados nulos serão excluídos.

# In[15]:


dados[dados['Condominio'].isnull()].shape[0]  #visualizando quantos valores de condominios tenho nulos


# In[17]:


selecao = (dados['Tipo'] == 'Apartamento') & (dados['Condominio'].isnull()) #aqui eu aplico a logica do condominio nulo
selecao


# In[18]:


A = dados.shape[0]                                              #excluo 745 de apartamentos que tem condominios nulos
dados = dados[~selecao]
B = dados.shape[0]
A - B


# In[21]:


dados[dados['Condominio'].isnull()].shape[0]               #os dados de condominios nulos e IPVA eu vou mandar no banco mas como zero


# In[25]:


dados.to_csv('dados/aluguel_residencial.csv', sep = ';', index = False)  #salvar esse arquivo modificado


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




