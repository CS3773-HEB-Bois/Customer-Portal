# --- !Ups

CREATE TABLE ProductCategory (
	id int NOT NULL,
	name varchar(255) NOT NULL,
	PRIMARY KEY (id)
);

# --- !Downs

DROP TABLE ProductCategory;