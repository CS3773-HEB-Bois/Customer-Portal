package repositories;

import com.google.inject.ImplementedBy;

import java.util.concurrent.CompletionStage;
import java.util.stream.Stream;

import models.*;

@ImplementedBy(JPAProductRepository.class)
public interface ProductRepository {
    CompletionStage<Product> create(Product product);
    CompletionStage<Product> update(Product product);
    CompletionStage<Product> get(int productId);
    CompletionStage<Stream<Product>> list();
}