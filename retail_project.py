import pandas as pd
import streamlit as st
import psycopg2

conn = psycopg2.connect(
            host="harishrds.chiyki4sw370.ap-south-1.rds.amazonaws.com",
            user="postgres",
            password="harish123",
            port=5432,
            dbname="postgres")



ANALYSIS_question=[
"21 Top-Selling Products: Identify the products that generate the highest revenue based on sale prices.",
"22 Monthly Sales Analysis: Compare year-over-year sales to identify growth or decline in certain months.",
"23 Product Performance: Use functions like GROUP BY, HAVING, ROW_NUMBER(), and CASE WHEN to categorize and rank products by their revenue, profit margin, etc.",
"24 Regional Sales Analysis: Query sales data by region to identify which areas are performing best.",
"25 Discount Analysis: Identify products with discounts greater than 20% and calculate the impact of discounts on sales."]
GUVI_questions=[
"1 Find top 10 highest revenue generating products.",
"2 Find the top 5 cities with the highest profit margins.",
"3 Calculate the total discount given for each category.",
"4 Find the average sale price per product category.",
"5 Find the region with the highest average sale price.",
"6 Find the total profit per category.",
"7 Identify the top 3 segments with the highest quantity of orders.",
"8 Determine the average discount percentage given per region.",
"9 Find the product category with the highest total profit.",
"10 Calculate the total revenue generated per year."]
OWN_questions=[
"11 List all orders that resulted in a loss (negative profit).",
"12.What is the total revenue (sale_price) by state?",
"13 Find the product with the highest sale price.",
"14 Which postal code had the most orders?",
"15 What is the average profit per order for each ship mode?",
"16 How many unique product IDs are there in the 'Office Supplies' category?",
"17 Which region has the highest total revenue?",
"18 Find the total discount amount provided for orders in the 'South' region.",
"19 List all orders shipped to California.",
"20 What is the average list price for products in each sub-category?"]

queries_guvi=[#1 Find top 10 highest revenue generating products
"select product_id , sub_category,category, sum(sale_price) as cumulative_sales_each_product from sales_table group by product_id,sub_category,category order by  cumulative_sales_each_product desc limit 10",
#2 Find the top 5 cities with the highest profit margins
"select a.city,a.postal_code,a.state,sum(s.profit) profit_each_city from address_table as a join sales_table as s on s.postal_code = a.postal_code group by a.city,a.postal_code,a.state order by profit_each_city desc limit 5",
#3 Calculate the total discount given for each category
"select sub_category ,category, sum(discount) from sales_table group by sub_category , category order by sub_category asc",
#4 Find the average sale price per product category
"select category ,avg(sale_price) from sales_table group by category",
#5 Find the region with the highest average sale price
"select region,avg_per_region from(select a.region,avg(s.sale_price) avg_per_region from sales_table as s join address_table as a on s.postal_code=a.postal_code group by region order by avg_per_region desc limit 1)",
#6 Find the total profit per category
"select category,sum(profit) from sales_table group by category order by category asc",
#7 Identify the top 3 segments with the highest quantity of orders
"select segment,sum(quantity) from sales_table group by segment order by sum(quantity) desc",
#8 Determine the average discount percentage given per region
"select a.region,avg(s.discount_percent) avg_disc_each_reg from sales_table as s join address_table as a on s.postal_code = a.postal_code group by a.region",
#9 Find the product category with the highest total profit
"select category,sum(profit) total_profit from sales_table group by category order by total_profit desc limit 1",
#10 Calculate the total revenue generated per year
"select extract(year from order_date)as order_year,sum(sale_price) from sales_table group by order_year order by order_year asc"]
queries_mine=[
#11 List all orders that resulted in a loss (negative profit).
"select order_id, sub_category , category,profit from sales_table where sign(profit)=-1",
#12.What is the total revenue (sale_price) by state?
"select a.state, sum(s.sale_price) from address_table as a join sales_table as s on a.postal_code = s.postal_code group by a.state order by a.state asc",
#13 Find the product with the highest sale price.
"select product_id,sub_category,category,sum(sale_price/quantity) sale_price_each_product from sales_table group by product_id,sub_category,category order by sale_price_each_product desc limit 1",
#14 Which postal code had the most orders?
"select postal_code,count(order_id) from sales_table group by postal_code order by count(order_id) desc limit 1",
#15 What is the average profit per order for each ship mode?
"select ship_mode,avg(profit),count(ship_mode) from sales_table group by ship_mode order by avg(profit) desc",
#16 How many unique product IDs are there in the 'Office Supplies' category?
"select count(distinct product_id) as unique_product_count from sales_table where category = 'Office Supplies';",
#17 Which region has the highest total revenue?
"select a.region,sum(s.sale_price) from sales_table as s join address_table as a on s.postal_code = a.postal_code group by a.region order by sum(s.sale_price) desc limit 1",
#18 Find the total discount amount provided for orders in the "South" region.
"select a.region,sum(s.discount) from address_table as a join sales_table as s on s.postal_code = a.postal_code where a.region = 'South' group by a.region",
#19 List all orders shipped to California.
"select s.order_id, s.order_date,s.ship_mode, s.segment, s.product_id, s.category, s.sub_category,s.cost_price, s.list_price, s.quantity, a.country, a.city, a.state, a.region from sales_table as s join address_table as a on s.postal_code=a.postal_code where state = 'California'",
#20.What is the average list price for products in each sub-category?
"select avg(list_price),count(list_price),product_id,sub_category from sales_table group by product_id,sub_category order by sub_category asc"]

