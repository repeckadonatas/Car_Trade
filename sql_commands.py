new_table = """
    CREATE TABLE IF NOT EXISTS car_data (
        car_id INT NOT NULL,
        make VARCHAR(30),
        model VARCHAR(30),
        make_year INT,
        color VARCHAR(30),
        body_type VARCHAR(30),
        mileage_run FLOAT,
        no_of_owners VARCHAR(50),
        seating_capacity INT,
        fuel_type VARCHAR(30),
        fuel_tank_capacity_L INT,
        displacement_CC INT,
        transmission VARCHAR(30),
        transmission_type VARCHAR(30),
        power_BHP FLOAT,
        torque_Nm FLOAT,
        "mileage_L/100km" FLOAT,
        emission VARCHAR(30),
        price_EUR FLOAT
);
"""


load_csv = """
    COPY car_data (
        make, model, make_year, color, body_type, mileage_run, no_of_owners, seating_capacity,
        fuel_type, fuel_tank_capacity_L, displacement_CC, transmission, transmission_type, power_BHP,
        torque_Nm, "mileage_L/100km", emission, price_EUR, car_id)
    FROM STDIN 
    WITH
        DELIMITER ','
        CSV HEADER;
"""


table_check = """
    SELECT * FROM car_data;
"""