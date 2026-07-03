# Datahut-Science-Assignment
1.	Overall approaches to 3 Problems:

PROBLEM 1 : The objective was to scrape product data from the Adidas Men's Footwear website. Initially, I attempted to use BeautifulSoup with direct HTTP requests, but I got HTTP 403 (Forbidden) due to the website's anti-bot protection. I then used Selenium to load the webpage and BeautifulSoup to parse the HTML. The product information was extracted from the embedded __NEXT_DATA__ JSON object. Pagination was implemented to scrape all products across multiple pages, and a 2-second delay was added between requests for responsible scraping. The collected data was saved as ‘products_raw.csv’.

PROBLEM 2 : The raw data was loaded into Pandas for cleaning and validation. An initial EDA was performed to check for missing values, duplicate records, and data types. Since the price values were extracted from the embedded JSON, they were already in numeric format and required no additional cleaning. New columns : discount_amount and discount_pct, were created, followed by data validation checks such as identifying missing values, verifying that the sale price was not greater than the MRP, and counting full-price and discounted products. Finally, the cleaned dataset was saved as ‘products_clean.csv’.

PROBLEM 3 : 3 is to analyse the cleaned data. For that first I load the the cleaned data file using pandas. 
1. Analysed the catalogue by calculating: 
•	Total number of products 
•	Full-price and discounted products 
•	Share of products on sale 
•	Summary statistics (Mean, Median, Standard Deviation) for MRP, Sale Price, and Discount Percentage. 
•	Examined the discount distribution and found that discounts were clustered around common values (30%, 40%, and 50%) rather than being evenly distributed.

2. Grouped products by Brand / Sub-brand to compare: 
•	Number of products 
•	Percentage of discounted products 
•	Median discount percentage 
•	Identified Men Performance, Men Sportswear, and Men TERREX as the most discounted sub-brands and TERREX was the least discounted.

3. Divided products into Budget, Mid-range, and Premium price tiers using pd.qcut(). 
•	Calculated the correlation between MRP and Discount Percentage, which showed a weak negative relationship, indicating that higher-priced products have the smaller discounts.

4. Applied the IQR method to detect pricing outliers. No statistical outliers were found. 
5. Created the following visualizations to support the analysis: 
•	Histogram of Discount Percentage Distribution 
•	Bar Chart of Discount by Sub-brand 
•	Scatter Plot of MRP vs. Discount Percentage

2. How you determined whether the site was static or dynamic?
I determined that the website was dynamic because the product details were not available as normal HTML elements. Instead, they were stored in the embedded __NEXT_DATA__ JSON object after the page was rendered. Additionally, direct HTTP requests returned HTTP 403, so I used Selenium to render the page before scraping.

3. Challenges faced (pagination, price parsing, CAPTCHAs, dynamic content) and how you handled them.
•	Pagination: The catalogue spanned multiple pages. I automated pagination by increasing the start parameter by 48 until no more products were returned. 
•	Price Parsing: Products had either both Sale Price and MRP or only a single price. If no sale price was available, I treated the MRP as the sale price. 
•	Dynamic Content: Product data was stored in the embedded __NEXT_DATA__ JSON object, and direct HTTP requests returned HTTP 403 (Forbidden). I used Selenium to render the page and BeautifulSoup to extract the data.

4. For Problem 3: your analysis write-up — the most interesting pricing/discount findings, your
outlier method and why you chose it, and the statistical choices you made.

Key Findings :
•	Discounts mainly clustered at 30%, 40%, and 50%. 
•	Men Performance, Men Sportswear and Men TERREX had the highest median discounts. 
•	MRP and discount percentage showed a weak negative correlation (-0.264). 
Outlier Method :
•	Used the IQR method because it is robust to extreme values and does not assume normality. 
•	No pricing outliers were found. 
Statistical Methods :
•	Descriptive statistics – To summarized the dataset. 
•	Group-by analysis – compared sub-brands. 
•	pd.qcut() – created balanced price tiers. 
•	correlation – measured the relationship between price and discount. 
•	IQR – detected pricing outliers. 

5. Any limitations or assumptions in your solution.
Assumptions : The scraped product and price data were accurate at the time of scraping. The analysis is based only on the Men's Footwear category and does not represent other Adidas categories.
 
Limitations : The results are based on the current product catalogue and may vary as Adidas updates its pricing and discount strategies. The scraper does not include retry or recovery mechanisms, so it may stop if an unexpected error occurs during scraping.

