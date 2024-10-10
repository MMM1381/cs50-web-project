from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("mmm",views.MMM,name='mehdi'),
    path("lol",views.laugh,name='laugh')
]