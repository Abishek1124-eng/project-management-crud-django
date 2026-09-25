from django.urls import path
from . import views


urlpatterns = [
    path("",views.index,name="index"),
    path("register/",views.register,name="register"),
    path("list/",views.list,name="list"),
    path("update/<int:product_id>/",views.update,name="update"),
    path("delete/<int:product_id>/",views.delete,name="delete"),

]