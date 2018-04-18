# --- !Ups

CREATE TABLE Coupon (
	id int NOT NULL,
	code varchar(128) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (id) REFERENCES Discount(id)
);

# --- !Downs

DROP TABLE Coupon;