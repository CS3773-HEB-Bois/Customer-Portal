//BillingInformation.java
package models;

import java.util.*;
import javax.persistence.*;

import io.ebean.*;
import play.data.format.*;
import play.data.validation.*;

@Entity
public class BillingInformation {

    @Id
    public int id;

    @Id
    public int paymentInformationId;

    @address
    public String billingAddress

    
}