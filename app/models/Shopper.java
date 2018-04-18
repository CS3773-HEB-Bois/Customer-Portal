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
    private void setID(int id){
        this.id = id;
    }
    /**
     * set shopper firstName
     */
    private void setFirstName(String name){
        this.name = firstName;
    }
    /**
     * set shopper lastName
     */
    private void setLastName(String name){
        this.name = lastName;
    }
    /**
     * @return shopper id
     */
    private int getID(){
        return id;
    }
    /**
     * @return shopper firstName
     */
    private String getFirstName(){
        return firstName;
    }
    /**
     * @return shopper lastName
     */
    private String getLastName(){
        return lastName;
    }
}