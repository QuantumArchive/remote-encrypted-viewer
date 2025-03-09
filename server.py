from django.urls import path
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ExampleView(APIView):
    def get(self, request):
        return Response({"message": "GET request placeholder"}, status=status.HTTP_200_OK)

    def post(self, request):
        return Response({"message": "POST request placeholder"}, status=status.HTTP_201_CREATED)

    def put(self, request):
        return Response({"message": "PUT request placeholder"}, status=status.HTTP_200_OK)

    def delete(self, request):
        return Response({"message": "DELETE request placeholder"}, status=status.HTTP_204_NO_CONTENT)


urlpatterns = [
    path('example/', ExampleView.as_view(), name='example'),
]
