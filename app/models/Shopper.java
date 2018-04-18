//Shopper.java
package models;

import java.util.*;
import javax.persistence.*;

import play.data.format.*;
import play.data.validation.*;

@Entity
public class Shopper{

    @Id
    private int id;

    private String firstName;

    private String lastName;

    /**
     * set shopper firstName
     */
    public  void setFirstName(String name){
        this.firstName = name;
    }
    /**
     * set shopper lastName
     */
    public  void setLastName(String name){
        this.lastName = name;
    }
    /**
     * @return shopper id
     */
    public  int getID(){
        return id;
    }
    /**
     * @return shopper firstName
     */
    public  String getFirstName(){
        return firstName;
    }
    /**
     * @return shopper lastName
     */
    public  String getLastName(){
        return lastName;
    }
}