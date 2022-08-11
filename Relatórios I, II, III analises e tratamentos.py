#!/usr/bin/env python
# coding: utf-8

# ## Importando Bibliotecas Python

# In[44]:


import pandas as pd


# In[ ]:





# ## Relatório de Análise I
# ----

# In[45]:


dados_aluguel = pd.read_csv('dados/aluguel.csv', sep = ';')  #Leio meu dataSet
dados_aluguel 


# In[46]:


dados_aluguel.dtypes                                     #Identifico quais dados eu tenho dentro esse dataset


# In[47]:


dados_aluguel.Valor


# In[48]:


tipos_dados = pd.DataFrame(dados_aluguel.dtypes, columns= ['Tipos_dados']) #Renomei as colunas e inclui dentro de um dataframe
tipos_dados.columns.name='Variaveis'

tipos_dados


# ## Relatório de Análise II
# ----

# ##### Tipos de Imovéis identificar todos os tipos de imovéis do meu dataframe

# In[49]:


dados_aluguel['Tipo']                            #selecionei apenas a coluna que eu quero trabalhar


# In[50]:


tipos_dados = pd.DataFrame(dados_aluguel['Tipo']) #Inclui no dataframe
tipos_dados 


# In[51]:


tipos_dados.drop_duplicates()                  #peguei os registro únicos dentro da minha variavel 


# In[52]:


tipos_dados.drop_duplicates(keep='first', inplace=True) #Uso a função Keep Fist para exlcuir esse dados duplicados dentro da variavel


# In[53]:


tipos_dados.columns.name = 'id'     #Renomei o index
tipos_dados


# ## Relatório de Análise III
# ----

# #####  Selecionar Imoveis Residencias para analíse

# In[54]:


list(dados_aluguel['Tipo'].drop_duplicates())  #selecionei os elementos únicos e inclui em uma lista


# In[55]:


residencial = ['Quitinete',          #selecionei apena o que é residencial
'Casa',
'Apartamento',
'Casa de Condomínio',
'Casa de Vila']


# In[56]:


residencial


# In[57]:


selecao =dados_aluguel['Tipo'].isin(residencial)   
selecao                                            #uso o metodo isin para trazer uma lista de true ou false da minha selecao


# In[58]:


dados_residencial= dados_aluguel[selecao]       #incluo em um dataframe essa selecao trazendo apenas os dados de residencial
dados_residencial


# In[59]:


list(dados_residencial['Tipo'].drop_duplicates()) 


# In[60]:


dados_residencial.shape[0]           #nesse novo dataframe eu tenho os seguintes dados


# In[61]:


dados_residencial.index=range(dados_residencial.shape[0] ) #reconstruo o dataframe


# In[62]:


dados_residencial


# ### Exportar a base  de dados_residencial

# In[66]:


dados_residencial.to_csv('dados/aluguel_residencial.csv', sep = ';', index= False) #Exportei esse arquivo para futuramente usar em outros projetos


# In[68]:


dados_residencial_2 = pd.read_csv('dados/aluguel_residencial.csv', sep =';')  #Exportação feita
dados_residencial_2 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




