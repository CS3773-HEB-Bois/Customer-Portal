# --- !Ups

CREATE TABLE BillingInformation (
	id int NOT NULL,
	paymentInformationId int NOT NULL,
	billingAddress varchar(255) NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (paymentInformationId) REFERENCES PaymentInformation(id)
);

# --- !Downs

DROP TABLE BillingInformation;