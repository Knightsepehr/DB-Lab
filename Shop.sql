CREATE TABLE product(
	pid int NOT NUll AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    price bigint NOT NULL,
    description TEXT,
    PRIMARY KEY (pid)
);
CREATE TABLE vendor(
	vid int NOT NULL AUTO_INCREMENT,
    addr TEXT,
    PRIMARY KEY (vid)
);
CREATE TABLE employee(
	eid int NOT NULL AUTO_INCREMENT,
    fname varchar(255) NOT NULL,
    lname varchar(255) NOT NULL,
    salary bigint NOT NULL,
    vid int NOT NULL,
    PRIMARY KEY (eid),
    FOREIGN KEY (vid) REFERENCES vendor(vid)
);
CREATE TABLE customer(
	cid int NOT NULL AUTO_INCREMENT,
    name varchar(255) NOT NULL,
    PRIMARY KEY (cid)
);

CREATE TABLE order_management(
	oid int NOT NULL AUTO_INCREMENT,
    pid int NOT NULL,
    vid int NOT NULL,
    cid int NOT NULL,
    PRIMARY KEY (oid),
    FOREIGN KEY (vid) REFERENCES vendor(vid),
    FOREIGN KEY (cid) REFERENCES customer(cid),
    FOREIGN KEY (pid) REFERENCES product(pid)
);
CREATE TABLE loyality(
	lid int NOT NULL AUTO_INCREMENT,
    cid int NOT NULL,
    vid int NOT NULL,
    PRIMARY KEY (lid),
    FOREIGN KEY (vid) REFERENCES vendor(vid),
    FOREIGN KEY (cid) REFERENCES customer(cid)
);