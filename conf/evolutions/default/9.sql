# --- !Ups

CREATE TABLE DeliveryPreferences (
	id int NOT NULL,
	deliveryAddress varchar(255) NOT NULL,
	PRIMARY KEY (id)
);

# --- !Downs
DROP TABLE DeliveryPreferences;