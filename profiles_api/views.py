from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """API View"""
    def get(self, request, format=None):
        """Returns a list of API View Features"""
        an_apiview = [
            'uses HTTP method as function (get, post, patch, put, delete',
            'Is similar to a traditional django view',
            'Gives most controlled over application login',
            'Is mapped manually to URL',
        ]
        return Response({'Message':'Hello', 'an_APIview': an_apiview})