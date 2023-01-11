create table stops(
	id serial primary key,
	city varchar(128) not null,
	name varchar(128) not null
);

create table drivers(
	id serial primary key,
	passport_num varchar(9) not null,
	name varchar(128) not null,
	address varchar(128) default 'Israel'
);

create table routes(
	id serial primary key,
	route_num int not null,
	orig_stop_id int not null,
	dest_stop_id int not null,
	foreign key (orig_stop_id) references stops(id) on delete restrict,
	-- foreign key (orig_stop_id) references stops(id) on delete set null,
	-- foreign key (orig_stop_id) references stops(id) on delete set default,
	-- foreign key (orig_stop_id) references stops(id) on delete cascade,
	foreign key (dest_stop_id) references stops(id) on delete restrict
);

create table rides(
	id serial primary key,
	weekday varchar(3) not null,
	route_id int not null,
	driver_id int not null,
	foreign key (route_id) references routes(id) on delete cascade,
	foreign key (driver_id) references drivers(id) on delete set null on update cascade
);

create table ride_stops(
	id serial primary key,
	stop_ordinal int not null,
	arrival_time time not null,
	departure_time time not null,
	ride_id int not null,
	stop_id int not null,
	foreign key (ride_id) references rides(id) on delete cascade,
	foreign key (stop_id) references stops(id) on delete cascade
	
);



create table service_interruptions(
	id serial primary key,
	interrupt_type varchar(16) not null,
	ts timestamp not null,
	ride_id int not null,
	foreign key (ride_id) references rides(id) on delete set null
);

