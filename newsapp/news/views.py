from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator

from .models import News
from .forms import NewsForm

"""
    Query all the News objects
    Get page size from the POST request, otherwise default 10 news per page
    Create paginator object, get the desired page number from URL and return the desired page object
    Send the page object to homepage.html
"""
def homepage(request):
    news_list = News.objects.all()
    if request.method == 'POST':
        page_size = request.POST["page-size"]
    else:
        page_size = 10

    paginator = Paginator(news_list, page_size)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "news/homepage.html", {"page_obj": page_obj})

"""
    Query specific News object with the provided id in the URL
    Raise HTTP 404 error if the model does not exist
    Send the News object to details.html
"""
def details(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    return render(request, "news/details.html", {"news": news})

"""
    If user is authenticated, render account.html
    Otherwise, redirect to login.html
"""
def account(request):
    if request.user.is_authenticated:
        return render(request, "news/account.html", {})
    else:
        return redirect("login")

"""
    If user is authenticated then handle the request, otherwise redirect to login.html
    Check if request is POST or GET:
        - If POST, create NewsForm object with the parameters provided in the request
        Check form's validity, save it in the database and redirect to this News article page
        Raise errors if this NewsForm object is not valid
        - If GET, create empty NewsForm object and send it to add.html
"""
def add(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = NewsForm(request.POST, request.FILES)

            if form.is_valid():
                n = form.save()
                request.user.newslist.add(n)
                messages.success(request, f"News added: {n.title}")
                return redirect("news:details", n.id)
            else:
                for field in form:
                    messages.error(request, f"{field.errors}")
                return render(request, "news/add.html", {"form": form})
        else:
            form = NewsForm()

        return render(request, "news/add.html", {"form": form})
    else:
        return redirect("login")

"""
    If user is authenticated then handle the request, otherwise redirect to login.html
    Query specific News object with the provided id in the URL
    Raise HTTP 404 error if the model does not exist
    Check if request is POST or GET:
        - If POST, create NewsForm object with the parameters provided in the request
        Check form's validity, save it in the database and redirect to this News article page
        Raise errors if this NewsForm object is not valid
        - If GET, create empty NewsForm object and send it to add.html
"""
def edit(request, news_id):
    if request.user.is_authenticated:
        news = get_object_or_404(News, pk=news_id)

        if request.method == "POST":
            form = NewsForm(request.POST, request.FILES, instance=news)

            if form.is_valid():
                n = form.save()
                messages.success(request, f"News edited: {n.title}")
                return redirect("news:details", n.id)
            else:
                for field in form:
                    messages.error(request, f"{field.errors}")
                return render(request, "news/edit.html", {"form": form})
        else:
            form = NewsForm(instance=news)

        return render(request, "news/edit.html", {"form": form})
    else:
        return redirect("login")

"""
    If user is authenticated then handle the request, otherwise redirect to login.html
    Query specific News object with the provided id in the URL
    Raise HTTP 404 error if the model does not exist
    Delete queried object from database
    Render account.html
"""
def delete(request, news_id):
    if request.user.is_authenticated:
        news = get_object_or_404(News, pk=news_id)
        title = news.title
        news.delete()
        messages.success(request, f"News deleted: {title}")
        return render(request, "news/account.html", {})
    else:
        return redirect("login")
