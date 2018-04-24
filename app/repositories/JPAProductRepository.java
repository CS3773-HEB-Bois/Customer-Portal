package repositories;

import play.db.jpa.JPAApi;

import models.*;
import javax.inject.Inject;
import javax.persistence.EntityManager;
import java.util.List;
import java.util.concurrent.CompletionStage;
import java.util.function.Function;
import java.util.stream.Stream;

import static java.util.concurrent.CompletableFuture.supplyAsync;


public class JPAProductRepository implements ProductRepository {
    private final JPAApi jpaApi;
    private final DatabaseExecutionContext executionContext;

    @Inject
    public JPAProductRepository(JPAApi jpaApi, DatabaseExecutionContext executionContext) {
        this.jpaApi = jpaApi;
        this.executionContext = executionContext;
    }

    @Override
    public CompletionStage<Product> create(Product product) {
        return supplyAsync(() -> wrap(em -> insert(em, product)), executionContext);
    }

    public CompletionStage<Product> update(Product product) {
        return supplyAsync(() -> wrap(em -> update(em, product)), executionContext);
    }

    public CompletionStage<Product> get(int productId) {
        return supplyAsync(() -> wrap(em -> get(em, productId)), executionContext);
    }

    public CompletionStage<Stream<Product>> list() {
        return supplyAsync(() -> wrap(em -> list(em)), executionContext);
    }

    public CompletionStage<ProductItem> createItem(ProductItem productItem) {
        return supplyAsync(
            () -> wrap(em -> insertItem(em, productItem)), 
            executionContext
        );
    }

    private <T> T wrap(Function<EntityManager, T> function) {
        return jpaApi.withTransaction(function);
    }

    private Product insert(EntityManager em, Product product) {
        em.persist(product);
        return product;
    }

    private ProductItem insertItem(EntityManager em, ProductItem productItem) {
        em.persist(productItem);
        return productItem;
    }

    private Stream<Product> list(EntityManager em) {
        List<Product> products = em.createQuery(
            Queries.SELECT_PRODUCTS_QUERY, Product.class).getResultList();
        return products.stream();
    }

    private Product get(EntityManager em, int productId) {
        Product product = em.find(Product.class, productId);
        return product;
    }

    private Product update(EntityManager em, Product product) {
        em.persist(product);
        return product;
    }

    class Queries {
        public static final String SELECT_PRODUCTS_QUERY = "SELECT p from Product p";
    }

}