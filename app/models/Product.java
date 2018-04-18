//Product.java
package models;

import java.util.*;
import javax.persistence.*;

import io.ebean.*;
import play.data.format.*;
import play.data.validation.*;

@Entity
public class Product extends Model {

    @Id
    public int id;

    @Id
    public int productCatigoryId;

    public int availableStock;

    public double price;

    @Constraints.Required
    public String name;

    @Constraints.Required
    public String location;
}