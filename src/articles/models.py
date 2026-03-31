from django.db import models
from django.db.models import TextField
from django_mariadb_vector import MariaDBVectorField, MariaDBVectorIndex
from django_mariadb_vector.managers import RecommendationManager

try:
    from django_mariadb_vector import __version__ as django_mariadb_vector_version
except ImportError:
    __version__ = "0.0.0"

from config.settings import VECTOR_EMBEDDING_DIMENSION, VECTOR_EMBEDDING_INDEX_M, BINARY_RESPONSE

DIMENSIONS = VECTOR_EMBEDDING_DIMENSION
VECTOR_INDEX_M = VECTOR_EMBEDDING_INDEX_M
DJANGO_MARIADB_VECTOR_MIN_VERSION = (0, 2, 0)

ver = tuple(map(int, django_mariadb_vector_version.split(".")[:3]))
if ver < DJANGO_MARIADB_VECTOR_MIN_VERSION:
    assert (
        False
    ), f"django-mariadb-vector version must be at least {DJANGO_MARIADB_VECTOR_MIN_VERSION}, found {django_mariadb_vector_version}"


print(f"django_mariadb_vector_version: v{django_mariadb_vector_version}, {DIMENSIONS=}, {BINARY_RESPONSE=}")


class Article(models.Model):
    context = TextField()
    embedding = MariaDBVectorField(dimensions=DIMENSIONS, binary_response=BINARY_RESPONSE)

    objects = RecommendationManager(vector_field="embedding")

    class Meta:
        indexes = [
            # Vector index (MariaDB 11.8.2+)
            MariaDBVectorIndex(fields=["embedding"], dimensions=DIMENSIONS, m=VECTOR_INDEX_M),
        ]
