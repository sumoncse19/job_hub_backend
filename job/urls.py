from django.urls import path

from . import views

urlpatterns = [
    path('category/', views.CategoriesListView.as_view()),
    path('newest/', views.NewestJobsList.as_view()),
    path('<int:pk>/', views.NewestJobDetailView.as_view()),
]