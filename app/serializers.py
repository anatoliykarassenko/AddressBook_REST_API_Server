from rest_framework import serializers 
from .models import User, Telephone, Email

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TelephoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telephone
        fields = '__all__'

class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = '__all__'

