from django.contrib.auth.models import User
from .serializers import UserSerializers
from rest_framework import generics
from django.contrib.auth.models import User



class UserAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class =  UserSerializers

class UserListAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers