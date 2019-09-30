-- Modified Data prepared by Cecilia Wei, ywei2@ualberta.ca
-- Published on Oct2,2018
-- Original Data prepapred by Davood Rafiei, drafiei@ualberta.ca
-- Published on Sept 27, 2018

-- 1. Find (name and email of) members who have at least two cars and at least one car is associated with a ride.
-- Chris, Joe, Ted
-- 2. Find (name and email of) members who have cars and bookings but have not offered any ride.
-- Mary, Grace
--3. Find (email of) members who are booked on a ride from Edmonton to Calgary in November 2018.
-- Chris,John,Grace
-- 4. Find requests that are served by the rides offered.
	-- 4 is served by 101
	--5 is served by 101
	-- 6 is served by 104
	-- 7 is served by 121
	-- 8 is served by 117
-- 5. Find top 3 destination cities with the largest number of rides.
-- Calgary, Red Deer, Toronto
-- 6. For every city, list the city, the province it is in, the number of rides from, the number of rides to,
--and the number of rides enroute that city. Include every city where at least one of the counts is non-zero.
-- Calgary|Alberta|0|12|1
-- Edmonton|Alberta|26|2|0
-- Mississauga|Ontario|0|2|0
-- Red Deer|Alberta|1|7|6
-- Toronto|Ontario|1|3|0
-- Vancouver|British Columbia|0|2|0
-- Winnipeg|Manitoba|0|0|1
-- 7. Find (the rno of) the cheapest ride(s)
--from Edmonton to Calgary in October 2018 with available seats (meaning not all seats are booked).
-- rno total booked price
-- 114,127
-- 8. Find (email of) members who have offered rides
--to more than half of the locations in Alberta and all their rides take place in 2016 or after.
-- name dstTOAlberta AlbertaTotal
-- chrise@a.com
-- joe@gmail.com
--10.
--rno booked avaliable price date src dst driver date_diff
-- "126"	"0"	"4"	"27.0"	"2018-12-30"	"Edmonton"	"Calgary"	"tedwalsh@td.com"	"2.0"
-- "124"	"0"	"3"	"30.0"	"2018-12-27"	"Edmonton"	"Calgary"	"joe@gmail.com"	"5.0"
-- "125"	"0"	"3"	"31.0"	"2018-12-01"	"Edmonton"	"Calgary"	"chrise@a.com"	"31.0"
insert into members values ('chrise@a.com','Chris Eng','780-111-3333','111');
insert into members values ('joe@gmail.com','Joe Anderson','780-111-2222','111');
insert into members values ('mary@abc.com','Mary Smith','780-222-3333','111');
insert into members values ('paul@a.com','John Paul','780-333-4444','111');
insert into members values ('whatever@e.com','What Ever','780-333-1111','111');
insert into members values ('tedwalsh@td.com','Ted Walsh','780-333-1231','111');
insert into members values ('flynn@rt.com','Flynn Le','780-321-1271','111');
insert into members values ('gc@art.com','Grace Evans','780-309-1234','111');
insert into members values ('hm@mah.com','Harry Mah','780-309-1234','111');

insert into cars values (1,'Aston Martin','DB5',1964,1,'chrise@a.com');
insert into cars values (2,'Honda','Civic',2017,4,'joe@gmail.com');
insert into cars values (3,'Nissan','Rogue',2018,4,'mary@abc.com');
insert into cars values (4,'Audi','A4',2015,4,'whatever@e.com');
insert into cars values (5,'Audi','A5',2016,5,'whatever@e.com');
insert into cars values (6,'Audi','R8',2018,6,'whatever@e.com');
insert into cars values (7,'Jeep','Cherokee',2019,8,'chrise@a.com');
insert into cars values (8,'Jeep','Compass',2019,7,'chrise@a.com');
insert into cars values (9,'Honda','Civic',2017,4,'joe@gmail.com');
insert into cars values (10,'Toyota','a1',2017,4,'tedwalsh@td.com');
insert into cars values (11,'Nissan','a2',2015,4,'tedwalsh@td.com');
insert into cars values (12,'Ford','a3',2015,4,'gc@art.com');
insert into cars values (13,'Hyundai','a4',2014,4,'hm@mah.com');


