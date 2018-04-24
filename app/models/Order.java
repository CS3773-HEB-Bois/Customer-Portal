//Order.java
package models;

import java.util.*;
import javax.persistence.*;

import play.data.format.*;
import play.data.validation.*;

@Entity
public class Order{

    @Id
    private int id;
    
    @OneToOne
    private ShoppingCart shoppingcart;

    @OneToOne
    private BillingInformation billinginformation;

    private double subtotal;

    private double deliveryFee;

    /**
     * set order subtotal
     */
    public void setSubtotal(double subtotal){
        this.subtotal = subtotal;
    }

    /**
     * set Order delivery Fee
     */
    public void setDeliveryFee(double deliveryFee){
        this.deliveryFee = deliveryFee;
    }

    /**
     * @return Order id
     */
    public  int getID(){
        return id;
    }

    /**
     * get order subtotal
     */
    public double getSubtotal(){
        return subtotal;
    }

    /**
     * get Order delivery Fee
     */
    public double getDeliveryFee(){
        return deliveryFee;
    }

}