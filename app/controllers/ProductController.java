package controllers;

import models.Product;
import repositories.ProductRepository;
import play.data.FormFactory;
import play.libs.concurrent.HttpExecutionContext;
import play.mvc.Controller;
import play.mvc.Result;

import javax.inject.Inject;
import java.util.concurrent.CompletionStage;
import java.util.stream.Collectors;

import static play.libs.Json.toJson;

/**
 * The controller keeps all database operations behind the repository, and uses
 * {@link play.libs.concurrent.HttpExecutionContext} to provide access to the
 * {@link play.mvc.Http.Context} methods like {@code request()} and {@code flash()}.
 */
public class ProductController extends Controller {

    private final FormFactory formFactory;
    private final ProductRepository productRepository;
    private final HttpExecutionContext ec;

    @Inject
    public ProductController(FormFactory formFactory, 
                            ProductRepository productRepository, 
                            HttpExecutionContext ec) {
        this.formFactory = formFactory;
        this.productRepository = productRepository;
        this.ec = ec;
    }

    public Result index() {
        return ok(views.html.index.render());
    }

    public CompletionStage<Result> getProducts() {
        return productRepository.list().thenApplyAsync(productStreams -> {
            return ok(toJson(productStreams.collect(Collectors.toList())));
        }, ec.current());
    }

}