# --- !Ups

CREATE TABLE Shopper (
	id int NOT NULL PRIMARY KEY,
	firstName varchar(255) NOT NULL,
	lastName varchar(255) NOT NULL
)

# --- !Downs

DROP TABLE Shopper;