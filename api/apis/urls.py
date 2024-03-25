from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('news/', views.news_list, name='get-news'),
    path('news/create/', views.create_news, name='create-news')
]