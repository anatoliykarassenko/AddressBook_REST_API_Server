from rest_framework import viewsets, status
from . import models
from . import serializers

class UserViewset(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

class TelephoneViewset(viewsets.ModelViewSet):
    queryset = models.Telephone.objects.all()
    serializer_class = serializers.TelephoneSerializer

class EmailViewset(viewsets.ModelViewSet):
    queryset = models.Email.objects.all()
    serializer_class = serializers.EmailSerializer