
# coding: utf-8

# In[7]:


import json
from pprint import pprint


# In[24]:


with open('mySecurityTweets.json') as f:
    data = json.load(f)


# In[31]:


d=data[0]['url']


# In[32]:


pprint(d)


# In[33]:


d="www.twitter.com"+d


# In[34]:


pprint(d)

