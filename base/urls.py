from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = "home"),
    path('index/', views.index, name = "index"),
    path('search/', views.search, name = "search"),
    path('product/<pcces_encode>', views.product, name = "product"),
    path('category/', views.category, name = "category"),
    path('category/<primary_category>', views.primary_category_products, name = "primary_category_products"),
    path('category/<primary_category>/<industrial_category>', views.industrial_category_products, name = "industrial_category_products"),
]

