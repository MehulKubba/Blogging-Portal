from django.urls import path
from . import views
from .views import home, post,category


urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<slug:url>/', views.post, name='post'),
    path('category/<slug:url>/', views.category, name='category'),
]
