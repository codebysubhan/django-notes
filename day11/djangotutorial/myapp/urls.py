
# testing code start
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
# testing code end
