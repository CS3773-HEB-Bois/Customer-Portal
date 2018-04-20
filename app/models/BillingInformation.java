//BillingInformation.java
package models;

import java.util.*;
import javax.persistence.*;


import play.data.format.*;
import play.data.validation.*;

private int id;
private int paymentInfoId;
private String billingAddress;

public int getID(){
    return id;
}
public int getPaymentInfoId(){
    return paymentInfoId
}
public String getBillingAddress(){
    return billingAddress;
}
public void setBillingAddress(String billingAddress){
    this.billingAddress = billingAddress;
}