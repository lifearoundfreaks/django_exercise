
from django.shortcuts import render


def home_page(request):
    content = {
        "title": "Home page"
    }
    return render(request, "index.html", content)
