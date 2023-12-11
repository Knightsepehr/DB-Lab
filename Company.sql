CREATE DATABASE Company;
-- ======
USE Company;
-- ======
CREATE TABLE Company(
	id int NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    PRIMARY KEY (id)
);
CREATE TABLE Employee(
	id int NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    salary bigint NOT NULL,
    cid int NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (cid) REFERENCES Company(id)
);
CREATE TABLE Projects(
	id int NOT NULL AUTO_INCREMENT,
    title varchar(255) NOT NULL,
    eid int NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (eid) REFERENCES Employee(id)
);
-- ======
INSERT INTO `Company`(`name`) VALUES ('Steam');
INSERT INTO `Company`(`name`) VALUES ('Epicgames');
INSERT INTO `Company`(`name`) VALUES ('Fasau');
-- ======
INSERT INTO `Employee`(`name`, `salary`, `cid`) VALUES ('David Doe','5000000','1');
INSERT INTO `Employee`(`name`, `salary`, `cid`) VALUES ('John Doe','6000000','1');
INSERT INTO `Employee`(`name`, `salary`, `cid`) VALUES ('Melika Doe','4000000','3');
INSERT INTO `Employee`(`name`, `salary`, `cid`) VALUES ('Reza Doe','8000000','2');
INSERT INTO `Employee`(`name`, `salary`, `cid`) VALUES ('Sepehr Doe','99000000','3');
-- ======
INSERT INTO `Projects`(`title`, `eid`) VALUES ('PetShop','1');
INSERT INTO `Projects`(`title`, `eid`) VALUES ('HackNasa','5');
INSERT INTO `Projects`(`title`, `eid`) VALUES ('DoHomeWork','3');
INSERT INTO `Projects`(`title`, `eid`) VALUES ('ComputerFactory','4');
INSERT INTO `Projects`(`title`, `eid`) VALUES ('CatnipShop','2');
-- ======
-- which company and whome from the company

SELECT cid,eid,title FROM ((Employee INNER JOIN Company ON Employee.cid = Company.id) INNER JOIN Projects ON Projects.eid = Employee.id);
