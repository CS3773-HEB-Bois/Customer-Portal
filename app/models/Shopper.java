//Shopper.java
package models;

import java.util.*;
import javax.persistence.*;

import play.data.format.*;
import play.data.validation.*;

@Entity
public class Shopper extends Model {

    @Id
    private int id;

    private String firstName;

    private String lastName;
    /**
     * set shopper id
     */
    public  void setID(int id){
        this.id = id;
    }
    /**
     * set shopper firstName
     */
    public  void setFirstName(String name){
        this.name = firstName;
    }
    /**
     * set shopper lastName
     */
    public  void setLastName(String name){
        this.name = lastName;
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