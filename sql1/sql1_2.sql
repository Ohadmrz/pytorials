--With GROUP BY:
--Get total amount of customers for each marital status
select
	count(*),
	marital_status
from
	superstore_data
group by
	marital_status
order by
	count;
--Get total purchases of sweets and wine per each education status
select
	sum(mntsweetproducts) as total_sweets,
	sum(mntwines) as total_wine,
	education
from
	superstore_data
group by
	education;
--Get the maximum and the minimum age of customers with the same marital status and education ordered by education, and then minimum age
select
	education,
	marital_status,
	min(date_part('year', now()) - year_birth) as min_age,
	max((date_part('year', now()) - year_birth)) as max_age
from
	superstore_data
group by
	education,
	marital_status
order by
	education,
	min(date_part('year', now()) - year_birth);
--Get amount of customers of each age that have accepted the offer and have not complained in the past 2 years
select
	count(*),
	date_part('year', now()) - year_birth as _age
from
	superstore_data
group by
	distinct(date_part('year', now()) - year_birth),
	response = 1,
	complain = 0
order by
	date_part('year', now()) - year_birth;
--Get the youngest customer for each education level (id,  education, age)
select
	distinct on
	(education)
	education,
	id,
	min(date_part('year', now()) - year_birth) as min_age
from
	superstore_data
group by
	education,
	id
order by
	education,
	min_age;
--Get average amount of purchases for each product type (fish, meat, sweets, wine, gold) for groups of customers with the same amounts of children at home (kids and teens)
select
	teenhome + kidhome as total_children,
	avg(mntwines) as avg_wines,
	avg(mntsweetproducts) as avg_sweets,
	avg(mntmeatproducts) as avg_meat,
	avg(mntfishproducts) as avg_fish
from superstore_data
group by
	teenhome + kidhome

--Get the youngest customer id and birth year, for every possible number of teens at home that exist in the table
select
	distinct on
	(teenhome) teenhome,
	id,
	min(date_part('year', now()) - year_birth) as min_age
from
	superstore_data
group by
	id,
	teenhome;

--Get total number of customers who accepted and did not accept the offer
select
	count(*)
from
	superstore_data
group by
	response
order by
	response = 1;

--Get average number of kids and average number of teens for customers with the same marital status (per status)
select
    marital_status,
	round(avg(kidhome)) as avg_k,
	round(avg(teenhome)) as avg_t
from
	superstore_data
group by
	marital_status,
	kidhome,
	teenhome;


-- Get the minimum, maximum, and average income for every education level of customers
select
    distinct on (education)
    education,
    date_part('year', now()) - year_birth as customer_age,
    id
from
    superstore_data
order by
    education, customer_age;















