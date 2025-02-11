from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_post),
    path("<int:id>/", views.post)
]