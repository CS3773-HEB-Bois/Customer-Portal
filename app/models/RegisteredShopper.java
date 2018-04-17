//RegisteredShopper.java
package models;

import java.util.*;
import javax.persistence.*;

import io.ebean.*;
import play.data.format.*;
import play.data.validation.*;

@Entity
public class RegisteredShopper extends Shopper {

    @Id
    public int id;

    @Constraints.Required
    public String username;

    @Constraints.Required
    public String passwordHash;
}