queries_analysis=["select product_id,sub_category,category,sum(sale_price) from sales_table group by product_id,sub_category,category order by sum(sale_price) desc limit 1 ",
"select extract(year from order_date) as order_year,extract(month from order_date) as order_month, sum(profit) as profit_each_month from sales_table group by order_year, order_month order by order_year, order_month",
"select product_id,sum(profit) profit_each_product,sum(sale_price) revenue_from_each_product,category,row_number()over(partition by category order by sum(profit) desc), case when (sign(sum(profit))=1) then 'profit' else 'loss' end as profit_or_loss from sales_table group by product_id,category having sum(profit)!=0",
"select sum(s.profit),a.region from sales_table as s join address_table as a on s.postal_code=a.postal_code group by a.region order by sum(s.profit) desc limit 1",
"select product_id,sub_category, category from sales_table where discount_percent > 20"]

st.set_page_config(layout="wide")

page_bg_img = '''
<style>
.stApp {
    background-image: url("https://as1.ftcdn.net/v2/jpg/06/27/85/70/1000_F_627857071_bREuJgK1MTU5YcTPTfgJPOYZ86F1l421.jpg");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}

.css-1d391kg {
    background-image: url("https://as1.ftcdn.net/v2/jpg/06/27/85/70/1000_F_627857071_bREuJgK1MTU5YcTPTfgJPOYZ86F1l421.jpg");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("Retail Order Data Analysis")
st.sidebar.title("CATEGORY")
option=st.sidebar.radio("(choose question category)",("GUVI","OWN","ANALYSIS"))
if option=="GUVI":
    query = st.selectbox("Choose The Query",GUVI_questions)
    query_index = GUVI_questions.index(query)
    if query:
        df=pd.read_sql(queries_guvi[query_index],conn)
        if df is not None and not df.empty:
            st.dataframe(df)
            st.write("No.of Records: ",len(df))
            st.success("Generated query:")
        else:
            st.error("NO RECORD FOUND")
        st.write(queries_guvi[query_index])
elif option=="OWN":
    query = st.selectbox("Choose The Query",OWN_questions)
    query_index = OWN_questions.index(query)
    if query:
        df=pd.read_sql(queries_mine[query_index],conn)
        if df is not None and not df.empty:
            st.dataframe(df)
            st.write("No.of Records: ",len(df))
            st.success("Generated query:")
        else:
            st.error("NO RECORD FOUND")
        st.write(queries_guvi[query_index])
elif option=="ANALYSIS":
    query = st.selectbox("Choose The Query",ANALYSIS_question)
    query_index = ANALYSIS_question.index(query)
    if query:
        df=pd.read_sql(queries_analysis[query_index],conn)
        if df is not None and not df.empty:
            st.dataframe(df)
            st.write("No.of Records: ",len(df))
            st.success("Generated query:")
        else:
            st.error("NO RECORD FOUND")
        st.write(queries_guvi[query_index])
