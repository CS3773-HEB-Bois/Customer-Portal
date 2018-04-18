# --- !Ups

CREATE TABLE Shopper (
	id int NOT NULL,
	firstName varchar(255) NOT NULL,
	lastName varchar(255) NOT NULL,
	PRIMARY KEY (id)
);

# --- !Downs

DROP TABLE Shopper;