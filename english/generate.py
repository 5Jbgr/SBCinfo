#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import json

table=pd.read_csv(r"english_info.csv",encoding="gbk")
table


# In[2]:


c_dict={"id":1,"name":"character","list":[]}
head=table.head()
for i in table.values:
    f=[j["name"]==i[0] for j in c_dict["list"]]
    if any(f):
        o=c_dict["list"][f.index(True)]
    else:
        o={"name": i[0],"id": len(c_dict["list"])+1,"category":[]}
        c_dict["list"].append(o)
    skin=[]
    for j in pd.DataFrame(i).dropna()[0][3:]:
            skin.append({"name":j,"id":len(skin)+1})
    o["category"].append({"name":i[1],"id":len(o["category"])+1,"star":str(i[2]),"skin":skin})
c_dict


# In[3]:


o_dict={"id":2,"name":"other","list":[]}
o_dict["list"]=[{"name":"enemy","id":1},{"name":"npc","id":2},{"name":"other","id":3},{"name":"weapon","id":4}]
m_dict={"id":3,"name":"Music/Sound Effects","list":[]}
m_dict["list"]=[{"name":"Music/Sound Effects","id":1}]
u_dict={"id":99,"name":"unknown","list":[]}
u_dict["list"]=[{"name":"unknown","id":1}]
all_in_one=[c_dict,o_dict,m_dict,u_dict]
all_in_one


# In[4]:


with open(r"category.json","w",encoding="utf-8") as f:
    json.dump(all_in_one,f)


# In[ ]:

