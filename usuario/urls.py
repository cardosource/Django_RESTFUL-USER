from django.urls import path
from .views import UserAPIView ,UserListAPIView
urlpatterns =[
    path('registrar/', UserAPIView.as_view()),
    path('usuario/<int:pk>/', UserListAPIView.as_view()),
]