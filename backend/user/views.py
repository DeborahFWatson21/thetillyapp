"""
Views for the User API.
"""
from core.models import Address, Business
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import status
from rest_framework.response import Response

from user.serializers import (
    AddressSerializer,
    BusinessSerializer,
    ClientSerializer,
    UserSerializer,
    AuthTokenSerializer,
)


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer
    # send registration email


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user."""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateDestroyAPIView):
    """Manage the authenticated user."""
    serializer_class = UserSerializer
    authentication_class = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user."""
        return self.request.user


class BusinessView(generics.ListCreateAPIView):
    """Create or get a user business(s)."""
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer
    authentication_class = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request, *args, **kwargs):
        serializer = BusinessSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientView(generics.ListCreateAPIView):
    """Create or return a list clients for a user or business"""
    serializer_class = ClientSerializer
    authentication_class = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # address
        print(request.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
