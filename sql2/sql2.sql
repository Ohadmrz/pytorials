--a

--b

--c

--d
select
	d.id,
	d."name" ,
	count(*) as movies_num,
	count(distinct(s.id)) as series_num
from
	directors d
join movies m on
	d.id = m.director_id
join series s on
	s.id = m.series_id
group by
	d.id;

--e
select
	s2.name,
	m2.name,
	d.name
from
	movies m2
join series s2 on
	s2.id = m2.series_id
join directors d on
	d.id = m2.director_id
where
	m2.series_id in (
	select
		s.id
	from
		movies m
	join series s on
		m.series_id = s.id
	group by
		s.id
	having
		count(m.id) >= 2);

--f
select
	m.name,
	d.name
from
	movies m
join directors d on
	d.id = m.director_id
where
	m.series_id is null;