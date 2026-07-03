#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

data = pd.read_csv("products_clean.csv")
data.head()


# ## 1. Catalogue & discount overview

# In[2]:


#catalogue and discount overview
total_products = len(data)
print("Total products:", total_products)

#count of full price product
fullprice=data[data["Sale Price"] == data["MRP / Original Price"]]
print("Count of full price products:",len(fullprice))

#count of discount products
discount=data[data["Sale Price"] < data["MRP / Original Price"]]
print("Count of discount price products:",len(discount))

#share of the catelogue in on sale
share_on_sale=(len(discount)/total_products)*100
print(f"share of the catelogue in on sale:{share_on_sale:.2f}%")


# In[3]:


#distribution of discounts
discount = data[data["discount_pct"]>0]
len(discount)

#is it smooth or cluster
print(discount["discount_pct"].value_counts()) #it is clustered rather than continuous. 


# In[4]:


#- Summary statistics for MRP, sale price, and discount
data[['MRP / Original Price', "Sale Price", "discount_pct"]].describe()


# ## 2. Which sub-brands discount hardest?

# In[5]:


#Group products by sub-brands
#no. of products in each groups
product_count = data.groupby('Brand / Sub-brand')['Product URL'].count()
print('Total product count for each Brand / Sub-brand')
print('-'*50)
print(product_count)


# In[8]:


#share of discounts
#group by discount
discount_product = data[data["Sale Price"] < data['MRP / Original Price']]
discount_product

discount_count = discount_product.groupby('Brand / Sub-brand')['Product URL'].count()
#print(discount_count)

print("Share of each Brand / Sub-brand on discount")
print('-'*40)
discount_percentage = (discount_count/product_count)*100
print(discount_percentage.round(2))


# In[9]:


#median discount for each brand

median_discount = data.groupby('Brand / Sub-brand')['discount_pct'].median()
print('Median discount of each Brand / Sub-brand')
print('-'*50)
print(median_discount)


# In[10]:


print(median_discount.sort_values(ascending = False))


# In[11]:


#most and least discounted Brand / Sub-brand
#most discounted brand - Men Performance, Men Sportswear, Men TERREX
#least discounted brand - TERREX


# ## 3. Is there a relationship between price tier and discount depth?

# In[12]:


#seperate price into different quartiles
data['price_category'] = pd.qcut(data['MRP / Original Price'],q=3,labels=['Budget','Mid-range','Premium'])	


# In[13]:


data.head()


# In[15]:


#find discount for different price range
data.groupby('price_category')['discount_pct'].median()


# In[17]:


#find correlation between MRP / Original Price and discount_pct

correlation = data['MRP / Original Price'].corr(data['discount_pct'])
print(correlation)


# In[18]:


#its a weak neagtive correlation. which means when price increases, discount decreases. here premium has the least discount


# ## 4. Flag pricing outliers

# In[23]:


#find outliers

q1 = data['discount_pct'].quantile(0.25)
q3 = data['discount_pct'].quantile(0.75)

IQR = q3 - q1

lower_limit = q1 - 1.5 * IQR
upper_limit = q3 + 1.5 * IQR

print(lower_limit)
print(upper_limit)
outliers = data[(data['discount_pct'] < lower_limit) | (data['discount_pct'] > upper_limit)]
outliers


# In[24]:


outlier_products = outliers[["Product Name","Brand / Sub-brand","MRP / Original Price", "Sale Price", "discount_pct"]]
outlier_products


# In[26]:


outlier_products.to_csv("pricing_outliers.csv",index=False)


# ## 5. Visualization

# In[28]:


import matplotlib.pyplot as plt


# In[40]:


#discount-percentage distribution
#Histogram

plt.figure(figsize=(6,4))
plt.hist(data['discount_pct'], bins=5,edgecolor="black")
plt.title("Discount - Percentage Distribution")
plt.xlabel("Percentage")
plt.ylabel("Number of Products")
plt.savefig("discount-percentage distribution.png")
plt.show()


# In[52]:


#discount-by-sub-brand comparison
#Bar chart
plt.figure(figsize=(15,6))
plt.bar(data['Brand / Sub-brand'],data['discount_pct'])
plt.title("Discount-by-sub-brand comparison")
plt.xlabel("Brand / Sub-brand")
plt.ylabel("Discount Percentage")
plt.savefig("discount-by-sub-brand comparison.png")
plt.show()


# In[56]:


#MRP-vs-discount scatter
#Scatter plot
plt.figure(figsize=(8,6))
plt.scatter(data["MRP / Original Price"],data['discount_pct'])
plt.title("MRP-vs-discount scatter")
plt.xlabel("MRP / Original Price")
plt.ylabel("discount_percentage")
plt.savefig("MRP-vs-discount scatter.png")
plt.show()


# In[ ]:




