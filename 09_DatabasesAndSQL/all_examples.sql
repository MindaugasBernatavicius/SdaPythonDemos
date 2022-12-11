
-- Database creation / deletion
CREATE DATABASE twitter1;

DROP DATABASE twitter1; -- ctrl + /

CREATE DATABASE twitter1;

SELECT * FROM employees e ;

-- User creation / deletion
CREATE USER user2 IDENTIFIED BY 'pass1';

SELECT user FROM mysql.user;


RENAME USER user1 TO user2;

SHOW GRANTS FOR 'user2'@'%';

GRANT SELECT ON test1.* TO 'user2'@'%';

REVOKE SELECT ON test1.* FROM 'user2'@'%';


DROP USER user2;


-- DDL - creating tables

create table people(
	id bigint primary key auto_increment,
	name varchar(100) not null,
	created_at timestamp default current_timestamp
);

drop table if exists people;

SHOW COLUMNS FROM people;

alter table people
modify column surname varchar(100) not null
after name;

select * from people;


-- DML

select * from people p;


INSERT INTO people (id, name, surname, created_at)
VALUES (5, "Max", "Maximum", now() + 1);

INSERT INTO people (id, name, surname, created_at)
VALUES (6, "name1", "surname1", "2001-01-01 01:01:01");

-- INSERT INTO people (id, name, surname, created_at)
-- VALUES (6, "name1", "surname1", "2001-01-01 01:01:01" + 1);


-- INSERT INTO people (name, surname)
-- VALUES ("name1", "surname1");

-- SQL Error [1136] [21S01]: Column count doesn't match value count at row 1
-- INSERT INTO people
-- VALUES ("name1", "surname1");


INSERT INTO people
VALUES (1001, "name1", "surname1", "2001-01-01 01:01:01");


INSERT INTO people (name, surname, created_at, id)
VALUES ("name1", "surname1", "2001-01-01 01:01:01", 1002);


INSERT INTO people
	(name, surname)
VALUES
	("name1001", "surname1023"),
	("name1001", "surname1022"),
	("name1001", "surname1022"),
	("name1001", "surname1022"),
	("name1001", "surname1003"),
	("name1001", "surname1003"),
	("name1001", "surname1003");


select * from people p;

UPDATE people
SET name='max1', surname='maximum1', created_at=current_timestamp()
where id=999 or id=6;


UPDATE people
SET name='max1', surname='maximum1', created_at=current_timestamp()
where id > 1000;


select * from people p where id > 100;
delete from people where id > 100;

select * from people p;
delete from people;


truncate table people;


-- SELECT (DQL)
select 1;
select * from people;
select surname, id from people;


select * from people
where id > 1
and id < 10
and name = 'Johan';

select * from people where name = 'Johan';


select * from people
order by id desc;

select * from people
order by created_at desc;


select * from people
order by created_at, id;

select * from people
order by created_at, id desc;



-- SELECT TOP 2
select * from employees
order by id desc
limit 2;

select * from employees
limit 2;

select * from employees
order by age desc
limit 1, 1;




select * from employees
where name like 'M%';

select * from employees
where name like '%s';

select * from employees
where age like '5%';

select * from employees
where age like '%9';

select * from employees
where name like 'S%r';



SELECT
	name as 'el nameo',
	age as 'how old is the employee'
FROM employees
-- 	WHERE age between 20 and 150
	where age in (55, 66)
	and name is not null
	AND name like 'M%';


-- FOREIGN KEYS

create table manufacturer(
    Id INTEGER PRIMARY KEY,
    Name VARCHAR(20)
);


CREATE TABLE Product
(
    Id INTEGER PRIMARY KEY,
    Name VARCHAR(20),
    ManufacturerId INTEGER,
    CONSTRAINT manufacturerId_fk FOREIGN KEY (ManufacturerId) REFERENCES manufacturer(Id)
);

select * from manufacturer;

select * from Product;

INSERT INTO test1.product
	(Id, Name, ManufacturerId)
values
	(1, 'Yaris 2.0', 2),
	(2, '320i', 1);


INSERT INTO test1.product
	(Id, Name, ManufacturerId)
values
	(99, 'Yaris 3.0', 3);


INSERT INTO test1.manufacturer
	(Id, Name)
values
	(1, 'BMW'),
	(2, 'Toyota');



ALTER TABLE Product ADD CONSTRAINT manufacturer_fk FOREIGN KEY (ManufacturerId) REFERENCES manufacturer(Id);

update Product
set ManufacturerId = null
where ManufacturerId not in
(select id from manufacturer); -- subquery (subselect)


-- JOIN
select * from product p;
select * from manufacturer m;

-- old style join, not used anymore
select p.name, m.name
from product p, manufacturer m
where p.ManufacturerId = m.Id

--
select p.id, p.name, m.id as 'manuf_id', m.name from product p
inner join manufacturer m
on p.ManufacturerId = m.id
order by m.Name desc;

