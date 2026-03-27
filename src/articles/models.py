from django.db import models
from django.db.models import TextField
from django_mariadb_vector import MariaDBVectorField, MariaDBVectorIndex
from django_mariadb_vector.managers import RecommendationManager

from config.settings import VECTOR_EMBEDDING_DIMENSION, VECTOR_EMBEDDING_INDEX_M

DIMENSIONS = VECTOR_EMBEDDING_DIMENSION
VECTOR_INDEX_M = VECTOR_EMBEDDING_INDEX_M


class Article(models.Model):
    context = TextField()
    embedding = MariaDBVectorField(dimensions=DIMENSIONS)

    objects = RecommendationManager(vector_field="embedding")

    class Meta:
        indexes = [
            # Vector index (MariaDB 11.8.2+)
            MariaDBVectorIndex(fields=["embedding"], dimensions=DIMENSIONS, m=VECTOR_INDEX_M),
        ]