insert into locations values ('ab1','Edmonton','Alberta','UofA LRT st');
insert into locations values ('ab2','Edmonton','Alberta','Century LRT st');
insert into locations values ('ab3','Edmonton','Alberta',null);
insert into locations values ('ab4','Calgary','Alberta','111 Edmonton Tr');
insert into locations values ('ab5','Calgary','Alberta','Airport');
insert into locations values ('ab6','Red Deer','Alberta','City Hall');
insert into locations values ('ab7','Red Deer','Alberta','Airport');
insert into locations values ('bc1','Vancouver','British Columbia','Stanley Park');
insert into locations values ('bc2','Vancouver','British Columbia','Airport');
insert into locations values ('on1','Toronto','Ontario','Airport');
insert into locations values ('on2','Mississauga','Ontario','idk');
insert into locations values ('on3','Mississauga','Ontario','whatnot');
insert into locations values ('mb1','Winnipeg','Manitoba','dt');
--edm - cal
insert into rides values (100, 30, '2018-11-12', 3, 'small bag', 'ab1', 'ab7', 'joe@gmail.com', 2);
--edm- cal
insert into rides values (101, 30, '2018-11-13', 3, 'small bag', 'ab3', 'ab5', 'joe@gmail.com', null);
--edm- cal
insert into rides values (102, 30, '2018-09-12', 3, 'small bag', 'ab3', 'ab2', 'chrise@a.com', 7);
--edm- van
insert into rides values (103, 20, '2018-11-12', 3, 'small bag', 'ab1', 'bc2', 'chrise@a.com', 8);
--rd -van
insert into rides values (104, 80, '2018-11-12', 3, 'small bag', 'ab6', 'bc2', 'whatever@e.com', null);
--trt- mi
insert into rides values (105, 100, '2018-12-25', 3, 'large bag', 'on1', 'on3', 'whatever@e.com', null);
--edm -mi
insert into rides values (106, 100, '2018-12-26', 3, 'large bag', 'ab1', 'on2', 'whatever@e.com', null);
--edm - edm
insert into rides values (107, 100, '2018-12-27', 3, 'large bag', 'ab1', 'ab2', 'whatever@e.com', null);
--edm - trt
insert into rides values (108, 100, '2018-12-25', 3, 'large bag', 'ab1', 'on1', 'whatever@e.com', null);
--edm - trt
insert into rides values (109, 100, '2018-12-29', 3, 'large bag', 'ab2', 'on1', 'whatever@e.com', null);
-- edm - cal
insert into rides values (110, 50, '2018-10-10', 5, 'small bag', 'ab1', 'ab4', 'joe@gmail.com', 2);
-- edm - cal
insert into rides values (111, 40, '2018-10-11', 6, 'small bag', 'ab2', 'ab5', 'chrise@a.com', 8);
-- edm - cal
insert into rides values (112, 40, '2018-10-12', 6, 'small bag', 'ab3', 'ab4', 'chrise@a.com', 8);
-- edm - cal
insert into rides values (113, 100, '2015-12-26', 3, 'large bag', 'ab1', 'ab5', 'whatever@e.com', null);
-- edm - cal
insert into rides values (114, 30, '2018-10-27', 3, 'large bag', 'ab1', 'ab5', 'joe@gmail.com', null);
	-- edm - rd
insert into rides values (115, 100, '2016-12-28', 3, 'large bag', 'ab1', 'ab6', 'chrise@a.com', null);
	-- edm - rd
insert into rides values (116, 100, '2016-12-28', 3, 'large bag', 'ab1', 'ab6', 'chrise@a.com', null);
	-- edm - rd
insert into rides values (117, 100, '2016-12-29', 4, 'large bag', 'ab1', 'ab7', 'chrise@a.com', null);
	-- edm - rd
