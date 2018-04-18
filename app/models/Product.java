//Product.java
package models;

import java.util.*;
import javax.persistence.*;


import play.data.format.*;
import play.data.validation.*;

@Entity
public class Product 
{

    @Id
    private int id;
    
    @ManyToOne
    private ProductCategory category;

    private int availableStock;

    private double price;

    private String name;

    private String location;

    public int getId()
    {
        return id;
    }

    public ProductCategory getCategory()
    {
        return category;
    }

    public void setCategory(ProductCategory category)
    {
        this.category = category;
    }

    public int getAvailableStock()
    {
        return availableStock;
    }

    public void setAvailableStock(int availableStock)
    {
        this.availableStock = availableStock;
    }

    public double getPrice()
    {
        return price;
    }

    public void setPrice(double price)
    {
        this.price = price;
    }

    public String getName()
    {
        return name;
    }

    public void setName(String name)
    {
        this.name = name;
    }

    public String getLocation()
    {
        return location;
    }

    public void setLocation(String location)
    {
        this.location = location;
    }
}