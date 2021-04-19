from django.urls import path
from . views import HomeListAPIView, HomeDetailAPIView, ImageView, Search 

urlpatterns = [
    path('', HomeListAPIView.as_view()),
    path('search/',Search.as_view()),
    path('<slug>/', HomeDetailAPIView.as_view()),
    path('images/<int:pk>/', ImageView.as_view()),
]