insert into rides values (118, 100, '2016-12-30', 5, 'large bag', 'ab1', 'ab6', 'joe@gmail.com', null);
-- edm - cal
insert into rides values (119, 100, '2017-12-27', 3, 'large bag', 'ab1', 'ab5', 'tedwalsh@td.com', 10);
--edm - cal
insert into rides values (120, 100, '2018-11-30', 4, 'large bag', 'ab1', 'ab4', 'tedwalsh@td.com', 11);
--edm - trt
insert into rides values (121, 70, '2018-08-13', 4, 'large bag', 'ab1', 'on1', 'hm@mah.com', null);


insert into rides values (122, 100, '2019-12-26', 3, 'large bag', 'ab1', 'ab6', 'whatever@e.com', null);
insert into rides values (123, 100, '2019-12-27', 3, 'large bag', 'ab1', 'ab7', 'whatever@e.com', null);

insert into rides values (124, 30, '2018-12-27', 3, 'large bag', 'ab1', 'ab5', 'joe@gmail.com', null);
insert into rides values (125, 31, '2018-12-01', 3, 'large bag', 'ab1', 'ab5', 'chrise@a.com', null);
insert into rides values (126, 27, '2018-12-30', 4, 'large bag', 'ab2', 'ab4', 'tedwalsh@td.com', null);

insert into rides values (127, 30, '2018-10-25', 3, 'large bag', 'ab1', 'ab5', 'joe@gmail.com', null);


insert into bookings values (10, 'chrise@a.com', 100, null, 1, 'ab2', null);
insert into bookings values (12, 'chrise@a.com', 101, 28, 1, 'ab2', 'ab5');
insert into bookings values (14, 'paul@a.com', 100, null, 1, null, null);
insert into bookings values (15, 'whatever@e.com', 103, null, 1, null, null);
insert into bookings values (16, 'mary@abc.com', 104, null, 1, null, null);

insert into bookings values (17, 'mary@abc.com', 110, null, 2, null, null);
-- booked 2 seats on 111
insert into bookings values (18, 'whatever@e.com', 111, null, 2, null, null);
--- booked 3 seats on 111
insert into bookings values (19, 'joe@gmail.com', 111, null, 3, null, null);
-- booked 1 seat on 111
insert into bookings values (20, 'mary@abc.com', 111, null, 1, null, null);
-- booked 4 seats on 112
insert into bookings values (21, 'mary@abc.com', 112, null, 4, null, null);
insert into bookings values (22, 'gc@art.com', 120, null, 2, null, null);

insert into bookings values (23, 'gc@art.com', 103, null, 2, null, null);
insert into bookings values (24, 'paul@a.com', 120, null, 1, null, null);


insert into enroute values (100, 'ab6');
insert into enroute values (101, 'ab7');
insert into enroute values (102, 'ab6');
-- 103 has two enroutes
insert into enroute values (103, 'ab4');
insert into enroute values (103, 'ab6');
-- winnipeg is only a enroute city
insert into enroute values (105, 'mb1');

insert into enroute values (119, 'ab7');
insert into enroute values (119, 'ab6');


insert into requests values (1, 'paul@a.com', '2018-12-22', 'ab3', 'bc1', 80);
insert into requests values (2, 'chrise@a.com', '2018-12-24', 'ab1', 'ab7', 30);
insert into requests values (3, 'whatever@e.com', '2018-11-13', 'ab1', 'ab4', 17);
insert into requests values (4, 'whatever@e.com', '2018-11-13', 'ab2', 'ab4', 30);
insert into requests values (5, 'mary@abc.com', '2018-11-13', 'ab2', 'ab4', 35);
insert into requests values (6, 'joe@gmail.com', '2018-11-12', 'ab7', 'bc1', 85);
insert into requests values (7, 'tedwalsh@td.com', '2018-08-13', 'ab2', 'on1', 70);
insert into requests values (8, 'gc@art.com', '2016-12-29', 'ab3', 'ab6', 120);
insert into requests values (9, 'hm@mah.com', '2016-12-29', 'ab2', 'ab6', 99);
