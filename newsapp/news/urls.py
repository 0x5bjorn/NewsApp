from django.urls import path
from . import views

# Namespacing of Newsapp urls
app_name = "news"

urlpatterns = [
    # ex: /
    path("", views.homepage, name="homepage"),
    # ex: /1/
    path("<int:news_id>/", views.details, name="details"),
    # ex: /account/
    path("account/", views.account, name="account"),
    # ex: /add/
    path("add/", views.add, name="add"),
    # ex: /edit/1/
    path("edit/<int:news_id>/", views.edit, name="edit"),
    # ex: /delete/1/
    path("delete/<int:news_id>/", views.delete, name="delete"),
]