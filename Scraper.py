#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install selenium


# In[ ]:


pip install webdriver-manager


# In[1]:


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import json
import time
import pandas as pd


# In[8]:


driv = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# In[9]:


products_clean = []


# In[ ]:


start=0
while True:
    try:
        url = f"https://www.adidas.co.in/men-shoes?start={start}"
        driv.get(url)
        time.sleep(2)
        htmls = driv.page_source

        soup = BeautifulSoup(htmls, "html.parser")   
        script = soup.find("script", id="__NEXT_DATA__")
        texts = script.text

        datas = json.loads(texts)
        products = datas["props"]["pageProps"]["products"]
        if len(products)==0:
            break

        for item in products:
            saleprice = None
            mrp=None
            priceinfo = item.get("priceData", {}).get("prices", [])

            for p in priceinfo:
                if p.get("type")=="sale":
                    saleprice=p.get("value")
                elif p.get("type")=="original":
                    mrp=p.get("value")
            if saleprice is None:
                saleprice=mrp

            product = {
                "Product URL": item.get("url"),
                "Product Name": item.get("title"),
                "Brand / Sub-brand": item.get("subTitle"),
                "Sale Price": saleprice,
                "MRP / Original Price": mrp
            }

            products_clean.append(product)
        start += 48
    except Exception as e:
        print(e)
        break


# In[ ]:


print(script)


# In[ ]:


df = pd.DataFrame(products_clean)
print(df.shape)


# In[38]:


df.to_csv("products_raw.csv", index=False)


# In[40]:


print(df)


# In[ ]:




