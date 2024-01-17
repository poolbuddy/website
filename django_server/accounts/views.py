from rest_framework import viewsets, serializers 
from .models import User
from rest_framework import status, generics
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.decorators import authentication_classes, permission_classes 
from datetime import datetime
from django.utils import timezone



# Viewset for the User model
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    # Additional actions, if needed
    @action(detail=False, methods=['GET'])
    def search_by_email(self, request):
        email = request.query_params.get('email', None)
        if not email:
            return Response({'error': 'Email parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(email=email)
            serializer = self.get_serializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response({'error': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
