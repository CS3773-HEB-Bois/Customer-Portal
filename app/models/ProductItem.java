//ProductItem.java
package models;

import java.util.*;
import javax.persistence.*;

import play.data.format.*;
import play.data.validation.*;

@Entity
public class ProductItem
{

    @Id
    public int id;

    @ManyToOne
    public Product product;

    @ManyToOne
    public ShoppingCart shoppingCart;

    public int quantity;

    public int getId()
    {
        return id;
    }

    public void setId(int id)
    {
        this.id = id;
    }

    public Product getProduct()
    {
        return product;
    }

    public void setProduct(Product product)
    {
        this.product = product;
    }

    public ShoppingCart getShoppingCart()
    {
        return shoppingCart;
    }

    public void setShoppingCart(ShoppingCart shoppingCart)
    {
        this.shoppingCart = shoppingCart;
    }

    public int getQuantity()
    {
        return quantity;
    }

    public void setQuantity(int quantity)
    {
        this.quantity = quantity;
    }
}