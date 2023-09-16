from django.urls import path

from . import views

urlpatterns = [
    path('', views.BrowseJobsList.as_view()),
    path('categories/', views.CategoriesListView.as_view()),
    path('my-jobs/', views.MyJobsView.as_view()),
    path('create-jobs/', views.CreateJobsView.as_view()),
    path('newest/', views.NewestJobsList.as_view()),
    path('<int:pk>/', views.NewestJobDetailView.as_view()),
]