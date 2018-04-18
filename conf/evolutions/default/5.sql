# --- !Ups

CREATE TABLE Product (
	id int NOT NULL,
	productCategoryId int NOT NULL,
	name varchar(255) NOT NULL,
	availableStock int NOT NULL,
	price decimal NOT NULL,
	location varchar(255) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (productCategoryId) REFERENCES ProductCategory(id)
);

# --- !Downs

DROP TABLE Product;