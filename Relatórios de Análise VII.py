#!/usr/bin/env python
# coding: utf-8

# ### Importando Bibliotecas

# In[17]:


import pandas as pd
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt


# #### Criando agrupamentos

# In[5]:


dados = pd.read_csv('dados/aluguel_residencial.csv', sep = ';')
dados


# In[6]:


dados['Valor'].mean()


# In[7]:


bairros = ['Barra da Tijuca', 'Copacabana', 'Ipanema', 'Leblon', 'Botafogo', 'Flamengo', 'Tijuca'] #abri um dataframe para fazer a media de acordo com os bairros
selecao = dados['Bairro'].isin(bairros)
dados = dados[selecao]


# In[9]:


dados['Bairro'].drop_duplicates()   #ok todos os bairros unidos


# In[11]:


grupo_bairro = dados.groupby('Bairro')
grupo_bairro


# In[14]:


grupo_bairro[['Valor', 'Condominio']].mean().round(2) #media dos bairros, condominios e valores


# ### Estatísticas descritivas

# In[16]:


grupo_bairro['Valor'].describe().round(2)  #algumas metricas interessantes 


# In[19]:


plt.rc('figure', figsize = (20,10))
fig = grupo_bairro['Valor'].std().plot.bar(color = 'blue')


# In[20]:


fig = grupo_bairro['Valor'].mean().plot.bar(color = 'blue')
fig.set_ylabel('Valor do Aluguel')
fig.set_title('Valor Médio do Aluguel por Bairro', {'fontsize': 22})


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




