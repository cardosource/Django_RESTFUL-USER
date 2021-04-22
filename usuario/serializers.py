from rest_framework import serializers
from django.contrib.auth.models import User



class UserSerializers(serializers.ModelSerializer):
    class Meta:
        extra_kwargs ={
            'email':{'write_only':True},
            'password':{'write_only':True},
            'is_staff':{'write_only':True},
            'is_active':{'write_only':True},

        }
        model = User
        fields = (
            'id',
            'username',
            'email',
            'is_staff',
            'is_active',
            'password'

        )