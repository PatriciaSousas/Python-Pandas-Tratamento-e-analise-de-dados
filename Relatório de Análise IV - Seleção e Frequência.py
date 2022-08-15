#!/usr/bin/env python
# coding: utf-8

# ## Relatório de Análise IV
# ----

# ### Seleções e Frequencias dos seguintes dados
# 
# - Selecione somente os imóveis classificados com tipo 'Apartamento'.
# 
# - Selecione os imóveis classificados com tipos 'Casa', 'Casa de Condomínio' e 'Casa de Vila'.
# 
# - Selecione os imóveis com área entre 60 e 100 metros quadrados, incluindo os limites.
# 
# - Selecione os imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00.

# ## Importando Bibliotecas

# In[1]:


import pandas as pd


# In[ ]:





# ### Análise de dados
# ----

# In[2]:


dados_aluguel = pd.read_csv('dados/aluguel_residencial.csv', sep =';')
dados_aluguel


# - Selecione somente os imóveis classificados com tipo 'Apartamento'

# In[3]:


selecao = dados_aluguel['Tipo'] == 'Apartamento' #seleciono apenas os dados apartamentos da variavel e chamo shape para saber a quantidade

n1= dados_aluguel[selecao].shape[0]
n1


# - Selecione os imóveis classificados com tipos 'Casa', 'Casa de Condomínio' e 'Casa de Vila'.

# In[6]:


selecao = (dados_aluguel['Tipo'] == 'Casa') | (dados_aluguel['Tipo'] == 'Casa de Condomínio') | (dados_aluguel['Tipo'] == 'Casa de Vila')

n2= dados_aluguel[selecao].shape[0]
n2


# - Selecione os imóveis com área entre 60 e 100 metros quadrados, incluindo os limites.

# In[8]:


selecao = (dados_aluguel['Area'] >= 60) & (dados_aluguel['Area'] <= 100)
n3 = dados_aluguel[selecao].shape[0]
n3


# - Selecione os imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00

# In[9]:


selecao = (dados_aluguel['Quartos'] >= 4) & (dados_aluguel['Valor'] < 2000)
n4 = dados_aluguel[selecao].shape[0]
n4


# ### Conclusão

# In[10]:


print("Nº de imóveis classificados com tipo 'Apartamento' -> {}".format(n1))
print("Nº de imóveis classificados com tipos 'Casa', 'Casa de Condomínio' e 'Casa de Vila'-> {}".format(n2))
print("Nº de imóveis com área entre 60 e 100 metros quadrados, incluindo os limites -> {}".format(n3))
print("Nº de imóveis que tenham pelo menos 4 quartos e aluguel menor que R$ 2.000,00 -> {}".format(n4))


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




