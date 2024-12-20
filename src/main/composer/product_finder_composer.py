from src.data.product_finder import ProductFinder
from src.models.redis.respository.redis_repository import RedisRepository
from src.models.redis.settings.connection import redis_connection_handler
from src.models.sqlite.repository.products_repository import ProductsRepository
from src.models.sqlite.settings.connection import sqlitedb_connection_handler


def product_finder_composer():
    sqlite_conn = sqlitedb_connection_handler.get_connection()
    redis_conn = redis_connection_handler.get_connection()

    products_repo = ProductsRepository(sqlite_conn)
    redis_repo = RedisRepository(redis_conn)

    usecase = ProductFinder(redis_repo, products_repo)
    return usecase
