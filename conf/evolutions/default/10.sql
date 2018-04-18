# --- !Ups

CREATE TABLE `Order` (
	id int NOT NULL,
	shoppingCartId int NOT NULL,
	billingInformationId int NOT NULL,
	subtotal decimal NOT NULL,
	total decimal NOT NULL,
	deliveryFee decimal NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (shoppingCartId) REFERENCES ShoppingCart(id),
	FOREIGN KEY (billingInformationId) REFERENCES BillingInformation(id)
);

# --- !Downs

DROP TABLE `Order`;