#!/usr/bin/env python
# coding: utf-8

# ## Importando Bibliotecas Python

# In[100]:


import pandas as pd


# ### Analíse de relatório I
# ----

# ### Lendo diferentes tipos de dados

# In[101]:


dados_json = pd.read_json('dados/aluguel.json')  #Inclui os dados dentro de uma variavel
dados_json                      


# In[102]:


dados_txt = pd.read_table('dados/aluguel.txt')  #Leio meu dataframe txt
dados_txt                   


# In[103]:


dados_xlsx = pd.read_excel('dados/aluguel.xlsx')  #Leio meu dataframe txt
dados_xlsx


# In[104]:


dados_html = pd.read_html('dados/dados_html_1.html')  #Leio meu dataframe HTML
dados_html


# ### Criando Series e Dataframes

# In[105]:


data= [1,2,3]


# In[106]:


s= pd.Series(data)


# In[107]:


s


# In[108]:


data = [[1, 2, 3], 
        [4, 5, 6], 
        [7, 8, 9]]


# In[109]:


df1 = pd.DataFrame(data = data)


# In[110]:


index = ['Linha' + str(i) for i in range(3)]


# In[111]:


df1 = pd.DataFrame(data = data, index = index)
df1


# ### Organizando DataFrames

# In[112]:


data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# In[113]:


list('321')


# In[114]:


list('321')


# In[115]:


df = pd.DataFrame(data, list('321'), list('ZYX'))


# In[116]:


df.sort_index(inplace = True)


# 

# ### Formação de Seleção

# In[117]:


data = [(1, 2, 3, 4),
        (5, 6, 7, 8),
        (8, 10, 11, 12),
        (13, 14, 15, 16)]
df = pd.DataFrame(data, 'l1 l2 l3 l4'.split(), 'c1 c2 c3 c4'.split())
df


# In[118]:


df['c1']


# In[119]:


df[:]


# In[120]:


df[1:3]


# In[121]:


df.iloc[[2,0],[3,0]]


# ### Metodos de Interpolarização

# In[122]:


data = [0.5, None, None, 0.52, 0.54, None, None, 0.59, 0.6, None, 0.7]
s = pd.Series(data)


# In[123]:


s.fillna(0)


# In[124]:


s.fillna(method = 'ffill')


# In[125]:


s.fillna(method = 'bfill')


# In[126]:


s.fillna(s.mean())


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




