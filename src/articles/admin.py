from ast import literal_eval

from django import forms
from django.conf import settings
from django.contrib import admin
from django.core.exceptions import ValidationError
from django_mariadb_vector.fields import warmup_vector_index

from .models import Article


class ArticleAdminForm(forms.ModelForm):
    class Meta:
        model = Article

        fields = "__all__"

    def clean_embedding(self):
        value = self.cleaned_data.get("embedding")

        if value in (None, ""):
            raise ValidationError("Embedding is required.")

        if isinstance(value, str):
            try:
                value = literal_eval(value)
            except (ValueError, SyntaxError, TypeError):
                raise ValidationError("Embedding must be a valid vector string, for example: [0.1, 0.2, 0.3].")

        if not isinstance(value, (list, tuple)):
            raise ValidationError("Embedding must be a list, tuple, or vector string.")

        if not value:
            raise ValidationError("Embedding cannot be empty.")

        for index, item in enumerate(value):
            if not isinstance(item, (int, float)):
                raise ValidationError(f"Embedding item at position {index + 1} must be a number.")

        field = self.Meta.model._meta.get_field("embedding")
        expected_dimension = field.dimensions if hasattr(field, "dimensions") else settings.VECTOR_EMBEDDING_DIMENSION
        if len(value) != expected_dimension:
            raise ValidationError(f"Embedding must contain exactly {expected_dimension} values.")

        return value


@admin.action(description="Clear embedding values for selected records to ZERO")
def clear_embeddings(model_admin, request, queryset):
    # This performs a bulk update in the database
    count = queryset.update(embedding=[0.0], updated_at=None, model_name=None)
    model_admin.message_user(request, f"Successfully cleared embeddings for {count} records.")


@admin.action(description="Warmup index of embeddings")
def warmup_index_embeddings(model_admin, request, queryset):
    # This performs a bulk update in the database
    table = model_admin.model._meta.db_table  # noqa
    response = warmup_vector_index(table, "embedding")
    model_admin.message_user(request, f"Successfully warmed index of embeddings: {response}.")


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
    actions = [clear_embeddings, warmup_index_embeddings]


admin.site.register(Article, ArticleAdmin)
