from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('index/', views.index, name = "index"),
    path('search/', views.search, name = "search"),
    path('product/<pcces_encode>', views.product, name = "product" )
]