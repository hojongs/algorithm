-- 183. Customers Who Never Order
# Write your MySQL query statement below
select c.name as Customers
from Customers c
left outer join Orders o on c.id = o.customerId
where o.customerId is null
