INSERT INTO 
	drivers (passport_num, "name", address) 
values
	('111111111', 'Israel Israeli', 'Tel Aviv');

INSERT INTO 
	drivers (passport_num, "name", address) 
values
	('222222222', 'Moshe Cohen', 'Hod Hasharon');

INSERT INTO 
	drivers (passport_num, "name", address) 
values
	('333333333', 'David Shwimmer', 'Tveriya');

INSERT INTO 
	drivers (passport_num, "name", address) 
values
	('444444444', 'Tali Shani', 'Tel Aviv');

INSERT INTO 
	drivers (passport_num, "name", address) 
values
	('555555555', 'Sagi Shem Tov', 'Tel Aviv');


INSERT INTO stops (city, "name") 
VALUES('Tel Aviv', 'Central bus station');

INSERT INTO stops (city, "name") 
VALUES('Tel Aviv', 'Alenby');

INSERT INTO stops (city, "name") 
VALUES('Tel Aviv', 'University');

INSERT INTO stops (city, "name") 
VALUES('Haifa', 'Matam');

INSERT INTO stops (city, "name") 
VALUES('Haifa', 'Technion');



INSERT INTO routes (route_num, orig_stop_id, dest_stop_id) 
VALUES(100, 1, 4);

INSERT INTO routes (route_num, orig_stop_id, dest_stop_id) 
VALUES(200, 1, 3);

INSERT INTO routes (route_num, orig_stop_id, dest_stop_id) 
VALUES(300, 4, 5);

INSERT INTO routes (route_num, orig_stop_id, dest_stop_id) 
VALUES(400, 3, 5);

INSERT INTO routes (route_num, orig_stop_id, dest_stop_id) 
VALUES(500, 3, 2);



INSERT INTO rides (weekday, route_id, driver_id) 
VALUES('sun', 1, 1);

INSERT INTO rides (weekday, route_id, driver_id) 
VALUES('tue', 2, 1);

INSERT INTO rides (weekday, route_id, driver_id) 
VALUES('tue', 1, 3);

INSERT INTO rides (weekday, route_id, driver_id) 
VALUES('thu', 4, 2);

INSERT INTO rides (weekday, route_id, driver_id) 
VALUES('sun', 1, 5);


-- T
INSERT INTO ride_stops (stop_ordinal, arrival_time, departure_time, ride_id, stop_id) 
VALUES(1, '10:30', '10:31', 1, 1);

INSERT INTO ride_stops (stop_ordinal, arrival_time, departure_time, ride_id, stop_id) 
VALUES(2, '10:50', '10:55', 1, 3);

INSERT INTO ride_stops (stop_ordinal, arrival_time, departure_time, ride_id, stop_id) 
VALUES(3, '11:30', '11:32', 1, 5);

INSERT INTO ride_stops (stop_ordinal, arrival_time, departure_time, ride_id, stop_id) 
VALUES(4, '11:50', '11:50', 1, 4);


INSERT INTO service_interruptions (interrupt_type, ts, ride_id) 
VALUES('cancelation', '2023-01-08 04:05:06', 1);

INSERT INTO service_interruptions (interrupt_type, ts, ride_id) 
VALUES('delay', '2023-01-09 17:05:00', 2);

INSERT INTO service_interruptions (interrupt_type, ts, ride_id) 
VALUES('delay', '2023-01-06 14:00:00', 1);

INSERT INTO service_interruptions (interrupt_type, ts, ride_id) 
VALUES('cancelation', '2023-01-05 09:05:10', 3);

INSERT INTO service_interruptions (interrupt_type, ts, ride_id) 
VALUES('cancelation', '2023-01-08 12:00:00', 1);












