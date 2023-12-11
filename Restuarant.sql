CREATE DATABASE Restaurant;

USE Restaurant;

CREATE TABLE Menu(
    menu_id INT NOT NULL AUTO_INCREMENT,
    item_name VARCHAR(50) NOT NULL,
    price INT NOT NULL,
    PRIMARY KEY(menu_id)
); 

CREATE TABLE Customers(
    customer_id INT NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    contact_number VARCHAR(15) NOT NULL,
    PRIMARY KEY(customer_id)
);

CREATE TABLE Tables(
	table_id int NOT NULL AUTO_INCREMENT,
    capacity int,
    PRIMARY KEY (table_id)
);

CREATE TABLE Orders(
	order_id int NOT NULL AUTO_INCREMENT,
    customer_id int NOT NULL,
    table_id int NOT NULL,
    order_time timestamp NOT NULL,
    PRIMARY KEY (order_id),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id),
    FOREIGN KEY (table_id) REFERENCES Tables(table_id)
);


INSERT INTO Menu (item_name,price) VALUES ("koobide",75000);
INSERT INTO Menu (item_name,price) VALUES ("jooje",85000);
INSERT INTO Menu (item_name,price) VALUES ("zereshpolo",65000);
INSERT INTO Menu (item_name,price) VALUES ("gheyme",55000);


INSERT into Customers (first_name,last_name,contact_number) VALUES("Abbas","Khatar","555-555-255");
INSERT into Customers (first_name,last_name,contact_number) VALUES("Ali","Khatar","555-444-555");
INSERT into Customers (first_name,last_name,contact_number) VALUES("Mohsen","Salari","555-445-255");
INSERT into Customers (first_name,last_name,contact_number) VALUES("Salar","Mohseni","555-554-255");

INSERT INTO Tables (capacity) VALUES (2);
INSERT INTO Tables (capacity) VALUES (2);
INSERT INTO Tables (capacity) VALUES (4);
INSERT INTO Tables (capacity) VALUES (4);
INSERT INTO Tables (capacity) VALUES (6);
INSERT INTO Tables (capacity) VALUES (6);
INSERT INTO Tables (capacity) VALUES (2);
INSERT INTO Tables (capacity) VALUES (8);


INSERT INTO `Orders`(`customer_id`, `table_id`) VALUES ('2','5');
INSERT INTO Orders (customer_id,table_id) VALUES(2,3);