select p.id, p.name, m.id as 'manuf_id', m.name from product p
left join manufacturer m
on p.ManufacturerId = m.id
order by m.Name desc;

select p.id, p.name, m.id as 'manuf_id', m.name from product p
right join manufacturer m
on p.ManufacturerId = m.id
order by m.Name desc;

-- full join with union
select p.id, p.name, m.id as 'manuf_id', m.name from product p
left join manufacturer m
on p.ManufacturerId = m.id
union
select p.id, p.name, m.id as 'manuf_id', m.name from product p
right join manufacturer m
on p.ManufacturerId = m.id;



-- multi table joins
CREATE TABLE `Customer` (
   `id` bigint NOT NULL auto_increment PRIMARY KEY,
   `name` varchar(255) DEFAULT NULL
);

CREATE TABLE `Address` (
  `id` bigint NOT NULL auto_increment PRIMARY KEY,
  `City` varchar(255) DEFAULT NULL,
  `Street` varchar(255) DEFAULT NULL,
  `Building_Number` varchar(255) DEFAULT NULL,
  `Customer_id` bigint NOT NULL
);

CREATE TABLE `Orders` (
  `id` bigint NOT NULL auto_increment PRIMARY KEY,
  `Item` varchar(255) DEFAULT NULL,
  `Customer_id` bigint NOT NULL
);


INSERT INTO address
   (City, Street, Building_Number, Customer_id)
VALUES
  ('Kaunas', 'Saulės', '33', 4),
  ('Vilnius', 'Gedimino pr.', '44', 2);

INSERT INTO customer
   (Name)
VALUES
  ('Mindaugas'),
  ('Jonas');

INSERT INTO orders
   (Item, Customer_id)
VALUES
   ('Towel', 2);


SELECT * FROM Address;
SELECT * FROM Customer;
SELECT * FROM Orders;


select c.name, a.City, a.Street, o.Item from customer c
join address a on c.id  = a.Customer_id
join orders o on c.id = o.Customer_id
order by o.id;


-- Aggregations

alter table Product add price decimal(8,2);
-- add the prices manually

select
	avg(price),
	count(id),
	sum(price),
	sum(price) / count(id) as 'average_calculated_manually',
	stddev(price)
from product;
-- where ManufacturerId = 2;

select count(id) from product p;

-- group by
select * from product p;
select price, ManufacturerId from product p;
select max(price), avg(price), ManufacturerId from product p group by ManufacturerId;

select group_concat(p.name SEPARATOR '; '), m.Name from product p
join manufacturer m on p.ManufacturerId = m.Id
group by p.ManufacturerId;

select max(price), avg(price), ManufacturerId
from product p
where ManufacturerId is not null
group by ManufacturerId
having avg(price) > 9600;


-- Triggers (row level triggers)

create table audit(
	id int auto_increment primary key,
	value_deleted varchar(1000)
)

select * from audit;
select * from product;

delete from product where id = 3;

CREATE TRIGGER deletion_tracker
BEFORE DELETE ON product
FOR EACH ROW
	insert into audit(value_deleted) values (old.name);


-- Stored procedures
--
-- CREATE PROCEDURE GetPriceStatsForManufacturer(IN manufacturer_id VARCHAR(20))
-- BEGIN
--     select max(price), avg(price), ManufacturerId from product
--    	where ManufacturerId = manufacturer_id;
-- END;

call GetPriceStatsForManufacturer(1);


-- Transactions (ACID: atomicity, consistency, isolation, durability)

select * from product p;

-- SELECT @@autocommit; // SET autocommit=0;
START TRANSACTION;
INSERT INTO product (id, name) VALUES (10901,'XYZ');
-- select * from product;
COMMIT;
-- ROLLBACK;


create table bank_accounts (
	account_number int auto_increment primary key,
	type varchar(50) not null,
	balance decimal(15,2) not null default 0
)

INSERT INTO bank_accounts
	(account_number, type, balance)
VALUES
	(123456, 'credit', 1050),
	(654321, 'debit', 11250);

select * from bank_accounts;




CREATE PROCEDURE tranfer_funds(IN from_acc INT, IN to_acc INT, IN amount decimal)
BEGIN
    START TRANSACTION;

    -- Withdraw money from the first account
    UPDATE bank_accounts
    SET balance = balance - amount
    WHERE account_number = from_acc;

    -- Deposit money in the second account
    UPDATE bank_accounts
    SET balance = balance + amount
    WHERE account_number = to_acc;

    -- Check if the balance of the account is negative
    IF (SELECT balance FROM bank_accounts WHERE account_number = from_acc) < 0 THEN
        ROLLBACK;
    ELSE
        COMMIT;
    END IF;
END


select * from bank_accounts;
CALL tranfer_funds(123456, 654321, 200);


