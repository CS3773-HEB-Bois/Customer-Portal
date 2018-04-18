# --- !Ups

CREATE TABLE PaymentInformation (
	id int NOT NULL,
	PRIMARY KEY (id)
);

# --- !Downs

DROP TABLE PaymentInformation;