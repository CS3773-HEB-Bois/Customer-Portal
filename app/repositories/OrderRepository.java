package repositories;

import com.google.inject.ImplementedBy;
import java.util.concurrent.CompletionStage;
import java.util.stream.Stream;
import models.Order;

public interface OrderRepository {
    public CompletionStage<Order> get(int orderId);
    public CompletionStage<Order> create(Order order);
}