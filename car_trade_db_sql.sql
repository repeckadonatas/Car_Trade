SET ROLE db_admin;

SELECT current_user;

-- Checking GRANT permissions for db_admin
SELECT * 
FROM information_schema.role_table_grants 
WHERE grantee = 'db_admin';

SELECT grantee, privilege_type 
FROM information_schema.role_table_grants 
WHERE table_name = 'car_data';


-- Adding a car_unique_id column to car_data
ALTER TABLE car_data
ADD COLUMN car_unique_id SERIAL PRIMARY KEY;

SELECT * FROM car_data;



-- Creating a schema to be used by user db_analyst
CREATE SCHEMA analyst;



-- Creating a car_info table from car_data table to conform to 2NF
CREATE TABLE analyst.car_info
AS
SELECT car_id, make, model, make_year, color, body_type, mileage_run, 
	no_of_owners, seating_capacity, fuel_tank_capacity_L, price_EUR
FROM car_data;

ALTER TABLE analyst.car_info
ADD COLUMN car_unique_id SERIAL UNIQUE;

-- Creating a unique composite primary key
ALTER TABLE analyst.car_info
ADD PRIMARY KEY (car_unique_id, make, model);

SELECT * FROM analyst.car_info LIMIT 5;


-- Creating a car_engine table from car_data table to conform to 2NF
CREATE TABLE analyst.car_engine
AS
SELECT car_id, displacement_CC, power_BHP, torque_Nm, fuel_type,
	"mileage_L/100km", emission
FROM car_data;

ALTER TABLE analyst.car_engine
ADD COLUMN engine_id SERIAL PRIMARY KEY,
ADD COLUMN car_id_fk SERIAL;

ALTER TABLE analyst.car_engine
ADD CONSTRAINT car_id_fk
FOREIGN KEY (car_id_fk) REFERENCES analyst.car_info (car_unique_id);

SELECT * FROM analyst.car_engine;



-- Creating a car_transmission table from car_data table 
-- to conform to 2NF
CREATE TABLE analyst.car_transmission
AS
SELECT transmission, transmission_type, car_id
FROM car_data;

ALTER TABLE analyst.car_transmission
ADD COLUMN transmission_id SERIAL PRIMARY KEY,
ADD COLUMN car_id_fk SERIAL;

ALTER TABLE analyst.car_transmission
ADD CONSTRAINT car_id_fk
FOREIGN KEY (car_id_fk) REFERENCES analyst.car_info (car_unique_id);

SELECT * FROM analyst.car_transmission;


-- Granting permissions on a schema to db_analyst user
GRANT ALL
ON SCHEMA analyst
TO db_analyst;


SET ROLE db_analyst;

SELECT current_user;

SELECT * FROM analyst.car_info
WHERE make = 'Volkswagen';



SELECT * FROM car_data
WHERE make = 'Volkswagen';









