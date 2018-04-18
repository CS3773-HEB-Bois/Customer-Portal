//ProductCategory.java
package models;

import java.util.*;
import javax.persistence.*;

import io.ebean.*;
import play.data.format.*;
import play.data.validation.*;

@Entity
public class ProductCategory extends Model {

    @Id
    public int id;

    @Constraints.Required
    public String name;
}