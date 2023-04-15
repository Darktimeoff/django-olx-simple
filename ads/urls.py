from django.urls import path
from ads import views

ads = [
    path('ad/', views.AdsListView.as_view()),
    path('ad/create/', views.CreateAdView.as_view()),
    path('ad/<int:pk>/', views.DetailAdView.as_view()),
    path('ad/<int:pk>/upload_image/', views.upload_image),
    path('ad/<int:pk>/update/', views.UpdateAdView.as_view()),
    path('ad/<int:pk>/delete/', views.DeleteAdView.as_view()),
]

cat = [
    path('cat/', views.CategoriesListView.as_view()),
    path('cat/create/', views.CreateCategoryView.as_view()),
    path('cat/<int:pk>/', views.DetailCategoryView.as_view()),
    path('cat/<int:pk>/update/', views.UpdateCategoryView.as_view()),
    path('cat/<int:pk>/delete/', views.DeleteCategoryView.as_view()),
]

user = [
    path('user/', views.ListUserView.as_view()),
    path('user/create/', views.CreateUserView.as_view()),
    path('user/<int:pk>/', views.DetailUserView.as_view()),
    path('user/<int:pk>/update/', views.UpdateUserView.as_view()),
    path('user/<int:pk>/delete/', views.DeleteUserView.as_view()),
]

urlpatterns = ads + cat + user