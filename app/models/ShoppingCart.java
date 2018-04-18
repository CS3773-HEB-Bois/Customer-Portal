//Product.java
package models;

import java.util.*;
import javax.persistence.*;

import play.data.format.*;
import play.data.validation.*;

@Entity
public class ShoppingCart {

    @Id
    private int id;
    
    @OneToOne
    private Shopper shopper;
    
    public int getId()
    {
        return id;
    }

    public Shopper getShopper()
    {
        return shopper;
    }

    public void setShopper(Shopper shopper)
    {
        this.shopper = shopper;
    }

}






