//ProductCategory.java
package models;

import java.util.*;
import javax.persistence.*;

import play.data.format.*;
import play.data.validation.*;

@Entity
public class ProductCategory
{

    @Id
    private int id;

    private String name;

    public int getId()
    {
        return id;
    }

    public String getName()
    {
        return name;
    }

    public void setName(String name)
    {
        this.name = name;
    }
}