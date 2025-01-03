This repository provides two key datasets:
1. The sales table with details about customer orders, products, pricing, and profitability.
2. An address table that maps postal codes to geographical locations.

These datasets can be used to explore sales performance, regional trends, and customer behavior.

This project consist of both python programming for cleaning the table, and creating data set with meaningful format and sql queries.

SQL QUERIES:
Top-Selling Products: Identify the products that generate the highest revenue based on sale prices.
Monthly Sales Analysis: Compare year-over-year sales to identify growth or decline in certain months.
Product Performance: Use functions like GROUP BY, HAVING, ROW_NUMBER(), and CASE WHEN to categorize and rank products by their revenue, profit margin, etc.
Regional Sales Analysis: Query sales data by region to identify which areas are performing best.
Discount Analysis: Identify products with discounts greater than 20% and calculate the impact of discounts on sales.

1.# Find top 10 highest revenue generating products
2.# Find the top 5 cities with the highest profit margins
3.# Calculate the total discount given for each category
4.# Find the average sale price per product category
5.# Find the region with the highest average sale price
6.# Find the total profit per category
7.# Identify the top 3 segments with the highest quantity of orders
8.# Determine the average discount percentage given per region
9.# Find the product category with the highest total profit
10.# Calculate the total revenue generated per year
--11.#List all orders that resulted in a loss (negative profit).
--12.What is the total revenue (sale_price) by state?
--13.Find the product with the highest sale price.
--14.Which postal code had the most orders?
--15What is the average profit per order for each ship mode?
--16How many unique product IDs are there in the 'Office Supplies' category?
--17.Which region has the highest total revenue?
--18.Find the total discount amount provided for orders in the "South" region.
--19.List all orders shipped to California.
--20.What is the average list price for products in each sub-category?

Then created Streamlit application using vscode to create a url to get table consist of data from its query listed in the option.
