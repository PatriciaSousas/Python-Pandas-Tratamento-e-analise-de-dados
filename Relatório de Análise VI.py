#!/usr/bin/env python
# coding: utf-8

# ### Importando Bibliotecas

# In[1]:


import pandas as pd


# #### - Novas Variáveis

# In[4]:


dados = pd.read_csv('dados/aluguel_residencial.csv', sep = ';')
dados


# In[7]:


dados['Valor Bruto']= dados['Valor'] + dados['Condominio'] + dados['IPTU'] #somando e incluir o valor bruto no meu dataframe


# In[6]:


dados.head(10)


# In[10]:


dados['Valor m2'] = dados['Valor']/dados['Area']                    #valor do metro quadrado 
dados['Valor m2'] = dados['Valor m2'].round(2)


# In[9]:


dados.head(10)


# In[11]:


dados['Valor Bruto m2'] = (dados['Valor Bruto']/dados['Area']).round(2)  #valor por metro quadrado bruto


# In[12]:


dados.head(10)


# In[16]:


casa = ['Casa', 'Casa do Condominio', 'Case de Vila']                #categorizar o que é casa e apartamento
dados['Tipo Agregado'] = dados['Tipo'].apply(lambda x: 'Casa' if x in casa else 'Apartamento')


# In[17]:


dados.head(15)


# ### Excluindo variaveis 

# In[19]:


dados_aux = pd.DataFrame(dados[['Tipo Agregado', 'Valor m2', 'Valor Bruto', 'Valor Bruto m2']])
dados_aux 


# In[20]:


del dados_aux['Tipo Agregado']


# In[21]:


dados_aux 


# In[22]:


dados.drop(['Valor Bruto', 'Valor Bruto m2'], axis = 1, inplace = True) #enxlui as variaveis dentro do meu dataframe


# In[24]:


dados.to_csv('dados/aluguel_residencial.csv', sep = ';', index = False) #salvei essa versão no dataframe


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




