#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[68]:


data = pd.read_csv("products_raw.csv")
data


# In[69]:


data.head()


# In[70]:


data.info()


# In[71]:


print(data.shape)


# In[72]:


print(data.size)


# In[73]:


# checking for duplicate products

print(data["Product URL"].duplicated().sum()) #no duplicates


# In[74]:


# normalize price into numeric columns

data.dtypes


# In[75]:


# create new colum discount_amount

data["discount_amount"] = data["MRP / Original Price"] - data["Sale Price"]


# In[76]:


# create column discount_percentage

data["discount_pct"] = (data["discount_amount"] / data["MRP / Original Price"])*100


# In[77]:


data.head()


# In[80]:


data["discount_pct"] = data["discount_pct"].round(2)


# In[81]:


data.head()


# In[82]:


data.tail()


# In[84]:


data.dtypes


# In[62]:


# validate data
#finding there is any col with missing values
data.isnull().sum()


# In[63]:


#checking for valid sales price and mrp
invalid_count = data[data["Sale Price"] > data["MRP / Original Price"]]
print(len(invalid_count))


# In[64]:


#count of onsale products

onsale=data[data["Sale Price"] < data["MRP / Original Price"]]
print("On sale products count :" ,len(onsale))


# In[65]:


fullprice=data[data["Sale Price"] == data["MRP / Original Price"]]
print("Full price products count :" ,len(fullprice))


# In[66]:


print("Report")
print("-"*40)
print("Number of missing values in columns:\n",data.isnull().sum())
print('-'*40)
invalid_count = data[data["Sale Price"] > data["MRP / Original Price"]]
print("Count of invalid sales price and mrp:",len(invalid_count))
print('-'*40)
onsale=data[data["Sale Price"] < data["MRP / Original Price"]]
print("On sale products count :" ,len(onsale))
print('-'*40)
fullprice=data[data["Sale Price"] == data["MRP / Original Price"]]
print("Full price products count :" ,len(fullprice))


# In[67]:


data.to_csv("products_clean.csv", index=False)

