# --- !Ups

CREATE TABLE Discount (
	id int NOT NULL,
	amount decimal NOT NULL,
	PRIMARY KEY (id)
);

# --- !Downs

DROP TABLE Discount;