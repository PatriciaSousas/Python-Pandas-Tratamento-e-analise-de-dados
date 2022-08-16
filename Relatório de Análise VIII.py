#!/usr/bin/env python
# coding: utf-8

# ## Identificando e Removendo Outliers

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd
import matplotlib.pyplot as plt
plt.rc('figure', figsize = (14,6))


# In[3]:


dados = pd.read_csv('dados/aluguel_residencial.csv', sep = ';')
dados 


# In[4]:


Q1 = valor.quantile(.25)    #quebrando por qurtis os valores
Q3 = valor.quantile(.75)
IIQ = Q3 - Q1
limite_inferior = Q1 - 1.5 * IIQ
limite_superior = Q3 + 1.5 * IIQ


# In[6]:


dados.hist(['Valor'])      #Plotando esses valores
dados_new.hist(['Valor'])


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




