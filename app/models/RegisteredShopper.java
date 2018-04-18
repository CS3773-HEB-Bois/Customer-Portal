//RegisteredShopper.java
package models;

import java.util.*;
import javax.persistence.*;

import play.data.format.*;
import play.data.validation.*;

@Entity
public class RegisteredShopper extends Shopper {

    @Id
    private int id;

    private String username;

    private String passwordHash;
    /**
     * set shopper id
     */
    private void setID(int id){
        this.id = id;
    }
    /**
     * set shopper username
     */
    private void setUsername(String username){
        this.username = username;
    }
    /**
     * set shopper passwordHash
     */
    private void setPasswordHash(String passwordHash){
        this.passwordHash = passwordHash;
    }
    /**
     * @return shopper id
     */
    private int getID(){
        return id;
    }
    /**
     * @return shopper username
     */
    private String getUsername(){
        return username;
    }
    /**
     * @return shopper passwordHash
     */
    private String getPasswordHash(){
        return passwordHash;
    }
}