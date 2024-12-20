from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.models.redis.respository.interfaces.redis_repository import (
    RedisRepositoryInterface,
)
from src.models.sqlite.repository.interfaces.products_repository import (
    ProductsRepositoryInterface,
)


class ProductFinder:
    def __init__(
        self,
        redis_repo: RedisRepositoryInterface,
        products_repo: ProductsRepositoryInterface,
    ) -> None:
        self.redis_repo = redis_repo
        self.products_repo = products_repo

    def find_by_name(self, http_request: HttpRequest) -> HttpResponse:
        pass
