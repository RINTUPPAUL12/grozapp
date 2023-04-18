from .import views  
from django.urls import path  
  
urlpatterns = [
    path('', views.ProductCategoriesView.as_view(),name="basic"),
    
]