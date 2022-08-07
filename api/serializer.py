from rest_framework import serializers
from api.models import Record, User, Auth


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('userID', 'name', 'mobile', 'gender', 'address', 'image')

class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auth
        fields = ('authID', 'username', 'password')


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ('recordID', 'userID', 'disease','diagnosis', 'prescription', 'date', 'payment')
