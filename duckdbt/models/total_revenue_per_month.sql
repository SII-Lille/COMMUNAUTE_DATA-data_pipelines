{{ config(materialized='table') }}

with sales_sum as (

    SELECT EXTRACT(YEAR FROM date) as year,EXTRACT(MONTH FROM date) as month, SUM(revenue) as total_revenue FROM "Sales" GROUP BY 1, 2

)

select *
from sales_sum