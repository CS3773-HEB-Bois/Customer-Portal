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
    public void setID(int id){
        this.id = id;
    }
    /**
     * set shopper username
     */
    public  void setUsername(String username){
        this.username = username;
    }
    /**
     * set shopper passwordHash
     */
    public  void setPasswordHash(String passwordHash){
        this.passwordHash = passwordHash;
    }
    /**
     * @return shopper id
     */
    public  int getID(){
        return id;
    }
    /**
     * @return shopper username
     */
    public  String getUsername(){
        return username;
    }
    /**
     * @return shopper passwordHash
     */
    public  String getPasswordHash(){
        return passwordHash;
    }
}