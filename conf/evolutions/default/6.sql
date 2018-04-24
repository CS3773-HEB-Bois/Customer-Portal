# --- !Ups

CREATE TABLE ShoppingCart (
	id int NOT NULL,
	shopperId int NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (shopperId) REFERENCES Shopper(id)
);


CREATE TABLE ProductItem (
	id int NOT NULL,
	productId int NOT NULL,
	shoppingCartId int NOT NULL,
	quantity int NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (productId) REFERENCES Product(id),
	FOREIGN KEY (shoppingCartId) REFERENCES ShoppingCart(id)
);

# --- !Downs

DROP TABLE ProductItem;
DROP TABLE ShoppingCart;
