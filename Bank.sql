CREATE DATABASE Bank;

USE Bank;

CREATE TABLE customers (
    customer_id int NOT NULL AUTO_INCREMENT,
	name varchar(55) NOT NULL,
    contact varchar(255) NOT NULL,
    PRIMARY KEY (customer_id)
);
CREATE TABLE accounts(
	account_number int NOT NULL AUTO_INCREMENT,
    balance bigint NOT NULL,
    customer_id int NOT NULL,
    PRIMARY KEY (account_number),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
CREATE TABLE transactions(
	transaction_id int NOT NULL AUTO_INCREMENT,
	account_number int NOT NULL,
    amount bigint NOT NULL DEFAULT 0,
    date timestamp NOT NULL,
    PRIMARY KEY (transaction_id),
    FOREIGN KEY (account_number) REFERENCES accounts(account_number)
);