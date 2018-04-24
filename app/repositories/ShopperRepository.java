package repositories;

import com.google.inject.ImplementedBy;
import java.util.concurrent.CompletionStage;
import java.util.stream.Stream;
import models.Shopper;

public interface ShopperRepository {
    public CompletionStage<Shopper> get(int shopperId);
    public CompletionStage<Shopper> create(Shopper shopper);
    public CompletionStage<Shopper> update(Shopper shopper);
}