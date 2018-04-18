//Product.java
package models;

import java.util.*;
import javax.persistence.*;

import io.ebean.*;
import play.data.format.*;
import play.data.validation.*;

@Entity
public class ShoppingCart extends Model {

    @Id
    public int id;
    
    public int shopperId;
}