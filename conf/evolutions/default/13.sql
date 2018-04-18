# --- !Ups

CREATE TABLE OrderDiscount (
	orderId int NOT NULL,
	discountId int NOT NULL,
	FOREIGN KEY (orderId) REFERENCES `Order`(id),
	FOREIGN KEY (discountId) REFERENCES Discount(id)
);

# --- !Downs
DROP TABLE OrderDiscount;