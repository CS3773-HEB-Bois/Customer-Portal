# --- !Ups

CREATE TABLE VisitorShopper (
	id int NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (id) REFERENCES Shopper(id)
);

# --- !Downs

DROP TABLE VisitorShopper;