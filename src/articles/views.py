from django.shortcuts import render, get_object_or_404
from .models import Article

# Create your views here.


def article_list(request):
    articles = Article.objects.all()
    return render(request, "article/list.html", {"articles": articles})


def similar_articles(request, pk):
    reference = get_object_or_404(Article, pk=pk)
    results = Article.objects.similar_to(reference.id, limit=5)

    return render(
        request,
        "article/similar.html",
        {
            "reference": reference,
            "results": results,
        },
    )
