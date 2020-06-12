from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

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
