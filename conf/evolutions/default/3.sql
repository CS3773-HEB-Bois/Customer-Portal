# --- !Ups

CREATE TABLE RegisteredShopper (
	id int NOT NULL,
	username varchar(255) NOT NULL,
	passwordHash varchar(255) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (id) REFERENCES Shopper(id)
);

# --- !Downs

DROP TABLE RegisteredShopper;