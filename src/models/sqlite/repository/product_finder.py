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
