from django.urls import path
from ads import views

urlpatterns = [
    path('ad/', views.AdsListView.as_view()),
    path('ad/create/', views.CreateAdView.as_view()),
    path('ad/<int:pk>/', views.DetailAdView.as_view()),
    path('cat/', views.CategoriesListView.as_view()),
    path('cat/create/', views.CreateCategoryView.as_view()),
    path('cat/<int:pk>/', views.DetailCategoryView.as_view()),
]