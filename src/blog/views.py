from django.http import HttpResponse


# Create your views here.
from django.shortcuts import render


def index(request):
    return render(request, "blog/index.html")


def article(request, numero_article):
    if numero_article not in ["01","02","03"]:
        return render(request, "blog/article_not_found.html")
    print(numero_article)
    return render(request, f"blog/article_{numero_article}.html")
