from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profile_api import serializers

class HelloApiView(APIView):
    """Test Api View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of api view f"""
        as_list = ['Some String1', 'Some String2', 'Some String3']
        return Response({"code": 0, "result": as_list})

    def post(self, request):
        """Create Data With GIven name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            return Response({"code": 0, "result": f'Hi {name}'})

        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)