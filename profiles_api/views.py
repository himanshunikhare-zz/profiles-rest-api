from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from profiles_api import serializers
from profiles_api import models

class HelloApiView(APIView):
    """API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of API View Features"""
        an_apiview = [
            'uses HTTP method as function (get, post, patch, put, delete',
            'Is similar to a traditional django view',
            'Gives most controlled over application login',
            'Is mapped manually to URL',
        ]
        return Response({'Message':'Hello', 'an_APIview': an_apiview})

    def post(self, request):
        """Crete hello API with out name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle Updating Object"""
        return Response({"method":"PUT"})

    def patch(self, request, pk=None):
        """Handle partial update of an object"""
        return Response({"method":"PATCH"})

    def delete(self, request, pk=None):
        return Response({"method": "DELETE"})

class HelloViewSet(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer

    """Test API ViewSet"""
    def list(self, request):
        a_viewset = [
            'uses HTTP method as function (get, post, patch, put, delete',
            'Is similar to a traditional django view',
            'Gives most controlled over application login',
            'Is mapped manually to URL',
        ]
        return Response({'Message':'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by id"""
        return Response({'http':'get'})

    def update(self, request, pk=None):
        """Handle getting an object by id"""
        return Response({'http':'put'})

    def partial_update(self, request, pk=None):
        """Handle getting an object by id"""
        return Response({'http':'patch'})

    def destroy(self, request, pk=None):
        """Removing an object"""
        return Response({"http":'delete'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
