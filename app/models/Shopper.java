//Shopper.java
package models;

import java.util.*;
import javax.persistence.*;

import io.ebean.*;
import play.data.format.*;
import play.data.validation.*;

@Entity
public class Shopper extends Model {

    @Id
    public int id;

    @Constraints.Required
    public String firstName;

    @Constraints.Required
    public String lastName;
}