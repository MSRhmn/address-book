from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add_contact, name="add_contact"),
    path("search/", views.search_contact, name="search_contact"),
    path("delete/<int:pk>/", views.delete_contact, name="delete_contact"),
]
