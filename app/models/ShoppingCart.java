//Product.java
package models;

import java.util.*;
import javax.persistence.*;

import play.data.format.*;
import play.data.validation.*;

@Entity
public class ShoppingCart {

    @Id
    public int id;
    
    @OnetoOne
    public Shopper shopper;
    
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






